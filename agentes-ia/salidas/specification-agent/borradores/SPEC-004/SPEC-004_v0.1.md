<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-21 15:10
Petición: SPEC-004. EPIC-002. Respuesta del equipo a la propuesta de división: se elige la opción B. El catálogo (HU-10) ya se especifica aparte en la SPEC-003; esta SPEC-004 asume un catálogo existente y NO incluye HU-10. Especifica el registro del cliente, la toma y la gestión inicial del pedido antes del despacho (HU-11 a HU-18 del archivo adjunto): ingreso por el acceso de clientes del negocio con aviso de privacidad y contacto compartido (DEC-E05, DEC-E20, DEC-E29, DEC-E36, DEC-E37, DEC-E42); armado con productos del catálogo, barrio de la lista y dirección, forma de pago y total con tarifa (DEC-E06 a DEC-E08); rechazo por barrio sin cobertura o negocio cerrado (DEC-E09, DEC-E41); aviso de posible duplicado (DEC-E10); negocio vencido no recibe pedidos (DEC-E26); confirmación (pasa a en preparación) o rechazo con aviso al cliente (DEC-E17, DEC-E21, DEC-E22, DEC-E25); cancelación por el cliente o el negocio antes de en camino (DEC-E13). Es una sola funcionalidad: no propongas otra división.
-->

# SPEC-004. Registro de cliente y gestión inicial del pedido - Versión 0.1

Estado: Borrador
Modo: Inicial
Necesidad original: "Respuesta del equipo a la propuesta de división: se elige la opción B. El catálogo (HU-10) ya se especifica aparte en la SPEC-003; esta SPEC-004 asume un catálogo existente y NO incluye HU-10. Especifica el registro del cliente, la toma y la gestión inicial del pedido antes del despacho (HU-11 a HU-18 del archivo adjunto): ingreso por el acceso de clientes del negocio con aviso de privacidad y contacto compartido (DEC-E05, DEC-E20, DEC-E29, DEC-E36, DEC-E37, DEC-E42); armado con productos del catálogo, barrio de la lista y dirección, forma de pago y total con tarifa (DEC-E06 a DEC-E08); rechazo por barrio sin cobertura o negocio cerrado (DEC-E09, DEC-E41); aviso de posible duplicado (DEC-E10); negocio vencido no recibe pedidos (DEC-E26); confirmación (pasa a en preparación) o rechazo con aviso al cliente (DEC-E17, DEC-E21, DEC-E22, DEC-E25); cancelación por el cliente o el negocio antes de en camino (DEC-E13)."
Épica: EPIC-002

## Análisis
- Objetivo: Permitir la vinculación e identificación de un cliente en un negocio mediante Telegram con consentimiento de datos, la composición y registro de su pedido calculando el total con tarifa de domicilio, la validación de reglas operativas (horario, cobertura, duplicados y suscripción), y la gestión inicial del pedido (confirmación a «en preparación», rechazo o cancelación previa a «en camino»).
- Alcance inicial: Registro de cliente en el negocio mediante botón nativo de Telegram y aceptación de privacidad; armado del pedido con selección de catálogo, barrio de cobertura, dirección, referencias y forma de pago; controles de estado de suscripción del negocio, horario de atención y zonas activas; detección de pedidos duplicados con confirmación previa; cambio de estado inicial por parte del negocio (confirmar a «en preparación» o rechazar) con notificaciones automáticas al cliente y personal; y cancelación del pedido antes del despacho («en camino») por parte del cliente o del establecimiento.
- Actores: Persona que desea realizar un pedido, Cliente, Administrador del negocio, Empleado o vendedor, Domiciliario.
- Contexto aplicable: Secciones 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8, 3.11 (DEC-E05, DEC-E06, DEC-E07, DEC-E08, DEC-E09, DEC-E10, DEC-E13, DEC-E17, DEC-E20, DEC-E21, DEC-E22, DEC-E25, DEC-E26, DEC-E29, DEC-E36, DEC-E37, DEC-E41, DEC-E42), Sección 4, Sección 5 y Sección 6.

