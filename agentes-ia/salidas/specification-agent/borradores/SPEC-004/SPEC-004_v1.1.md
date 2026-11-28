<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: ninguno (corrección manual de la revisión cruzada)
Fecha: 2026-11-21 15:39
Petición: corrección manual de la revisión cruzada de las SPEC, pedida por la estudiante
- OPEN-Q-001: un posible duplicado es un pedido igual del mismo cliente al mismo negocio dentro de 5 minutos (DEC-E50).
- OPEN-Q-002: cada negocio configura las formas de pago que acepta en su configuración (SPEC-002); el cliente elige entre ellas (DEC-E51).
- OPEN-Q-003: al enviar el pedido se revalida el catálogo; si un producto quedó agotado o desactivado (DEC-E46), se avisa al cliente para que lo quite o lo cambie (DEC-E52).
- OPEN-Q-004: cada negocio puede fijar un valor mínimo de compra en su configuración (0 = sin mínimo); si el pedido no lo alcanza, no se puede enviar (DEC-E53).
- Además: el cliente puede consultar el catálogo y armar su pedido por el chat o por la Mini App (DEC-E47), navegando por categorías (DEC-E45).
-->

# SPEC-004. Registro de cliente y gestión inicial del pedido - Versión 1.1
Estado: Candidata
Modo: Cambio
Necesidad original: "Respuesta del equipo a la propuesta de división: se elige la opción B. El catálogo (HU-10) ya se especifica aparte en la SPEC-003; esta SPEC-004 asume un catálogo existente y NO incluye HU-10. Especifica el registro del cliente, la toma y la gestión inicial del pedido antes del despacho (HU-11 a HU-18 del archivo adjunto): ingreso por el acceso de clientes del negocio con aviso de privacidad y contacto compartido (DEC-E05, DEC-E20, DEC-E29, DEC-E36, DEC-E37, DEC-E42); armado con productos del catálogo, barrio de la lista y dirección, forma de pago y total con tarifa (DEC-E06 a DEC-E08); rechazo por barrio sin cobertura o negocio cerrado (DEC-E09, DEC-E41); aviso de posible duplicado (DEC-E10); negocio vencido no recibe pedidos (DEC-E26); confirmación (pasa a en preparación) o rechazo con aviso al cliente (DEC-E17, DEC-E21, DEC-E22, DEC-E25); cancelación por el cliente o el negocio antes de en camino (DEC-E13)."
Épica: EPIC-002

## Análisis
- Objetivo: Permitir la vinculación e identificación de un cliente en un negocio mediante Telegram con consentimiento de datos, la composición y registro de su pedido calculando el total con tarifa de domicilio, la validación de reglas operativas (horario, cobertura, valor mínimo, productos vigentes, duplicados y suscripción), y la gestión inicial del pedido (confirmación a «en preparación», rechazo o cancelación previa a «en camino»).
- Alcance inicial: Registro de cliente en el negocio mediante botón nativo de Telegram y aceptación de privacidad; navegación del catálogo por categorías (desde chat o Mini App); armado del pedido con selección de productos activos, barrio de cobertura, dirección, referencias, forma de pago configurada y verificación de valor mínimo de compra; controles de estado de suscripción del negocio, horario de atención y zonas activas; revalidación del catálogo al enviar; detección de pedidos duplicados (ventana de 5 minutos) con confirmación previa; cambio de estado inicial por parte del negocio (confirmar a «en preparación» o rechazar) con notificaciones automáticas al cliente y personal; y cancelación del pedido antes del despacho («en camino») por parte del cliente o del establecimiento.
- Actores: Persona que desea realizar un pedido, Cliente, Administrador del negocio, Empleado o vendedor, Domiciliario.
- Contexto aplicable: Secciones 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8, 3.11 (DEC-E05, DEC-E06, DEC-E07, DEC-E08, DEC-E09, DEC-E10, DEC-E13, DEC-E17, DEC-E20, DEC-E21, DEC-E22, DEC-E25, DEC-E26, DEC-E29, DEC-E36, DEC-E37, DEC-E41, DEC-E42, DEC-E45, DEC-E46, DEC-E47, DEC-E50, DEC-E51, DEC-E52, DEC-E53), Sección 4, Sección 5 y Sección 6.

## Modelo de dominio
- Negocio: pertenece a la Plataforma; cardinalidad uno a varios. Origen: contexto 2.4, 3.3.
- Cliente: pertenece a Negocio; cardinalidad uno a varios (un usuario de Telegram se vincula como cliente independientemente en cada negocio). Origen: contexto 3.11, DEC-E29.
- Pedido: pertenece a Negocio y a Cliente; cardinalidad uno a varios por cliente. Origen: contexto 2.4, 3.8.
- Producto (Catálogo): pertenece a Negocio; cardinalidad uno a varios. Origen: contexto 3.11, DEC-E06, DEC-E45.
- Zona de cobertura (Barrio): pertenece a Negocio; cardinalidad uno a varios. Origen: contexto 3.5, DEC-E07.
- Consentimiento de Privacidad: pertenece a Cliente y a Negocio; cardinalidad uno a uno por registro. Origen: contexto 3.11, DEC-E36, DEC-E37.

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
- DEC-001 (DEC-E50): afecta a RF-009, BR-004, AC-012, AC-013 y añade CL-005. Todos actualizados con la regla de 5 minutos.
- DEC-002 (DEC-E51): afecta a RF-004, BR-003 y AC-010. Todos actualizados para indicar que el cliente selecciona únicamente entre las formas de pago configuradas por el negocio.
- DEC-003 (DEC-E52): afecta a RF-016, BR-008, E7 y añade AC-019. Todos actualizados para exigir la revalidación del catálogo al momento del envío.
- DEC-004 (DEC-E53): afecta a RF-017, BR-007, E8 y añade AC-020 y CL-006. Todos actualizados con la validación del monto mínimo de compra en productos.
- DEC-005 (DEC-E45, DEC-E47): afecta a HU-012, RF-004, BR-002, AC-009 y AC-010. Todos actualizados para soportar consulta por categorías tanto en chat como en Mini App.

