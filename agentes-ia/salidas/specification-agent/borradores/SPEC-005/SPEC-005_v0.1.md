<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-21 15:26
Petición: SPEC-005. EPIC-003. Especifica la asignación y el despacho de pedidos: el negocio marca listo para recoger (DEC-E21, DEC-E22); consulta de pedidos sin domiciliario y de la carga de cada domiciliario; asignación desde en preparación por el administrador o el empleado (DEC-E11) con tope de pedidos simultáneos que incluye asignaciones pendientes de respuesta (DEC-E12, DEC-E30, DEC-E40, DEC-E44) y asignación atómica sin doble asignación (regla crítica); un domiciliario pertenece a un solo negocio (DEC-E03); disponibilidad del domiciliario y liberación de pedidos no iniciados al marcarse no disponible (DEC-E31); aceptación o rechazo y liberación si rechaza o no responde a tiempo, con aviso a quien asignó (DEC-E23); datos del cliente que ve el domiciliario solo con el pedido activo (DEC-E32); avisos al domiciliario de asignaciones y cancelaciones (DEC-E25). Las historias aprobadas están en el archivo adjunto: usa HU-19 a HU-25 y HU-37. Dependencias: SPEC-002 y SPEC-004 (candidatas). Es una sola funcionalidad.
-->

# SPEC-005. Asignación y despacho de pedidos - Versión 0.1

Estado: Borrador
Modo: Inicial
Necesidad original: "SPEC-005. EPIC-003. Especifica la asignación y el despacho de pedidos: el negocio marca listo para recoger (DEC-E21, DEC-E22); consulta de pedidos sin domiciliario y de la carga de cada domiciliario; asignación desde en preparación por el administrador o el empleado (DEC-E11) con tope de pedidos simultáneos que incluye asignaciones pendientes de respuesta (DEC-E12, DEC-E30, DEC-E40, DEC-E44) y asignación atómica sin doble asignación (regla crítica); un domiciliario pertenece a un solo negocio (DEC-E03); disponibilidad del domiciliario y liberación de pedidos no iniciados al marcarse no disponible (DEC-E31); aceptación o rechazo y liberación si rechaza o no responde a tiempo, con aviso a quien asignó (DEC-E23); datos del cliente que ve el domiciliario solo con el pedido activo (DEC-E32); avisos al domiciliario de asignaciones y cancelaciones (DEC-E25). Las historias aprobadas están en el archivo adjunto: usa HU-19 a HU-25 y HU-37. Dependencias: SPEC-002 y SPEC-004 (candidatas). Es una sola funcionalidad."
Épica: EPIC-003

## Análisis
- Objetivo: Permite al negocio gestionar la preparación y el despacho de sus pedidos, asignando domiciliarios disponibles de forma atómica y bajo el tope de carga configurado, notificando a los repartidores para que acepten o rechacen el servicio, y permitiendo al domiciliario consultar sus entregas y controlar su disponibilidad de entrega.
- Alcance inicial: Cubre el cambio de estado del pedido a listo para recoger; la consulta de la consola de despacho; el proceso de asignación atómica con control de tope de carga; la respuesta de aceptación o rechazo por parte del repartidor; el control de expiración de asignación no respondida; el registro de disponibilidad del domiciliario con liberación de pedidos no iniciados; la consulta de servicios asignados con acceso condicionado a datos del cliente; y el envío de notificaciones operativas al personal y domiciliarios.
- Actores: Administrador del negocio, Empleado o vendedor, Domiciliario, Cliente.
- Contexto aplicable: Secciones 3.2, 3.3, 3.6, 3.7, 3.8, 3.11 (DEC-E03, DEC-E11, DEC-E12, DEC-E13, DEC-E21, DEC-E22, DEC-E23, DEC-E25, DEC-E30, DEC-E31, DEC-E32, DEC-E38, DEC-E40, DEC-E44).

## Modelo de dominio
- Negocio: pertenece a la Plataforma; cardinalidad uno a varios respecto a Usuarios, Domiciliarios y Pedidos. Origen: contexto 3.3.
- Pedido: pertenece a un Negocio y a un Cliente; cardinalidad de cero a uno respecto al Domiciliario asignado. Origen: contexto 3.8 y DEC-E21.
- Domiciliario: persona vinculada a un único Negocio con rol de repartidor; cardinalidad de cero a varios pedidos asignados simultáneamente. Origen: DEC-E03 y DEC-E12.
- Asignación: vínculo entre un Pedido y un Domiciliario en estado pendiente, aceptado o liberado; cardinalidad exacta de un Domiciliario por Pedido asignado. Origen: contexto 3.8, DEC-E11 y DEC-E30.

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
No aplica.