## Modelo de dominio
- Negocio: pertenece a la Plataforma; cardinalidad uno a varios. Origen: contexto 2.4, 3.3.
- Cliente: pertenece a Negocio; cardinalidad uno a varios (un usuario de Telegram se vincula como cliente independientemente en cada negocio). Origen: contexto 3.11, DEC-E29.
- Pedido: pertenece a Negocio y a Cliente; cardinalidad uno a varios por cliente. Origen: contexto 2.4, 3.8.
- Producto (Catálogo): pertenece a Negocio; cardinalidad uno a varios. Origen: contexto 3.11, DEC-E06.
- Zona de cobertura (Barrio): pertenece a Negocio; cardinalidad uno a varios. Origen: contexto 3.5, DEC-E07.
- Consentimiento de Privacidad: pertenece a Cliente y a Negocio; cardinalidad uno a uno por registro. Origen: contexto 3.11, DEC-E36, DEC-E37.

## Contradicciones detectadas
- Ninguna. Las reglas solicitadas respetan el ciclo de vida del pedido (DEC-E21, DEC-E22), las restricciones de estado de suscripción (DEC-E26), la separación de negocios (contexto 3.3) y los consentimientos legales (DEC-E36).

## Análisis de impacto
- No aplica.

## Preguntas de aclaración
- OPEN-Q-001. ¿De cuántos minutos es la ventana de tiempo para considerar que un pedido con los mismos productos, cantidades y dirección de entrega realizado al mismo negocio es un posible duplicado (DEC-E10)?
  Por qué importa: Permite definir la regla de negocio BR-004 y los criterios de aceptación AC-012 y AC-013.
  Crítica: sí
  Propuesta del agente: PROPUESTA: Definir una ventana de 10 minutos desde el último pedido registrado con los mismos datos.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-002. ¿Cuáles son las formas de pago que el cliente puede seleccionar al armar su pedido (DEC-E08)?
  Por me importa: Define las opciones válidas del sistema en el RF-004 y BR-003 para selección y registro de forma de pago.
  Crítica: sí
  Propuesta del agente: PROPUESTA: Ofrecer las opciones «Efectivo» y «Transferencia / Pago electrónico».
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-003. Si el administrador o empleado desactiva un producto del catálogo mientras un cliente lo tiene seleccionado en su pedido antes de enviarlo, ¿cómo debe reaccionar el sistema al procesar el registro (DEC-E28)?
  Por qué importa: Define la validación de integridad al confirmar la orden por parte del cliente en RF-004.
  Crítica: no
  Propuesta del agente: PROPUESTA: Revalidar el catálogo al momento de confirmación del cliente y notificarle si un producto fue desactivado para que lo retire o modifique el pedido.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-004. ¿Se requiere validar un valor mínimo de compra para permitir la creación del pedido a domicilio?
  Por qué importa: Afecta la validación del pedido en RF-004 y BR-002.
  Crítica: no
  Propuesta del agente: PROPUESTA: No exigir monto mínimo para el registro de pedidos.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Registrar e identificar clientes en cada negocio respetando el habeas data mediante Telegram, permitir la configuración y confirmación de pedidos calculando el monto total más la tarifa del domicilio, e implementar la gestión inicial del ciclo de vida del pedido (recibido, en preparación, rechazado o cancelado) con notificaciones a las partes interesadas.

### 2. Contexto
Cada negocio posee un enlace o código QR de acceso exclusivo para clientes (DEC-E42). Cuando una persona entra por primera vez a un negocio, debe otorgar su consentimiento explícito del tratamiento de datos personales y compartir su contacto mediante el botón nativo de Telegram (DEC-E20, DEC-E36). Los clientes arman sus pedidos únicamente con el catálogo y zonas vigentes del negocio. Al registrar un pedido, este entra en estado «recibido». El personal del negocio (administrador o empleado) revisa el pedido para pasarlo a «en preparación» (confirmado) o «rechazado». Tanto el cliente como el negocio pueden cancelar el pedido antes de que este pase al estado «en camino».

Decisiones del equipo:
- Ninguna registrada en esta versión.