## Preguntas de aclaración
No hay preguntas pendientes.

## Especificación

### 1. Objetivo
Registrar e identificar clientes en cada negocio respetando el habeas data mediante Telegram, permitir la consulta de catálogo por categorías (vía chat o Mini App) y la configuración de pedidos calculando el monto total más la tarifa de domicilio (validando compra mínima, disponibilidad de productos y formas de pago aceptadas), e implementar la gestión inicial del ciclo de vida del pedido (recibido, en preparación, rechazado o cancelado) con notificaciones a las partes interesadas.

### 2. Contexto
Cada negocio posee un enlace o código QR de acceso exclusivo para clientes (DEC-E42). Cuando una persona entra por primera vez a un negocio, debe otorgar su consentimiento explícito del tratamiento de datos personales y compartir su contacto mediante el botón nativo de Telegram (DEC-E20, DEC-E36). Los clientes arman sus pedidos navegando por el catálogo estructurado en categorías (por chat o Mini App) eligiendo productos activos y zonas vigentes del negocio. Al registrar un pedido, el sistema revalida la disponibilidad de productos, el monto mínimo y las posibles duplicidades en 5 minutos. Si todo es correcto, el pedido entra en estado «recibido». El personal del negocio (administrador o empleado) revisa el pedido para pasarlo a «en preparación» (confirmado) o «rechazado». Tanto el cliente como el negocio pueden cancelar el pedido antes de que este pase al estado «en camino».

Decisiones del equipo:
- DEC-001. Un posible duplicado es un pedido igual (mismos productos, cantidades y dirección) del mismo cliente al mismo negocio realizado dentro de los 5 minutos posteriores a un pedido anterior. Responde a OPEN-Q-001 (Origen: DEC-E50).
- DEC-002. Cada negocio configura las formas de pago que acepta en su administración (SPEC-002); el cliente elige entre esas opciones al armar su pedido. Responde a OPEN-Q-002 (Origen: DEC-E51).
- DEC-003. Al enviar el pedido se revalida el catálogo; si un producto seleccionado quedó agotado o desactivado, se rechaza la solicitud y se avisa al cliente para que lo quite o lo cambie. Responde a OPEN-Q-003 (Origen: DEC-E52).
- DEC-004. Cada negocio puede fijar un valor mínimo de compra en productos en su configuración ($0 = sin mínimo); si la suma de los productos del pedido no alcanza dicho valor, el pedido no se puede enviar. Responde a OPEN-Q-004 (Origen: DEC-E53).
- DEC-005. El cliente puede consultar el catálogo y armar su pedido navegando por categorías tanto a través del chat de Telegram como de la Mini App. Responde a requerimiento del equipo (Origen: DEC-E45, DEC-E47).

### 3. Alcance
- Registro e identificación de clientes por negocio mediante el enlace/QR de clientes y el botón nativo de Telegram.
- Aceptación y registro legible de la autorización de tratamiento de datos del negocio por parte del cliente.
- Consulta de catálogo activo organizado por categorías desde el chat de Telegram o mediante la Mini App.
- Selección de productos, cantidades, barrio de entrega, dirección con referencias y forma de pago entre las configuradas por el negocio.
- Validación de monto mínimo de compra en productos configurado por el negocio.
- Cálculo automático del monto del pedido (suma de productos + tarifa de domicilio de la zona seleccionada).
- Bloqueo de toma de pedidos si el negocio está cerrado por horario, si el barrio no tiene cobertura o si la suscripción del negocio está vencida.
- Revalidación de disponibilidad de productos al formalizar el envío del pedido.
- Advertencia de pedido potencialmente duplicado (dentro de 5 minutos) con solicitud de confirmación explícita.
- Cambio de estado del pedido por el personal del negocio de «recibido» a «en preparación» (confirmar) o «rechazado».
- Cancelación del pedido por el cliente o el negocio mientras el estado sea «recibido», «en preparación» o «listo para recoger».
- Notificaciones automáticas por Telegram a cliente y personal ante cambios de estado y nuevos pedidos.

### 4. Actores e historias de usuario
Actores:
- Persona que desea realizar un pedido: usuario de Telegram que accede al negocio para vincularse como cliente.
- Cliente: persona registrada e identificada en el negocio que arma y gestiona sus pedidos.
- Administrador del negocio: gestiona la atención del negocio, confirma, rechaza o cancela pedidos de su establecimiento.
- Empleado o vendedor: atiende la operación, confirma, rechaza o cancela pedidos de su establecimiento.
- Domiciliario: repartidor vinculado al negocio (sin permisos para confirmar, rechazar ni tomar pedidos).

