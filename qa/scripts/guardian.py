#!/usr/bin/env python3
"""Guardián mecánico del kit SDD (sin LLM).

Convierte en comprobaciones las reglas del plan que no deben depender de que
un modelo obedezca su prompt:

  foto        Guarda el hash de los archivos protegidos (pruebas, qa/, SPEC
              aprobadas) antes de que corra un paso B1/B2/B3/B4.
  verificar   Después del paso: falla si cambió un archivo protegido o si el
              código de producción contiene trampas (valores de las pruebas,
              catch vacíos, comentarios «para que pase la prueba»).
  revisar     Solo el análisis del código, sin foto (útil a mano o en CI).
  rojas       Ejecuta las pruebas del módulo (comando de proyecto.json) y comprueba
              que fallan por aserción o por «No implementado», no porque la suite
              no compila.

Uso:
    python3 qa/scripts/guardian.py foto
    python3 qa/scripts/guardian.py verificar
    python3 qa/scripts/guardian.py revisar
    python3 qa/scripts/guardian.py rojas --modulo <modulo>

Código de salida: 0 si todo está bien; 1 si hay una violación.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import importlib.util
import json
import os
import re
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FOTO = RAIZ / "qa" / "ejecuciones" / ".guardian-foto.json"
INFORMES = RAIZ / "qa" / "ejecuciones"


def _cargar_proyecto_py():
    spec = importlib.util.spec_from_file_location("proyecto", RAIZ / "agentes-ia" / "proyecto.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


PROYECTO_PY = _cargar_proyecto_py()
PROYECTO = PROYECTO_PY.cargar(RAIZ)
PATRONES_PRUEBA = list(PROYECTO["rutas"]["pruebas"])
PATRONES_CODIGO = list(PROYECTO["rutas"]["codigo"])
EXTENSIONES = set(PROYECTO["rutas"]["extensiones_codigo"])

# Archivos que B1-B4 nunca pueden tocar: pruebas dentro del código, qa/ y SPEC aprobadas.
PROTEGIDOS_QA = [
    "qa/casos/*",
    "qa/revision/*",
    "qa/oraculos-pendientes.md",
    f"{PROYECTO_PY.carpeta_specs(PROYECTO)}/aprobadas/*",
]
IGNORAR_NOMBRES = {"desktop.ini"}

# Literales «sospechosos»: códigos/cédulas numéricos y ids sintéticos tipo `solicitud-1`.
LITERAL = re.compile(r"""['"`]((?:\d[\d.\-]{4,}\d)|(?:[a-z]+(?:-[a-z]+)*-\d+))['"`]""")
TRAMPAS = [
    (re.compile(r"catch\s*(\([^)]*\))?\s*\{\s*(//[^\n]*\s*|/\*.*?\*/\s*)*\}", re.S),
     "catch vacío (silencia errores)"),
    (re.compile(r"(para|por)\s+(cumplir|pasar|satisfacer)\s+(con\s+)?(el|la|los|las)?\s*(caso|prueba|test)", re.I),
     "comentario que adapta el código a la prueba"),
    (re.compile(r"(make|so)\s+(the\s+)?tests?\s+pass", re.I), "comentario que adapta el código a la prueba"),
    (re.compile(r"process\.env\.(NODE_ENV|JEST_WORKER_ID)\s*===?\s*['\"]test", re.I),
     "rama de código exclusiva para pruebas"),
    (re.compile(r"PYTEST_CURRENT_TEST"), "rama de código exclusiva para pruebas"),
]
TRAMPAS_PRUEBA = [
    (re.compile(r"@pytest\.mark\.(skip|xfail)|@(Disabled|Ignore)\b"), "prueba desactivada"),
    (re.compile(r"\b(it|test|describe)\.(skip|only)\s*\("), "skip/only en una prueba"),
    (re.compile(r"\b(xit|xdescribe|fit|fdescribe)\s*\("), "prueba desactivada o enfocada"),
]


def cumple(rel: str, patrones: list[str]) -> bool:
    # fnmatch: «*» también cruza «/», igual que en herramientas.py.
    return any(fnmatch.fnmatchcase(rel, p) for p in patrones)