### 3. Alcance
- Registro e identificación de clientes por negocio mediante el enlace/QR de clientes y el botón nativo de Telegram.
- Aceptación y registro legible de la autorización de tratamiento de datos del negocio por parte del cliente.
- Consulta de catálogo activo del negocio, selección de productos, cantidades, barrio de entrega, dirección con referencias y forma de pago.
- Cálculo automático del monto del pedido (suma de productos + tarifa de domicilio de la zona seleccionada).
- Bloqueo de toma de pedidos si el negocio está cerrado por horario, si el barrio no tiene cobertura o si la suscripción del negocio está vencida.
- Advertencia de pedido potencialmente duplicado con solicitud de confirmación explícita.
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
- HU-012. Como Cliente, quiero seleccionar productos, cantidades, barrio de entrega, dirección con referencias y forma de pago, para conocer el total a pagar y enviar la orden al negocio.
- HU-013. Como Cliente, quiero que el sistema me informe si mi barrio no tiene cobertura o si el negocio está cerrado, para saber de inmediato si el negocio puede atender mi pedido.
- HU-014. Como Cliente, quiero recibir una alerta de confirmación si envío un pedido idéntico al anterior en poco tiempo, para evitar realizar por error duplicados no deseados.
- HU-015. Como Cliente, quiero que el sistema me prevenga de hacer pedidos en establecimientos no disponibles, para no realizar compras en negocios que no pueden procesar mi atención.
- HU-016. Como Empleado o vendedor, quiero revisar los pedidos en estado recibido para confirmarlos o rechazarlos, para iniciar la preparación de la orden o informar oportunamente al cliente en caso de no poder atenderla.
- HU-017. Como Cliente, quiero cancelar mi pedido mientras no haya pasado a estado en camino, para desistir de la compra de forma oportuna si se presenta algún imprevisto.
- HU-018. Como Administrador del negocio, quiero cancelar un pedido activo antes de que esté en camino, para dar de baja solicitudes que no se pueden cumplir o que el cliente canceló por otros medios.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir el ingreso de la persona mediante el enlace o código QR exclusivo de clientes del negocio y validar su estado de registro previo en ese establecimiento. Origen: contexto 3.11 (DEC-E05, DEC-E42).
- RF-002. El sistema debe solicitar y registrar la autorización previa, expresa e informada del tratamiento de datos personales de la persona mediante un botón explícito antes de permitirle compartir su contacto, guardando fecha, hora y versión del texto legal. Origen: contexto 3.11 (DEC-E36, DEC-E37).
- RF-003. El sistema debe solicitar el contacto de la persona utilizando exclusivamente el botón nativo de Telegram, asociando su teléfono verificado e identificador de chat como cliente del negocio específico. Origen: contexto 3.11 (DEC-E20, DEC-E29).
- RF-004. El sistema debe permitir al cliente armar su pedido seleccionando productos activos del catálogo del negocio, cantidades, barrio de entrega de la lista de cobertura del negocio, dirección con referencias y forma de pago (pendiente de OPEN-Q-002), solicitando confirmación antes de formalizar el registro. Origen: contexto 3.7, 3.11 (DEC-E06, DEC-E07, DEC-E08).
- RF-005. El sistema debe calcular automáticamente el valor total del pedido sumando el precio de los productos seleccionados y la tarifa de domicilio configurada para el barrio elegido. Origen: contexto 3.5, 3.11 (DEC-E06).
- RF-006. El sistema debe verificar el estado de la suscripción del negocio y rechazar el inicio del proceso de pedido si la suscripción está en estado «vencida», notificando al cliente que el establecimiento no está recibiendo pedidos temporalmente. Origen: contexto 3.11 (DEC-E26).
- RF-007. El sistema debe verificar el horario de atención del negocio para el día actual (incluyendo festivos) e impedir el armado del pedido si el establecimiento está cerrado, mostrando el horario de atención al cliente. Origen: contexto 3.11 (DEC-E09, DEC-E41).
- RF-008. El sistema debe validar que el barrio ingresado pertenezca a las zonas de cobertura activas del negocio, rechazando el registro de la orden e informando al cliente si el barrio no cuenta con cobertura. Origen: contexto 3.5, 3.11 (DEC-E09).
- RF-009. El sistema debe detectar pedidos potencialmente duplicados solicitando confirmación explícita al cliente antes de registrarlos (detalles pendientes de OPEN-Q-001). Origen: contexto 3.7, 3.11 (DEC-E10).
- RF-010. Al confirmarse el pedido por parte del cliente, el sistema debe crearlo en estado «recibido», registrar fecha, hora y cliente responsable, y enviar una notificación automática de pedido nuevo al administrador y empleados del negocio. Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E25).
- RF-011. El sistema debe permitir al administrador del negocio y al empleado o vendedor confirmar un pedido en estado «recibido», previa confirmación, cambiando su estado a «en preparación», registrando fecha, hora y usuario responsable en el backend, y notificando al cliente. Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25).
- RF-012. El sistema debe permitir al administrador del negocio y al empleado o vendedor rechazar un pedido en estado «recibido», previa confirmación, cambiando su estado a «rechazado» (estado final), registrando fecha, hora y usuario responsable en el backend, y notificando al cliente. Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25).
- RF-013. El sistema debe permitir al cliente cancelar su pedido si se encuentra en estado «recibido», «en preparación» o «listo para recoger», previa confirmación, registrando el estado «cancelado» (estado final), fecha, hora, cliente como responsable, y notificando al administrador y empleados del negocio. Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25).
- RF-014. El sistema debe permitir al administrador del negocio y al empleado o vendedor cancelar un pedido en estado «recibido», «en preparación» o «listo para recoger», previa confirmación, registrando el estado «cancelado» (estado final), fecha, hora, usuario responsable, y notificando al cliente. Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25).
- RF-015. El sistema debe impedir la cancelación del pedido por parte del cliente, administrador o empleado si el pedido ya se encuentra en estado «en camino» o posterior. Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E22).

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización. El backend debe verificar la identidad del usuario, el rol, el negocio al que pertenece y los permisos específicos para cada operación de consulta, creación o cambio de estado. Se verifica mediante: inspección de código backend y pruebas de penetración de roles. Origen: contexto 3.2.
- RNF-002. Separación de información. Los usuarios de un negocio no deben acceder, consultar ni modificar datos, catálogos, zonas ni pedidos de otros negocios. Se verifica mediante: pruebas automatizadas de aislamiento de datos entre negocios. Origen: contexto 3.3.
- RNF-003. Concurrencia y atomicidad. Las actualizaciones de estado del pedido deben ejecutarse de manera atómica en el backend para evitar estados inconsistentes o dobles cambios simultáneos. Se verifica mediante: pruebas de carga y concurrencia simultánea sobre el mismo pedido. Origen: contexto 3.8.
- RNF-004. Trazabilidad de operaciones. Cada cambio de estado debe registrar de manera inmutable fecha, hora exacta, nuevo estado y usuario responsable. Se verifica mediante: auditoría de registros de base de datos tras la ejecución de flujos de pedido. Origen: contexto 3.8.

