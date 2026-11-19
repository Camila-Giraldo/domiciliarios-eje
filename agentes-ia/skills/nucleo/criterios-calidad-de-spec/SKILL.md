---
name: criterios-calidad-de-spec
description: Lista de comprobación para revisar si una SPEC es verificable, no ambigua, completa, consistente y trazable. Úsalo en S1 antes de diseñar casos o escribir pruebas.
---
# Criterios de calidad de una SPEC

## 1. Verificable

- Existe una observación concreta que dice pasa/no pasa.
- El resultado esperado es observable desde fuera del sistema.
- No depende de «que funcione bien» ni de la opinión de quien prueba.

## 2. No ambigua

Señala y cita:

- Términos vagos: «rápido», «adecuado», «fácil», «amigable», «óptimo», «según corresponda».
- Sujeto omitido: «se valida», «se notifica» (¿quién?).
- «Etc.», «y demás», «entre otros».
- Números sin unidad o sin límite.
- Dos reglas distintas para el mismo caso.

## 3. Completa

- Casos de error, cancelación y excepción.
- Valores límite: por debajo, en el límite y por encima.
- Estados y transiciones, con quién provoca cada una.
- Quién ejecuta la acción, con qué verificación y sobre qué datos (roles, permisos y pertenencia).
- Qué pasa si falla una dependencia externa.
- Qué se considera un duplicado y qué pasa con él.

## 4. Consistente

- No choca con otro RF, BR, AC, flujo o caso límite.
- Los mismos números en todas las secciones.
- Coincide con la sección 3 del contexto del proyecto.
- No contradice las restricciones (sección 4), el contexto normativo (sección 6) ni las reglas críticas del proyecto.

## 5. Trazable

- Cada RF tiene al menos un AC.
- Cada AC apunta a un RF.
- Cada BR y cada CL crítico tiene AC.
- La sección de trazabilidad no tiene huecos.

## Valores límite

Haz una tabla con **todos** los números que aparecen en la SPEC (cantidades, tiempos, intentos, plazos, capacidades):

| Valor | Debajo | En el límite | Por encima |
|---|---|---|---|
| <número de la SPEC> | sí/no | sí/no | sí/no |

Un número sin AC en los tres lados es un hallazgo.

## Veredicto

- `APTA`: sin hallazgos bloqueantes.
- `APTA_CON_RESERVAS`: hallazgos no bloqueantes o preguntas abiertas.
- `NO_APTA`: al menos un bloqueante. El módulo se detiene.
