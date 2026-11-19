---
name: cuando-escalar
description: Condiciones para detener un bucle automático y preguntar a una persona. Úsalo en B4 cuando un fallo no avanza o afecta una aserción, la concurrencia, los permisos o los datos sensibles. Evita bucles infinitos y arreglos que ocultan defectos.
---
# Cuándo escalar

Escala a una persona (y deja de corregir) cuando se cumpla **cualquiera** de estas condiciones:

## Por número de intentos

- 3 iteraciones sin que la prueba pase.
- El mismo error aparece dos veces seguidas sin cambio en el código.
- El tiempo de ejecución o el consumo de recursos crece sin explicación.

## Por el tipo de arreglo

- El arreglo exige cambiar una SPEC, un AC, un TC o un oráculo.
- El arreglo exige tocar una prueba.
- El arreglo exige skip, only, bajar un umbral o capturar una excepción para ocultar el fallo.
- El valor esperado no está en el TC y habría que «deducirlo» del código.

## Por el dominio

- Falla una prueba de **concurrencia** sobre un recurso compartido.
- Falla una prueba de **permisos o separación de datos** (un usuario ve u opera datos ajenos).
- Falla una prueba de **datos sensibles** (mensajes o logs que exponen datos de la lista del proyecto).
- Falla una prueba ligada a una **regla crítica** del proyecto o a una norma del contexto.
- No hay SPEC o decisión para el comportamiento esperado.

## Por el entorno

- El fallo es de infraestructura (contenedor, puerto, migración, credenciales) y no se reproduce de forma determinista.
- El entorno de prueba no está disponible o no coincide con la versión desplegada.

## Cómo escalar

1. Detén el bucle. No sigas «probando suerte».
2. Crea o actualiza `docs/preguntas/PREG-xxx.md` con:
   - la prueba y el error exacto;
   - las iteraciones hechas y qué cambió en cada una;
   - la evidencia (log enmascarado);
   - la decisión que necesitas.
3. Propón marcar el TC como `escalado` en `qa/trazabilidad.md`.
4. Devuelve un resumen con: qué falla, qué probaste, qué necesitas y qué no tocarás.