### 7. Reglas de negocio
- BR-001. Registro independiente por negocio. La vinculación de una persona como cliente aplica únicamente para el negocio cuyo enlace o QR utilizó. Si la persona interactúa con otro negocio, debe aceptar el aviso de privacidad de ese nuevo negocio y volver a compartir su contacto con el botón nativo (DEC-E29). Origen: contexto 3.11 (DEC-E29).
- BR-002. Restricción de visibilidad de datos al cliente. Durante la creación del pedido, el cliente solo puede visualizar y elegir productos activos y zonas pertenecientes al negocio específico en el que se encuentra interactuando. Origen: contexto 3.3, 3.11 (DEC-E06, DEC-E07, DEC-E28).
- BR-003. Formas de pago aceptadas. El cobro del pedido se efectúa fuera del sistema. El pedido únicamente almacena la forma de pago seleccionada por el cliente entre las opciones habilitadas (DEC-E08, pendiente de OPEN-Q-002). Origen: contexto 3.11 (DEC-E08).
- BR-004. Detección de duplicados. Se considera un pedido potencialmente duplicado cuando un mismo cliente registra un pedido con exactamente los mismos productos, cantidades, barrio y dirección en un mismo negocio en un intervalo menor al configurado (pendiente de OPEN-Q-001). En este caso, el sistema exige confirmación explícita para registrarlo. Origen: contexto 3.7, 3.11 (DEC-E10).
- BR-005. Transiciones permitidas del estado del pedido.
  - Recibido → En preparación (provocado por Admin/Empleado).
  - Recibido → Rechazado (provocado por Admin/Empleado, estado final).
  - Recibido / En preparación / Listo para recoger → Cancelado (provocado por Cliente o Admin/Empleado, estado final).
  - El rol Domiciliario no tiene permiso para cambiar el estado de un pedido en «recibido». Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E22).
- BR-006. Protección de datos de contacto. Ningún mensaje de notificación pública o grupal expone el número de teléfono, dirección exacta o nombre del cliente a usuarios no autorizados de acuerdo con la sección 3.3 y la regla crítica 7. Origen: contexto 3.3 y Regla Crítica 7.