## Preguntas de aclaración
- OPEN-Q-001. ¿Cuál es el tiempo límite (en minutos) para que un domiciliario acepte o rechace la asignación de un pedido antes de que el sistema libere automáticamente la asignación y avise a quien asignó?
  Por qué importa: Define el valor concreto del temporizador de expiración para la regla de negocio BR-004, el RF-005 y los AC asociados (HU-23, DEC-E23 y vacío conocido 1 del contexto).
  Crítica: sí
  Propuesta del agente: 5 minutos.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Gestionar el ciclo de despacho y asignación de pedidos en el negocio, garantizando la atomicidad al vincular repartidores, el cumplimiento estricto del tope de carga por domiciliario, el control de disponibilidad de los repartidores y la visibilidad segura y temporal de los datos de entrega.

### 2. Contexto
La funcionalidad opera sobre pedidos que ya han sido confirmados y han pasado al estado en preparación. El administrador o empleado coordina el alistamiento marcando el pedido como listo para recoger y asignando un domiciliario disponible. La asignación notifica de inmediato al domiciliario en Telegram para su aceptación o rechazo. El sistema asegura que dos usuarios no asignen el mismo pedido simultáneamente y protege los datos personales del cliente permitiendo que el domiciliario únicamente los consulte mientras el pedido permanezca activo y asignado a él.
Decisiones del equipo:
- DEC-E03. Un domiciliario pertenece a un solo negocio con vinculación activa o pendiente.
- DEC-E11. Administrador o empleado asigna el pedido al domiciliario; el domiciliario acepta o rechaza en Telegram.
- DEC-E12. Cada negocio configura un tope de pedidos simultáneos por domiciliario (entre 1 y 7, por defecto 3).
- DEC-E21 y DEC-E22. Confirmar pedido es pasarlo a en preparación. Administrador o empleado lo marca listo para recoger. La asignación se realiza desde en preparación.
- DEC-E23. Si el domiciliario rechaza o no responde a tiempo, la asignación se libera y se notifica a quien asignó.
- DEC-E25. Administrador y empleado reciben avisos de rechazo o falta de respuesta; domiciliario recibe notificaciones de asignaciones y cancelaciones.
- DEC-E30. Las asignaciones pendientes de respuesta cuentan para el tope de carga del domiciliario.
- DEC-E31. El domiciliario gestiona su disponibilidad. Al marcarse no disponible se liberan sus pedidos asignados que aún no van en camino y se notifica a quien asignó.
- DEC-E32. El domiciliario solo ve datos del cliente (nombre, dirección, referencias, teléfono) mientras el pedido esté activo y asignado a él.
- DEC-E40. El tope de carga por domiciliario es configurable por el negocio entre 1 y 7 (por defecto 3).
- DEC-E44. Si el administrador reduce el tope por debajo de la carga actual del domiciliario, los pedidos vigentes se respetan y no recibe nuevos hasta quedar por debajo del tope.

### 3. Alcance
- Marcado de pedidos en preparación como listo para recoger por parte de administrador o empleado.
- Consulta de la consola de despacho: pedidos sin domiciliario asignado y carga actual de repartidores.
- Asignación atómica de repartidores respetando el tope de carga configurado y la disponibilidad activa.
- Aceptación y rechazo conversacional por parte del domiciliario.
- Liberación automática por superación del tiempo límite de respuesta del domiciliario (sujeto a OPEN-Q-001).
- Cambio de disponibilidad del domiciliario (disponible / no disponible) y liberación automática de asignaciones no iniciadas en ruta.
- Consulta de lista de servicios asignados por parte del domiciliario con restricción de datos personales según estado del pedido.
- Envío de notificaciones automáticas por asignación, rechazo, caducidad, cambio de disponibilidad y cancelación.

