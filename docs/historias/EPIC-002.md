# EPIC-002. Catálogo y pedidos del cliente — Historias de usuario

Estado: Aprobada por Camila (2026-11-19)
Fecha: 2026-11-19

Origen y validación:
- Generadas por `generador-hu-invest` (agentes-ia/salidas/generador-hu-invest/HU-002_20261119-0910_user-stories_epic-002_hu-10.md).
- Revisadas por `user-story-reviewer` (agentes-ia/salidas/user-story-reviewer/RHU-002_20261119-0914_story-review_epic-002.md): corrigió HU-10, HU-11, HU-12, HU-16 y HU-17; sin historias nuevas; sin términos técnicos en los criterios.
- Correcciones elegidas por la estudiante y aplicadas por el asistente Claude Code sobre la revisión; aprobadas por Camila:
  1. HU-10: el precio no está «por definir» (lo escribe quien gestiona el catálogo); el administrador y el empleado gestionan el catálogo y los clientes lo consultan (DEC-E27); nuevo criterio para desactivar productos sin borrar el historial (DEC-E28). El tercer criterio del revisor impedía al cliente consultar el catálogo.
  2. HU-11: el cliente se registra en cada negocio; nuevo criterio para el ingreso a un negocio nuevo (DEC-E29).
  3. Revisión de conflictos (2026-11-19): HU-13 ya no programa pedidos; fuera de horario se rechazan (DEC-E09).
  4. Protección de datos (2026-11-19): HU-11 exige aceptar el aviso de privacidad del negocio (DEC-E36, DEC-E37).
- Siguen abiertos para la SPEC: categorías y agotados del catálogo, formas de pago y minutos para duplicado.

---

### HU-10 — Configuración del catálogo de productos del negocio

Yo, como Administrador del negocio,
quiero registrar y actualizar los productos de mi establecimiento con sus precios,
para que los clientes consulten una oferta clara y actualizada al realizar sus pedidos.

Está hecho cuando:
- Dado que el administrador del negocio accede a la gestión del catálogo, cuando ingresa un nuevo producto con su nombre y precio, entonces el sistema guarda el producto en la lista de oferta de ese negocio.
- Dado que el administrador del negocio modifica el precio de un producto existente, cuando solicita guardar los cambios, entonces el sistema le pide confirmación antes de hacer efectiva la actualización.
- Dado que un cliente o un usuario de otro negocio intenta crear, modificar o desactivar productos del catálogo, cuando envía la solicitud, entonces el sistema la rechaza; el administrador del negocio y el empleado o vendedor del negocio sí pueden gestionarlo, y los clientes del negocio pueden consultarlo (DEC-E27).
- Dado un producto activo, cuando el administrador o el empleado lo desactiva y confirma, entonces el sistema deja de mostrarlo a los clientes sin borrarlo de los pedidos anteriores (DEC-E28).

Cómo se simula en el prototipo: Se almacenan productos ficticios en arreglos en memoria asignados al identificador del negocio.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple con los criterios INVEST. Es independiente de la creación de pedidos, acotada al ámbito de administración del catálogo y testea los controles de permisos y separación por negocio.

---

### HU-11 — Registro e identificación del cliente en el negocio

Yo, como Persona que desea realizar un pedido,
quiero ingresar al bot a través del enlace o código QR propio del negocio e identificarme con mi contacto de Telegram,
para realizar pedidos de forma verificada en ese establecimiento.

Está hecho cuando:
- Dado que la persona accede mediante el enlace o código QR específico de un negocio, cuando inicia la interacción en el bot, entonces el sistema le solicita compartir su número telefónico mediante el botón nativo de Telegram.
- Dado que la persona llega al negocio por primera vez, cuando el sistema le presenta el aviso de privacidad de ese negocio, entonces solo puede compartir su contacto si acepta el tratamiento de datos con el botón; la aceptación queda registrada con fecha y versión del texto (DEC-E36, DEC-E37).
- Dado que la persona presiona el botón nativo de compartir contacto de Telegram, cuando se completa el proceso, entonces el sistema registra su teléfono verificado y lo vincula como cliente en ese negocio.
- Dado que una persona intenta enviar un número de teléfono ingresándolo de manera manual en el chat, cuando envía el mensaje, entonces el sistema no lo acepta y solicita nuevamente el uso del botón nativo.
- Dado que la persona ya compartió su contacto en otro negocio, cuando entra por el enlace o QR de un negocio nuevo, entonces el sistema le pide compartir su contacto de nuevo para registrarse como cliente de ese negocio (DEC-E29).

