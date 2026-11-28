# EPIC-003. Asignación y despacho — Historias de usuario

Estado: Aprobada por Camila (2026-11-19)
Fecha: 2026-11-19

Origen y validación:
- Generadas por `generador-hu-invest` (agentes-ia/salidas/generador-hu-invest/HU-003_20261119-0930_user-stories_epic-003_hu-19.md).
- Revisadas por `user-story-reviewer` (agentes-ia/salidas/user-story-reviewer/RHU-003_20261119-0938_story-review_epic-003.md).
- Correcciones elegidas por la estudiante y aplicadas por el asistente Claude Code (revisión de conflictos, 2026-11-19); aprobadas por Camila:
  1. HU-19: el paso de «recibido» a «en preparación» es la confirmación del pedido (HU-16); HU-19 solo marca «listo para recoger» (DEC-E21).
  2. HU-20 y HU-21: un domiciliario no disponible no se ofrece para asignar (DEC-E31); las asignaciones pendientes de respuesta cuentan para el tope (DEC-E30).
  3. HU-24: el domiciliario ve nombre, dirección, referencias y teléfono del cliente solo mientras el pedido está activo y asignado a él (DEC-E32).
  4. HU-37 nueva: disponibilidad del domiciliario (DEC-E31). La redactó el asistente Claude Code, no un agente del kit, y la aprobó Camila; no tiene autoevaluación de agente.

---

### HU-19 — Cambio de estado del pedido a «listo para recoger»

Yo, como empleado o vendedor,
quiero marcar como «listo para recoger» un pedido confirmado que está en preparación,
para organizar los tiempos de alistamiento y marcar el momento en que el pedido puede ser entregado al domiciliario.

Está hecho cuando:
- Dado un pedido en estado «en preparación», cuando el empleado o el administrador indica que la orden está lista, entonces el sistema cambia su estado a «listo para recoger», registrando la fecha y el empleado o administrador responsable.
- Dado un cliente o un domiciliario, cuando intenta marcar un pedido como «listo para recoger», entonces el sistema rechaza la operación por falta de permisos. El paso de «recibido» a «en preparación» ocurre al confirmar el pedido (HU-16, DEC-E21).

Cómo se simula en el prototipo: Se usan mensajes conversacionales con botones de cambio de estado en el bot y un registro ficticio de auditoría en memoria.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es independiente de la asignación del domiciliario y pequeña al limitarse al alistamiento interno del negocio. Es totalmente testeable verificando permisos y la persistencia de la trazabilidad.

---

### HU-20 — Consulta de pedidos pendientes de asignación y disponibilidad de domiciliarios

Yo, como administrador del negocio,
quiero consultar los pedidos pendientes de asignación y la carga de trabajo actual de cada domiciliario vinculado,
para decidir a quién despachar sin sobrecargar a ningún repartidor.

Está hecho cuando:
- Dado un administrador del negocio o un empleado, cuando solicita la lista de pedidos para despacho de su establecimiento, entonces el sistema muestra únicamente los pedidos de su propio negocio en estado «en preparación» o «listo para recoger» que no tienen un domiciliario asignado.
- Dado el listado de domiciliarios vinculados y activos del negocio, cuando el administrador o el empleado consulta su carga, entonces el sistema muestra el número de pedidos asignados actualmente a cada uno y su tope máximo permitido configurado por el negocio.
- Dado un domiciliario marcado como «no disponible», cuando el administrador o el empleado consulta los domiciliarios para despacho, entonces el sistema lo muestra como no disponible y no lo ofrece para asignar (DEC-E31).
- Dado un domiciliario o un cliente, cuando intenta consultar la consola de despacho del negocio, entonces el sistema le niega el acceso.

Cómo se simula en el prototipo: Se responde a un comando de Telegram con una lista formateada en texto conteniendo domiciliarios ficticios y sus conteos de pedidos activos.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Aporta visibilidad operativa esencial antes del despacho. Es estimable y testeable simulando diferentes volúmenes de pedidos y domiciliarios activos.

---