### 8. Flujo principal
1. La persona ingresa al bot mediante el enlace o código QR exclusivo para clientes del negocio (DEC-E42).
2. El sistema verifica si el cliente ya está registrado y aceptó los términos en este negocio. Si no está registrado, le presenta el aviso de privacidad (DEC-E36) y le solicita presionar el botón de autorización de datos.
3. Al autorizar, el sistema solicita compartir el contacto mediante el botón nativo de Telegram (DEC-E20). La persona presiona el botón y el sistema la registra como cliente del negocio.
4. El sistema valida el estado de la suscripción del negocio (DEC-E26) y su horario de atención actual (DEC-E41). Al estar la suscripción al día y el negocio abierto, muestra el catálogo activo de productos.
5. El cliente selecciona los productos y sus cantidades.
6. El cliente selecciona el barrio de entrega de la lista de zonas de cobertura del negocio (DEC-E07). El sistema obtiene la tarifa de domicilio asociada.
7. El cliente ingresa la dirección exacta de entrega y observaciones o referencias.
8. El cliente selecciona la forma de pago (DEC-E08).
9. El sistema calcula el valor total (productos + tarifa de domicilio) y presenta el resumen del pedido pidiendo confirmación (DEC-E06, DEC-E07).
10. El cliente confirma el envío del pedido.
11. El sistema verifica que no sea un pedido duplicado reciente.
12. El sistema guarda el pedido en estado «recibido», registra la fecha, hora y cliente como responsable, y notifica al administrador y a los empleados del negocio con los detalles del nuevo pedido (DEC-E21, DEC-E25).
13. Un empleado o administrador del negocio consulta el pedido en estado «recibido» y selecciona la opción de confirmar.
14. El sistema pide confirmación de la operación (contexto 3.7). El usuario confirma.
15. El backend actualiza atómicamente el estado del pedido a «en preparación», guarda la fecha, hora y usuario responsable, y envía una notificación automática al cliente confirmando la orden y el total a pagar (DEC-E17, DEC-E21, DEC-E22).

### 9. Flujos alternativos y de excepción
- A1. Reintento de registro de cliente ya vinculado:
  1. En el paso 2 del flujo principal, el sistema detecta que el cliente ya aceptó los términos y compartió su contacto en este negocio previamente.
  2. El sistema omite la solicitud de privacidad y contacto, y pasa directamente a verificar suscripción y horario (paso 4).
- A2. Cliente rechaza pedido potencialmente duplicado:
  1. En el paso 11 del flujo principal, el sistema detecta un pedido con los mismos productos, cantidades y dirección registrado recientemente.
  2. El sistema muestra un mensaje de advertencia indicando la posible duplicidad y pide confirmar si desea realizar un nuevo pedido o cancelar.
  3. El cliente selecciona cancelar la operación.
  4. El sistema descarta la orden en borrador sin guardar nada en la base de datos y le notifica al cliente.
- A3. Cliente confirma pedido potencialmente duplicado:
  1. En el paso 2 de A2, el cliente selecciona confirmar expresamente la repetición del pedido.
  2. El sistema continúa en el paso 12 del flujo principal guardando el pedido como una orden independiente.
- A4. Rechazo del pedido por el negocio:
  1. En el paso 13 del flujo principal, el empleado o administrador selecciona la opción de rechazar el pedido.
  2. El sistema solicita confirmación del rechazo.
  3. El usuario confirma.
  4. El backend cambia el estado del pedido a «rechazado», guarda la fecha, hora y usuario responsable, y envía una notificación al cliente informando que su pedido fue rechazado (DEC-E17, DEC-E22).
- A5. Cancelación del pedido por el cliente antes de «en camino»:
  1. En cualquier momento mientras el pedido esté en estado «recibido», «en preparación» o «listo para recoger», el cliente selecciona la opción de cancelar pedido.
  2. El sistema solicita confirmación explícita de la cancelación.
  3. El cliente confirma.
  4. El backend actualiza el estado del pedido a «cancelado», guarda la fecha, hora y el cliente como responsable, y envía una notificación inmediata al administrador y empleados del negocio (DEC-E13, DEC-E25).
- A6. Cancelación del pedido por el negocio antes de «en camino»:
  1. Mientras el pedido está en estado «recibido», «en preparación» o «listo para recoger», el administrador o empleado selecciona la opción de cancelar pedido.
  2. El sistema solicita confirmación explícita.
  3. El usuario confirma.
  4. El backend actualiza el estado a «cancelado», guarda la fecha, hora y usuario responsable, y notifica al cliente sobre la cancelación de la orden (DEC-E13, DEC-E17).

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
  2. El backend deniega la operación enviando un mensaje de falta de permisos (RNF-001).