Historias de usuario:
- HU-011. Como Persona que desea realizar un pedido, quiero ingresar al bot a través del enlace o código QR propio del negocio e identificarme con mi contacto de Telegram y aceptar la política de privacidad, para realizar pedidos de forma verificada en ese establecimiento.
- HU-012. Como Cliente, quiero consultar el catálogo por categorías (desde el chat o la Mini App), seleccionar productos activos, cantidades, barrio de entrega, dirección con referencias y forma de pago aceptada por el negocio, para conocer el total a pagar y enviar la orden si cumple el valor mínimo de compra.
- HU-013. Como Cliente, quiero que el sistema me informe si mi barrio no tiene cobertura o si el negocio está cerrado, para saber de inmediato si el negocio puede atender mi pedido.
- HU-014. Como Cliente, quiero recibir una alerta de confirmación si envío un pedido idéntico al anterior en menos de 5 minutos, para evitar realizar por error duplicados no deseados.
- HU-015. Como Cliente, quiero que el sistema me prevenga de hacer pedidos en establecimientos no disponibles, para no realizar compras en negocios que no pueden procesar mi atención.
- HU-016. Como Empleado o vendedor, quiero revisar los pedidos en estado recibido para confirmarlos o rechazarlos, para iniciar la preparación de la orden o informar oportunamente al cliente en caso de no poder atenderla.
- HU-017. Como Cliente, quiero cancelar mi pedido mientras no haya pasado a estado en camino, para desistir de la compra de forma oportuna si se presenta algún imprevisto.
- HU-018. Como Administrador del negocio, quiero cancelar un pedido activo antes de que esté en camino, para dar de baja solicitudes que no se pueden cumplir o que el cliente canceló por otros medios.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir el ingreso de la persona mediante el enlace o código QR exclusivo de clientes del negocio y validar su estado de registro previo en ese establecimiento. Origen: contexto 3.11 (DEC-E05, DEC-E42).
- RF-002. El sistema debe solicitar y registrar la autorización previa, expresa e informada del tratamiento de datos personales de la persona mediante un botón explícito antes de permitirle compartir su contacto, guardando fecha, hora y versión del texto legal. Origen: contexto 3.11 (DEC-E36, DEC-E37).
- RF-003. El sistema debe solicitar el contacto de la persona utilizando exclusivamente el botón nativo de Telegram, asociando su teléfono verificado e identificador de chat como cliente del negocio específico. Origen: contexto 3.11 (DEC-E20, DEC-E29).
- RF-004. El sistema debe permitir al cliente consultar el catálogo por categorías y armar su pedido (desde el chat de Telegram o mediante la Mini App), seleccionando productos activos, cantidades, barrio de entrega de la lista de cobertura del negocio, dirección con referencias y forma de pago entre las configuradas por el negocio, solicitando confirmación antes de formalizar el registro. Origen: contexto 3.7, 3.11 (DEC-E06, DEC-E07, DEC-E08, DEC-E45, DEC-E47, DEC-E51); DEC-002, DEC-005.
- RF-005. El sistema debe calcular automáticamente el valor total del pedido sumando el precio de los productos seleccionados y la tarifa de domicilio configurada para el barrio elegido. Origen: contexto 3.5, 3.11 (DEC-E06).
- RF-006. El sistema debe verificar el estado de la suscripción del negocio y rechazar el inicio del proceso de pedido si la suscripción está en estado «vencida», notificando al cliente que el establecimiento no está recibiendo pedidos temporalmente. Origen: contexto 3.11 (DEC-E26).
- RF-007. El sistema debe verificar el horario de atención del negocio para el día actual (incluyendo festivos) e impedir el armado del pedido si el establecimiento está cerrado, mostrando el horario de atención al cliente. Origen: contexto 3.11 (DEC-E09, DEC-E41).
- RF-008. El sistema debe validar que el barrio ingresado pertenezca a las zonas de cobertura activas del negocio, rechazando el registro de la orden e informando al cliente si el barrio no cuenta con cobertura. Origen: contexto 3.5, 3.11 (DEC-E09).
- RF-009. El sistema debe detectar pedidos potencialmente duplicados (mismo cliente, mismo negocio, mismos productos, cantidades y dirección de entrega registrados dentro de los 5 minutos posteriores a un pedido previo), solicitando confirmación explícita al cliente antes de registrarlo. Origen: contexto 3.7, 3.11 (DEC-E10, DEC-E50); DEC-001.
- RF-010. Al confirmarse el pedido por parte del cliente, el sistema debe crearlo en estado «recibido», registrar fecha, hora y cliente responsable, y enviar una notificación automática de pedido nuevo al administrador y empleados del negocio. Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E25).
- RF-011. El sistema debe permitir al administrador del negocio y al empleado o vendedor confirmar un pedido en estado «recibido», previa confirmación, cambiando su estado a «en preparación», registrando fecha, hora y usuario responsable en el sistema, y notificando al cliente. Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25).
- RF-012. El sistema debe permitir al administrador del negocio y al empleado o vendedor rechazar un pedido en estado «recibido», previa confirmación, cambiando su estado a «rechazado» (estado final), registrando fecha, hora y usuario responsable en el sistema, y notificando al cliente. Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25).
- RF-013. El sistema debe permitir al cliente cancelar su pedido si se encuentra en estado «recibido», «en preparación» o «listo para recoger», previa confirmación, registrando el estado «cancelado» (estado final), fecha, hora, cliente como responsable, y notificando al administrador y empleados del negocio. Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25).
- RF-014. El sistema debe permitir al administrador del negocio y al empleado o vendedor cancelar un pedido en estado «recibido», «en preparación» o «listo para recoger», previa confirmación, registrando el estado «cancelado» (estado final), fecha, hora, usuario responsable, y notificando al cliente. Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25).
- RF-015. El sistema debe impedir la cancelación del pedido por parte del cliente, administrador o empleado si el pedido ya se encuentra en estado «en camino» o posterior. Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E22).
- RF-016. El sistema debe revalidar el catálogo al momento de formalizar el pedido y rechazar la creación si un producto seleccionado cambió a estado agotado o desactivado, notificando al cliente para que modifique o retire el producto. Origen: contexto 3.11 (DEC-E46, DEC-E52); DEC-003.
- RF-017. El sistema debe verificar que la suma del precio de los productos alcance o supere el valor mínimo de compra configurado por el negocio ($0 = sin mínimo) antes de permitir el envío del pedido, impidiendo el registro si no se alcanza. Origen: contexto 3.11 (DEC-E53); DEC-004.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización. El sistema debe verificar la identidad del usuario, el rol, el negocio al que pertenece y los permisos específicos para cada operación de consulta, creación o cambio de estado. Se verifica mediante: inspección de código sistema y pruebas de penetración de roles. Origen: contexto 3.2.
- RNF-002. Separación de información. Los usuarios de un negocio no deben acceder, consultar ni modificar datos, catálogos, zonas ni pedidos de otros negocios. Se verifica mediante: pruebas automatizadas de aislamiento de datos entre negocios. Origen: contexto 3.3.
- RNF-003. Concurrencia y atomicidad. Las actualizaciones de estado del pedido deben ejecutarse de manera atómica en el sistema para evitar estados inconsistentes o dobles cambios simultáneos. Se verifica mediante: pruebas de carga y concurrencia simultánea sobre el mismo pedido. Origen: contexto 3.8.
- RNF-004. Trazabilidad de operaciones. Cada cambio de estado debe registrar de manera inmutable fecha, hora exacta, nuevo estado y usuario responsable. Se verifica mediante: auditoría de registros de base de datos tras la ejecución de flujos de pedido. Origen: contexto 3.8.

