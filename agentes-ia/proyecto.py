#!/usr/bin/env python3
"""Configuración del proyecto para el kit de agentes SDD.

Todo lo que cambia entre proyectos vive en `proyecto.json`, en la raíz del proyecto:
nombre, archivo de contexto, stack, rutas, comandos de prueba, módulos, datos sensibles
y reglas críticas. Los agentes, el runner, el orquestador y el guardián leen de aquí;
ningún prompt ni script tiene valores de un proyecto concreto.

La raíz del proyecto es la carpeta que contiene `agentes-ia/`. Se puede cambiar con la
variable de entorno SDD_PROYECTO (útil si el kit vive en otra carpeta).

Marcadores que se reemplazan en los prompt.md:
    {{NOMBRE_PROYECTO}}   {{IDIOMA}}             {{CONTEXTO_PROYECTO}}  {{ARCHIVO_CONTEXTO}}
    {{STACK}}             {{DOCUMENTO_STACK}}    {{CANALES}}            {{RUTAS}}
    {{COMANDOS}}          {{MODULOS}}            {{DATOS_SENSIBLES}}    {{REGLAS_CRITICAS}}
    {{EVIDENCIAS}}        {{CARPETA_SPECS}}      {{CARPETA_ARQ}}        {{SKILLS}}

Uso directo:
    python agentes-ia/proyecto.py            # muestra la configuración efectiva
    python agentes-ia/proyecto.py --validar  # código 1 si falta algo obligatorio
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
from pathlib import Path

RAIZ_AGENTES = Path(__file__).resolve().parent
RAIZ_PROYECTO = Path(os.environ.get("SDD_PROYECTO") or RAIZ_AGENTES.parent).resolve()
ARCHIVO_PROYECTO = "proyecto.json"
CARPETA_SKILLS_KIT = RAIZ_AGENTES / "skills"

POR_DEFECTO: dict = {
    "nombre": "Proyecto sin nombre",
    "archivo_contexto": "CONTEXTO_PROYECTO.md",
    "idioma": "español de Colombia",
    "stack": {
        "documento": "docs/arquitectura/propuesta-tecnologica.md",
        "resumen": "Pendiente: lo propone el agente de arquitectura y lo aprueba una persona.",
    },
    "perfiles": [],
    "canales": [],
    "rutas": {
        "salidas": "agentes-ia/salidas",
        "codigo": ["apps/*", "src/*"],
        "pruebas": ["*.spec.*", "*.test.*", "*/pruebas/*", "*/tests/*", "*/e2e/*"],
        "modulo": "apps/api/src/modulos/{carpeta}",
        "pruebas_modulo": "apps/api/src/modulos/{carpeta}/pruebas",
        "e2e": "apps/web/e2e",
        "canal_conversacional": "apps/api/src/entradas/{canal}",
        "interfaz": "apps/web",
        "extensiones_codigo": [".ts", ".tsx", ".js", ".jsx", ".py", ".java", ".cs", ".go"],
        "skills_proyecto": "skills-proyecto",
    },
    "comandos": {
        "directorio": ".",
        "permitidos": [],
        "pruebas_modulo": "",
        "senales_error_tecnico": [
            "SyntaxError", "ReferenceError", "Cannot find module", "ModuleNotFoundError",
            "ImportError", "is not a function", "error TS", "compilation failed",
        ],
        "senal_no_implementado": "No implementado",
    },
    "modulos": [],
    "datos_sensibles": [],
    "reglas_criticas": [],
    "evidencias": "docs/evidencias-ia.md",
}

OBLIGATORIOS = ["nombre", "archivo_contexto"]


def _mezclar(base: dict, encima: dict) -> dict:
    resultado = copy.deepcopy(base)
    for clave, valor in encima.items():
        if isinstance(valor, dict) and isinstance(resultado.get(clave), dict):
            resultado[clave] = _mezclar(resultado[clave], valor)
        else:
            resultado[clave] = valor
    return resultado


def cargar(raiz: Path | None = None) -> dict:
    """proyecto.json mezclado con los valores por defecto. Si no existe, solo los valores por defecto."""
    raiz = Path(raiz or RAIZ_PROYECTO)
    ruta = raiz / ARCHIVO_PROYECTO
    datos = {}
    if ruta.is_file():
        try:
            datos = json.loads(ruta.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            sys.exit(f"{ruta} no es un JSON válido: {error}")
    proyecto = _mezclar(POR_DEFECTO, {k: v for k, v in datos.items() if not k.startswith("_")})
    proyecto["_existe"] = ruta.is_file()
    proyecto["_raiz"] = str(raiz)
    return proyecto


def validar(proyecto: dict) -> list[str]:
    problemas = []
    if not proyecto.get("_existe"):
        problemas.append(f"No existe {ARCHIVO_PROYECTO} en {proyecto['_raiz']}. Copia plantilla/proyecto.json.")
    for clave in OBLIGATORIOS:
        if not proyecto.get(clave):
            problemas.append(f"Falta «{clave}» en {ARCHIVO_PROYECTO}.")
    contexto = Path(proyecto["_raiz"]) / proyecto["archivo_contexto"]
    if not contexto.is_file():
        problemas.append(f"No existe el archivo de contexto {proyecto['archivo_contexto']}.")
    for perfil in proyecto.get("perfiles", []):
        if not (CARPETA_SKILLS_KIT / "perfiles" / perfil).is_dir():
            problemas.append(f"El perfil «{perfil}» no existe en agentes-ia/skills/perfiles/.")
    for modulo in proyecto.get("modulos", []):
        if not isinstance(modulo, dict) or not modulo.get("nombre"):
            problemas.append("Cada módulo de «modulos» debe ser un objeto con «nombre».")
    return problemas


# ----------------------------------------------------------------- consultas

def carpeta_specs(proyecto: dict) -> str:
    return f"{proyecto['rutas']['salidas']}/specification-agent"


def carpeta_arq(proyecto: dict) -> str:
    return f"{proyecto['rutas']['salidas']}/architecture-agent"


def modulos(proyecto: dict) -> list[dict]:
    return [m for m in proyecto.get("modulos", []) if isinstance(m, dict) and m.get("nombre")]


def nombres_modulos(proyecto: dict) -> list[str]:
    return [m["nombre"] for m in modulos(proyecto)]


def datos_modulo(proyecto: dict, nombre: str) -> dict:
    for modulo in modulos(proyecto):
        if modulo["nombre"] == nombre:
            return modulo
    return {"nombre": nombre}


def ruta_modulo(proyecto: dict, nombre: str, clave: str = "modulo") -> str:
    carpeta = datos_modulo(proyecto, nombre).get("carpeta") or nombre
    return proyecto["rutas"][clave].replace("{carpeta}", carpeta)


def comando_pruebas_modulo(proyecto: dict, nombre: str) -> str:
    plantilla = proyecto["comandos"].get("pruebas_modulo") or ""
    modulo = datos_modulo(proyecto, nombre)
    carpeta = modulo.get("carpeta") or nombre
    ruta = ruta_modulo(proyecto, nombre, "pruebas_modulo")
    directorio = proyecto["comandos"].get("directorio") or "."
    if directorio not in (".", ""):
        prefijo = directorio.rstrip("/") + "/"
        ruta_rel = ruta[len(prefijo):] if ruta.startswith(prefijo) else ruta
    else:
        ruta_rel = ruta
    return plantilla.replace("{carpeta}", carpeta).replace("{modulo}", nombre).replace("{ruta_pruebas}", ruta_rel)


# ------------------------------------------------------------------- skills

def buscar_skill(nombre: str, proyecto: dict) -> Path | None:
    """Busca un skill: primero los del proyecto, luego los perfiles activos, luego el núcleo."""
    raiz = Path(proyecto["_raiz"])
    candidatos = [raiz / proyecto["rutas"]["skills_proyecto"] / nombre / "SKILL.md"]
    candidatos += [CARPETA_SKILLS_KIT / "perfiles" / p / nombre / "SKILL.md" for p in proyecto.get("perfiles", [])]
    candidatos += [CARPETA_SKILLS_KIT / "nucleo" / nombre / "SKILL.md"]
    for candidato in candidatos:
        if candidato.is_file():
            return candidato
    return None


def texto_skills(nombres: list[str], proyecto: dict) -> str:
    """Contenido de los skills pedidos por un agente, listo para ir dentro del prompt."""
    if not nombres:
        return "Este agente no tiene skills asignados."
    partes = []
    for nombre in nombres:
        ruta = buscar_skill(nombre, proyecto)
        if ruta is None:
            partes.append(f"## Skill `{nombre}`\n\nNo disponible en este proyecto (perfil no activo o skill no "
                          "creado). Si lo necesitas, crea una PREG; no inventes su contenido.")
            continue
        texto = ruta.read_text(encoding="utf-8")
        if texto.startswith("---"):
            texto = texto.split("---", 2)[2]
        partes.append(f"## Skill `{nombre}`\n\n{texto.strip()}")
    return "\n\n".join(partes)


# --------------------------------------------------------------- marcadores

def _lista(valores, vacio: str) -> str:
    valores = [v for v in (valores or []) if v]
    return "\n".join(f"- {v}" for v in valores) if valores else f"- {vacio}"


def _rutas(proyecto: dict) -> str:
    r = proyecto["rutas"]
    return "\n".join([
        f"- Salidas de los agentes: `{r['salidas']}/<agente>/`",
        f"- SPEC: `{carpeta_specs(proyecto)}/aprobadas/` (solo aprobadas) y `borradores/`",
        f"- ARQ: `{carpeta_arq(proyecto)}/aprobadas/` y `borradores/`",
        f"- Código de producción: {', '.join(f'`{p}`' for p in r['codigo'])}",
        f"- Archivos de prueba (protegidos para quien construye): {', '.join(f'`{p}`' for p in r['pruebas'])}",
        f"- Carpeta de un módulo: `{r['modulo']}`",
        f"- Pruebas de un módulo: `{r['pruebas_modulo']}`",
        f"- Pruebas extremo a extremo: `{r['e2e']}`",
        f"- Canal conversacional: `{r['canal_conversacional']}`",
        f"- Interfaz gráfica: `{r['interfaz']}`",
        "- Preguntas: `docs/preguntas/PREG-xxx.md` · MVP: `docs/mvp.md` · Decisiones: `docs/decisiones.md`",
        "- QA: `qa/revision/`, `qa/casos/`, `qa/trazabilidad.md`, `qa/oraculos-pendientes.md`, "
        "`qa/ejecuciones/`, `qa/humo/`, `qa/incidentes/`",
        f"- Evidencias de uso de IA: `{proyecto['evidencias']}`",
    ])


def _comandos(proyecto: dict) -> str:
    c = proyecto["comandos"]
    permitidos = ", ".join(f"`{p}`" for p in c.get("permitidos", [])) or "ninguno configurado"
    return "\n".join([
        f"- Directorio donde se ejecutan las pruebas: `{c.get('directorio') or '.'}`",
        f"- Comandos de prueba permitidos: {permitidos}",
        f"- Pruebas de un módulo: `{c.get('pruebas_modulo') or 'sin configurar'}`",
        f"- Una prueba roja válida falla por aserción o por el mensaje «{c.get('senal_no_implementado')}».",
    ])


def _modulos(proyecto: dict) -> str:
    if not modulos(proyecto):
        return "- Aún no hay módulos registrados (los define el corte técnico del MVP)."
    lineas = []
    for m in modulos(proyecto):
        detalle = ", ".join(f"{k}: {v}" for k, v in m.items() if k != "nombre")
        lineas.append(f"- {m['nombre']}" + (f" ({detalle})" if detalle else ""))
    return "\n".join(lineas)


def reemplazar(texto: str, proyecto: dict, skills: list[str] | None = None) -> str:
    """Reemplaza los marcadores {{...}} del prompt con los datos del proyecto."""
    raiz = Path(proyecto["_raiz"])
    contexto = raiz / proyecto["archivo_contexto"]
    stack = proyecto["stack"]
    valores = {
        "NOMBRE_PROYECTO": proyecto["nombre"],
        "IDIOMA": proyecto["idioma"],
        "ARCHIVO_CONTEXTO": proyecto["archivo_contexto"],
        "STACK": stack.get("resumen") or "Pendiente.",
        "DOCUMENTO_STACK": stack.get("documento") or "docs/arquitectura/propuesta-tecnologica.md",
        "CANALES": ", ".join(proyecto.get("canales") or []) or "sin definir",
        "RUTAS": _rutas(proyecto),
        "COMANDOS": _comandos(proyecto),
        "MODULOS": _modulos(proyecto),
        "DATOS_SENSIBLES": _lista(proyecto.get("datos_sensibles"), "Ninguno declarado: pregunta antes de exponer datos personales."),
        "REGLAS_CRITICAS": _lista(proyecto.get("reglas_criticas"), "Ninguna declarada."),
        "EVIDENCIAS": proyecto["evidencias"],
        "CARPETA_SPECS": carpeta_specs(proyecto),
        "CARPETA_ARQ": carpeta_arq(proyecto),
    }
    if "{{CONTEXTO_PROYECTO}}" in texto:
        if not contexto.is_file():
            sys.exit(f"No se encontró el archivo de contexto: {contexto}")
        valores["CONTEXTO_PROYECTO"] = contexto.read_text(encoding="utf-8")
    if "{{SKILLS}}" in texto:
        valores["SKILLS"] = texto_skills(skills or [], proyecto)
    for clave, valor in valores.items():
        texto = texto.replace("{{" + clave + "}}", valor)
    sobrantes = sorted(set(re.findall(r"\{\{([A-Z_]+)\}\}", texto)))
    if sobrantes:
        sys.exit(f"Marcadores sin valor en el prompt: {', '.join(sobrantes)}")
    return texto


# --------------------------------------------------------------- evidencias

ENCABEZADO_EVIDENCIAS = """# Evidencias de uso de agentes de IA

