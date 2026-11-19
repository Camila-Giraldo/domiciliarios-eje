# Documentación del proyecto — guía del flujo SDD

Esta carpeta es la fuente de verdad del flujo guiado por especificaciones. Ningún agente decide alcance por su cuenta.

## Orden del flujo

```text
Necesidad
  → Generador de HU / Revisor de HU (opcional)
  → Agente de Especificaciones (SPEC-*)
  → Agente de Arquitectura (ARQ-*)
  → docs/mvp.md: Requisitos (Especificaciones) + Corte técnico (Arquitectura)
  → Puerta humana: una persona escribe aprobado_por en docs/mvp.md
  → QA shift-left: S1 revisa → S2 diseña casos y oráculos → S3 genera pruebas rojas
  → Puerta humana: aprobar oráculos
  → Construcción: B1, B2, B3 + B4 hasta verde
  → QA shift-right: R1 humo sobre el entorno desplegado (R2 si falla)
  → Puerta humana: aprobar entrega
```

## Quién es dueño de qué

| Archivo o carpeta | Dueño | Regla |
|---|---|---|
| `proyecto.json` y el archivo de contexto | Persona | Configuran el kit; ningún agente los escribe. |
| `agentes-ia/salidas/specification-agent/` | Especificaciones | SPEC por estado; `aprobadas/` es la única fuente de SPEC aprobadas. |
| `agentes-ia/salidas/architecture-agent/` | Arquitectura | ARQ por estado. |
| `docs/arquitectura/propuesta-tecnologica.md` | Persona (lo propone Arquitectura) | Stack aprobado. |
| `docs/mvp.md` → Requisitos | Especificaciones | Arquitectura no la edita; deja observaciones. |
| `docs/mvp.md` → Corte técnico | Arquitectura | Especificaciones no la edita; deja observaciones. |
| `docs/preguntas/` | Cualquier agente que detecte una ambigüedad | Una pregunta por archivo `PREG-xxx.md`. |
| `docs/decisiones.md` | Persona | Decisiones del equipo con id `DEC-Pxx`. |
| `docs/evidencias-ia.md` | Runtime + persona | El runtime agrega filas; la persona llena «Validación». |
| `qa/revision/` | S1 | Informes de revisión estática. |
| `qa/casos/` | S2 | Casos `TC-*.md` con su oráculo. |
| `qa/trazabilidad.md` | S2, S3 | Se actualiza, no se reescribe sin evidencia. |
| Código (`rutas.codigo`) | B1–B4 | B4 solo corrige código de producción. |
| `qa/ejecuciones/` | B4, R1 y runtime | Registros `RUN-*.json` y bitácoras; solo se agregan. |
| `qa/humo/` | R1 | Reportes de humo. |
| `qa/incidentes/` | R2 | Triage de solo lectura. |
| `pipeline.json` | Orquestador y `marcar.py` | Estado del flujo; no es una decisión de alcance. |

## Puertas humanas

1. Aprobar cada SPEC y cada ARQ.
2. Aprobar `docs/mvp.md` (con `aprobado_por`).
3. Aprobar los oráculos (`qa/oraculos-pendientes.md`).
4. Aprobar la entrega (humo verde y evidencias validadas).

Sin estas aprobaciones, el orquestador no habilita el siguiente paso.