### 7. Reglas de negocio
- BR-001. Registro independiente por negocio. La vinculación de una persona como cliente aplica únicamente para el negocio cuyo enlace o QR utilizó. Si la persona interactúa con otro negocio, debe aceptar el aviso de privacidad de ese nuevo negocio y volver a compartir su contacto con el botón nativo (DEC-E29). Origen: contexto 3.11 (DEC-E29).
- BR-002. Restricción de visibilidad de datos al cliente. Durante la creación del pedido (por chat o Mini App), el cliente solo puede visualizar y elegir categorías y productos activos, y zonas pertenecientes al negocio específico en el que se encuentra interactuando. Origen: contexto 3.3, 3.11 (DEC-E06, DEC-E07, DEC-E28, DEC-E45, DEC-E47); DEC-005.
- BR-003. Formas de pago aceptadas. El cobro del pedido se efectúa fuera del sistema. El pedido únicamente almacena la forma de pago seleccionada por el cliente entre las opciones previamente habilitadas en la configuración del negocio (SPEC-002). Origen: contexto 3.11 (DEC-E08, DEC-E51); DEC-002.
- BR-004. Detección de duplicados. Se considera un pedido potencialmente duplicado cuando un mismo cliente registra un pedido con exactamente los mismos productos, cantidades, barrio y dirección en un mismo negocio en un intervalo menor o igual a 5 minutos desde un pedido previo. En este caso, el sistema exige confirmación explícita para registrarlo. Origen: contexto 3.7, 3.11 (DEC-E10, DEC-E50); DEC-001.
- BR-005. Transiciones permitidas del estado del pedido.
  - Recibido → En preparación (provocado por Admin/Empleado).
  - Recibido → Rechazado (provocado por Admin/Empleado, estado final).
  - Recibido / En preparación / Listo para recoger → Cancelado (provocado por Cliente o Admin/Empleado, estado final).
  - El rol Domiciliario no tiene permiso para cambiar el estado de un pedido en «recibido». Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E22).
- BR-006. Protección de datos de contacto. Ningún mensaje de notificación pública o grupal expone el número de teléfono, dirección exacta o nombre del cliente a usuarios no autorizados de acuerdo con la sección 3.3 y la regla crítica 7. Origen: contexto 3.3 y Regla Crítica 7.
- BR-007. Valor mínimo de compra. El negocio establece un valor mínimo de compra en productos en su configuración ($0 significa sin valor mínimo). El pedido no puede ser enviado si la suma del valor de los productos es menor a dicho valor mínimo. La tarifa de domicilio se calcula aparte y no suma para alcanzar el monto mínimo. Origen: contexto 3.11 (DEC-E53); DEC-004.
- BR-008. Revalidación de catálogo al enviar. Al momento de confirmar el envío del pedido, el sistema verifica que todos los productos seleccionados permanezcan en estado activo. Si un producto cambió a agotado o desactivado, la orden no se registra en «recibido» y se notifica al cliente para que ajuste su pedido. Origen: contexto 3.11 (DEC-E46, DEC-E52); DEC-003.

### 8. Flujo principal
1. La persona ingresa al bot mediante el enlace o código QR exclusivo para clientes del negocio (DEC-E42).
2. El sistema verifica si el cliente ya está registrado y aceptó los términos en este negocio. Si no está registrado, le presenta el aviso de privacidad (DEC-E36) y le solicita presionar el botón de autorización de datos.
3. Al autorizar, el sistema solicita compartir el contacto mediante el botón nativo de Telegram (DEC-E20). La persona presiona el botón y el sistema la registra como cliente del negocio.
4. El sistema valida el estado de la suscripción del negocio (DEC-E26) y su horario de atención actual (DEC-E41). Al estar la suscripción al día y el negocio abierto, presenta el catálogo activo organizado por categorías para navegarlo por chat o Mini App (DEC-E45, DEC-E47).
5. El cliente selecciona los productos y sus cantidades.
6. El cliente selecciona el barrio de entrega de la lista de zonas de cobertura del negocio (DEC-E07). El sistema obtiene la tarifa de domicilio asociada.
7. El cliente ingresa la dirección exacta de entrega y observaciones o referencias.
8. El cliente selecciona la forma de pago entre las opciones configuradas por el negocio (DEC-E51).
9. El sistema verifica que la suma de los productos cumpla con el valor mínimo de compra configurado por el negocio (DEC-E53).
10. El sistema calcula el valor total (productos + tarifa de domicilio) y presenta el resumen del pedido pidiendo confirmación (DEC-E06, DEC-E07).
11. El cliente confirma el envío del pedido.
12. El sistema revalida la disponibilidad activa de todos los productos del pedido (DEC-E52) y verifica que no sea un pedido duplicado registrado dentro de los últimos 5 minutos (DEC-E50).
13. El sistema guarda el pedido en estado «recibido», registra la fecha, hora y cliente como responsable, y notifica al administrador y a los empleados del negocio con los detalles del nuevo pedido (DEC-E21, DEC-E25).
14. Un empleado o administrador del negocio consulta el pedido en estado «recibido» y selecciona la opción de confirmar.
15. El sistema pide confirmación de la operación (contexto 3.7). El usuario confirma.
16. El sistema actualiza atómicamente el estado del pedido a «en preparación», guarda la fecha, hora y usuario responsable, y envía una notificación automática al cliente confirmando la orden y el total a pagar (DEC-E17, DEC-E21, DEC-E22).