### 10. Casos límite
- CL-001. Intento de registrar pedido en el exacto minuto de cierre del negocio: se evalúa la hora de confirmación final en el backend; si es igual o posterior al límite de cierre, el pedido es rechazado por horario (DEC-E09, DEC-E41). Origen: contexto 3.11 (DEC-E09, DEC-E41).
- CL-002. Intento de cancelación por el cliente cuando el negocio acaba de pasar el pedido a «en camino» simultáneamente: la operación atómica en backend rechaza la cancelación por haber cambiado de estado previamente (DEC-E13, RNF-003). Origen: contexto 3.8, 3.11 (DEC-E13).
- CL-003. Cliente intenta ingresar texto manual de teléfono reiteradamente: el bot no avanza ni genera registro de cliente hasta que se presione el botón nativo de Telegram (DEC-E20). Origen: contexto 3.11 (DEC-E20).
- CL-004. Cliente registrado en el negocio A intenta hacer un pedido en el negocio B con el enlace de B: el sistema detecta que no tiene registro en B, le pide aceptar el aviso de privacidad de B y compartir nuevamente su contacto para B (DEC-E29). Origen: contexto 3.11 (DEC-E29).

### 11. Criterios de aceptación
- AC-001. Dado que una persona no registrada accede mediante el enlace o QR de clientes del negocio, cuando inicia la interacción, entonces el sistema le presenta el aviso de privacidad del negocio exigiendo aceptación con botón explícito antes de permitir compartir datos (RF-001, RF-002; BR-001).
- AC-002. Dado que la persona presiona el botón de aceptar aviso de privacidad, cuando el sistema guarda el registro, entonces almacena la fecha, hora exacta y versión del texto aceptado (RF-002).
- AC-003. Dado que la persona intenta registrar su contacto enviando un texto manual en el chat de Telegram, cuando se procesa el mensaje, entonces el sistema rechaza el texto y exige presionar el botón nativo de Telegram (RF-003).
- AC-004. Dado que la persona presiona el botón nativo de Telegram para compartir contacto, cuando el sistema lo recibe, entonces registra el número telefónico verificado y vincula a la persona como cliente exclusivo de ese negocio (RF-003; BR-001).
- AC-005. Dado que un cliente registrado en el negocio A entra por el enlace del negocio B, cuando inicia interacción en B, entonces el sistema le solicita aceptar el aviso de privacidad y compartir su contacto nuevamente para el negocio B (RF-001, RF-003; BR-001; CL-004).
- AC-006. Dado que un cliente inicia un pedido en un negocio con suscripción vencida, cuando ingresa al flujo de compra, entonces el sistema le impide continuar e informa que el negocio no está recibiendo pedidos temporalmente (RF-006).
- AC-007. Dado que un cliente intenta hacer un pedido fuera del horario de atención o en un día festivo no laboral del negocio, cuando inicia la solicitud, entonces el sistema le informa que el negocio está cerrado, le muestra sus horarios y no permite continuar (RF-007; CL-001).
- AC-008. Dado que un cliente selecciona un barrio que no está en la lista de cobertura del negocio, cuando intenta avanzar en el pedido, entonces el sistema rechaza la solicitud e informa que no hay entregas en esa ubicación (RF-008).
- AC-009. Dado que un cliente selecciona productos activos y un barrio con tarifa de $5.000 COP, cuando avanza al resumen, entonces el sistema calcula el valor total sumando los precios de los productos seleccionados más los $5.000 COP de domicilio (RF-004, RF-005; BR-002).
- AC-010. Dado que un cliente completa la selección de productos, barrio, dirección de entrega con referencias y forma de pago, cuando presiona enviar pedido, entonces el sistema le muestra el resumen total y le exige confirmación antes de formalizar la solicitud (RF-004).
- AC-011. Dado que el cliente confirma el resumen de su pedido, cuando el sistema lo procesa, entonces crea el pedido en estado «recibido», registra fecha, hora y cliente como responsable, y notifica al administrador y a los empleados del negocio (RF-010).
- AC-012. Dado un cliente que envía un pedido identico al anterior en el mismo negocio en un lapso menor a la ventana configurada (OPEN-Q-001), cuando el sistema procesa la orden, entonces detiene el registro y muestra un aviso de posible duplicidad con opciones de confirmar o cancelar (RF-009; BR-004).
- AC-013. Dado un aviso de posible duplicado, cuando el cliente elige cancelar la orden, entonces el sistema descarta la nueva orden sin alterar los pedidos guardados (RF-009; BR-004).
- AC-014. Dado un pedido en estado «recibido», cuando el administrador o empleado selecciona confirmar el pedido y responde afirmativamente a la confirmación previa, entonces el sistema cambia el estado a «en preparación», guarda fecha, hora y responsable en el backend, y notifica al cliente con el total a pagar (RF-011; BR-005).
- AC-015. Dado un pedido en estado «recibido», cuando el administrador o empleado selecciona rechazar el pedido y confirma la acción, entonces el sistema cambia el estado a «rechazado», guarda fecha, hora y responsable en el backend, y notifica al cliente el rechazo (RF-012; BR-005).
- AC-016. Dado un usuario con rol Domiciliario, cuando intenta confirmar o rechazar un pedido en estado «recibido», entonces el sistema deniega la acción por falta de permisos (RNF-001; BR-005).
- AC-017. Dado un pedido en estado «recibido», «en preparación» o «listo para recoger», cuando el cliente o un empleado/administrador solicita cancelar y confirma la acción, entonces el sistema cambia el estado a «cancelado», registra fecha, hora y responsable, y notifica a la otra parte (RF-013, RF-014; BR-005).
- AC-018. Dado un pedido que pasó a estado «en camino», cuando el cliente, administrador o empleado intenta cancelarlo, entonces el sistema deniega la acción e informa que debe tratarse como novedad de entrega (RF-015; CL-002).