### 4. Actores e historias de usuario
Actores: Administrador del negocio, Empleado o vendedor, Domiciliario, Cliente.
- HU-019. Como empleado o vendedor, quiero marcar como listo para recoger un pedido confirmado en preparación, para organizar los tiempos de alistamiento y marcar la disponibilidad de entrega al repartidor.
- HU-020. Como administrador del negocio, quiero consultar los pedidos pendientes de asignación y la carga de trabajo actual de cada domiciliario vinculado, para decidir a quién despachar sin sobrecargar repartidores.
- HU-021. Como empleado o vendedor, quiero asignar un domiciliario a un pedido en preparación o listo para recoger, para coordinar el despacho respetando el límite de pedidos simultáneos del negocio de forma atómica.
- HU-022. Como domiciliario, quiero responder a la notificación de una nueva asignación confirmando si la acepto o la rechazo, para informar de inmediato mi disponibilidad de realizar la entrega.
- HU-023. Como administrador del negocio, quiero que el sistema libere automáticamente un pedido cuya asignación no sea respondida a tiempo por el domiciliario, para reasignarlo sin demorar el servicio.
- HU-024. Como domiciliario, quiero consultar la lista de mis servicios asignados y pendientes de entrega, para conocer las órdenes que debo entregar y sus detalles autorizados.
- HU-025. Como domiciliario, quiero recibir un aviso automático cuando un pedido asignado sea cancelado por el negocio o el cliente, para evitar desplazamientos innecesarios y liberar mi cupo de carga.
- HU-037. Como domiciliario, quiero marcarme como disponible o no disponible en el bot, para recibir asignaciones únicamente cuando me encuentre en capacidad de realizar entregas.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir al administrador o empleado cambiar el estado de un pedido en preparación a listo para recoger, registrando la fecha, hora, estado y responsable de la operación. Origen: contexto 3.8, DEC-E21, DEC-E22.
- RF-002. El sistema debe mostrar al administrador o empleado la consola de despacho con la lista de pedidos en estado en preparación o listo para recoger que no tengan repartidor asignado, y el listado de domiciliarios vinculados al negocio indicando su estado de disponibilidad, pedidos activos asignados y tope máximo permitido. Origen: contexto 3.8, DEC-E30, DEC-E31.
- RF-003. El sistema debe permitir al administrador o empleado asignar un domiciliario vinculado y disponible a un pedido en estado en preparación o listo para recoger, siempre que el repartidor no haya alcanzado o superado su tope de carga simultánea. Origen: contexto 3.8, DEC-E11, DEC-E12, DEC-E40.
- RF-004. El sistema debe ejecutar la asignación de un repartidor a un pedido de forma atómica en el backend, garantizando que ante solicitudes simultáneas solo una asignación sea exitosa y las demás sean rechazadas con un aviso de pedido ya asignado. Origen: contexto 3.2, 3.8 (regla crítica del proyecto).
- RF-005. El sistema debe notificar de inmediato al domiciliario sobre la nueva asignación enviando las opciones para aceptar o rechazar el servicio. Si el domiciliario no responde dentro del tiempo límite establecido (pendiente de OPEN-Q-001), el sistema debe remover la asignación, dejar el pedido sin repartidor y notificar a quien realizó la asignación. Origen: contexto 3.8, DEC-E23, DEC-E25.
- RF-006. El sistema debe procesar la respuesta del domiciliario a la asignación: si acepta, la asignación pasa a estado aceptada; si rechaza, la asignación se remueve, el pedido queda disponible para despacho y se envía un aviso inmediato a quien asignó el pedido. Origen: DEC-E11, DEC-E23, DEC-E25.
- RF-007. El sistema debe permitir al domiciliario cambiar su estado de disponibilidad entre disponible y no disponible previo mensaje de confirmación. Origen: contexto 3.7, DEC-E31.
- RF-008. Al marcar un domiciliario como no disponible, el sistema debe remover de forma automática todas sus asignaciones de pedidos que se encuentren en estado en preparación o listo para recoger (no iniciados en camino), dejando los pedidos sin repartidor y enviando una notificación a quien los asignó. Los pedidos que ya estén en camino permanecen asignados al domiciliario hasta su finalización. Origen: DEC-E25, DEC-E31.
- RF-009. El sistema debe permitir al domiciliario consultar la lista de servicios asignados activos en su negocio vinculado. Al seleccionar un pedido activo, el sistema debe mostrar los productos, el nombre del cliente, la dirección de entrega, las referencias y el teléfono del cliente. Origen: DEC-E32.
- RF-010. El sistema debe denegar la visualización de los datos de contacto del cliente (nombre, dirección, referencias, teléfono) al domiciliario cuando el pedido pase a estado entregado, cancelado, con novedad o si la asignación ha sido removida/reasignada. Origen: contexto 3.3, DEC-E32.
- RF-011. El sistema debe notificar automáticamente al domiciliario cuando un pedido asignado a su cargo sea cancelado por el cliente o el negocio antes de pasar a en camino, removiendo el pedido de sus servicios activos y descontándolo de su carga ocupada. Origen: DEC-E13, DEC-E25.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y Autorización. Las operaciones de cambio de estado a listo para recoger, consulta de consola de despacho y asignación deben verificarse estrictamente en el backend evaluando usuario, rol (administrador o empleado) y pertenencia al negocio. Método de verificación: Inspección del código backend y pruebas unitarias/integración de control de acceso. Origen: contexto 3.2 (regla crítica del proyecto).
- RNF-002. Aislamiento de Datos por Negocio. Ningún administrador, empleado o domiciliario podrá consultar, asignar o modificar pedidos o domiciliarios pertenecientes a otro negocio. Método de verificación: Pruebas de integración multitenant e intentos de acceso cruzado entre identificadores de diferentes negocios. Origen: contexto 3.3 (regla crítica del proyecto).
- RNF-003. Concurrencia y Atomicidad. El proceso de asignación de domiciliario debe garantizar aislamiento mediante bloqueos transaccionales en el backend para evitar la asignación duplicada de una misma orden ante peticiones en paralelo. Método de verificación: Pruebas de carga estresando el endpoint de asignación con solicitudes simultáneas. Origen: contexto 3.8 (regla crítica del proyecto).
- RNF-004. Protección de Datos Sensibles. Los mensajes de notificación broadcast o de resumen general presentados en el bot no deben expone nombre, teléfono, dirección ni Telegram ID del cliente ni la ubicación del repartidor, reservando los datos de contacto únicamente a la vista individual del domiciliario con pedido activo. Método de verificación: Inspección de plantillas de mensajes de notificación y pruebas de salida del bot. Origen: regla crítica del proyecto 7 y DEC-E32.