### 9. Flujos alternativos y de excepción
- A1. Reintento de registro de cliente ya vinculado:
  1. En el paso 2 del flujo principal, el sistema detecta que el cliente ya aceptó los términos y compartió su contacto en este negocio previamente.
  2. El sistema omite la solicitud de privacidad y contacto, y pasa directamente a verificar suscripción y horario (paso 4).
- A2. Cliente rechaza pedido potencialmente duplicado:
  1. En el paso 12 del flujo principal, el sistema detecta un pedido con los mismos productos, cantidades y dirección registrado dentro de los últimos 5 minutos (DEC-E50).
  2. El sistema muestra un mensaje de advertencia indicando la posible duplicidad y pide confirmar si desea realizar un nuevo pedido o cancelar.
  3. El cliente selecciona cancelar la operación.
  4. El sistema descarta la orden en borrador sin guardar nada en la base de datos y le notifica al cliente.
- A3. Cliente confirma pedido potencialmente duplicado:
  1. En el paso 2 de A2, el cliente selecciona confirmar expresamente la repetición del pedido.
  2. El sistema continúa en el paso 13 del flujo principal guardando el pedido como una orden independiente.
- A4. Rechazo del pedido por el negocio:
  1. En el paso 14 del flujo principal, el empleado o administrador selecciona la opción de rechazar el pedido.
  2. El sistema solicita confirmación del rechazo.
  3. El usuario confirma.
  4. El sistema cambia el estado del pedido a «rechazado», guarda la fecha, hora y usuario responsable, y envía una notificación al cliente informando que su pedido fue rechazado (DEC-E17, DEC-E22).
- A5. Cancelación del pedido por el cliente antes de «en camino»:
  1. En cualquier momento mientras el pedido esté en estado «recibido», «en preparación» o «listo para recoger», el cliente selecciona la opción de cancelar pedido.
  2. El sistema solicita confirmación explícita de la cancelación.
  3. El cliente confirma.
  4. El sistema actualiza el estado del pedido a «cancelado», guarda la fecha, hora y el cliente como responsable, y envía una notificación inmediata al administrador y empleados del negocio (DEC-E13, DEC-E25).
- A6. Cancelación del pedido por el negocio antes de «en camino»:
  1. Mientras el pedido está en estado «recibido», «en preparación» o «listo para recoger», el administrador o empleado selecciona la opción de cancelar pedido.
  2. El sistema solicita confirmación explícita.
  3. El usuario confirma.
  4. El sistema actualiza el estado a «cancelado», guarda la fecha, hora y usuario responsable, y notifica al cliente sobre la cancelación de la orden (DEC-E13, DEC-E17).

- E1. Intento de enviar número por texto manual:
  1. En el paso 3 del flujo principal, la persona escribe su número de teléfono en texto en lugar de presionar el botón nativo de Telegram.
  2. El sistema rechaza el texto escrito e informa que debe presionar obligatoriamente el botón nativo para verificar su teléfono (DEC-E20).
- E2. Negocio con suscripción vencida:
  1. En el paso 4 del flujo principal, el sistema verifica que la suscripción del negocio está marcada como «vencida» (DEC-E26).
  2. El sistema bloquea el flujo y muestra un mensaje al cliente informando que el negocio no está recibiendo pedidos temporalmente.
- E3. Negocio cerrado por horario:
  1. En el paso 4 del flujo principal, el sistema verifica que la hora actual está fuera del rango de atención del negocio o en día festivo cerrado (DEC-E09, DEC-E41).
  2. El sistema rechaza la solicitud de pedido, informa el horario de atención del establecimiento y no permite continuar con el registro.
- E4. Barrio sin cobertura de domicilio:
  1. En el paso 6 del flujo principal, el cliente intenta ingresar un barrio que no está en la lista de cobertura del negocio.
  2. El sistema rechaza el barrio e informa que no realiza entregas en dicha ubicación (DEC-E09).
- E5. Intento de cancelación en estado «en camino» o posterior:
  1. En el paso 1 de A5 o A6, el pedido ya cambió de estado a «en camino».
  2. El sistema deniega la acción de cancelación e informa que el pedido ya fue despachado y que cualquier eventualidad debe ser tratada como novedad (DEC-E13).
- E6. Domiciliario intenta confirmar o rechazar pedido:
  1. Un usuario con rol Domiciliario intenta ejecutar la confirmación o rechazo de un pedido en estado «recibido».
  2. El sistema deniega la operación enviando un mensaje de falta de permisos (RNF-001).
- E7. Producto agotado o desactivado al enviar el pedido:
  1. En el paso 12 del flujo principal, la revalidación del sistema detecta que un producto del pedido pasó a estar agotado o desactivado (DEC-E52).
  2. El sistema detiene la creación del pedido en «recibido» e informa al cliente qué producto ya no está disponible para que lo retire o lo cambie.
