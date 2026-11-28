# EPIC-004. Seguimiento, ubicación y Mini App — Historias de usuario

Estado: Aprobada por Camila (2026-11-19)
Fecha: 2026-11-19

Origen y validación:
- Generadas por `generador-hu-invest` (agentes-ia/salidas/generador-hu-invest/HU-005_20261119-0943_user-stories_epic-004_hu-26.md).
- Revisadas por `user-story-reviewer` (agentes-ia/salidas/user-story-reviewer/RHU-005_20261119-0945_story-review_epic-004.md).
- Correcciones elegidas por la estudiante y aplicadas por el asistente Claude Code (revisión de conflictos, 2026-11-19); aprobadas por Camila:
  1. Se descartó la HU-33 que agregó el revisor (cliente cancela antes de «en camino»): duplica HU-17 de EPIC-002 y repetía el número HU-33 de EPIC-005.
  2. HU-28: una novedad en camino deja el pedido en el estado final «con novedad» (DEC-E21 modificada).
  3. HU-29: el aviso por ubicación interrumpida llega al administrador y al empleado (DEC-E24 modificada).

---

### HU-26 — Inicio de entrega con ubicación en tiempo real

Yo, como domiciliario,
quiero cambiar el estado de un pedido asignado a «en camino» compartiendo mi ubicación en tiempo real,
para indicar que salí hacia la entrega y permitir el seguimiento del pedido por parte del negocio y del cliente.

Está hecho cuando:
- Dado un pedido en estado «listo para recoger» asignado a mi usuario, cuando comparto mi ubicación en tiempo real mediante el canal de interacción e inicio el trayecto, entonces el sistema me solicita confirmación antes de ejecutar la operación (contexto 3.7).
- Dado que confirmo la operación, cuando el sistema procesa el cambio, entonces actualiza el estado del pedido a «en camino», registra la fecha, la hora y el responsable (contexto 3.8), y envía un aviso al cliente informándole que su pedido va en camino con el acceso al mapa (DEC-E14, DEC-E17, DEC-E22).
- Dado un pedido asignado a mi usuario, cuando intento cambiar el estado a «en camino» sin haber compartido la ubicación en tiempo real, entonces el sistema rechaza la operación, mantiene el estado actual e informa que compartir la ubicación es obligatorio para iniciar el recorrido (DEC-E14).
- Dado un usuario con rol de cliente o un domiciliario distinto al asignado, cuando intenta cambiar el estado del pedido a «en camino», entonces el sistema rechaza la solicitud y no modifica la información del pedido (contexto 3.2, 3.8).

Cómo se simula en el prototipo: Se utiliza una cuenta de prueba de domiciliario en Telegram compartiendo una ubicación en directo fijada en 15 minutos sobre un pedido precargado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: La historia es independiente porque opera a partir de un pedido asignado. Incorpora las reglas críticas de confirmación y trazabilidad sin incluir detalles técnicos de implementación.

---

### HU-27 — Confirmación de entrega del pedido

Yo, como domiciliario,
quiero marcar un pedido en camino como «entregado»,
para dar por finalizado el servicio, suspender la transmisión de mi ubicación y liberar mi cupo de carga asignada.

Está hecho cuando:
- Dado un pedido en estado «en camino» bajo mi responsabilidad, cuando elijo la opción de entrega completada, entonces el sistema me solicita confirmación previa antes de ejecutar el cambio (contexto 3.7).
- Dado que confirmo la entrega, cuando el sistema procesa la solicitud, entonces actualiza el estado a «entregado», registra fecha, hora y responsable (contexto 3.8), cesa la disponibilidad de mi ubicación en tiempo real para el cliente (DEC-E14) y notifica al cliente que su entrega concluyó con éxito (DEC-E17, DEC-E22).
- Dado un pedido que no se encuentra en estado «en camino», cuando intento marcarlo como «entregado», entonces el sistema no permite el cambio y notifica que el servicio no está en ruta.