### 7. Reglas de negocio
- BR-001. Permisos para marcar listo para recoger. Únicamente usuarios autenticados con rol de administrador o empleado pertenecientes al negocio del pedido pueden marcar una orden como listo para recoger. Clientes y domiciliarios tienen prohibida esta acción. Origen: contexto 3.2, 3.8, DEC-E22.
- BR-002. Cálculo de Carga Simultánea. La carga de trabajo actual de un domiciliario se calcula sumando las asignaciones en estado pendiente de respuesta, las asignaciones aceptadas de pedidos en preparación o listo para recoger, y las órdenes en camino. Si la suma alcanza o supera el tope máximo de carga configurado para el negocio, el sistema impide asignarle nuevos pedidos. Origen: DEC-E12, DEC-E30, DEC-E40.
- BR-003. Exclusividad de Negocio del Domiciliario. Un domiciliario solo puede estar vinculado activamente a un único negocio. Durante el despacho, la consola solo debe mostrar repartidores vinculados activamente al negocio propietario del pedido. Origen: DEC-E03.
- BR-004. Tiempo de Respuesta y Libramiento de Asignación. Una asignación enviada al domiciliario permanece en estado pendiente de respuesta durante el tiempo límite definido (pendiente de OPEN-Q-001). Si el domiciliario no responde dentro de dicho plazo, la asignación expira, el sistema disocia al domiciliario del pedido y notifica al usuario que realizó la asignación. Respuestas extemporáneas del domiciliario deben ser rechazadas con aviso de caducidad. Origen: DEC-E23, DEC-E25.
- BR-005. Confirmación previa para operaciones importantes. El cambio de disponibilidad del domiciliario a no disponible y la asignación manual de un pedido exigen un paso de confirmación explícita antes de ser procesadas por el sistema. Origen: contexto 3.7.
- BR-006. Efecto de No Disponibilidad sobre Asignaciones No Iniciadas. Al confirmar la no disponibilidad, todas las asignaciones del domiciliario sobre pedidos en preparación o listo para recoger quedan anuladas de inmediato, liberando los pedidos para la consola de despacho y avisando a los asignadores correspondientes. Los pedidos en estado en camino no se liberan y deben ser entregados o reportados con novedad por el domiciliario. Origen: DEC-E25, DEC-E31.
- BR-007. Acceso Temporal a Datos Personales del Cliente. El domiciliario solo tiene acceso visible al nombre, dirección, referencias de entrega y teléfono del cliente mientras el pedido esté asignado a él y en estado activo (en preparación, listo para recoger o en camino). Una vez el pedido pase a entregado, cancelado, con novedad o si es reasignado, el sistema oculta inmediatamente esta información al domiciliario. Origen: contexto 3.3, DEC-E32.
- BR-008. Ajuste de Tope de Carga Inferior a Carga Actual. Si el administrador reduce el tope de carga simultánea por debajo de los pedidos que un domiciliario tiene actualmente asignados, los pedidos vigentes se conservan sin alteración, pero el repartidor no podrá recibir nuevas asignaciones hasta que su carga caiga por debajo del nuevo tope. Origen: DEC-E44.