def _archivos_del_proyecto() -> list[Path]:
    salida = []
    for p in RAIZ.rglob("*"):
        partes = p.relative_to(RAIZ).parts
        if not p.is_file() or p.name in IGNORAR_NOMBRES:
            continue
        if partes and partes[0] in (".git", "agentes-ia", "venv", ".venv"):
            continue
        if "node_modules" in partes or "__pycache__" in partes:
            continue
        salida.append(p)
    return salida


def es_prueba(rel: str) -> bool:
    return cumple(rel, PATRONES_PRUEBA)


def archivos_protegidos() -> list[Path]:
    vistos: set[Path] = set()
    for p in _archivos_del_proyecto():
        rel = p.relative_to(RAIZ).as_posix()
        if (cumple(rel, PATRONES_CODIGO) and es_prueba(rel)) or cumple(rel, PROTEGIDOS_QA):
            vistos.add(p)
    return sorted(vistos)


def huella(p: Path) -> str:
    # Normaliza fin de línea para que copiar entre Windows y Linux no dispare falsos positivos.
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def foto() -> int:
    datos = {str(p.relative_to(RAIZ)): huella(p) for p in archivos_protegidos()}
    FOTO.parent.mkdir(parents=True, exist_ok=True)
    FOTO.write_text(json.dumps({"fecha": datetime.now().isoformat(timespec="seconds"),
                                "archivos": datos}, indent=2), encoding="utf-8")
    print(f"Foto de {len(datos)} archivos protegidos → {FOTO.relative_to(RAIZ)}")
    return 0


def cambios_protegidos() -> list[str]:
    if not FOTO.is_file():
        return ["No hay foto previa: ejecuta `guardian.py foto` antes del paso B."]
    antes = json.loads(FOTO.read_text(encoding="utf-8"))["archivos"]
    ahora = {str(p.relative_to(RAIZ)): huella(p) for p in archivos_protegidos()}
    problemas = []
    for ruta in sorted(set(antes) | set(ahora)):
        if ruta not in ahora:
            problemas.append(f"archivo protegido eliminado: {ruta}")
        elif ruta not in antes:
            problemas.append(f"archivo protegido creado: {ruta}")
        elif antes[ruta] != ahora[ruta]:
            problemas.append(f"archivo protegido modificado: {ruta}")
    return problemas


def fuentes(prueba: bool) -> list[Path]:
    salida = []
    for p in _archivos_del_proyecto():
        rel = p.relative_to(RAIZ).as_posix()
        if p.suffix in EXTENSIONES and cumple(rel, PATRONES_CODIGO) and es_prueba(rel) == prueba:
            salida.append(p)
    return salida


def linea_de(texto: str, pos: int) -> int:
    return texto.count("\n", 0, pos) + 1


def revisar_codigo() -> list[str]:
    problemas = []
    literales_prueba: set[str] = set()
    for p in fuentes(prueba=True):
        texto = p.read_text(encoding="utf-8", errors="replace")
        literales_prueba |= {m.group(1) for m in LITERAL.finditer(texto)}
        for patron, motivo in TRAMPAS_PRUEBA:
            for m in patron.finditer(texto):
                problemas.append(f"{motivo}: {p.relative_to(RAIZ)}:{linea_de(texto, m.start())}")
    for p in fuentes(prueba=False):
        texto = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(RAIZ)
        for m in LITERAL.finditer(texto):
            if m.group(1) in literales_prueba:
                problemas.append(f"valor de prueba «{m.group(1)}» en código de producción: "
                                 f"{rel}:{linea_de(texto, m.start())}")
        for patron, motivo in TRAMPAS:
            for m in patron.finditer(texto):
                problemas.append(f"{motivo}: {rel}:{linea_de(texto, m.start())}")
    return problemas


def informe(titulo: str, problemas: list[str]) -> Path:
    sello = datetime.now().strftime("%Y%m%d-%H%M%S")
    ruta = INFORMES / f"guardian-{sello}.md"
    cuerpo = [f"# Guardián — {titulo}", "", f"Fecha: {sello}", "",
              "Clasificación: violación de reglas duras (plan §1.4 y §4 B4). Se escala a una persona.", ""]
    cuerpo += [f"- {p}" for p in problemas]
    cuerpo += ["", "Qué hacer: revisa el diff (`git diff`), revierte lo que viole las reglas y "
               "decide si la prueba es sospechosa (crear PREG) o si el código debe rehacerse."]
    ruta.write_text("\n".join(cuerpo) + "\n", encoding="utf-8")
    return ruta


