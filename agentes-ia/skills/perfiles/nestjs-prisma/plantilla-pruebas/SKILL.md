---
name: plantilla-pruebas
description: Perfil nestjs-prisma. Estructura de pruebas con Jest + Testcontainers (+ Playwright y grammY simulado si esos perfiles están activos). Úsalo en S3 al convertir casos TC-* en pruebas ejecutables que fallan primero.
---
# Plantilla Jest + NestJS + Testcontainers + Playwright

## Dónde va cada prueba

| Qué se prueba | Herramienta | Ubicación |
|---|---|---|
| Reglas de dominio puras | Jest unitario | `apps/api/src/modulos/<x>/pruebas/dominio.spec.ts` |
| Servicios y API | Jest + Nest Testing | `apps/api/src/modulos/<x>/pruebas/servicios.spec.ts` |
| Base de datos y transacciones | Jest + Testcontainers PostgreSQL | `apps/api/src/modulos/<x>/pruebas/integracion.spec.ts` |
| Concurrencia | Jest + Testcontainers + `Promise.allSettled` | `apps/api/src/modulos/<x>/pruebas/concurrencia.spec.ts` |
| Flujos web | Playwright | `apps/web/e2e/<flujo>.spec.ts` |
| Bot Telegram | grammY con updates simulados | `apps/api/src/entradas/telegram/pruebas/` |
| Servicios externos (SMS, correo, pagos) | Stub/spy del proveedor | junto al servicio que los usa |

## Convención de nombres

```ts
it('AC-036 / TC-041: <resultado esperado del TC>', async () => { ... });
it('@supuesto AC-012 / TC-018: ...', async () => { ... });
```

## Unitario (dominio)

```ts
describe('Regla de dominio', () => {
  it('AC-031 / TC-001: rechaza la operación si el recurso no está disponible', () => {
    const recurso = crearRecurso({ capacidad: 1, ocupados: 1 });
    expect(puedeOcupar(recurso)).toBe(false);
  });
});
```

## Integración con Testcontainers

```ts
import { PostgreSqlContainer } from '@testcontainers/postgresql';

let container: StartedPostgreSqlContainer;

beforeAll(async () => {
  container = await new PostgreSqlContainer().start();
  // aplicar migraciones del módulo
}, 60_000);

afterAll(async () => { await container.stop(); });
```

## Concurrencia (números de la SPEC)

```ts
it('AC-036 / TC-036: N intentos sobre K recursos dejan máximo K éxitos', async () => {
  const intentos = Array.from({ length: N }, () => operar(datos));
  const resultados = await Promise.allSettled(intentos);
  const exitos = resultados.filter(r => r.status === 'fulfilled' && r.value.ok).length;
  expect(exitos).toBeLessThanOrEqual(K);
});
```

## grammY simulado

```ts
const update = { message: { text: '/start', chat: { id: 1 } } } as Update;
await bot.handleUpdate(update);
expect(respuestas[0]).toContain('<texto de la plantilla>');
expect(respuestas[0]).not.toMatch(DATOS_SINTETICOS_SENSIBLES);
```

## Reglas

1. La prueba debe fallar por «no implementado», no por error de sintaxis.
2. No toques código de producción.
3. No uses `skip`/`only` para evitar fallos.
4. Datos sintéticos y plantillas fijas.
5. Toda prueba debe poder rastrearse a un `TC` y un `AC`.