### 8. Flujo principal
1. El empleado o administrador accede a la consola de despacho desde Telegram y solicita los pedidos pendientes de asignación de su negocio.
2. El backend valida usuario, rol y negocio, y retorna la lista de pedidos en estado en preparación o listo para recoger sin repartidor, junto con los domiciliarios disponibles y su carga actual (pendientes + aceptadas + en camino vs tope).
3. El empleado o administrador selecciona un pedido pendiente y un domiciliario disponible que no haya superado su tope de carga, y solicita la asignación.
4. El sistema pide confirmación previa de la asignación.
5. El empleado o administrador confirma la acción.
6. El backend valida en una transacción atómica que el pedido continúe sin asignación y que el domiciliario no haya superado su tope de carga.
7. El backend registra la asignación en estado pendiente de respuesta, incrementa la carga del repartidor, registra la trazabilidad (fecha, hora, asignador) y envía una notificación privada al Telegram del domiciliario con los detalles resumidos de la entrega y botones interactivos para Aceptar o Rechazar.
8. El domiciliario recibe la notificación y presiona el botón Aceptar.
9. El backend valida que la asignación esté vigente y pasa el estado de la asignación a aceptada.
10. El domiciliario consulta su lista de servicios asignados en el bot, selecciona la orden y el sistema le despliega los datos del cliente (nombre, dirección, referencias, teléfono) y los productos a entregar.

### 9. Flujos alternativos y de excepción
- A1. El negocio marca un pedido como listo para recoger antes de asignar:
  1. El empleado o administrador selecciona un pedido en estado en preparación y elige la opción marcar listo para recoger.
  2. El backend verifica permisos, actualiza el estado del pedido a listo para recoger registrando fecha y responsable, y actualiza la consola de despacho.

- A2. El domiciliario rechaza la asignación:
  1. En el paso 8 del flujo principal, el domiciliario presiona el botón Rechazar.
  2. El backend remueve la asignación, descuenta la orden de la carga del domiciliario y deja el pedido disponible en la consola de despacho.
  3. El backend envía una notificación inmediata al empleado o administrador que realizó la asignación indicando el rechazo para que proceda a seleccionar otro repartidor.

- A3. El domiciliario se marca no disponible:
  1. El domiciliario selecciona en el bot la opción de cambiar estado a no disponible.
  2. El sistema solicita confirmación explícita.
  3. El domiciliario confirma.
  4. El backend cambia el estado del domiciliario a no disponible.
  5. El backend identifica los pedidos asignados al domiciliario en estado en preparación o listo para recoger, remueve sus asignaciones, restablece las órdenes como sin asignación en la consola de despacho y notifica a los usuarios que realizaron dichas asignaciones.
  6. Los pedidos en estado en camino se mantienen asignados al domiciliario.

- E1. Intento de asignación sobre un pedido ya asignado (Concurrencia):
  1. En el paso 6 del flujo principal, la transacción en el backend detecta que otro usuario asignó el mismo pedido una fracción de segundo antes.
  2. El backend revierte la operación y responde con un error de orden ya asignada.
  3. El bot informa al usuario que el pedido fue asignado previamente por otra persona.

- E2. Asignación a domiciliario que alcanzó el tope de carga:
  1. En el paso 3 del flujo principal, el usuario intenta seleccionar a un domiciliario cuya carga actual (incluyendo pendientes) es igual o mayor a su tope configurado.
  2. El backend rechaza la petición e informa que el domiciliario sobrepasó su límite de carga simultánea.

- E3. Expiración del tiempo de respuesta del domiciliario:
  1. En el paso 7 del flujo principal, el domiciliario no presiona Aceptar ni Rechazar durante el tiempo límite establecido (pendiente de OPEN-Q-001).
  2. El temporizador del backend marca la asignación como expirada y la remueve.
  3. El backend remueve la orden de la carga del domiciliario, actualiza el pedido a sin asignación en la consola y envía una notificación de caducidad al usuario que asignó.
  4. Si el domiciliario intenta presionar Aceptar o Rechazar posteriormente, el backend rechaza la acción informando que la asignación ha caducado.

- E4. Cancelación del pedido asignado por parte del negocio o cliente:
  1. Un pedido en estado en preparación o listo para recoger con domiciliario asignado es cancelado por el cliente o por el negocio.
  2. El backend actualiza el pedido a estado cancelado, remueve la asignación y envía una notificación automática al Telegram del domiciliario informando la cancelación del servicio.
  3. El pedido se elimina de la lista activa del domiciliario y los datos del cliente se vuelven inaccesibles de inmediato.