- E8. Pedido no alcanza el valor mínimo de compra:
  1. En el paso 9 del flujo principal, la suma de los productos no alcanza el valor mínimo de compra fijado por el negocio (DEC-E53).
  2. El sistema bloquea el avance del pedido, informa el valor mínimo requerido y el faltante en productos para poder realizar la orden.

### 10. Casos límite
- CL-001. Intento de registrar pedido en el exacto minuto de cierre del negocio: se evalúa la hora de confirmación final en el sistema; si es igual o posterior al límite de cierre, el pedido es rechazado por horario (DEC-E09, DEC-E41). Origen: contexto 3.11 (DEC-E09, DEC-E41).
- CL-002. Intento de cancelación por el cliente cuando el negocio acaba de pasar el pedido a «en camino» simultáneamente: la operación atómica en sistema rechaza la cancelación por haber cambiado de estado previamente (DEC-E13, RNF-003). Origen: contexto 3.8, 3.11 (DEC-E13).
- CL-003. Cliente intenta ingresar texto manual de teléfono reiteradamente: el bot no avanza ni genera registro de cliente hasta que se presione el botón nativo de Telegram (DEC-E20). Origen: contexto 3.11 (DEC-E20).
- CL-004. Cliente registrado en el negocio A intenta hacer un pedido en el negocio B con el enlace de B: el sistema detecta que no tiene registro en B, le pide aceptar el aviso de privacidad de B y compartir nuevamente su contacto para B (DEC-E29). Origen: contexto 3.11 (DEC-E29).
- CL-005. Cliente envía un pedido idéntico a los 4 minutos y 59 segundos de haber registrado el pedido anterior: el sistema lo detecta como posible duplicado y exige confirmación explícita antes de guardarlo (DEC-E50). Origen: contexto 3.11 (DEC-E50); DEC-001.
- CL-006. Cliente intenta enviar un pedido cuyo valor de productos es de $9.999 COP en un negocio con compra mínima de $10.000 COP y domicilio de $3.000 COP (total $12.999 COP): el sistema bloquea el envío indicando que el subtotal en productos no alcanza el mínimo (DEC-E53). Origen: contexto 3.11 (DEC-E53); DEC-004.

### 11. Criterios de aceptación
- AC-001. Dado que una persona no registrada accede mediante el enlace o QR de clientes del negocio, cuando inicia la interacción, entonces el sistema le presenta el aviso de privacidad del negocio exigiendo aceptación con botón explícito antes de permitir compartir datos (RF-001, RF-002; BR-001).
- AC-002. Dado que la persona presiona el botón de aceptar aviso de privacidad, cuando el sistema guarda el registro, entonces almacena la fecha, hora exacta y versión del texto aceptado (RF-002).
- AC-003. Dado que la persona intenta registrar su contacto enviando un texto manual en el chat de Telegram, cuando se procesa el mensaje, entonces el sistema rechaza el texto y exige presionar el botón nativo de Telegram (RF-003).
- AC-004. Dado que la persona presiona el botón nativo de Telegram para compartir contacto, cuando el sistema lo recibe, entonces registra el número telefónico verificado y vincula a la persona como cliente exclusivo de ese negocio (RF-003; BR-001).
- AC-005. Dado que un cliente registrado en el negocio A entra por el enlace del negocio B, cuando inicia interacción en B, entonces el sistema le solicita aceptar el aviso de privacidad y compartir su contacto nuevamente para el negocio B (RF-001, RF-003; BR-001; CL-004).
- AC-006. Dado que un cliente inicia un pedido en un negocio con suscripción vencida, cuando ingresa al flujo de compra, entonces el sistema le impide continuar e informa que el negocio no está recibiendo pedidos temporalmente (RF-006).
- AC-007. Dado que un cliente intenta hacer un pedido fuera del horario de atención o en un día festivo no laboral del negocio, cuando inicia la solicitud, entonces el sistema le informa que el negocio está cerrado, le muestra sus horarios y no permite continuar (RF-007; CL-001).
- AC-008. Dado que un cliente selecciona un barrio que no está en la lista de cobertura del negocio, cuando intenta avanzar en el pedido, entonces el sistema rechaza la solicitud e informa que no hay entregas en esa ubicación (RF-008).
- AC-009. Dado que un cliente navega por categorías de productos activos y selecciona una zona con tarifa de $5.000 COP, cuando avanza al resumen, entonces el sistema calcula el valor total sumando el monto de los productos seleccionados más los $5.000 COP de domicilio (RF-004, RF-005; BR-002).
- AC-010. Dado que un cliente completa la selección de productos, barrio, dirección de entrega con referencias y forma de pago configurada por el negocio, cuando presiona enviar pedido, entonces el sistema le muestra el resumen total y le exige confirmación antes de formalizar la solicitud (RF-004; BR-003).
- AC-011. Dado que el cliente confirma el resumen de su pedido y cumple todas las validaciones, cuando el sistema lo procesa, entonces crea el pedido en estado «recibido», registra fecha, hora y cliente como responsable, y notifica al administrador y a los empleados del negocio (RF-010).
- AC-012. Dado un cliente que envía un pedido idéntico al anterior en el mismo negocio en un lapso menor o igual a 5 minutos, cuando el sistema procesa la orden, entonces detiene el registro y muestra un aviso de posible duplicidad exigiendo confirmación (RF-009; BR-004; CL-005).
- AC-013. Dado un aviso de posible duplicado por ventana de 5 minutos, cuando el cliente elige cancelar la orden, entonces el sistema descarta la nueva solicitud sin alterar los pedidos ya registrados (RF-009; BR-004).
- AC-014. Dado un pedido en estado «recibido», cuando el administrador o empleado selecciona confirmar el pedido y responde afirmativamente a la confirmación previa, entonces el sistema cambia el estado a «en preparación», guarda fecha, hora y responsable en el sistema, y notifica al cliente con el total a pagar (RF-011; BR-005).
- AC-015. Dado un pedido en estado «recibido», cuando el administrador o empleado selecciona rechazar el pedido y confirma la acción, entonces el sistema cambia el estado a «rechazado», guarda fecha, hora y responsable en el sistema, y notifica al cliente el rechazo (RF-012; BR-005).
- AC-016. Dado un usuario con rol Domiciliario, cuando intenta confirmar o rechazar un pedido en estado «recibido», entonces el sistema deniega la acción por falta de permisos (RNF-001; BR-005).
- AC-017. Dado un pedido en estado «recibido», «en preparación» o «listo para recoger», cuando el cliente o un empleado/administrador solicita cancelar y confirma la acción, entonces el sistema cambia el estado a «cancelado», registra fecha, hora y responsable, y notifica a la otra parte (RF-013, RF-014; BR-005).
- AC-018. Dado un pedido que pasó a estado «en camino», cuando el cliente, administrador o empleado intenta cancelarlo, entonces el sistema deniega la acción e informa que debe tratarse como novedad de entrega (RF-015; CL-002).
- AC-019. Dado un cliente que envía un pedido cuyos productos seleccionados cambiaron a agotado o desactivado durante el armado, cuando confirma el envío, entonces el sistema detiene el registro en «recibido» y notifica al cliente para que modifique el carrito (RF-016; BR-008).
- AC-020. Dado un cliente en un negocio con valor mínimo de compra de $10.000 COP, cuando intenta enviar un pedido cuyos productos suman $9.999 COP, entonces el sistema bloquea el envío e informa que no se alcanza la compra mínima (RF-017; BR-007; CL-006).

