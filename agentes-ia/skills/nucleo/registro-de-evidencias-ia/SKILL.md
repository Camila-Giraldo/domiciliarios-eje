---
name: registro-de-evidencias-ia
description: Cómo queda la evidencia de cada uso de un agente (agente, tarea, contexto, resultado y validación humana) en docs/evidencias-ia.md. Úsalo al cerrar cualquier ejecución y al preparar la entrega.
---
# Registro de evidencias de IA

## Qué se registra

Cada ejecución de un agente deja una fila en el archivo de `evidencias` de proyecto.json (por defecto `docs/evidencias-ia.md`):

| Columna | Quién la llena | Contenido |
|---|---|---|
| Fecha | runtime | Fecha y hora de la ejecución. |
| Agente | runtime | Nombre del agente (y paso del pipeline, si aplica). |
| Modelo | runtime | Modelo que respondió (incluido el de respaldo si se usó). |
| Tarea | runtime | La petición o tarea que recibió el agente. |
| Contexto suministrado | runtime | Archivo de contexto, adjuntos, módulo y skills. |
| Resultado | runtime | Archivo generado, versión y estado, o código y resumen del paso. |
| Validación de la persona | persona | Qué revisó, qué corrigió, si aceptó o descartó el resultado y por qué. |

`agente.py` y `herramientas.py` escriben las seis primeras columnas solos. La última empieza en `pendiente`.

## Reglas

1. No borres filas. Si un resultado se descarta, escríbelo en la validación.
2. La validación la escribe una persona; un agente nunca la llena.
3. Una validación útil dice qué se comparó (por ejemplo, «revisé los 12 AC contra la sección 3 del contexto; corregí AC-004»), no solo «ok».
4. No pegues datos personales reales en la tabla.
5. Si un agente se ejecutó fuera del runtime (a mano, en otra herramienta), agrega la fila a mano con las mismas columnas.

## Para la entrega

- La tabla completa es la evidencia del uso crítico y verificable de los agentes.
- Filtra por agente para mostrar qué hizo cada uno y cómo se validó.
- Enlaza los archivos de la columna «Resultado» (SPEC, ARQ, informes, RUN) en la documentación.