- E5. Intento de cambio de estado o consulta por un actor no autorizado:
  1. Un cliente o domiciliario intenta ejecutar un comando de la consola de despacho o marcar listo para recoger.
  2. El backend valida el rol y deniega la operación retornando un mensaje de permiso denegado.

### 10. Casos límite
- CL-001. Asignación simultánea del mismo pedido por dos empleados al mismo tiempo: el backend debe procesar una sola asignación atómica; el segundo intento debe fallar limpiamente con mensaje explicativo. Origen: contexto 3.8 (regla crítica del proyecto).
- CL-002. Reducción del tope del negocio por debajo de la carga actual del repartidor: el sistema mantiene las asignaciones activas existentes sin cancelarlas, pero impide nuevas asignaciones hasta que la carga baje del nuevo tope. Origen: DEC-E44.
- CL-003. Domiciliario que pasa a no disponible con pedidos en camino y pedidos en preparación: el sistema debe conservar las asignaciones de los pedidos en camino y liberar únicamente los pedidos en preparación o listo para recoger. Origen: DEC-E31.
- CL-004. Intento de respuesta del domiciliario cuando el pedido ha sido cancelado mientras decidía: la acción debe ser rechazada informando que el pedido fue cancelado y liberando el cupo del repartidor. Origen: DEC-E13, DEC-E25.
- CL-005. Consulta de datos del cliente inmediatamente después de cambiar el estado a entregado o cancelado: el backend debe denegar la entrega de nombre, dirección, referencias y teléfono al domiciliario. Origen: DEC-E32.

### 11. Criterios de aceptación
- AC-001. Marcado de listo para recoger por personal autorizado.
  Dado un pedido en el negocio N1 en estado en preparación, cuando un empleado o administrador del negocio N1 envía la orden de marcar listo para recoger, entonces el backend actualiza el estado del pedido a listo para recoger, registra fecha, hora y el identificador del usuario responsable, y la consola de despacho refleja el nuevo estado.

- AC-002. Rechazo de listo para recoger por falta de permisos.
  Dado un pedido en estado en preparación, cuando un cliente o un domiciliario intenta ejecutar la acción de marcar listo para recoger, entonces el backend rechaza la solicitud por falta de permisos y el estado del pedido permanece sin cambios.

- AC-003. Consola de despacho aislada por negocio.
  Dado el negocio N1 con pedidos en preparación sin repartidor y domiciliarios vinculados, cuando un administrador de N1 consulta la consola de despacho, entonces el sistema retorna únicamente los pedidos sin repartidor y los repartidores vinculados activamente a N1 con sus respectivos conteos de carga (pendientes, aceptados, en camino) y su disponibilidad actual, excluyendo datos de cualquier otro negocio.

- AC-004. Validar tope de carga en asignación.
  Dado un domiciliario D1 del negocio N1 con tope de carga de 3 pedidos y que cuenta actualmente con 2 pedidos aceptados y 1 asignación pendiente de respuesta (total carga = 3), cuando un empleado de N1 intenta asignarle un nuevo pedido P1, entonces el backend impide la asignación y muestra un mensaje indicando que el domiciliario alcanzó el cupo máximo permitido.

- AC-005. Asignación atómica exitosa.
  Dado un pedido P1 en estado listo para recoger sin repartidor y un domiciliario D1 disponible con carga por debajo de su tope, cuando el empleado confirma la asignación a D1, entonces el backend vincula a D1 de forma atómica en estado pendiente de respuesta, incrementa la carga de D1 y envía una notificación de asignación al Telegram de D1 con botones de aceptar y rechazar.

- AC-006. Prevención de asignación simultánea concurrente.
  Dado un pedido P1 sin repartidor, cuando el usuario U1 y el usuario U2 intentan asignar a P1 simultáneamente a repartidores distintos, entonces el backend procesa únicamente la primera solicitud que adquiere el bloqueo, asigna el pedido a esa solicitud y responde al otro usuario que el pedido ya fue asignado previamente.

- AC-007. Aceptación de asignación por el domiciliario.
  Dado un pedido P1 asignado en estado pendiente de respuesta al domiciliario D1, cuando D1 presiona el botón Aceptar en Telegram dentro del tiempo límite, entonces el backend cambia el estado de la asignación a aceptada, confirma a D1 y habilita el pedido en sus servicios asignados.

- AC-008. Rechazo de asignación por el domiciliario.
  Dado un pedido P1 asignado en estado pendiente de respuesta al domiciliario D1, cuando D1 presiona el botón Rechazar en Telegram, entonces el backend elimina la asignación, descuenta la carga de D1, deja el pedido P1 en la consola de despacho como sin repartidor y notifica al usuario que realizó la asignación informando del rechazo.