def reportar(titulo: str, problemas: list[str]) -> int:
    if not problemas:
        print(f"Guardián ({titulo}): sin violaciones.")
        return 0
    print(f"Guardián ({titulo}): {len(problemas)} violación(es):")
    for p in problemas:
        print(f"  ✗ {p}")
    print(f"Informe: {informe(titulo, problemas).relative_to(RAIZ)}")
    return 1


def rojas(modulo: str) -> int:
    """Corre las pruebas del módulo con el comando de proyecto.json y exige que fallen por la razón correcta.

    Roja válida: el comando termina con código distinto de 0, la salida no contiene señales de
    error técnico (no compila, falta un módulo) salvo en la línea del mensaje «No implementado»,
    y no hay pruebas desactivadas. Si el comando sale con 0, las pruebas ya pasan: se reporta.
    """
    comando = PROYECTO_PY.comando_pruebas_modulo(PROYECTO, modulo)
    if not comando:
        print("Falta comandos.pruebas_modulo en proyecto.json.")
        return 1
    carpeta_pruebas = RAIZ / PROYECTO_PY.ruta_modulo(PROYECTO, modulo, "pruebas_modulo")
    if not carpeta_pruebas.is_dir() or not any(p.is_file() for p in carpeta_pruebas.rglob("*")):
        print(f"No hay pruebas en {PROYECTO_PY.ruta_modulo(PROYECTO, modulo, 'pruebas_modulo')}/.")
        return 1
    partes = shlex.split(comando)
    if os.name == "nt" and partes[0] in ("npm", "npx", "pnpm", "yarn"):
        partes[0] += ".cmd"
    directorio = RAIZ / (PROYECTO["comandos"].get("directorio") or ".")
    try:
        proc = subprocess.run(partes, cwd=directorio, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=900)
    except FileNotFoundError:
        print(f"No se encontró {partes[0]}: instala las dependencias del proyecto.")
        return 1
    except subprocess.TimeoutExpired:
        print("Las pruebas superaron 900 s.")
        return 1
    salida = proc.stdout + proc.stderr
    sello = datetime.now().strftime("%Y%m%d-%H%M%S")
    INFORMES.mkdir(parents=True, exist_ok=True)
    registro = INFORMES / f"rojas-{modulo}-{sello}.txt"
    registro.write_text(f"$ {comando}\ncódigo {proc.returncode}\n\n{salida}", encoding="utf-8")

    problemas = []
    no_implementado = PROYECTO["comandos"].get("senal_no_implementado") or "No implementado"
    if proc.returncode == 0:
        problemas.append("las pruebas ya pasan: no hay rojas que verificar (¿la prueba es una tautología?)")
    for senal in PROYECTO["comandos"].get("senales_error_tecnico", []):
        for linea in salida.splitlines():
            if senal in linea and no_implementado not in linea:
                problemas.append(f"error técnico en la salida («{senal}»): {linea.strip()[:160]}")
                break
    for p in carpeta_pruebas.rglob("*"):
        if p.is_file() and p.suffix in EXTENSIONES:
            texto = p.read_text(encoding="utf-8", errors="replace")
            for patron, motivo in TRAMPAS_PRUEBA:
                if patron.search(texto):
                    problemas.append(f"{motivo}: {p.relative_to(RAIZ).as_posix()}")
    print(f"Pruebas {modulo}: código {proc.returncode}. Salida: {registro.relative_to(RAIZ).as_posix()}")
    return reportar(f"rojas {modulo}", problemas)


def main() -> int:
    parser = argparse.ArgumentParser(description="Guardián mecánico de reglas duras.")
    parser.add_argument("accion", choices=["foto", "verificar", "revisar", "rojas"])
    parser.add_argument("--modulo", help="Módulo para `rojas`.")
    args = parser.parse_args()
    if args.accion == "foto":
        return foto()
    if args.accion == "verificar":
        return reportar("verificar", cambios_protegidos() + revisar_codigo())
    if args.accion == "revisar":
        return reportar("revisar", revisar_codigo())
    if not args.modulo:
        sys.exit("`rojas` requiere --modulo.")
    return rojas(args.modulo)


if __name__ == "__main__":
    raise SystemExit(main())