Cómo se simula en el prototipo: Se confirma la entrega pulsando el botón correspondiente en el bot de Telegram para un pedido de prueba en estado «en camino».

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es valiosa y fácil de probar al cerrar el ciclo de vida feliz del pedido, garantizando la privacidad de la ubicación del domiciliario una vez entregado el producto.

---

### HU-28 — Registro de novedad en la entrega

Yo, como domiciliario,
quiero registrar una novedad sobre un pedido que llevo en camino,
para reportar oportunamente los impedimentos de la entrega y alertar al negocio para que tome decisiones.

Está hecho cuando:
- Dado un pedido en estado «en camino» asignado a mi usuario, cuando selecciono registrar novedad y elijo una opción del catálogo de novedades `[por definir con el equipo]`, entonces el sistema me solicita confirmación antes de guardar el registro (contexto 3.7).
- Dado que confirmo la novedad, cuando el sistema la registra, entonces guarda el motivo, la fecha, la hora y el responsable (contexto 3.8), cesa el seguimiento en mapa para el cliente (DEC-E14) y envía un aviso inmediato con los detalles del suceso al administrador del negocio y al empleado o vendedor (DEC-E22, DEC-E25).
- Dado que se registró la novedad, cuando el sistema la procesa, entonces el pedido pasa al estado final «con novedad», libera mi cupo de carga y deja de aceptar otros cambios de estado (DEC-E21).
- Dado un pedido que ya está en estado «entregado», «cancelado» o «con novedad», cuando intento registrar una novedad, entonces el sistema rechaza la acción informando que el servicio ya finalizó (DEC-E13, DEC-E22).

Cómo se simula en el prototipo: Se muestran dos opciones ficticias de novedad (cliente ausente y dirección no encontrada) desde botones interactivos en el chat de Telegram.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Delimita adecuadamente la contingencia durante el transporte sin inventar tipos de novedades no definidos, los cuales quedan marcados como pendientes.

---

### HU-29 — Notificación por interrupción de ubicación en camino

Yo, como empleado o vendedor,
quiero recibir una alerta si un domiciliario en ruta deja de compartir su ubicación,
para verificar la última posición conocida, solicitarle la reactivación y coordinar el despacho sin cancelar el pedido.

Está hecho cuando:
- Dado un pedido en estado «en camino» perteneciente a mi negocio, cuando el domiciliario interrumpe la transmisión de su ubicación en tiempo real, entonces el sistema mantiene el pedido en estado «en camino», le pide al domiciliario reactivar su ubicación y envía una alerta al empleado o vendedor y al administrador del negocio notificando la pérdida de señal (DEC-E24, DEC-E25).
- Dado que se interrumpió la ubicación de un domiciliario en camino, cuando el sistema lo detecta, entonces avisa al administrador del negocio y al empleado o vendedor (DEC-E24).
- Dado que se interrumpió la señal, cuando el empleado o vendedor o el administrador del negocio consulta el mapa del servicio, entonces el sistema presenta la última posición registrada junto con la hora exacta de ese registro (DEC-E24).
- Dado que el domiciliario reactiva la transmisión de su ubicación, cuando el sistema detecta nuevamente la señal, entonces actualiza el mapa con la nueva posición y continúa el seguimiento en tiempo real sin reiniciar el pedido (DEC-E24).

Cómo se simula en el prototipo: Se interrumpe intencionalmente el envío de ubicación en vivo desde el Telegram de prueba del domiciliario y se comprueba el aviso generado al empleado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Resuelve de forma independiente la pérdida momentánea de señal GPS sin alterar el estado del pedido y manteniendo la trazabilidad del último punto conocido.

---

### HU-30 — Seguimiento del pedido en mapa por el cliente

Yo, como cliente,
quiero ver en un mapa interactivo la ubicación del domiciliario que transporta mi pedido en camino,
para conocer el avance de mi entrega en tiempo real de forma segura.