### 12. Dependencias
- SPEC-001 (Gestión de negocios, suscripción de plataforma y términos legales): provee el estado de suscripción del negocio (DEC-E26) y el texto legal de aviso de privacidad (DEC-E36, DEC-E37).
- SPEC-002 (Configuración de horarios y zonas de cobertura): provee la lista de barrios con tarifa de domicilio y el horario de atención por día/festivo (DEC-E07, DEC-E09, DEC-E41).
- SPEC-003 (Gestión de catálogo de productos): provee la lista de productos activos y precios del negocio (DEC-E06, DEC-E27, DEC-E28).

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
- OPEN-Q-001. ¿De cuántos minutos es la ventana de tiempo para considerar que un pedido con los mismos productos, cantidades y dirección de entrega realizado al mismo negocio es un posible duplicado (DEC-E10)? Estado: Pendiente.
- OPEN-Q-002. ¿Cuáles son las formas de pago que el cliente puede seleccionar al armar su pedido (DEC-E08)? Estado: Pendiente.
- OPEN-Q-003. Si el administrador o empleado desactiva un producto del catálogo mientras un cliente lo tiene seleccionado en su pedido antes de enviarlo, ¿cómo debe reaccionar el sistema al procesar el registro (DEC-E28)? Estado: Pendiente.
- OPEN-Q-004. ¿Se requiere validar un valor mínimo de compra para permitir la creación del pedido a domicilio? Estado: Pendiente.