- AC-009. Expiración de asignación por tiempo agotado.
  Dado un pedido P1 asignado al domiciliario D1 en estado pendiente de respuesta, cuando transcurre el tiempo límite de respuesta (pendiente de OPEN-Q-001) sin que D1 responda, entonces el backend expira la asignación, remueve a D1 del pedido, restablece la orden en la consola de despacho sin repartidor y notifica al usuario asignador sobre la caducidad.

- AC-010. Cambio a no disponible y libramiento de servicios no iniciados.
  Dado un domiciliario D1 con el pedido P1 en estado listo para recoger (asignado) y el pedido P2 en estado en camino, cuando D1 cambia su disponibilidad a no disponible y confirma la operación, entonces el backend actualiza el estado de D1 a no disponible, libera el pedido P1 dejándolo sin repartidor en la consola y notificando al asignador, mientras mantiene el pedido P2 asignado a D1 para su finalización en ruta.

- AC-011. Restricción de visibilidad de datos personales del cliente.
  Dado el domiciliario D1 con el pedido P1 asignado activamente, cuando D1 consulta el detalle de P1 en el bot, entonces el backend retorna los productos, nombre, dirección, referencias y teléfono del cliente; cuando el pedido P1 pasa a estado entregado o cancelado y D1 intenta consultar nuevamente el detalle de P1, el backend deniega el acceso a los datos personales del cliente.

- AC-012. Notificación al domiciliario por cancelación de pedido.
  Dado un pedido P1 asignado al domiciliario D1 en estado listo para recoger, cuando el cliente o el negocio cancela el pedido P1, entonces el backend actualiza P1 a cancelado, remueve el pedido de los servicios activos de D1, descuenta la orden de su carga ocupada y envía una notificación automática al Telegram de D1 informando la cancelación del servicio.

### 12. Dependencias
- SPEC-002: Configuración del negocio (definición de tope de carga simultánea por domiciliario y personal del negocio).
- SPEC-004: Registro de pedidos y catálogo (pedidos creados y pasados a estado en preparación).
- Bot de Telegram: servicio de transporte de mensajes interactivos con botones inline para personal y repartidores.

### 13. Restricciones
- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración. Sección 4.
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante. Sección 4.
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar. Sección 4.
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales. Sección 4.
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración. Sección 4.
- Plazo: unas 8 semanas o más (DEC-E19). Sección 4.
- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada (3.3). Sección 6.
- Colombia: artículo 15 de la Constitución (habeas data), Ley 1581 de 2012 y Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015 (autorización previa, expresa e informada; aviso de privacidad; política de tratamiento; derechos de los titulares; transmisión y transferencia de datos). Autoridad: Superintendencia de Industria y Comercio. Sección 6.
- Referencia internacional de buenas prácticas (no se asume que aplique jurídicamente): principios del Reglamento General de Protección de Datos de la Unión Europea (minimización, limitación de finalidad y de plazo de conservación, transparencia). Sección 6.
- Textos de los avisos: docs/legal/avisos-de-privacidad.md (borrador; requiere revisión de una persona con formación jurídica antes de usarse con datos reales). Sección 6.

### 14. Fuera de alcance
- No es una central de repartidores (sección 5).
- No es un marketplace (sección 5).
- No cobra comisión por pedido ni por entrega (sección 5).
- No depende de otro aplicativo para su funcionamiento básico (sección 5).
- Mecanismo de persistencia y bloqueos de base de datos para la atomicidad de asignación: tema para arquitectura. Origen: RF-004.
- Gestión de colas o tareas en segundo plano para el temporizador de expiración de respuesta del domiciliario: tema para arquitectura. Origen: RF-005.

### 15. Preguntas abiertas
- OPEN-Q-001: Pendiente.