Está hecho cuando:
- Dado un pedido propio en estado «en camino», cuando abro el enlace de seguimiento recibido en la notificación de estado (DEC-E17), entonces el sistema presenta el mapa interactivo mostrando exclusivamente la posición del domiciliario asignado a mi pedido y la dirección de entrega correspondiente (DEC-E16).
- Dado el mapa interactivo en pantalla, cuando el pedido pasa a estado «entregado» o «con novedad», entonces el sistema retira el mapa en tiempo real y muestra un mensaje de servicio concluido (DEC-E14, DEC-E16).
- Dado un cliente autenticado, cuando intenta abrir el enlace de seguimiento de un pedido de otro cliente o de otro negocio, entonces el sistema le deniega el acceso y no revela posiciones ni datos ajenos (contexto 3.3, DEC-E16).

Cómo se simula en el prototipo: Se accede a la Mini App de Telegram mediante el botón de aviso recibido en la sesión de un cliente ficticio que tiene un pedido en camino.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: La historia cumple con INVEST al otorgar valor directo al cliente respetando los límites de visibilidad y protección de datos personales de ubicación.

---

### HU-31 — Monitoreo de domiciliarios en ruta por el negocio

Yo, como administrador del negocio,
quiero ver en un mapa interactivo a todos los domiciliarios de mi establecimiento que se encuentran en camino,
para supervisar el avance global de las entregas y balancear la operación.

Está hecho cuando:
- Dado un administrador del negocio o un empleado o vendedor autenticado, cuando abre la vista de monitoreo en ruta de su negocio, entonces el sistema muestra en el mapa interactivo a todos los domiciliarios de su establecimiento con pedidos en estado «en camino» (DEC-E16).
- Dado un usuario con rol de domiciliario o cliente, cuando intenta acceder a la vista de monitoreo general del negocio, entonces el sistema rechaza el acceso por falta de permisos (contexto 3.2, DEC-E16).
- Dado un domiciliario que pertenece a otro negocio, cuando se encuentra en ruta activa, entonces el sistema garantiza que su posición no se visualice en el mapa del establecimiento consultado (contexto 3.3).

Cómo se simula en el prototipo: Se visualiza la Mini App administrativa con dos domiciliarios ficticios en ruta pertenecientes al mismo negocio.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Establece con claridad los límites de acceso por rol y por negocio, permitiendo verificar la vista consolidada de domiciliarios en ruta sin cruzar datos entre establecimientos.

---

### HU-32 — Consulta de historial de recorrido de un pedido finalizado

Yo, como administrador del negocio,
quiero consultar el recorrido realizado por un domiciliario en un pedido finalizado durante el tiempo de conservación fijado,
para revisar inquietudes o aclaraciones sobre el trayecto de la entrega antes de su borrado.

Está hecho cuando:
- Dado un pedido finalizado de mi negocio cuya entrega ocurrió dentro del plazo de conservación `[por definir con el equipo]`, cuando consulto el detalle de su recorrido, entonces el sistema despliega el trazado histórico desde la salida hasta el punto de entrega (DEC-E15).
- Dado un pedido finalizado cuya antigüedad supera el plazo de conservación `[por definir con el equipo]`, cuando se consulta su detalle, entonces el sistema informa que el historial de recorrido ha sido eliminado por política de privacidad de datos sensibles, manteniendo únicamente la fecha, la hora, el estado final y el responsable (contexto 3.3, 3.8, DEC-E15).
- Dado un usuario perteneciente a otro negocio, cuando intenta consultar el recorrido de este pedido, entonces el sistema bloquea el acceso por separación de datos (contexto 3.3).

Cómo se simula en el prototipo: Se consultan puntos de ruta almacenados de un pedido de muestra marcado como entregado hace pocas horas frente a otro cuya fecha excede el límite de prueba.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Aborda el almacenamiento temporal de datos de ubicación geográfica manteniendo como parámetro pendiente el tiempo de retención sin afectar la estimación.