Cómo se simula en el prototipo: Se simula la recepción del objeto de contacto nativo de Telegram asociando el ID de chat al perfil del cliente.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Delimita con precisión la llegada e identificación del cliente según DEC-E05 y DEC-E20. Es totalmente testeable y no incluye mecanismos externos de autenticación.

---

### HU-12 — Armado y registro del pedido por parte del cliente

Yo, como Cliente,
quiero seleccionar productos, cantidades, barrio de entrega, dirección con referencias y forma de pago,
para conocer el total a pagar y enviar la orden al negocio.

Está hecho cuando:
- Dado que el cliente selecciona productos del catálogo y un barrio dentro de la zona de cobertura, cuando avanza en la solicitud, entonces el sistema calcula automáticamente el total sumando los productos y la tarifa de domicilio configurada para ese barrio.
- Dado que el cliente ingresa la dirección de entrega, observaciones de referencia y selecciona una forma de pago `[por definir con el equipo]`, cuando presiona enviar pedido, entonces el sistema le solicita confirmación antes de formalizar el registro.
- Dado que el cliente confirma el registro del pedido, cuando el sistema lo procesa, entonces guarda el pedido en estado recibido, registra la fecha, hora y cliente responsable, y envía una notificación automática de pedido nuevo al administrador del negocio y al empleado o vendedor.
- Dado que el cliente pertenece o interactúa con un negocio específico, cuando arma su pedido, entonces el sistema únicamente le permite ver y seleccionar productos y barrios pertenecientes a dicho negocio.

Cómo se simula en el prototipo: Se utilizan catálogos y tarifas preconfiguradas para calcular el resumen de la compra antes de registrar la orden.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cubre el flujo principal de creación del pedido alineado con DEC-E06, DEC-E07, DEC-E08, DEC-E21 y DEC-E25, manteniendo la separación estricta de datos por negocio.

---

### HU-13 — Control de cobertura y horario de atención

Yo, como Cliente,
quiero que el sistema me informe si mi barrio no tiene cobertura o si el negocio está cerrado,
para saber de inmediato si el negocio puede atender mi pedido.

Está hecho cuando:
- Dado que el cliente selecciona un barrio que no está registrado en las zonas de cobertura del negocio, cuando intenta continuar, entonces el sistema rechaza la solicitud y le informa que no se realizan entregas en esa ubicación.
- Dado que el cliente intenta realizar un pedido fuera del horario de atención del negocio, cuando inicia el pedido, entonces el sistema le informa que el negocio está cerrado, le muestra el horario de atención y no le permite registrar el pedido (DEC-E09).

Cómo se simula en el prototipo: Se simulan horarios de atención y listas de barrios con un atributo booleano de cobertura.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple con INVEST y aplica DEC-E09 (modificada): rechazo por cobertura y por horario, sin pedidos programados.

---

### HU-14 — Advertencia de pedido potencialmente duplicado

Yo, como Cliente,
quiero recibir una alerta de confirmación si envío un pedido idéntico al anterior en poco tiempo,
para evitar realizar por error duplicados no deseados.

Está hecho cuando:
- Dado que un cliente envía un pedido con los mismos productos, cantidades y dirección de entrega al mismo negocio dentro de un intervalo menor a `[por definir con el equipo]` minutos desde su último pedido, cuando procesa la solicitud, entonces el sistema detiene el registro y le muestra un aviso indicando la posible duplicidad.
- Dado que el cliente recibe la alerta de posible duplicado, cuando decide cancelar la operación, entonces el sistema descarta el nuevo pedido sin alterar el pedido previamente registrado.
- Dado que el cliente recibe la alerta de posible duplicado, cuando confirma expresamente que desea repetir el pedido, entonces el sistema registra la orden como un pedido independiente.

Cómo se simula en el prototipo: Se evalúa una ventana temporal sobre el historial reciente de pedidos del cliente almacenado en memoria.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Aplica de forma limpia DEC-E10 y el principio de confirmación de operaciones importantes (sección 3.7), siendo fácilmente testeable mediante marcas de tiempo.

---

### HU-15 — Restricción de pedidos en negocios con suscripción vencida

Yo, como Cliente,
quiero que el sistema me prevenga de hacer pedidos en establecimientos no disponibles,
para no realizar compras en negocios que no pueden procesar mi atención.

