#!/usr/bin/env python3
"""Runner secuencial del pipeline del kit SDD.

Ejecuta el siguiente paso que indique orquestador.py, o recorre la secuencia hasta la
próxima puerta humana. Los agentes corren con el runtime propio del kit
(agentes-ia/herramientas.py) y un LLM por API key (Gemini, Mistral, Groq u OpenRouter).
No depende de ningún asistente ni CLI externo. No aprueba nada por su cuenta: las
puertas de MVP, SPEC, oráculos y entrega siempre se detienen.

Uso:
    python qa/scripts/runner.py --estado
    python qa/scripts/runner.py --dry-run
    python qa/scripts/runner.py --seguir --auto-marcar
    python qa/scripts/runner.py --paso S1 --modulo <modulo>

Candados mecánicos:
  - Antes de B1/B2/B3/B4: `guardian.py foto`. Después: `guardian.py verificar`. Si un
    agente tocó pruebas o qa/, o dejó trampas en el código, el runner se detiene, suma
    una iteración y escala a una persona.
  - Las pruebas del módulo las corre el runner (comando de proyecto.json), no el modelo.
  - El modelo de cada paso sale de config.json del agente; MODELO_S1, MODELO_B1… en
    agentes-ia/.env lo sobrescriben.
  - El estado se lee con orquestador.reconciliar(): los archivos mandan.

Código de salida: 0 si terminó o se detuvo en una puerta humana; 1 si falló.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ORQUESTADOR = RAIZ / "orquestador.py"
PIPELINE = RAIZ / "pipeline.json"
MARCAR = RAIZ / "qa" / "scripts" / "marcar.py"
GUARDIAN = RAIZ / "qa" / "scripts" / "guardian.py"
LOG_DIR = RAIZ / "qa" / "ejecuciones"
PUERTAS = {"mvp", "registrar-modulos", "spec", "escalado", "escalar", "entrega"}
PASOS_EJECUTABLES = {"S1", "S2", "S3", "B1", "B2", "B3", "B4", "B1/B4", "B2/B4", "B3/B4", "R1", "R2"}


def _cargar(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar {ruta}")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


PROYECTO_PY = _cargar("proyecto", RAIZ / "agentes-ia" / "proyecto.py")
PROYECTO = PROYECTO_PY.cargar(RAIZ)


def cargar_orquestador():
    return _cargar("orquestador", ORQUESTADOR)


def leer_pipeline() -> dict:
    try:
        return json.loads(PIPELINE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"No se pudo leer pipeline.json: {exc}")


def pipeline_efectivo() -> dict:
    efectivo, avisos = cargar_orquestador().reconciliar(leer_pipeline(), RAIZ)
    for aviso in avisos:
        print(f"  ! {aviso}")
    return efectivo


def siguiente() -> dict:
    return cargar_orquestador().siguiente(pipeline_efectivo())[0]


def leer_env() -> dict:
    """Variables de agentes-ia/.env (sin depender de python-dotenv)."""
    datos = {}
    ruta = RAIZ / "agentes-ia" / ".env"
    if ruta.is_file():
        for linea in ruta.read_text(encoding="utf-8").splitlines():
            linea = linea.strip()
            if linea and not linea.startswith("#") and "=" in linea:
                clave, valor = linea.split("=", 1)
                datos[clave.strip()] = valor.strip().strip('"').strip("'")
    return datos


def modelo_para(paso: str) -> str | None:
    variable = f"MODELO_{paso.split('/')[0]}"
    return os.environ.get(variable) or leer_env().get(variable) or None


def guardian(*args: str) -> int:
    return subprocess.run([sys.executable, str(GUARDIAN), *args], cwd=RAIZ).returncode


def marcar(*args: str) -> int:
    return subprocess.run([sys.executable, str(MARCAR), *args], cwd=RAIZ).returncode


def preflight() -> list[str]:
    problemas = list(PROYECTO_PY.validar(PROYECTO))
    for modulo in ("openai", "dotenv"):
        if importlib.util.find_spec(modulo) is None:
            problemas.append(f"Falta el paquete Python `{modulo}` (pip install -r agentes-ia/requirements.txt).")
    llaves = ("GEMINI_API_KEY", "MISTRAL_API_KEY", "GROQ_API_KEY", "OPENROUTER_API_KEY")
    if not any(os.environ.get(k) or leer_env().get(k) for k in llaves):
        problemas.append("No hay ninguna API key en agentes-ia/.env (mira agentes-ia/.env.example).")
    if not PROYECTO["comandos"].get("pruebas_modulo"):
        problemas.append("Falta comandos.pruebas_modulo en proyecto.json: el ciclo de construcción no puede correr pruebas.")
    return problemas


def prompt_para(paso: str, modulo: str, extra: str = "") -> str:
    carpeta = PROYECTO_PY.ruta_modulo(PROYECTO, modulo, "modulo")
    pruebas = PROYECTO_PY.ruta_modulo(PROYECTO, modulo, "pruebas_modulo")
    contexto = (
        f"Módulo: {modulo}. Su código va en {carpeta}/ y sus pruebas en {pruebas}/: trabaja ahí y no crees "
        "otra carpeta para el módulo. Lee primero docs/mvp.md. No pidas confirmación: ejecuta hasta terminar o "
        "hasta una puerta humana. Usa solo datos sintéticos. Al terminar, registra tu uso en "
        f"{PROYECTO['evidencias']} si tu política lo permite; si no, inclúyelo en el resumen."
    )
    tareas = {
        "S1": "Revisa la SPEC del módulo y deja el informe en qa/revision/ con veredicto APTA, APTA_CON_RESERVAS o NO_APTA.",
        "S2": "Diseña los casos TC-* y actualiza qa/trazabilidad.md y qa/oraculos-pendientes.md.",
        "S3": "Genera las pruebas ejecutables de los TC aprobados y déjalas rojas por «no implementado».",
        "B1": "Implementa el dominio, los servicios, la persistencia y la API del módulo hasta dejar verdes sus pruebas, sin tocarlas.",
        "B2": "Implementa el canal conversacional del módulo usando solo la API de los módulos y plantillas fijas, sin tocar pruebas.",
        "B3": "Implementa la interfaz gráfica del módulo con el cliente tipado de la API, sin tocar pruebas.",
        "B4": "Ejecuta las pruebas del módulo, clasifica cada fallo y corrige solo código de producción, sin tocar pruebas.",
        "R1": "Ejecuta el humo del módulo contra el entorno de prueba y deja el informe en qa/humo/.",
        "R2": "Haz el triage de solo lectura del último hallazgo de humo y deja el informe en qa/incidentes/.",
    }
    texto = f"{contexto}\n\nTAREA: {tareas.get(paso.split('/')[0], 'Ejecuta tu tarea.')}"
    return f"{texto}\n\n{extra}" if extra else texto


def ejecutar_agente(paso: str, modulo: str, log, extra: str = "") -> int:
    herramientas = _cargar("herramientas", RAIZ / "agentes-ia" / "herramientas.py")

    def salida(texto: str) -> None:
        print(texto)
        log.write(texto + "\n")

    return herramientas.ejecutar_paso(paso, modulo, prompt_para(paso, modulo, extra), modelo_para(paso), salida)


def correr_pruebas(modulo: str) -> tuple[str, str]:
    """Pruebas del módulo, ejecutadas por el runner (no por el modelo).

    Devuelve ("verde" | "rojo" | "sin_pruebas", salida). Verde exige código 0.
    """
    carpeta = RAIZ / PROYECTO_PY.ruta_modulo(PROYECTO, modulo, "pruebas_modulo")
    if not carpeta.is_dir() or not any(p.is_file() for p in carpeta.rglob("*")):
        return "sin_pruebas", f"No hay pruebas en {carpeta.relative_to(RAIZ).as_posix()}/: S3 debe crearlas primero."
    comando = PROYECTO_PY.comando_pruebas_modulo(PROYECTO, modulo)
    if not comando:
        return "rojo", "Falta comandos.pruebas_modulo en proyecto.json."
    partes = shlex.split(comando)
    if os.name == "nt" and partes[0] in ("npm", "npx", "pnpm", "yarn"):
        partes[0] += ".cmd"
    directorio = RAIZ / (PROYECTO["comandos"].get("directorio") or ".")
    try:
        proc = subprocess.run(partes, cwd=directorio, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=900)
    except FileNotFoundError:
        return "rojo", f"No se encontró {partes[0]}: instala las dependencias del proyecto."
    except subprocess.TimeoutExpired:
        return "rojo", "Las pruebas superaron 900 s."
    return ("verde" if proc.returncode == 0 else "rojo"), (proc.stdout + proc.stderr)[-8000:]


def ciclo_construccion(paso: str, modulo: str, log) -> str:
    """El constructor del módulo (B1, B2 o B3) implementa; el runner corre las pruebas; si fallan,
    B4 corrige con la salida real. Hasta verde o 3 iteraciones; luego escala a una persona.

    Devuelve "verde", "escalado", "sin_pruebas", "revision" o un error "Bx=código".
    """
    constructor = paso.split("/")[0]
    if correr_pruebas(modulo)[0] == "sin_pruebas" and constructor != "B3":
        print(f"[ciclo] {modulo}: no hay pruebas; S3 debe generarlas antes de construir.")
        return "sin_pruebas"
    previas = leer_pipeline().get("iteraciones", {}).get(modulo, 0)
    extra = ""
    for numero in range(previas + 1, 4):
        sub = constructor if numero == previas + 1 else "B4"
        print(f"\n[ciclo] {modulo}: iteración {numero} de 3 con {sub}")
        log.write(f"\n[ciclo] {modulo}: iteración {numero} de 3 con {sub}\n")
        guardian("foto")
        codigo = ejecutar_agente(sub, modulo, log, extra)
        if guardian("verificar") != 0:
            marcar("iteracion", modulo)
            marcar("escalar", modulo, f"guardián: {sub} violó reglas duras (ver qa/ejecuciones/guardian-*.md)")
            return "escalado"
        if codigo != 0:
            return f"{sub}={codigo}"
        estado, salida = correr_pruebas(modulo)
        log.write(f"\n[pruebas {modulo}] {estado}\n{salida}\n")
        if estado == "sin_pruebas":
            print(f"[ciclo] {modulo}: {sub} terminó; no hay pruebas, queda para revisión manual.")
            return "revision"
        if estado == "verde":
            print(f"[ciclo] {modulo}: pruebas en verde.")
            marcar("modulo", modulo, "--implementacion", "verde")
            return "verde"
        print(f"[ciclo] {modulo}: pruebas en rojo tras la iteración {numero}.")
        marcar("iteracion", modulo)
        extra = ("RESULTADO DE LAS PRUEBAS (ejecutadas por el runner; corrige el código de producción, "
                 f"no las pruebas):\n{salida[-6000:]}")
    marcar("escalar", modulo, f"3 iteraciones de {paso} sin dejar las pruebas en verde")
    return "escalado"


def informe_mas_reciente(carpeta: Path, patron: str = "*.md") -> Path | None:
    if not carpeta.is_dir():
        return None
    archivos = sorted(carpeta.glob(patron), key=lambda p: p.stat().st_mtime, reverse=True)
    return archivos[0] if archivos else None


def veredicto_s1(modulo: str) -> str | None:
    spec_id = leer_pipeline().get("modulos", {}).get(modulo, {}).get("spec_id")
    if not spec_id:
        return None
    return cargar_orquestador().veredicto_informe(RAIZ, spec_id)


def resultado_humo() -> str | None:
    informe = informe_mas_reciente(RAIZ / "qa" / "humo", "RUN-humo-*.md")
    if not informe:
        return None
    texto = informe.read_text(encoding="utf-8", errors="replace").lower()
    if "fallido" in texto or "falló" in texto or "rojo" in texto:
        return "fallido"
    if "verde" in texto:
        return "verde"
    return None


def describir(accion: dict) -> str:
    return (
        f"[{accion['modulo']}] {accion['paso']} — {accion['responsable']}\n"
        f"  {accion['accion']}\n"
        f"  Bloqueado por: {accion.get('bloqueado_por', '—')}"
    )


def puerta(accion: dict) -> bool:
    return accion["paso"] in PUERTAS


def plan_humano(accion: dict) -> str:
    paso = accion["paso"]
    modulo = accion["modulo"]
    specs = PROYECTO_PY.carpeta_specs(PROYECTO)
    if paso == "mvp":
        return (
            "Puerta humana del MVP. Ejecuta los modos MVP y luego una persona escribe aprobado_por:\n"
            "  python agentes-ia/agente.py specification-agent \"priorizar MVP\" --adjuntar ...\n"
            "  python agentes-ia/agente.py architecture-agent \"cortar MVP\" --adjuntar ...\n"
            "  python qa/scripts/marcar.py mvp --estado aprobado --aprobado-por \"Nombre\""
        )
    if paso == "registrar-modulos":
        return (
            "El MVP ya está aprobado. Copia los módulos del Corte técnico a «modulos» de proyecto.json "
            "(nombre, carpeta, construye) y regístralos:\n"
            "  python qa/scripts/marcar.py modulo <nombre> --spec-id SPEC-00x"
        )
    if paso == "spec":
        return (
            f"Aprobación humana de la SPEC del módulo {modulo}. Congélala en {specs}/aprobadas/:\n"
            "  python agentes-ia/agente.py specification-agent \"El equipo aprueba la SPEC-00x\" --continuar SPEC-00x"
        )
    if paso in ("escalado", "escalar"):
        return "Escalamiento: decide una persona. Revisa el motivo en pipeline.json y resuélvelo con marcar.py."
    if paso == "entrega":
        return "Puerta humana final: revisa la definición de terminado y las evidencias de IA, y aprueba la entrega."
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Runner secuencial del pipeline del kit SDD.")
    parser.add_argument("--estado", action="store_true", help="Muestra el siguiente paso y sale.")
    parser.add_argument("--dry-run", action="store_true", help="Muestra la secuencia sin ejecutar agentes.")
    parser.add_argument("--seguir", action="store_true", help="Ejecuta pasos hasta una puerta humana.")
    parser.add_argument("--paso", help="Fuerza un paso: S1, S2, S3, B1/B4, B2/B4, B3/B4, B1–B4 sueltos, R1, R2.")
    parser.add_argument("--modulo", default=None, help="Módulo sobre el que trabaja el paso forzado.")
    parser.add_argument("--auto-marcar", action="store_true", help="Marca S1/S3/R1 cuando el resultado es inequívoco.")
    parser.add_argument("--max-pasos", type=int, default=20, help="Tope de pasos en --seguir.")
    args = parser.parse_args()

    accion = siguiente()
    problemas = preflight()
    print(f"\n== Runner del kit SDD — {PROYECTO['nombre']} ==")
    if problemas:
        print("Preflight:")
        for problema in problemas:
            print(f"  - {problema}")
    else:
        print("Preflight: OK")
    print(f"\nSiguiente paso:\n{describir(accion)}")

    if args.estado:
        return 0

    if args.dry_run:
        print("\n== Secuencia prevista ==")
        simulado = pipeline_efectivo()
        orquestador = cargar_orquestador()
        efectos = {"S1": ("revision", "APTA"), "S2": ("oraculos", "aprobados"), "S3": ("pruebas", "rojas"),
                   "R1": ("humo", "verde")}
        for n in range(args.max_pasos):
            act = orquestador.siguiente(simulado)[0]
            print(f"  {n + 1}. [{act['modulo']}] {act['paso']} — {act['responsable']}")
            if puerta(act):
                print(f"     Se detiene: {plan_humano(act).splitlines()[0]}")
                break
            modulo = simulado.setdefault("modulos", {}).setdefault(act["modulo"], {})
            if act["paso"] in efectos:
                campo, valor = efectos[act["paso"]]
                modulo[campo] = valor
            elif act["paso"].endswith("/B4"):
                modulo["implementacion"] = "verde"
        return 0

    if args.paso:
        if args.paso not in PASOS_EJECUTABLES:
            sys.exit(f"Paso no ejecutable: {args.paso}")
        if not args.modulo:
            sys.exit("--paso requiere --modulo.")
        accion = {"paso": args.paso, "modulo": args.modulo, "responsable": "runner",
                  "accion": "Paso forzado con --paso."}

    if puerta(accion) and not args.paso:
        print(f"\n{plan_humano(accion)}")
        return 0

    if problemas:
        print("\nCorrige el preflight antes de ejecutar agentes.", file=sys.stderr)
        return 1

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    sello = datetime.now().strftime("%Y%m%d-%H%M%S")
    ruta_log = LOG_DIR / f"runner-{sello}.log"
    resumen = {"fecha": sello, "proyecto": PROYECTO["nombre"], "pasos": []}

    with ruta_log.open("w", encoding="utf-8") as log:
        log.write(f"Runner {sello} | {PROYECTO['nombre']}\n")
        pasos = 0
        forzado = accion if args.paso else None
        while pasos < args.max_pasos:
            if forzado and pasos > 0:
                break  # un paso forzado se ejecuta una sola vez
            accion = forzado or siguiente()
            print(f"\n== Paso {pasos + 1}: {describir(accion)} ==")
            log.write(f"\n== Paso {pasos + 1}: {describir(accion)} ==\n")

            if puerta(accion):
                print(f"\n{plan_humano(accion)}")
                resumen["detenido_en"] = accion
                break

            paso = accion["paso"]
            modulo = accion["modulo"]
            if paso.endswith("/B4"):
                resultado = ciclo_construccion(paso, modulo, log)
                resumen["pasos"].append({"paso": paso, "modulo": modulo, "resultado": resultado})
                pasos += 1
                if resultado == "verde":
                    continue
                if resultado == "escalado":
                    print(f"\n{modulo}: se escaló a una persona (ver pipeline.json, escalados).")
                    resumen["detenido_en"] = {"motivo": "escalado", **accion}
                    break
                if resultado in ("sin_pruebas", "revision"):
                    motivo = ("faltan pruebas: ejecuta S3 del módulo" if resultado == "sin_pruebas"
                              else "revisión manual: marca --implementacion verde cuando esté listo")
                    print(f"\n{modulo}: {motivo}.")
                    resumen["detenido_en"] = {"motivo": motivo, **accion}
                    break
                print(f"{resultado}: el agente falló (cupo, API o error). Se detiene.", file=sys.stderr)
                resumen["error"] = resultado
                return 1

            codigo = ejecutar_agente(paso, modulo, log)
            if codigo != 0:
                print(f"{paso} falló con código {codigo}. Se detiene.", file=sys.stderr)
                resumen["error"] = f"{paso}={codigo}"
                return 1
            resumen["pasos"].append({"paso": paso, "modulo": modulo})
            pasos += 1

            if not args.auto_marcar:
                print("\nRevisa la salida y marca el estado con marcar.py. Se detiene para no asumir el resultado.")
                resumen["detenido_en"] = {"motivo": "marcado manual", **accion}
                break

            if paso == "S1":
                veredicto = veredicto_s1(modulo)
                if not veredicto:
                    print("S1 no dejó un veredicto legible; se detiene.", file=sys.stderr)
                    resumen["detenido_en"] = {"motivo": "sin veredicto S1", **accion}
                    break
                marcar("modulo", modulo, "--revision", veredicto)
                if veredicto == "NO_APTA":
                    print("S1 devolvió NO_APTA: se detiene para volver a Especificaciones.")
                    resumen["detenido_en"] = {"motivo": "NO_APTA", **accion}
                    break
            elif paso == "S3":
                if guardian("rojas", "--modulo", modulo) != 0:
                    print("S3: las pruebas no fallan por la razón correcta; no se marcan rojas.", file=sys.stderr)
                    resumen["detenido_en"] = {"motivo": "rojas no verificadas", **accion}
                    break
                marcar("modulo", modulo, "--pruebas", "rojas")
            elif paso == "R1":
                estado = resultado_humo()
                if not estado:
                    print("R1 no dejó un informe legible; se detiene.", file=sys.stderr)
                    resumen["detenido_en"] = {"motivo": "sin informe de humo", **accion}
                    break
                marcar("modulo", modulo, "--humo", estado)
            else:
                print(f"{paso} terminó. Revisa y marca el estado; el runner no asume el resultado.")
                resumen["detenido_en"] = {"motivo": "marcado manual", **accion}
                break

        if pasos >= args.max_pasos:
            print(f"\nSe alcanzó el tope de {args.max_pasos} pasos.")
            resumen["detenido_en"] = {"motivo": "max-pasos"}

    (LOG_DIR / f"runner-{sello}.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\nLog: {ruta_log.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
