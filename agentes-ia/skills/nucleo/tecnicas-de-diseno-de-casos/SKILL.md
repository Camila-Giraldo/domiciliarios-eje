---
name: tecnicas-de-diseno-de-casos
description: Elige y aplica la técnica de diseño de casos según el tipo de regla. Úsalo en S2 para derivar condiciones de prueba de cada AC con particiones de equivalencia, valores límite, tablas de decisión, transición de estados o Dado/Cuando/Entonces.
---
# Técnicas de diseño de casos

## Cuándo usar cada una

| Tipo de regla | Técnica | Ejemplo |
|---|---|---|
| Cantidades, tiempos, intentos, días | Particiones de equivalencia + valores límite | Límite N: N-1, N, N+1; 10 min: 9:59, 10:00, 10:01. |
| Combinaciones de reglas de negocio y permisos | Tabla de decisión | Rol × acción × pertenencia del dato (propio/ajeno). |
| Ciclos de vida | Transición de estados | Estados de la entidad de la SPEC: válidas, inválidas y finales. |
| Criterios de aceptación | Dado/Cuando/Entonces | Un caso por AC, más negativos y límites. |
| Flujos de usuario | Recorrido + alternativas | Camino feliz, error de validación, reintento. |
| Concurrencia | Ejecución paralela controlada | N intentos paralelos sobre K recursos ⇒ máximo K éxitos (números de la SPEC). |

## Procedimiento

1. Lee el AC y subraya las condiciones y el resultado observable.
2. Identifica los parámetros de entrada y sus rangos.
3. Aplica la técnica y escribe las condiciones de prueba.
4. Para cada condición, crea un `TC-xxx` con precondiciones, pasos, datos y resultado esperado.
5. Asigna el oráculo con `politica-de-oraculos`.
6. Añade al menos un caso negativo y uno de límite por regla numérica.
7. Si la SPEC menciona concurrencia, escribe el caso paralelo con el número exacto de intentos y el máximo esperado.

## Tabla de decisión (ejemplo)

| # | Rol | Dato | Acción permitida por la SPEC | Resultado |
|---|---|---|---|---|
| 1 | administrador | propio | sí | la operación se realiza |
| 2 | empleado | propio | no | rechazo con mensaje genérico |
| 3 | administrador | de otro negocio u otra persona | — | rechazo; no se revela que el dato existe |
| 4 | sin sesión | — | — | se pide autenticación |

## Reglas

- Un AC puede generar varios TC; un TC puede cubrir un solo AC.
- No dupliques casos con los mismos valores de equivalencia.
- Los datos son sintéticos.
- Si no puedes decidir el resultado esperado, no inventes: `PREG-xxx`.