### HU-21 — Asignación de domiciliario a un pedido con validación de tope de carga

Yo, como empleado o vendedor,
quiero asignar un domiciliario a un pedido que está en preparación o listo para recoger,
para coordinar el despacho del servicio respetando el límite de pedidos simultáneos del negocio.

Está hecho cuando:
- Dado un pedido sin repartidor y un domiciliario que no ha superado el tope de carga del negocio, cuando el empleado selecciona al repartidor y confirma la asignación, entonces el sistema vincula al domiciliario de forma atómica y le envía una notificación de asignación.
- Dado un domiciliario que ya alcanzó el número máximo de pedidos simultáneos configurado por el negocio, cuando el empleado intenta asignarle otro pedido, entonces el sistema impide la asignación y muestra un mensaje de advertencia.
- Dado un domiciliario con asignaciones pendientes de respuesta, cuando el sistema calcula su carga, entonces las cuenta dentro del tope junto con las aceptadas y las que van en camino (DEC-E30).
- Dado dos empleados o administradores intentando asignar el mismo pedido al mismo tiempo, cuando las solicitudes se procesan en paralelo, entonces el sistema asigna el pedido únicamente a la primera solicitud procesada y notifica a la otra persona que el pedido ya fue asignado.
- Dado un domiciliario vinculado a otro negocio, cuando el empleado intenta seleccionarlo para la asignación, entonces el sistema no lo muestra ni permite vincularlo.

Cómo se simula en el prototipo: Se utiliza un flujo conversacional con botones inline que muestran repartidores disponibles simulando concurrencia mediante pruebas secuenciales rápidas.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es valiosa por garantizar reglas críticas (atomicidad, confirmación previa, tope de carga y exclusividad de negocio según DEC-E03). Es testeable evaluando escenarios concurrentes y límites de cupo.

---

### HU-22 — Aceptación o rechazo de un pedido asignado por parte del domiciliario

Yo, como domiciliario,
quiero responder a la notificación de una nueva asignación confirmando si la acepto o la rechazo,
para informar de inmediato mi disponibilidad de realizar la entrega.

Está hecho cuando:
- Dado un pedido recién asignado, cuando el domiciliario presiona la opción de aceptar en el bot, entonces el sistema confirma la asignación y le habilita las opciones para gestionar la entrega.
- Dado un pedido recién asignado, cuando el domiciliario presiona la opción de rechazar, entonces el sistema remueve la asignación, deja el pedido disponible para despacho y notifica al empleado o administrador que hizo la asignación.
- Dado un pedido asignado a un repartidor específico, cuando otro domiciliario, un cliente o un empleado intenta responder a la notificación de asignación, entonces el sistema deniega la acción.

Cómo se simula en el prototipo: Se presentan botones de interacción directa («Aceptar» / «Rechazar») en el mensaje de notificación de Telegram.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es pequeña e independiente de las etapas de transporte. Su resultado es binario y totalmente testeable a través de las opciones interactivas del mensaje.

---

### HU-23 — Liberación de pedido por tiempo de respuesta agotado del domiciliario

Yo, como administrador del negocio,
quiero que el sistema libere automáticamente un pedido cuya asignación no sea respondida a tiempo por el domiciliario,
para reasignarlo sin demorar el servicio al cliente.

Está hecho cuando:
- Dado un pedido asignado a un domiciliario que no responde la solicitud transcurridos `[por definir con el equipo]` minutos, cuando el plazo expira, entonces el sistema elimina la asignación del pedido de forma automática.
- Dado el vencimiento del tiempo de respuesta, cuando el sistema remueve la asignación, entonces envía una notificación al empleado o administrador que realizó la asignación indicando que el pedido requiere un nuevo repartidor.
- Dado un domiciliario que intenta aceptar un pedido cuyo plazo de respuesta ya venció, cuando envía la respuesta tardía, entonces el sistema le informa que la asignación caducó y no modifica el pedido.

Cómo se simula en el prototipo: Un temporizador simulado en la ejecución del prototipo ejecuta el evento de expiración tras unos segundos de prueba.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Mantiene como pendiente configurable el tiempo límite sin inventar datos. Protege la continuidad de la operación y es testeable mediante la manipulación del reloj de pruebas.

