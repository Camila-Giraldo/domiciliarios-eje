---
name: plantillas-sin-datos-sensibles
description: Reglas y plantillas fijas para mensajes, notificaciones, errores y logs que no exponen los datos sensibles del proyecto. Úsalo en B1, B2, B3 y en cualquier agente que produzca texto visible.
---
# Plantillas sin datos sensibles

## Regla

Los datos sensibles son los de la lista `datos_sensibles` de proyecto.json (por ejemplo: documentos de identidad, teléfonos, correos, direcciones, datos de salud o financieros).

- **Ningún** log, fixture, ejemplo ni respuesta de error incluye esos datos reales. Los datos de prueba son sintéticos.
- Un mensaje o notificación muestra un dato sensible **solo** si la SPEC lo autoriza para el rol que lo recibe y solo el mínimo necesario (por ejemplo, la dirección de entrega al responsable asignado de ese pedido, y a nadie más).
- Los mensajes se escriben como plantillas fijas en un solo archivo, con identificadores internos en lugar de datos personales.

## Plantillas genéricas (adáptalas a la SPEC)

| Situación | Plantilla |
|---|---|
| Operación confirmada | «Tu solicitud #<id> fue confirmada.» |
| Cambio de estado | «La solicitud #<id> cambió a <estado>.» |
| Recordatorio | «Tienes una actividad pendiente: #<id>.» |
| Cancelación | «La solicitud #<id> fue cancelada.» |
| Sin permiso | «No tienes permiso para esta operación.» |
| No encontrado o ajeno | «No encontramos lo que buscas.» (no revela si existe en otro negocio o de otra persona) |
| Error genérico | «No pudimos completar la operación. Intenta de nuevo.» |
| Entrada no válida | «Revisa los datos e intenta de nuevo.» |
| Comando desconocido (chat) | «No reconozco ese comando. Usa el menú.» |

## Lista blanca de campos para logs

```text
evento, id interno de la entidad, id interno del negocio o tenant, estado anterior, estado nuevo,
rol que actuó, canal, duración, conteos, resultado, versión, id de correlación
```

Prohibidos en logs: cualquier campo de `datos_sensibles`, nombres de personas, textos libres escritos por usuarios y cuerpos completos de peticiones o respuestas.

## Prohibiciones

- No interpoles datos sensibles en plantillas que van a roles no autorizados.
- No registres el cuerpo completo de una petición o respuesta.
- No imprimas en consola datos de la solicitud.
- No guardes datos sensibles en el almacenamiento del navegador, en la analítica ni en el estado de una conversación de chat.

## Verificación

- Busca en el código y en los logs de prueba los valores de la lista de datos sintéticos.
- Una prueba debe verificar que ningún log expone un dato sensible.
- Una prueba debe verificar que un rol no autorizado no recibe el dato en un mensaje.
- Si encuentras una fuga, es un hallazgo **bloqueante** de tipo `datos-sensibles`.