### 12. Dependencias
- SPEC-001 (Gestión de negocios, suscripción de plataforma y términos legales): provee el estado de suscripción del negocio (DEC-E26) y el texto legal de aviso de privacidad (DEC-E36, DEC-E37).
- SPEC-002 (Configuración del negocio): provee las formas de pago aceptadas (DEC-E51), el valor mínimo de compra (DEC-E53), la lista de barrios con tarifa de domicilio y el horario de atención por día/festivo (DEC-E07, DEC-E09, DEC-E41).
- SPEC-003 (Gestión de catálogo de productos): provee las categorías, productos activos, precios y estado agotado/desactivado (DEC-E06, DEC-E27, DEC-E28, DEC-E45, DEC-E46).

### 13. Restricciones
- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración. Sección 4.
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante. Sección 4.
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar. Sección 4.
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales. Sección 4.
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración. Sección 4.
- Plazo: unas 8 semanas o más (DEC-E19). Sección 4.
- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada (3.3). Sección 6.
- Colombia: artículo 15 de la Constitución (habeas data), Ley 1581 de 2012 y Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015 (autorización previa, expresa e informada; aviso de privacidad; política de tratamiento; derechos de los titulares; transmisión y transferencia de datos). Autoridad: Superintendencia de Industria y Comercio. Sección 6.
- Referencia internacional de buenas prácticas: principios del Reglamento General de Protección de Datos de la Unión Europea (minimización, limitación de finalidad y de plazo de conservación, transparencia). Sección 6.

### 14. Fuera de alcance
- No es una central de repartidores. Sección 5.
- No es un marketplace. Sección 5.
- No cobra comisión por pedido ni por entrega. Sección 5.
- No depende de otro aplicativo para su funcionamiento básico. Sección 5.
- Administración del catálogo de productos (especificado en SPEC-003 / HU-010).
- Asignación de domiciliarios y seguimiento del pedido en camino / entregado (especificado en SPEC-005 / EPIC-003).
- Integración con pasarelas de pago electrónico en línea (el cobro ocurre fuera del sistema).
- [Estructura de arreglos o colecciones en memoria/base de datos para almacenamiento de pedidos y clientes]: tema para arquitectura. Origen: HU-11, HU-12.

### 15. Preguntas abiertas
- OPEN-Q-001: Respondida (DEC-001).
- OPEN-Q-002: Respondida (DEC-002).
- OPEN-Q-003: Respondida (DEC-003).
- OPEN-Q-004: Respondida (DEC-004).