Está hecho cuando:
- Dado que un negocio tiene su estado de suscripción marcado como vencido, cuando el cliente ingresa al bot de dicho negocio para iniciar un pedido, entonces el sistema le impide continuar e informa que el negocio no está recibiendo pedidos temporalmente.
- Dado que un negocio tiene su suscripción al día, cuando el cliente inicia la interacción, entonces el sistema le permite navegar el catálogo y proceder con su compra normalmente.

Cómo se simula en el prototipo: Se usa una variable de estado booleana para la suscripción del negocio.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Implementa de forma aislada e independiente la decisión DEC-E26, garantizando que el estado de suscripción bloquee oportunamente el flujo del cliente.

---

### HU-16 — Confirmación o rechazo de pedido por el negocio

Yo, como Empleado o vendedor,
quiero revisar los pedidos en estado recibido para confirmarlos o rechazarlos,
para iniciar la preparación de la orden o informar oportunamente al cliente en caso de no poder atenderla.

Está hecho cuando:
- Dado que el negocio cuenta con un pedido en estado recibido, cuando el administrador del negocio o el empleado o vendedor decide confirmarlo o rechazarlo, entonces el sistema le solicita confirmación antes de ejecutar la acción.
- Dado que el empleado o vendedor (o el administrador) aprueba la confirmación del pedido, cuando el sistema la procesa, entonces cambia el estado a en preparación, registra la fecha, hora y usuario responsable, y notifica al cliente la confirmación junto con el valor total a pagar.
- Dado que el empleado o vendedor (o el administrador) aprueba el rechazo del pedido, cuando el sistema lo procesa, entonces cambia el estado a rechazado, registra la fecha, hora y usuario responsable, y notifica al cliente la decisión.
- Dado un usuario con rol de domiciliario, cuando intenta confirmar o rechazar un pedido en estado recibido, entonces el sistema deniega la operación por falta de permisos.

Cómo se simula en el prototipo: Se simulan eventos de notificación en el bot del negocio y cambios de estado con trazabilidad en un arreglo de auditoría.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple con INVEST, respaldando la gestión del ciclo de vida del pedido por parte del negocio con autorización por rol y notificaciones requeridas (DEC-E17, DEC-E21, DEC-E22).

---

### HU-17 — Cancelación del pedido por parte del cliente

Yo, como Cliente,
quiero cancelar mi pedido mientras no haya pasado a estado en camino,
para desistir de la compra de forma oportuna si se presenta algún imprevisto.

Está hecho cuando:
- Dado que el pedido se encuentra en estado recibido, en preparación o listo para recoger, cuando el cliente solicita cancelar el pedido, entonces el sistema le exige una confirmación previa antes de proceder.
- Dado que el cliente confirma la cancelación antes de que el pedido esté en camino, cuando el sistema procesa la solicitud, entonces cambia el estado a cancelado, registra la fecha, hora y el cliente como responsable, y envía una notificación inmediata al administrador del negocio y al empleado o vendedor.
- Dado que el pedido se encuentra en estado en camino o posterior, cuando el cliente solicita la cancelación, entonces el sistema rechaza la acción e informa que debe coordinar cualquier novedad directamente con el establecimiento.

Cómo se simula en el prototipo: Se simula el comando de cancelación desde la vista de cliente verificando el estado del pedido en memoria.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es una historia clara y delimitada que aplica DEC-E13, DEC-E21 y DEC-E25, haciendo valer la irreversibilidad del pedido una vez pasa a estado «en camino».

---

### HU-18 — Cancelación del pedido por el negocio antes de despacho

Yo, como Administrador del negocio,
quiero cancelar un pedido activo antes de que esté en camino,
para dar de baja solicitudes que no se pueden cumplir o que el cliente canceló por otros medios.

Está hecho cuando:
- Dado que un pedido está en estado recibido, en preparación o listo para recoger, cuando el administrador del negocio o el empleado o vendedor selecciona cancelar el pedido, entonces el sistema solicita confirmación de la acción.
- Dado que se confirma la cancelación desde el negocio, cuando el sistema actualiza el estado a cancelado, entonces registra la fecha, hora y usuario responsable, y envía una notificación al cliente informando la cancelación del pedido.
- Dado que el pedido ya se encuentra en estado en camino, cuando el administrador o empleado intenta cambiarlo a cancelado, entonces el sistema bloquea la operación e indica que cualquier situación debe registrarse como novedad de entrega.

Cómo se simula en el prototipo: Se cambia el estado en memoria y se dispara un mensaje simulado de notificación hacia el cliente.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple totalmente con INVEST, garantizando la consistencia en el manejo de cancelaciones desde el lado del establecimiento según DEC-E13, DEC-E17, DEC-E21 y DEC-E25.