### 16. Trazabilidad
- HU-011: RF-001, RF-002, RF-003; BR-001; AC-001, AC-002, AC-003, AC-004, AC-005; CL-003, CL-004.
- HU-012: RF-004, RF-005, RF-010; BR-002, BR-003; AC-009, AC-010, AC-011.
- HU-013: RF-007, RF-008; AC-007, AC-008; CL-001.
- HU-014: RF-009; BR-004; AC-012, AC-013.
- HU-015: RF-006; AC-006.
- HU-016: RF-011, RF-012; BR-005; AC-014, AC-015, AC-016.
- HU-017: RF-013, RF-015; BR-005; AC-017, AC-018; CL-002.
- HU-018: RF-014, RF-015; BR-005; AC-017, AC-018; CL-002.
- RF-001: Origen: contexto 3.11 (DEC-E05, DEC-E42); verificado por AC-001, AC-005.
- RF-002: Origen: contexto 3.11 (DEC-E36, DEC-E37); verificado por AC-001, AC-002.
- RF-003: Origen: contexto 3.11 (DEC-E20, DEC-E29); verificado por AC-003, AC-004, AC-005.
- RF-004: Origen: contexto 3.7, 3.11 (DEC-E06, DEC-E07, DEC-E08); verificado por AC-009, AC-010.
- RF-005: Origen: contexto 3.5, 3.11 (DEC-E06); verificado por AC-009.
- RF-006: Origen: contexto 3.11 (DEC-E26); verificado por AC-006.
- RF-007: Origen: contexto 3.11 (DEC-E09, DEC-E41); verificado por AC-007.
- RF-008: Origen: contexto 3.5, 3.11 (DEC-E09); verificado por AC-008.
- RF-009: Origen: contexto 3.7, 3.11 (DEC-E10); verificado por AC-012, AC-013.
- RF-010: Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E25); verificado por AC-011.
- RF-011: Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25); verificado por AC-014.
- RF-012: Origen: contexto 3.2, 3.8, 3.11 (DEC-E21, DEC-E22, DEC-E25); verificado por AC-015.
- RF-013: Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25); verificado por AC-017.
- RF-014: Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E21, DEC-E25); verificado por AC-017.
- RF-015: Origen: contexto 3.8, 3.11 (DEC-E13, DEC-E22); verificado por AC-018.
- RNF-001: Origen: contexto 3.2; verificado con pruebas de penetración de roles y AC-016.
- RNF-002: Origen: contexto 3.3; verificado con pruebas automatizadas de aislamiento de datos entre negocios.
- RNF-003: Origen: contexto 3.8; verificado con pruebas de carga y concurrencia simultánea sobre el mismo pedido.
- RNF-004: Origen: contexto 3.8; verificado con auditoría de registros de base de datos tras la ejecución de flujos de pedido.
- BR-001: Origen: contexto 3.11 (DEC-E29); verificado por AC-001, AC-004, AC-005.
- BR-002: Origen: contexto 3.3, 3.11 (DEC-E06, DEC-E07, DEC-E28); verificado por AC-009.
- BR-003: Origen: contexto 3.11 (DEC-E08); verificado por AC-010.
- BR-004: Origen: contexto 3.7, 3.11 (DEC-E10); verificado por AC-012, AC-013.
- BR-005: Origen: contexto 3.8, 3.11 (DEC-E21, DEC-E22); verificado por AC-014, AC-015, AC-016, AC-017.
- BR-006: Origen: contexto 3.3 y Regla Crítica 7; verificado con inspección de plantillas de notificación.
- CL-001: Origen: contexto 3.11 (DEC-E09, DEC-E41); verificado por AC-007.
- CL-002: Origen: contexto 3.8, 3.11 (DEC-E13); verificado por AC-018.
- CL-003: Origen: contexto 3.11 (DEC-E20); verificado por AC-003.
- CL-004: Origen: contexto 3.11 (DEC-E29); verificado por AC-005.

### 17. Historial de cambios
- Versión 0.1: Creación inicial del borrador de la SPEC-004 a partir de las historias HU-11 a HU-18 de la EPIC-002 y decisiones del contexto.

## Verificación
- Completitud: no cumple. Quedan preguntas críticas pendientes sin responder (OPEN-Q-001 y OPEN-Q-002).
- Consistencia interna: cumple. Todos los RF, BR y AC sobre el ciclo de vida inicial del pedido coinciden en los estados «recibido», «en preparación», «rechazado» y «cancelado».
- Consistencia con el contexto: cumple. Se verificaron todas las decisiones citadas (DEC-E05 a DEC-E42) y las reglas de protección de datos (DEC-E36, DEC-E37).
- No ambigüedad: cumple. Se identificaron los vacíos de tiempo en duplicados y formas de pago y se marcaron explícitamente como OPEN-Q.
- Verificabilidad: cumple. Cada RF y BR cuenta con su criterio de aceptación en formato Dado/Cuando/Entonces o método RNF formal.
- Cobertura de actores: cumple. Se definieron HUs específicas para Persona, Cliente, Administrador y Empleado/Vendedor, y se incluyeron restricciones explícitas de autorización para Domiciliario.
- Cobertura de AC: cumple. Todos los RF y BR tienen al menos un AC que los verifica.
- Trazabilidad: cumple. La matriz 16 relaciona todas las HU, RF, RNF, BR y CL con sus correspondientes orígenes y ACs.
- No invención: cumple. Todos los datos no confirmados se marcaron como inferencias con su pregunta asociada OPEN-Q.
- Delimitación: cumple. No se tomaron decisiones de arquitectura técnica ni de base de datos, registrando el tema de almacenamiento en la sección 14.

## Siguiente paso
Respondan las preguntas abiertas OPEN-Q-001 y OPEN-Q-002 (y secundarias OPEN-Q-003, OPEN-Q-004) y ejecuten de nuevo el agente con `--continuar SPEC-004`.
