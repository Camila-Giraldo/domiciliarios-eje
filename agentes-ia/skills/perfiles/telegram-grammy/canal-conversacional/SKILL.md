---
name: canal-conversacional
description: Perfil telegram-grammy. Patrón para handlers de grammY con webhook, vinculación, plantillas fijas, botones de confirmación y pruebas con updates simulados. Úsalo en B2.
---
# Handlers de grammY

## Estructura

```text
apps/api/src/entradas/telegram/
├─ telegram.module.ts
├─ bot.ts              crea el bot y registra handlers
├─ handlers/           comandos y callbacks
├─ plantillas.ts       todos los textos fijos
└─ pruebas/            updates simulados
```

## Reglas

- El handler **solo** llama a la `api/` del módulo. No contiene reglas de negocio.
- No crea tablas ni usa Prisma directamente.
- La vinculación o autenticación usa el flujo que defina la SPEC. El id de Telegram identifica el chat; no prueba identidad salvo decisión aprobada. Nunca guardes datos sensibles en el estado de la conversación.
- Operaciones importantes: botón de confirmación (inline keyboard) antes de llamar a la API.
- Mini App: el backend valida la firma de `initData` con el token del bot.
- Todos los textos salen de `plantillas.ts`; no se interpolan datos sensibles no autorizados.
- Comandos desconocidos y errores: mensaje genérico.
- Webhook en el mismo servidor NestJS; token solo por variable de entorno.
- Pruebas con `bot.handleUpdate(update)`; nunca llames a Telegram real.

## Plantilla de handler

```ts
bot.command('start', async (ctx) => {
  await ctx.reply(PLANTILLAS.inicio);
});

bot.on('message:text', async (ctx) => {
  await ctx.reply(PLANTILLAS.noReconocido);
});
```

## Verificación

- La respuesta no contiene datos sensibles de la lista sintética del proyecto.
- El segundo mensaje del mismo flujo no duplica la acción.
- Los errores no filtran detalles internos.
