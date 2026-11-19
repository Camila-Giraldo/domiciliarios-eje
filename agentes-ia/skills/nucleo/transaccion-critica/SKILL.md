---
name: transaccion-critica
description: Patrón para operaciones que compiten por un recurso compartido (cupos, existencias, asignaciones, cambios de estado) con transacción, UPDATE condicional y rollback. Úsalo en B1, en Arquitectura y en las pruebas de concurrencia.
---
# Transacción crítica

## Problema

Dos personas actúan al mismo tiempo sobre el mismo recurso: el último cupo, la última unidad, el mismo pedido sin asignar o el mismo registro que cambia de estado. Sin control, ambas operaciones se confirman y aparece una **sobreasignación** o un estado imposible.

## Patrón (SQL de referencia; tradúcelo al ORM del stack)

```sql
BEGIN;

-- La condición va dentro del WHERE: solo actualiza si el recurso sigue disponible.
UPDATE recurso
SET disponible = disponible - :cantidad
WHERE id = :recurso AND tenant_id = :tenant AND disponible >= :cantidad;
-- 0 filas afectadas → ROLLBACK y responder «sin disponibilidad».

-- Cambio de estado: solo desde el estado esperado.
UPDATE entidad
SET estado = :nuevo, responsable_id = :responsable, actualizado_en = now()
WHERE id = :entidad AND tenant_id = :tenant AND estado = :estado_esperado;
-- 0 filas afectadas → ROLLBACK y responder «la operación ya no es posible».

INSERT INTO historial (entidad_id, estado_anterior, estado_nuevo, actor_id, fecha) VALUES (...);

COMMIT;
```

## Reglas

1. La condición (`disponible >= cantidad`, `estado = esperado`, `responsable IS NULL`) va **dentro del `WHERE`**. No leas el valor y luego actualices: eso abre la ventana de carrera.
2. Todo lo que debe ocurrir junto se confirma **junto o nada**. Si un `UPDATE` no afecta filas, `ROLLBACK`.
3. Cada `UPDATE` filtra también por el negocio o tenant del usuario: la separación de datos es parte de la condición.
4. Cada cambio de estado deja su registro de historial (fecha, estado, responsable) en la misma transacción.
5. Idempotencia: si llega un reintento de la misma operación, no la dupliques. Usa una clave de idempotencia.
6. No implementes la operación en memoria, en la interfaz ni en el canal de chat: solo en el backend.

## Prueba obligatoria de concurrencia

```text
N intentos en paralelo sobre K recursos disponibles ⇒ como máximo K éxitos.
(N y K salen de la SPEC; si la SPEC no los da, es una PREG, no un número inventado.)
```

- Usa la base de datos real del stack (contenedor de prueba), no un mock.
- Lanza los intentos en paralelo y espera todos los resultados.
- Verifica: éxitos ≤ K, ningún valor negativo, ningún estado imposible, historial coherente y rechazos con mensaje genérico.

## Errores que no se aceptan

- `SELECT` seguido de `UPDATE` sin bloqueo.
- Bajar el número de intentos de la prueba para que pase.
- Capturar la excepción y devolver «ok».
- Confirmar la operación y luego intentar descontar o cambiar el estado.
