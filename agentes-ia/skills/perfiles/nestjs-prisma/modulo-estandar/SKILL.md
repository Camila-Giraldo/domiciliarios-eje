---
name: modulo-estandar
description: Perfil nestjs-prisma. Estructura y reglas para implementar un módulo NestJS con fronteras, Prisma por esquema y pruebas. Úsalo en B1 al crear un módulo nuevo o completar uno existente.
---
# Módulo NestJS estándar

## Estructura

```text
apps/api/src/modulos/<nombre>/
├─ api/           servicio que exporta el módulo (única puerta de entrada)
├─ dominio/       reglas puras, sin I/O
├─ servicios/     casos de uso
├─ datos/         repositorio Prisma + migración del esquema
├─ pruebas/       Jest unitario, integración y concurrencia
└─ <nombre>.module.ts
```

## Fronteras

- Un módulo solo accede a datos ajenos por la `api/` del otro módulo.
- Nadie importa `datos/` de otro módulo.
- Un esquema PostgreSQL por módulo (el nombre del módulo de proyecto.json).
- Toda consulta filtra por el negocio o tenant del usuario cuando el proyecto separa datos por negocio.
- El controlador no contiene reglas: delega en `servicios/`.
- El dominio no importa NestJS, Prisma ni HTTP.

## Orden de implementación

1. Plan de 5 a 8 pasos antes de escribir código.
2. `dominio/` + pruebas unitarias.
3. `datos/` + migración + pruebas de integración con Testcontainers.
4. `servicios/` + pruebas.
5. `api/` y controladores + DTO.
6. Tareas programadas (por ejemplo, pg-boss) en `comunes/` si aplica; siempre idempotentes.

## Validación y errores

- DTO + Zod o class-validator en el borde.
- Errores con plantillas fijas; nunca incluyen datos sensibles (skill `plantillas-sin-datos-sensibles`).
- Logs con pino y lista blanca de campos.

## Pruebas

```bash
<comandos.pruebas_modulo de proyecto.json>
```

No modifiques las pruebas: si una parece incorrecta, `PREG-xxx`.