---

### HU-24 — Consulta de servicios asignados por el domiciliario

Yo, como domiciliario,
quiero consultar la lista de mis servicios asignados y pendientes de entrega,
para conocer las órdenes que debo entregar y sus detalles.

Está hecho cuando:
- Dado un domiciliario autenticado, cuando consulta sus entregas pendientes, entonces el sistema le muestra únicamente los pedidos que le han sido asignados y están activos en su negocio vinculado.
- Dado el listado de pedidos del domiciliario, cuando selecciona un pedido en particular, entonces el sistema muestra los productos, el nombre, la dirección, las referencias y el teléfono del cliente, sin exponer identificadores internos de Telegram (DEC-E32).
- Dado un domiciliario de otro negocio o un cliente, cuando intenta consultar los servicios asignados a un repartidor, entonces el sistema deniega el acceso a dicha información.
- Dado un pedido que ya fue entregado, cancelado o reasignado a otro domiciliario, cuando el domiciliario intenta consultar sus datos, entonces el sistema ya no le muestra el nombre ni el teléfono del cliente (DEC-E32).

Cómo se simula en el prototipo: Un comando del bot `/mis_servicios` despliega un menú con la lista de pedidos activos asociados al id ficticio del repartidor.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es pequeña, valiosa y respeta la privacidad de los datos personales. Cumple con INVEST y es testeable mediante consultas con diferentes cuentas.

---

### HU-25 — Notificación al domiciliario por cancelación de pedido asignado

Yo, como domiciliario,
quiero recibir un aviso automático cuando un pedido que se me asignó sea cancelado por el negocio o el cliente,
para evitar desplazamientos innecesarios y liberar mi cupo de carga.

Está hecho cuando:
- Dado un pedido asignado a un domiciliario, cuando el cliente, el administrador o el empleado lo cancela antes de pasar a «en camino», entonces el sistema envía una notificación inmediata al domiciliario informando de la cancelación.
- Dado la cancelación de un pedido asignado, cuando el sistema notifica al domiciliario, entonces remueve el pedido de su lista activa y descuenta la orden de su carga de trabajo.
- Dado un pedido en estado «en camino», cuando el cliente intenta cancelarlo, entonces el sistema impide la cancelación directa e informa que debe ser gestionado como novedad.

Cómo se simula en el prototipo: Se envía un mensaje automático al chat de Telegram del domiciliario cuando el estado del pedido cambia a «cancelado» en el backend ficticio.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cubre el ciclo de vida excepcional del servicio asignado. Es testeable provocando cancelaciones antes y después del cambio a ruta.

---

### HU-37 — Disponibilidad del domiciliario

Yo, como domiciliario,
quiero marcarme como disponible o no disponible en el bot,
para recibir asignaciones solo cuando puedo hacer entregas.

Está hecho cuando:
- Dado un domiciliario activo en su negocio, cuando se marca «disponible» y confirma, entonces el sistema lo ofrece al administrador y al empleado para nuevas asignaciones (DEC-E31).
- Dado un domiciliario disponible, cuando se marca «no disponible» y confirma, entonces el sistema deja de ofrecerlo para asignaciones nuevas (DEC-E31).
- Dado un domiciliario con pedidos asignados que aún no van en camino, cuando se marca «no disponible», entonces el sistema libera esos pedidos, los deja pendientes de asignación y avisa a quien los asignó; los pedidos que ya van en camino los sigue llevando hasta terminarlos (DEC-E31, DEC-E23).
- Dado un administrador, un empleado o un cliente, cuando intenta cambiar la disponibilidad de un domiciliario, entonces el sistema rechaza la operación: solo el domiciliario la cambia.

Cómo se simula en el prototipo: domiciliarios ficticios con un indicador de disponibilidad y pedidos asignados de prueba.

Evaluación INVEST: pendiente (historia agregada en la revisión de conflictos; no la generó ni la revisó un agente).