### 16. Trazabilidad
- HU-019: RF-001; BR-001; AC-001, AC-002.
- HU-020: RF-002; BR-002, BR-003; AC-003.
- HU-021: RF-003, RF-004; BR-002, BR-003, BR-005, BR-008; AC-004, AC-005, AC-006; CL-001, CL-002.
- HU-022: RF-005, RF-006; BR-004; AC-007, AC-008.
- HU-023: RF-005; BR-004; AC-009.
- HU-024: RF-009, RF-010; BR-007; AC-011; CL-005.
- HU-025: RF-011; BR-007; AC-012; CL-004.
- HU-037: RF-007, RF-008; BR-005, BR-006; AC-010; CL-003.
- RF-001: Origen: contexto 3.8, DEC-E21, DEC-E22; verificado por AC-001, AC-002.
- RF-002: Origen: contexto 3.8, DEC-E30, DEC-E31; verificado por AC-003.
- RF-003: Origen: contexto 3.8, DEC-E11, DEC-E12, DEC-E40; verificado por AC-004, AC-005.
- RF-004: Origen: contexto 3.2, 3.8 (regla crítica del proyecto); verificado por AC-006.
- RF-005: Origen: contexto 3.8, DEC-E23, DEC-E25; verificado por AC-005, AC-009.
- RF-006: Origen: DEC-E11, DEC-E23, DEC-E25; verificado por AC-007, AC-008.
- RF-007: Origen: contexto 3.7, DEC-E31; verificado por AC-010.
- RF-008: Origen: DEC-E25, DEC-E31; verificado por AC-010.
- RF-009: Origen: DEC-E32; verificado por AC-011.
- RF-010: Origen: contexto 3.3, DEC-E32; verificado por AC-011.
- RF-011: Origen: DEC-E13, DEC-E25; verificado por AC-012.
- RNF-001: Origen: contexto 3.2 (regla crítica del proyecto); verificado con Inspección del código backend y pruebas unitarias/integración de control de acceso.
- RNF-002: Origen: contexto 3.3 (regla crítica del proyecto); verificado con Pruebas de integración multitenant e intentos de acceso cruzado entre identificadores de diferentes negocios.
- RNF-003: Origen: contexto 3.8 (regla crítica del proyecto); verificado con Pruebas de carga estresando el endpoint de asignación con solicitudes simultáneas.
- RNF-004: Origen: regla crítica del proyecto 7 y DEC-E32; verificado con Inspección de plantillas de mensajes de notificación y pruebas de salida del bot.
- BR-001: Origen: contexto 3.2, 3.8, DEC-E22; verificado por AC-001, AC-002.
- BR-002: Origen: DEC-E12, DEC-E30, DEC-E40; verificado por AC-004.
- BR-003: Origen: DEC-E03; verificado por AC-003.
- BR-004: Origen: DEC-E23, DEC-E25; verificado por AC-007, AC-008, AC-009.
- BR-005: Origen: contexto 3.7; verificado por AC-005, AC-010.
- BR-006: Origen: DEC-E25, DEC-E31; verificado por AC-010.
- BR-007: Origen: contexto 3.3, DEC-E32; verificado por AC-011, AC-012.
- BR-008: Origen: DEC-E44; verificado por CL-002.
- CL-001: Origen: contexto 3.8 (regla crítica del proyecto); verificado por AC-006.
- CL-002: Origen: DEC-E44; verificado por CL-002.
- CL-003: Origen: DEC-E31; verificado por AC-010.
- CL-004: Origen: DEC-E13, DEC-E25; verificado por AC-012.
- CL-005: Origen: DEC-E32; verificado por AC-011.

### 17. Historial de cambios
- Versión 0.1: creación a partir de la necesidad.

## Verificación
- Completitud: no cumple (falta definir la respuesta de OPEN-Q-001 para la versión Candidata 1.0).
- Consistencia interna: cumple. Se verificaron las relaciones entre RF, BR, flujos, casos límite y criterios de aceptación, garantizando coincidencia en estados y reglas de carga.
- Consistencia con el contexto: cumple. Se compararon los requisitos y reglas de negocio con las decisiones DEC-E03, DEC-E11, DEC-E12, DEC-E21, DEC-E22, DEC-E23, DEC-E25, DEC-E30, DEC-E31, DEC-E32, DEC-E40 y DEC-E44 de la sección 3.
- No ambigüedad: cumple. Todos los comportamientos observables están redactados sin adjetivos vagos ni supuestos.
- Verificabilidad: cumple. Todos los criterios de aceptación están estructurados en formato Dado, Cuando, Entonces.
- Cobertura de actores: cumple. Se revisaron Administrador del negocio, Empleado o vendedor, Domiciliario y Cliente; cada actor cuenta con HU específicas (HU-019 a HU-025 y HU-037).
- Cobertura de AC: cumple. Todos los RF y BR cuentan con al menos un AC que los verifica.
- Trazabilidad: cumple. Todos los RF, RNF, BR y CL figuran en la sección 16 con su origen y método/AC de verificación.
- No invención: cumple. Se utilizaron únicamente las reglas del contexto y decisiones documentadas.
- Delimitación: cumple. No se incluyeron soluciones de diseño técnico ni código en la especificación funcional.

## Siguiente paso
Respondan las preguntas abiertas y ejecuten de nuevo el agente con --continuar SPEC-005.