### 16. Trazabilidad
- HU-011: RF-001, RF-002, RF-003; BR-001; AC-001, AC-002, AC-003, AC-004, AC-005; CL-003, CL-004.
- HU-012: RF-004, RF-005, RF-010, RF-016, RF-017; BR-002, BR-003, BR-007, BR-008; AC-009, AC-010, AC-011, AC-019, AC-020; CL-006.
- HU-013: RF-007, RF-008; AC-007, AC-008; CL-001.
- HU-014: RF-009; BR-004; AC-012, AC-013; CL-005.
- HU-015: RF-006; AC-006.
- HU-016: RF-011, RF-012; BR-005; AC-014, AC-015, AC-016.
- HU-017: RF-013, RF-015; BR-005; AC-017, AC-018; CL-002.
- HU-018: RF-014, RF-015; BR-005; AC-017, AC-018; CL-002.
- RF-001: Origen: contexto 3.11 (DEC-E05, DEC-E42); verificado por AC-001, AC-005.
- RF-002: Origen: contexto 3.11 (DEC-E36, DEC-E37); verificado por AC-001, AC-002.
- RF-003: Origen: contexto 3.11 (DEC-E20, DEC-E29); verificado por AC-003, AC-004, AC-005.
- RF-004: Origen: contexto 3.7, 3.11 (DEC-E06, DEC-E07, DEC-E08, DEC-E45, DEC-E47, DEC-E51); DEC-002, DEC-005; verificado por AC-009, AC-010.
- RF-005: Origen: contexto 3.5, 3.11 (DEC-E06); verificado por AC-009.
- RF-006: Origen: contexto 3.11 (DEC-E26); verificado por AC-006.
- RF-007: Origen: contexto 3.11 (DEC-E09, DEC-E41); verificado por AC-007.
- RF-008: Origen: contexto 3.5, 3.11 (DEC-E09); verificado por AC-008.
- RF-009: Origen: contexto 3.7, 3.11 (DEC-E10, DEC-E50); DEC-001; verificado por AC-012, AC-013.
- RF-010: Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E25); verificado por AC-011.
- RF-011: Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25); verificado por AC-014.
- RF-012: Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25); verificado por AC-015.
- RF-013: Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25); verificado por AC-017.
- RF-014: Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25); verificado por AC-017.
- RF-015: Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E22); verificado por AC-018.
- RF-016: Origen: contexto 3.11 (DEC-E46, DEC-E52); DEC-003; verificado por AC-019.
- RF-017: Origen: contexto 3.11 (DEC-E53); DEC-004; verificado por AC-020.
- RNF-001: Origen: contexto 3.2; verificado con pruebas de penetración de roles y AC-016.
- RNF-002: Origen: contexto 3.3; verificado con pruebas automatizadas de aislamiento de datos entre negocios.
- RNF-003: Origen: contexto 3.8; verificado con pruebas de carga y concurrencia simultánea sobre el mismo pedido.
- RNF-004: Origen: contexto 3.8; verificado con auditoría de registros de base de datos tras la ejecución de flujos de pedido.
- BR-001: Origen: contexto 3.11 (DEC-E29); verificado por AC-001, AC-004, AC-005.
- BR-002: Origen: contexto 3.3, 3.11 (DEC-E06, DEC-E07, DEC-E28, DEC-E45, DEC-E47); DEC-005; verificado por AC-009.
- BR-003: Origen: contexto 3.11 (DEC-E08, DEC-E51); DEC-002; verificado por AC-010.
- BR-004: Origen: contexto 3.7, 3.11 (DEC-E10, DEC-E50); DEC-001; verificado por AC-012, AC-013.
- BR-005: Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E22); verificado por AC-014, AC-015, AC-016, AC-017.
- BR-006: Origen: contexto 3.3 y Regla Crítica 7; verificado con inspección de plantillas de notificación.
- BR-007: Origen: contexto 3.11 (DEC-E53); DEC-004; verificado por AC-020.
- BR-008: Origen: contexto 3.11 (DEC-E46, DEC-E52); DEC-003; verificado por AC-019.
- CL-001: Origen: contexto 3.11 (DEC-E09, DEC-E41); verificado por AC-007.
- CL-002: Origen: contexto 3.8, 3.11 (DEC-E13); verificado por AC-018.
- CL-003: Origen: contexto 3.11 (DEC-E20); verificado por AC-003.
- CL-004: Origen: contexto 3.11 (DEC-E29); verificado por AC-005.
- CL-005: Origen: contexto 3.11 (DEC-E50); DEC-001; verificado por AC-012.
- CL-006: Origen: contexto 3.11 (DEC-E53); DEC-004; verificado por AC-020.

### 17. Historial de cambios
- Versión 0.1: Creación inicial del borrador de la SPEC-004 a partir de las historias HU-11 a HU-18 de la EPIC-002 y decisiones del contexto.
- Versión 1.0: Incorporación de decisiones del equipo (DEC-001 a DEC-005: ventana de 5 min para duplicados, formas de pago configuradas en SPEC-002, revalidación de catálogo al enviar, valor mínimo de compra, navegación por catálogo/Mini App por categorías). Cambio de estado a Candidata.
- Versión 1.1: corrección manual de la revisión cruzada de las SPEC (2026-11-21), sin modelo, aprobada por la estudiante: se reemplaza «backend» por «el sistema» (18 menciones; la validación en el servidor es una restricción de arquitectura del contexto 3.2). Sin otros cambios de contenido.

## Verificación
- Completitud: cumple. Se respondieron todas las preguntas abiertas de la versión anterior y no queda ninguna pregunta pendiente ni contenido inferido sin confirmar.
- Consistencia interna: cumple. Todos los RF, BR, flujos, casos límite y ACs están totalmente alineados sin contradicciones en relación con el ciclo de vida del pedido, formas de pago, duplicados y valor mínimo.
- Consistencia con el contexto: cumple. Se verificaron todas las decisiones citadas (DEC-E05 a DEC-E53) y las reglas de protección de datos (DEC-E36, DEC-E37).
- No ambigüedad: cumple. Las reglas de negocio especifican valores exactos (5 minutos para duplicados, valor mínimo de compra en productos y formas de pago habilitadas).
- Verificabilidad: cumple. Cada RF y BR cuenta con su criterio de aceptación en formato Dado/Cuando/Entonces o método RNF formal.
- Cobertura de actores: cumple. Se definieron HUs específicas para Persona, Cliente, Administrador y Empleado/Vendedor, e incluye restricciones explícitas de autorización para Domiciliario.
- Cobertura de AC: cumple. Todos los RF, BR y CL tienen al menos un AC que los verifica de forma explícita.
- Trazabilidad: cumple. La matriz de la sección 16 mapea correctamente todas las HU, RF, RNF, BR y CL con sus orígenes y ACs.
- No invención: cumple. Todas las reglas corresponden a lo decidido por el equipo o al contexto confirmado.
- Delimitación: cumple. No se incluyen decisiones técnicas de tecnología ni arquitectura, delimitando temas de persistencia a la sección 14.

## Siguiente paso
La SPEC-004 versión 1.0 está lista para revisión. Confirmen el objetivo y el alcance, las reglas de negocio, los criterios de aceptación críticos, las restricciones y lo que está fuera de alcance. Si la aprueban, queda congelada y lista para el Architecture Agent.
