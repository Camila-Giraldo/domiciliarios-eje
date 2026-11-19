#!/usr/bin/env python3
"""Prueba mecánica del kit de agentes SDD (sin LLM y sin API key).

Instala el kit con el ejemplo en una carpeta temporal y comprueba:
  1. proyecto.json del ejemplo es válido.
  2. Todos los prompts se arman sin marcadores sueltos y con sus skills.
  3. Las políticas de herramientas permiten y bloquean lo que deben.
  4. El orquestador pide la puerta del MVP en un proyecto nuevo.
  5. El guardián detecta que un paso B tocó una prueba.
  6. La evidencia de IA se registra.
  7. El kit no depende de ningún asistente externo ni de un proyecto concreto.

Uso:
    python qa/scripts/probar_todo.py
Código de salida: 0 si todo pasa.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

KIT = Path(__file__).resolve().parents[2]
RESULTADOS: list[tuple[str, bool, str]] = []


def caso(nombre: str, ok: bool, detalle: str = "") -> None:
    RESULTADOS.append((nombre, ok, detalle))


def cargar(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def correr(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp) / "proyecto"
        r = correr([sys.executable, str(KIT / "instalar.py"), str(raiz), "--ejemplo", "domiciliarios-eje"], KIT)
        caso("instalar.py con ejemplo", r.returncode == 0, r.stderr.strip()[-200:])

        r = correr([sys.executable, "agentes-ia/proyecto.py", "--validar"], raiz)
        caso("proyecto.json del ejemplo válido", r.returncode == 0, r.stdout.strip()[-300:])

        os.environ["SDD_PROYECTO"] = str(raiz)
        proyecto_py = cargar("proyecto", raiz / "agentes-ia" / "proyecto.py")
        proyecto = proyecto_py.cargar(raiz)

        # 2. prompts
        faltantes, sobrantes = [], []
        for carpeta in sorted((raiz / "agentes-ia" / "agentes").iterdir()):
            if not carpeta.is_dir():
                continue
            config = json.loads((carpeta / "config.json").read_text(encoding="utf-8"))
            texto = (carpeta / "prompt.md").read_text(encoding="utf-8")
            try:
                armado = proyecto_py.reemplazar(texto, proyecto, config.get("skills", []))
            except SystemExit as error:
                sobrantes.append(f"{carpeta.name}: {error}")
                continue
            if carpeta.name != "_plantilla" and "Domiciliarios Eje" not in armado:
                sobrantes.append(f"{carpeta.name}: no menciona el nombre del proyecto")
            for nombre in config.get("skills", []):
                if proyecto_py.buscar_skill(nombre, proyecto) is None:
                    faltantes.append(f"{carpeta.name}→{nombre}")
        caso("prompts sin marcadores sueltos", not sobrantes, "; ".join(sobrantes))
        esperados = {"frontend-interfaz-web→cliente-api-tipado", "frontend-interfaz-web→componentes-ui",
                     "frontend-interfaz-web→formularios", "qa-s3-generador-pruebas→plantilla-humo",
                     "qa-r1-humo→plantilla-humo"}
        inesperados = sorted(set(faltantes) - esperados)
        caso("skills resueltos (solo faltan los del perfil react-web, no activo en el ejemplo)",
             not inesperados, ", ".join(inesperados))

        # 3. políticas
        herramientas = cargar("herramientas", raiz / "agentes-ia" / "herramientas.py")
        ejecutor_b1 = herramientas.Ejecutor("B1", raiz=raiz)
        ejecutor_s1 = herramientas.Ejecutor("S1", raiz=raiz)

        def bloquea(ejecutor, ruta):
            try:
                ejecutor._puede_escribir(ruta)
                return False
            except PermissionError:
                return True

        politicas = [
            ("B1 escribe código", not bloquea(ejecutor_b1, "apps/api/src/modulos/pedidos/servicios/x.ts")),
            ("B1 no escribe pruebas", bloquea(ejecutor_b1, "apps/api/src/modulos/pedidos/pruebas/x.spec.ts")),
            ("B1 no escribe proyecto.json", bloquea(ejecutor_b1, "proyecto.json")),
            ("B1 no escribe el contexto", bloquea(ejecutor_b1, "CONTEXTO_PROYECTO.md")),
            ("S1 no escribe código", bloquea(ejecutor_s1, "apps/api/src/x.ts")),
            ("S1 escribe informes", not bloquea(ejecutor_s1, "qa/revision/informe-SPEC-001.md")),
        ]
        pruebas = herramientas.COMANDOS["pruebas"]
        politicas += [
            ("comando permitido", bool(pruebas.match("npx jest src/modulos/pedidos/pruebas"))),
            ("comando con shell bloqueado", not pruebas.match("npx jest x; rm -rf /")),
            ("comando no listado bloqueado", not pruebas.match("curl http://x")),
        ]
        malas = [n for n, ok in politicas if not ok]
        caso("políticas de herramientas", not malas, ", ".join(malas))

        # 4. orquestador
        r = correr([sys.executable, "orquestador.py", "--json"], raiz)
        try:
            siguiente = json.loads(r.stdout)["siguiente"][0]["paso"]
        except (json.JSONDecodeError, KeyError, IndexError):
            siguiente = f"error: {r.stderr.strip()[-200:]}"
        caso("orquestador pide la puerta del MVP", siguiente == "mvp", siguiente)

        # 5. guardián
        prueba = raiz / "apps" / "api" / "src" / "modulos" / "pedidos" / "pruebas" / "pedidos.spec.ts"
        prueba.parent.mkdir(parents=True, exist_ok=True)
        prueba.write_text("it('AC-001 / TC-001: x', () => { expect(1).toBe(2); });\n", encoding="utf-8")
        correr([sys.executable, "qa/scripts/guardian.py", "foto"], raiz)
        prueba.write_text("it('AC-001 / TC-001: x', () => { expect(1).toBe(1); });\n", encoding="utf-8")
        r = correr([sys.executable, "qa/scripts/guardian.py", "verificar"], raiz)
        caso("guardián detecta una prueba modificada", r.returncode == 1 and "modificado" in r.stdout, r.stdout.strip()[-200:])

        # 6. evidencias
        ruta = proyecto_py.registrar_evidencia(proyecto, "specification-agent", "modelo-x", "tarea de prueba",
                                               "contexto", "resultado")
        texto = ruta.read_text(encoding="utf-8")
        caso("evidencia registrada", "| specification-agent | modelo-x | tarea de prueba |" in texto)

    # 7. independencia
    prohibidos = re.compile(r"pharma|disfarma|\.claude|claude code|claude -p|opencode", re.I)
    hallazgos = []
    for p in KIT.rglob("*"):
        partes = p.relative_to(KIT).parts
        if not p.is_file() or ".git" in partes or "__pycache__" in partes or p.suffix not in (".py", ".md", ".json"):
            continue
        if p.name == "probar_todo.py":
            continue
        for n, linea in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if prohibidos.search(linea) and "primer proyecto" not in linea:
                hallazgos.append(f"{p.relative_to(KIT).as_posix()}:{n}")
    caso("sin dependencias de asistentes externos ni de otro proyecto", not hallazgos, ", ".join(hallazgos[:10]))

    print("Kit SDD — prueba mecánica\n")
    for nombre, ok, detalle in RESULTADOS:
        print(f"  {'✓' if ok else '✗'} {nombre}" + (f"\n      {detalle}" if detalle and not ok else ""))
    fallos = sum(1 for _, ok, _ in RESULTADOS if not ok)
    print(f"\n{len(RESULTADOS) - fallos}/{len(RESULTADOS)} pasan.")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