Cada ejecución de un agente agrega una fila automáticamente (agente.py y herramientas.py).
La columna «Validación» la llena una persona: qué revisó, qué corrigió y si aceptó el resultado.
No borres filas: si un resultado se descarta, escríbelo en la validación.

| Fecha | Agente | Modelo | Tarea | Contexto suministrado | Resultado | Validación de la persona |
|---|---|---|---|---|---|---|
"""


def _celda(texto: str, limite: int = 160) -> str:
    texto = " ".join(str(texto or "").split()).replace("|", "/")
    return texto if len(texto) <= limite else texto[: limite - 1] + "…"


def registrar_evidencia(proyecto: dict, agente: str, modelo: str, tarea: str, contexto: str, resultado: str) -> Path:
    """Agrega una fila a docs/evidencias-ia.md (o la ruta de «evidencias» en proyecto.json)."""
    from datetime import datetime

    ruta = Path(proyecto["_raiz"]) / proyecto["evidencias"]
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if not ruta.is_file():
        ruta.write_text(ENCABEZADO_EVIDENCIAS, encoding="utf-8", newline="\n")
    fila = (f"| {datetime.now():%Y-%m-%d %H:%M} | {_celda(agente, 40)} | {_celda(modelo, 40)} | {_celda(tarea)} | "
            f"{_celda(contexto)} | {_celda(resultado)} | pendiente |\n")
    with ruta.open("a", encoding="utf-8", newline="\n") as archivo:
        archivo.write(fila)
    return ruta


def main() -> int:
    parser = argparse.ArgumentParser(description="Muestra o valida la configuración del proyecto.")
    parser.add_argument("--validar", action="store_true")
    args = parser.parse_args()
    proyecto = cargar()
    problemas = validar(proyecto)
    if args.validar:
        for problema in problemas:
            print(f"  ✗ {problema}")
        print("proyecto.json: OK" if not problemas else f"{len(problemas)} problema(s).")
        return 1 if problemas else 0
    print(json.dumps({k: v for k, v in proyecto.items() if not k.startswith("_")}, ensure_ascii=False, indent=2))
    for problema in problemas:
        print(f"  ! {problema}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
