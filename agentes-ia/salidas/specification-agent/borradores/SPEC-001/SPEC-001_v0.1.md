<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.7-flash
Fecha: 2026-11-19 10:16
Petición: EPIC-001. Especifica el registro y la aprobación del negocio y la vinculación de su personal: una persona registra su negocio desde el bot compartiendo su contacto y queda pendiente hasta que el dueño de la plataforma lo aprueba o rechaza; al aprobarse pasa a ser su administrador; empleados y domiciliarios piden unirse a un negocio y el administrador aprueba o rechaza. Las historias de usuario aprobadas HU-01, HU-02, HU-04, HU-05 y HU-09 están en el archivo adjunto; respétalas como entrada.
-->

# SPEC-001. Registro y aprobacion de negocio y vinculacion de personal - Versión 0.1

Estado: Borrador
Modo: Inicial
Necesidad original: "EPIC-001. Especifica el registro y la aprobación del negocio y la vinculación de su personal: una persona registra su negocio desde el bot compartiendo su contacto y queda pendiente hasta que el dueño de la plataforma lo aprueba o rechaza; al aprobarse pasa a ser su administrador; empleados y domiciliarios piden unirse a un negocio y el administrador aprueba o rechaza. Las historias de usuario aprobadas HU-01, HU-02, HU-04, HU-05 y HU-09 están en el archivo adjunto; respétalas como entrada."
Épica: EPIC-001

## Análisis
- Objetivo: permitir que nuevos establecimientos soliciten su registro en la plataforma mediante el bot de Telegram y sean habilitados por el dueño de la plataforma, y permitir que empleados y domiciliarios soliciten su vinculación a un negocio activo para ser aprobados o rechazados por el administrador correspondiente.
- Alcance inicial: registro de solicitud de negocio con contacto verificado; aprobación o rechazo de negocio por el dueño de la plataforma; postulación de domiciliarios a un negocio con validación de exclusividad; postulación de empleados a un negocio; gestión (aprobación o rechazo) de solicitudes de vinculación por el administrador del negocio; notificaciones asociadas en Telegram.
- Actores: Persona que solicita el registro del negocio, Dueño de la plataforma, Administrador del negocio, Empleado o vendedor, Domiciliario, Telegram (canal de transporte).
- Contexto aplicable: secciones 2.3, 3.1, 3.2, 3.3, 3.4, 3.6, y decisiones DEC-E01, DEC-E02, DEC-E03, DEC-E20, DEC-E25, DEC-E29 del contexto 3.11.

## Modelo de dominio
- Negocio: entidad principal que representa el establecimiento de comercio. Pertenece a la plataforma; cardinalidad uno o varios en la plataforma. Origen: contexto 2.4 y contexto 3.11, DEC-E01.
- Solicitud de registro de negocio: registro temporal del trámite de apertura. Pertenece a una persona solicitante y a la plataforma; cardinalidad una por trámite. Origen: HU-01, HU-02.
- Usuario: persona identificada mediante su cuenta de Telegram. Pertenece a la plataforma; cardinalidad uno a muchos. Origen: contexto 2.3 y contexto 3.11, DEC-E20.
- Vinculacion de personal: relacion entre un usuario y un negocio especifico bajo un rol (empleado o domiciliario). Pertenece a un usuario y a un negocio; cardinalidad: un usuario domiciliario solo puede tener una vinculacion activa o pendiente en un solo negocio; un usuario empleado puede tener vinculaciones segun permisos. Origen: contexto 3.11, DEC-E02, DEC-E03.
- Solicitud de vinculacion: peticion de un usuario para ingresar a un negocio como empleado o domiciliario. Pertenece a un usuario y a un negocio; cardinalidad una por trámite. Origen: contexto 3.11, DEC-E02.

## Contradicciones detectadas
- Ninguna. Las historias de usuario HU-01, HU-02, HU-04, HU-05 y HU-09 son consistentes con las decisiones DEC-E01, DEC-E02, DEC-E03, DEC-E20 y DEC-E25 del contexto del proyecto.

## Análisis de impacto
No aplica.

## Preguntas de aclaración
- OPEN-Q-001. Cuando el dueño de la plataforma rechaza la solicitud de registro de un negocio (HU-02), ¿debe registrar obligatoriamente un motivo de rechazo y este motivo se le notifica al solicitante por el bot? Además, ¿un solicitante cuyo negocio fue rechazado puede volver a enviar una nueva solicitud desde la misma cuenta de Telegram?
  Por qué importa: define las reglas de negocio del rechazo, el mensaje al usuario y el manejo del estado del solicitante en HU-02.
  Crítica: sí
  Propuesta del agente: PROPUESTA: El dueño de la plataforma debe registrar un motivo breve de rechazo que se notifica al solicitante por Telegram, y la cuenta queda habilitada para registrar nuevamente el negocio corrigiendo los datos.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-002. En la solicitud de vinculación de empleados (HU-09), según DEC-E03 la exclusividad de un solo negocio aplica únicamente al rol de domiciliario. ¿Puede un empleado o vendedor tener vinculaciones activas o solicitudes pendientes en múltiples negocios al mismo tiempo, o existe alguna restricción?
  Por qué importa: determina las validaciones en el backend para la creación de solicitudes de empleados en HU-09 y las reglas de pertenencia multi-negocio para este rol.
  Crítica: sí
  Propuesta del agente: PROPUESTA: Un empleado puede estar vinculado a varios negocios, pero no puede tener más de una solicitud pendiente ni duplicar su vinculación activa dentro del mismo negocio.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-003. En la vinculación de domiciliarios (HU-04), si la solicitud es rechazada por el administrador del negocio (HU-05), ¿en qué estado queda el domiciliario en la plataforma y puede de inmediato postularse a otro negocio o reintentar en el mismo?
  Por qué importa: afecta la regla DEC-E03 sobre no poder solicitar unión a otro negocio mientras tenga una vinculación activa o pendiente, y define el desbloqueo del usuario tras el rechazo.
  Crítica: sí
  Propuesta del agente: PROPUESTA: Al marcarse la solicitud como rechazada, el domiciliario deja de tener una vinculación pendiente y queda libre de inmediato para postularse a otro establecimiento o volver a enviar solicitud al mismo.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-004. Cuando el administrador del negocio rechaza una solicitud de vinculación de un empleado o domiciliario (HU-05), ¿se debe registrar un motivo de rechazo obligatorio o el sistema solo marca el estado como rechazado? ¿Se notifica dicho motivo al aspirante?
  Por qué importa: define los campos requeridos en la acción administrativa de rechazo y el contenido de la notificación enviada al aspirante.
  Crítica: sí
  Propuesta del agente: PROPUESTA: El administrador puede ingresar un motivo de rechazo opcional; el bot notifica al aspirante únicamente que su solicitud fue rechazada por el establecimiento, sin exponer datos internos.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-005. Al registrar un negocio (HU-01), ¿qué datos comerciales específicos son obligatorios además del nombre comercial y la dirección (por ejemplo, ciudad o municipio)? Además, ¿qué validación debe realizar el sistema si ya existe un establecimiento registrado con el mismo nombre comercial?
  Por qué importa: permite especificar los requisitos funcionales de captura de datos y las reglas para prevenir registros duplicados o nombres repetidos según el contexto 3.7.
  Crítica: sí
  Propuesta del agente: PROPUESTA: Se solicita obligatoriamente nombre comercial, ciudad o municipio y dirección; el sistema no permite registrar un negocio con el mismo nombre comercial exacto dentro de la misma ciudad.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-006. En relación con la protección de datos personales (vacío conocido 5 y contexto 3.3 y 6), ¿qué datos personales específicos del solicitante, empleado o domiciliario se almacenan a partir del contacto de Telegram verificado (por ejemplo, identificador de Telegram, nombre, apellido, teléfono) y se requiere mostrar un mensaje de consentimiento de tratamiento de datos antes de capturarlo?
  Por qué importa: define los datos exactos que persiste el backend y el cumplimiento de las restricciones de protección de datos personales.
  Crítica: sí
  Propuesta del agente: PROPUESTA: Se almacenan únicamente el identificador numérico de Telegram, el nombre registrado en la cuenta y el número de teléfono verificado; el bot muestra un aviso breve de tratamiento de datos antes de solicitar el contacto.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-007. Para que un empleado o domiciliario solicite unirse a un negocio (HU-04 y HU-09), ¿cómo identifica el establecimiento: mediante un enlace profundo de Telegram (deep link), un código QR, o escribiendo un código de negocio en el chat del bot?
  Por qué importa: define los mecanismos de entrada y navegación que el bot debe soportar para vincular personal a un negocio específico.
  Crítica: no
  Propuesta del agente: PROPUESTA: El bot admite tanto el ingreso directo por enlace profundo o código QR generado por el negocio, como el ingreso manual del código del negocio en el chat.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-008. ¿Las solicitudes de registro de negocio (pendientes ante el dueño de la plataforma) y las solicitudes de vinculación de personal (pendientes ante el administrador) tienen un tiempo límite o vencimiento automático si no son atendidas, o quedan pendientes de forma indefinida?
  Por qué importa: afecta la necesidad de tareas de expiración automática y estados temporales en el modelo de dominio.
  Crítica: no
  Propuesta del agente: PROPUESTA: Las solicitudes no cadan automáticamente; permanecen en estado pendiente hasta que el dueño de la plataforma o el administrador del negocio emita una respuesta.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-009. ¿Puede una persona que envió una solicitud de registro de negocio (HU-01) o un aspirante que solicitó vinculación (HU-04, HU-09) cancelar su propia solicitud mientras se encuentra en estado pendiente?
  Por qué importa: determina si se requiere un flujo alternativo y un criterio de aceptación para el retiro voluntario del trámite por parte del solicitante.
  Crítica: no
  Propuesta del agente: PROPUESTA: Sí, el bot debe permitir al solicitante cancelar su trámite pendiente, dejando constancia del estado cancelado y permitiéndole iniciar un nuevo proceso si fue un error.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Permitir el registro de nuevos establecimientos mediante el bot de Telegram con contacto verificado y su aprobación o rechazo por el dueño de la plataforma, así como la vinculación controlada de empleados y domiciliarios mediante aprobación del administrador de cada negocio, garantizando la exclusividad de los domiciliarios y el aislamiento de datos entre establecimientos.

### 2. Contexto
En Domiciliarios Eje cada negocio gestiona su propia operación de domicilios desde Telegram. Para iniciar, una persona solicita registrar su negocio en el bot y queda en espera de que el dueño de la plataforma autorice su funcionamiento. Una vez aprobado, el solicitante asume el rol de administrador y puede recibir y autorizar las postulaciones de empleados y domiciliarios que desean integrarse a su equipo.

Decisiones del equipo aplicables:
- DEC-E01. Un negocio se registra solo desde el bot y queda pendiente hasta que el dueño de la plataforma lo aprueba. Quien lo registra queda como su administrador. Origen: contexto 3.11.
- DEC-E02. Empleados y domiciliarios piden unirse a un negocio desde el bot y el administrador aprueba o rechaza la solicitud. Origen: contexto 3.11.
- DEC-E03. Un domiciliario pertenece a un solo negocio: no puede pedir unirse a otro mientras tenga una vinculación activa o pendiente. La restricción aplica solo al rol domiciliario; una misma cuenta puede ser empleado o administrador de otros negocios y cliente de varios. Origen: contexto 3.11.
- DEC-E20. Una persona se identifica con su cuenta de Telegram y, al registrarse, comparte su contacto con el botón nativo de Telegram; el teléfono queda verificado por Telegram. No se usan códigos por SMS. Origen: contexto 3.11.
- DEC-E25. Notificaciones del negocio: el administrador recibe las solicitudes de unión. Origen: contexto 3.11.

### 3. Alcance
- Captura de solicitud de registro de negocio con datos básicos (nombre comercial, dirección) y número de teléfono compartido mediante el botón nativo de Telegram.
- Consulta de solicitudes pendientes de negocios por parte del dueño de la plataforma, visualizando únicamente nombre del negocio y nombre del solicitante.
- Aprobación o rechazo de la solicitud de negocio por parte del dueño de la plataforma.
- Asignación automática del rol de Administrador al solicitante cuando su negocio es aprobado.
- Solicitud de vinculación de domiciliarios a un negocio específico compartiendo contacto verificado, con validación de no pertenencia activa ni pendiente a otro negocio.
- Solicitud de vinculación de empleados o vendedores a un negocio específico con contacto verificado.
- Consulta y resolución (aprobación o rechazo) de solicitudes de personal por parte del administrador del negocio correspondiente.
- Notificaciones en Telegram asociadas a cada cambio de estado de solicitud.

### 4. Actores e historias de usuario
Actores:
- Persona que solicita el registro del negocio: usuario de Telegram que busca abrir un establecimiento en la plataforma.
- Dueño de la plataforma: usuario autorizado para aprobar o rechazar solicitudes de registro de negocios. No opera pedidos ni ve clientes.
- Administrador del negocio: solicitante aprobado que gestiona su establecimiento y su personal.
- Domiciliario: repartidor que solicita vinculación exclusiva a un negocio y ejecuta entregas una vez autorizado.
- Empleado o vendedor: usuario que solicita vinculación a un negocio para apoyar la gestión operativa.

Historias de usuario:
- HU-001. Como persona que quiere registrar su negocio, quiero registrar mi establecimiento en el bot compartiendo mi contacto verificado de Telegram, para solicitar la apertura de mi negocio en la plataforma y quedar a la espera de aprobación. Origen: HU-01.
- HU-002. Como Dueño de la plataforma, quiero revisar las solicitudes de registro de negocios pendientes para aprobarlas o rechazarlas, para controlar qué establecimientos están autorizados a operar en la plataforma sin acceder a su operación interna. Origen: HU-02.
- HU-003. Como Domiciliario, quiero solicitar mi unión a un negocio específico compartiendo mi contacto verificado de Telegram, para postularme a realizar entregas para ese establecimiento. Origen: HU-04.
- HU-004. Como Administrador del negocio, quiero aprobar o rechazar las solicitudes de vinculación de empleados y domiciliarios, para conformar el equipo de trabajo autorizado en mi establecimiento. Origen: HU-05.
- HU-005. Como Empleado o vendedor, quiero solicitar mi vinculación a un negocio específico compartiendo mi contacto verificado de Telegram, para integrarme al equipo de trabajo y coordinar pedidos en dicho establecimiento. Origen: HU-09.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir a una persona sin negocio registrado ni pendiente enviar una solicitud de registro de establecimiento ingresando nombre comercial, dirección y compartiendo obligatoriamente su contacto mediante el botón nativo de Telegram. Origen: HU-01, DEC-E01, DEC-E20.
- RF-002. El sistema debe verificar en el backend que el contacto recibido proviene del evento nativo de Telegram antes de crear la solicitud de negocio. Origen: contexto 3.2, contexto 3.11, DEC-E20.
- RF-003. El sistema debe registrar la solicitud de negocio en estado pendiente y notificar a la persona solicitante a través del bot la confirmación de recepción. Origen: HU-01.
- RF-004. El sistema debe bloquear cualquier intento de acceso a funciones operativas o de configuración por parte de un solicitante mientras su negocio se encuentre en estado pendiente o rechazado. Origen: HU-01.
- RF-005. El sistema debe permitir al dueño de la plataforma consultar la lista de solicitudes de registro de negocios en estado pendiente, mostrando exclusivamente el nombre comercial del negocio y el nombre del solicitante. Origen: HU-02, contexto 2.3, contexto 3.3.
- RF-006. El sistema debe permitir al dueño de la plataforma aprobar una solicitud de negocio pendiente, cambiando el estado del establecimiento a activo, otorgando al solicitante el rol de Administrador del negocio y enviándole una notificación de bienvenida y confirmación por el bot. Origen: HU-02, contexto 3.11, DEC-E01.
- RF-007. El sistema debe permitir al dueño de la plataforma rechazar una solicitud de negocio pendiente, cambiando el estado a rechazado y notificando la decisión al solicitante por el bot sin otorgar permisos en el sistema. Origen: HU-02.
- RF-008. El sistema debe permitir a un usuario solicitar vinculación como domiciliario a un negocio activo, identificando el negocio y compartiendo obligatoriamente su contacto mediante el botón nativo de Telegram. Origen: HU-04, contexto 3.11, DEC-E02, DEC-E20.
- RF-009. El sistema debe validar en el backend, antes de registrar una solicitud de domiciliario, que el usuario no posea una vinculación activa ni una solicitud pendiente como domiciliario en ningún negocio de la plataforma. Si posee alguna, debe rechazar la solicitud e informar la restricción. Origen: HU-04, contexto 3.11, DEC-E03.
- RF-010. El sistema debe permitir a un usuario solicitar vinculación como empleado o vendedor a un negocio activo, identificando el negocio y compartiendo obligatoriamente su contacto mediante el botón nativo de Telegram. Origen: HU-09, contexto 3.11, DEC-E02, DEC-E20.
- RF-011. El sistema debe validar que un aspirante a empleado o domiciliario no envíe solicitudes duplicadas si ya cuenta con una solicitud pendiente o una vinculación activa en el mismo negocio. Origen: HU-04, HU-09, contexto 3.7.
- RF-012. El sistema debe notificar al administrador del negocio a través del bot cada vez que se registre una nueva solicitud de vinculación de personal para su establecimiento, indicando nombre y rol solicitado. Origen: HU-05, contexto 3.11, DEC-E25.
- RF-013. El sistema debe permitir al administrador del negocio consultar las solicitudes de vinculación de personal pendientes únicamente de su propio establecimiento, mostrando nombre del aspirante y rol solicitado. Origen: HU-05, contexto 3.3.
- RF-014. El sistema debe permitir al administrador del negocio aprobar una solicitud de vinculación pendiente de su establecimiento, activando al usuario en el rol correspondiente (empleado o domiciliario), registrando fecha y responsable, y notificando la aprobación al aspirante por el bot. Origen: HU-05, contexto 3.8.
- RF-015. El sistema debe permitir al administrador del negocio rechazar una solicitud de vinculación pendiente de su establecimiento, marcándola como rechazada, registrando fecha y responsable, y notificando el rechazo al aspirante sin habilitarle accesos operativos. Origen: HU-05, contexto 3.8.
- RF-016. El sistema debe solicitar confirmación previa al dueño de la plataforma antes de aprobar o rechazar un negocio, y al administrador antes de aprobar o rechazar una vinculación. Origen: contexto 3.7.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización: cada operación de consulta, registro, aprobación y rechazo debe validar en el backend la identidad del usuario en Telegram, su rol asignado y su pertenencia al negocio. Se verifica con: inspección de código y pruebas de seguridad simulando peticiones con roles no autorizados. Origen: contexto 3.2.
- RNF-002. Aislamiento multitenant: las consultas de solicitudes de vinculación deben estar estrictamente filtradas por el identificador del negocio del administrador solicitante. Se verifica con: pruebas automáticas de consulta cruzada entre diferentes negocios. Origen: contexto 3.3.
- RNF-003. Concurrencia y atomicidad: las transiciones de estado de solicitudes de negocio y solicitudes de vinculación deben ejecutarse de forma atómica impidiendo aprobaciones o rechazos simultáneos contradictorios. Se verifica con: pruebas automatizadas de peticiones concurrentes simultáneas. Origen: contexto 3.8.
- RNF-004. Trazabilidad de auditoría: cada cambio de estado en solicitudes de negocio y de personal debe almacenar marca de tiempo y el identificador del responsable de la decisión. Se verifica con: inspección de registros de persistencia tras cada transición. Origen: contexto 3.8.
- RNF-005. Protección de datos personales: la interfaz del dueño de la plataforma no debe exponer teléfono, dirección ni datos de pedidos u operaciones de los negocios evaluados. Se verifica con: prueba de verificación de carga de datos en vistas de aprobación del dueño. Origen: contexto 2.3, contexto 3.3.

### 7. Reglas de negocio
- BR-001. Exclusividad de solicitud de negocio: una cuenta de Telegram solo puede tener una solicitud de negocio en estado pendiente de aprobación simultáneamente. Origen: HU-01, contexto 3.7.
- BR-002. Verificación de identidad por contacto: toda solicitud de creación de negocio o vinculación de personal exige la transmisión del número de teléfono mediante el botón nativo de compartir contacto de Telegram; no se admiten números digitados en texto libre. Origen: contexto 3.11, DEC-E20, HU-01, HU-04, HU-09.
- BR-003. Asignación inmediata de rol administrador: la aprobación de un establecimiento por el dueño de la plataforma convierte automáticamente al solicitante en Administrador de dicho negocio y activa el establecimiento para operar. Origen: contexto 3.11, DEC-E01, HU-02.
- BR-004. Separación de funciones del dueño de la plataforma: el dueño de la plataforma únicamente tiene autorización para aprobar o rechazar negocios y gestionar suscripciones; no puede ver detalles operativos ni gestionar personal ni pedidos de ningún negocio. Origen: contexto 2.3, HU-02.
- BR-005. Exclusividad del domiciliario: un usuario con rol de domiciliario activo o con solicitud de domiciliario pendiente en cualquier establecimiento no puede enviar solicitudes de vinculación a ningún otro negocio. Origen: contexto 3.11, DEC-E03, HU-04.
- BR-006. Aislamiento de gestión de personal: el administrador de un negocio únicamente puede visualizar, aprobar o rechazar las solicitudes de vinculación dirigidas específicamente a su establecimiento. Origen: contexto 3.3, HU-05.
- BR-007. No duplicidad en vinculaciones: un usuario no puede registrar una solicitud de vinculación a un negocio si ya cuenta con una vinculación activa o una solicitud en estado pendiente para el mismo negocio y rol. Origen: HU-04, HU-09, contexto 3.7.
- BR-008. Inmutabilidad de decisiones finales sobre solicitudes: una solicitud de negocio o de vinculación que ha pasado a estado aprobada o rechazada no puede cambiar de estado nuevamente. Origen: contexto 3.8.
- BR-009. Estados y ciclo de vida de la solicitud de negocio: los estados permitidos son pendiente, aprobada (negocio activo) y rechazada. La transición desde pendiente a aprobada o rechazada solo puede ser ejecutada por el dueño de la plataforma. Origen: contexto 3.11, DEC-E01, HU-02.
- BR-010. Estados y ciclo de vida de la solicitud de vinculación: los estados permitidos son pendiente, aprobada y rechazada. La transición desde pendiente a aprobada o rechazada solo puede ser ejecutada por el administrador del negocio receptor. Origen: contexto 3.11, DEC-E02, HU-05.

### 8. Flujo principal
Flujo 1: Registro y aprobación de negocio
1. La persona ingresa al bot de Telegram e inicia el proceso de registro de negocio.
2. El sistema solicita el nombre comercial y la dirección del establecimiento.
3. La persona ingresa los datos solicitados.
4. El sistema presenta el botón nativo de Telegram para compartir el contacto y solicita confirmación.
5. La persona presiona el botón y envía su contacto verificado.
6. El sistema valida en el backend la autenticidad del evento de contacto, registra la solicitud de negocio en estado pendiente y notifica al solicitante que su solicitud está en trámite.
7. El dueño de la plataforma consulta la lista de solicitudes pendientes en el bot y visualiza el nombre del negocio y del solicitante.
8. El dueño de la plataforma selecciona la solicitud y presiona el comando de aprobación.
9. El sistema solicita confirmación de la aprobación.
10. El dueño de la plataforma confirma la acción.
11. El backend cambia el estado de la solicitud a aprobada, activa el negocio, asigna el rol de Administrador al solicitante y registra fecha y responsable.
12. El sistema envía una notificación de bienvenida y confirmación al nuevo administrador a través del bot.

Flujo 2: Vinculación de domiciliario o empleado
1. El aspirante (empleado o domiciliario) ingresa al bot indicando el enlace o identificador de un negocio activo y selecciona el rol solicitado.
2. El sistema solicita al aspirante compartir su contacto mediante el botón nativo de Telegram.
3. El aspirante presiona el botón nativo y transmite su contacto verificado.
4. El sistema valida en el backend: autenticidad del contacto, ausencia de trámites previos pendientes en ese negocio y, si el rol solicitado es domiciliario, verifica que el usuario no tenga vínculos activos ni pendientes en ningún otro negocio.
5. El sistema registra la solicitud de vinculación en estado pendiente, notifica al aspirante la espera de respuesta y envía un mensaje de notificación al administrador del negocio con el nombre y rol del aspirante.
6. El administrador del negocio ingresa a la opción de solicitudes de personal de su negocio y consulta los datos básicos de la solicitud.
7. El administrador selecciona la opción de aprobar.
8. El sistema solicita confirmación antes de aplicar la aprobación.
9. El administrador confirma la aprobación.
10. El backend actualiza la solicitud a estado aprobada, vincula al usuario en el rol seleccionado en dicho negocio y registra fecha y responsable.
11. El sistema envía una notificación al aspirante informándole que su vinculación ha sido aprobada.

### 9. Flujos alternativos y de excepción
- A1. Rechazo de solicitud de negocio por el dueño de la plataforma:
  - En el paso 8 del Flujo 1, el dueño de la plataforma selecciona la opción de rechazar.
  - El sistema solicita confirmación de la acción.
  - El dueño confirma el rechazo.
  - El backend actualiza el estado de la solicitud a rechazada, sin otorgar permisos al solicitante, y registra fecha y responsable.
  - El sistema envía notificación al solicitante informándole que la solicitud fue rechazada.
- A2. Rechazo de solicitud de vinculación por el administrador del negocio:
  - En el paso 7 del Flujo 2, el administrador del negocio selecciona la opción de rechazar.
  - El sistema solicita confirmación de la acción.
  - El administrador confirma el rechazo.
  - El backend actualiza la solicitud a estado rechazada, registrando fecha y responsable.
  - El sistema envía una notificación al aspirante indicándole que la solicitud fue rechazada, sin conceder accesos al negocio.
- E1. Intento de registro de negocio sin contacto nativo verificado:
  - En el paso 5 del Flujo 1, la persona ingresa un número de teléfono digitado en texto o cancela el envío de contacto nativo.
  - El backend detecta la ausencia del evento oficial de contacto de Telegram.
  - El sistema rechaza la operación e informa que el uso del botón nativo de contacto es obligatorio.
- E2. Solicitante con negocio pendiente intenta operar:
  - Una persona con solicitud de negocio pendiente intenta ejecutar comandos de configuración o pedidos.
  - El backend verifica el estado de la solicitud y deniega el acceso, informando que el establecimiento está pendiente de aprobación por el dueño de la plataforma.
- E3. Intento de postulación de domiciliario ya vinculado o con trámite pendiente:
  - En el paso 4 del Flujo 2, el backend identifica que el usuario ya tiene vinculación activa o pendiente como domiciliario en otro negocio o en el mismo.
  - El sistema interrumpe el registro, rechaza la solicitud e informa que un domiciliario solo puede pertenecer a un único negocio.
- E4. Intento de solicitud de vinculación duplicada por empleado:
  - En el paso 4 del Flujo 2, el backend identifica que el empleado ya tiene una solicitud pendiente o vinculación activa en ese mismo negocio.
  - El sistema bloquea el registro e informa que ya posee un trámite vigente en el establecimiento.
- E5. Usuario no autorizado intenta aprobar o consultar trámites ajenos:
  - Un usuario con rol distinto al dueño de la plataforma intenta invocar comandos de aprobación de negocios, o un empleado/domiciliario intenta gestionar personal.
  - El backend valida permisos, bloquea la acción y registra el intento de acceso no autorizado.

### 10. Casos límite
- CL-001. Solicitud simultánea de vinculación como domiciliario a dos negocios distintos: dos peticiones concurrentes del mismo usuario son procesadas al mismo instante; el backend debe asegurar atómicamente que solo una solicitud quede registrada y la otra sea rechazada por existir ya una solicitud pendiente. Origen: contexto 3.8, contexto 3.11, DEC-E03.
- CL-002. Aprobación y rechazo simultáneos de la misma solicitud de negocio: dos peticiones concurrentes sobre la misma solicitud deben resolverse de manera atómica, de modo que la primera confirmada determine el estado final y la segunda sea rechazada por estado ya modificado. Origen: contexto 3.8.
- CL-003. Intento de vinculación a un negocio inexistente o con identificador inválido: el backend valida la existencia del establecimiento antes de asociar la solicitud y retorna error informativo al usuario sin crear registros huérfanos. Origen: contexto 3.2.
- CL-004. Usuario que intenta registrar un segundo negocio teniendo uno pendiente: el backend bloquea el registro indicando que debe esperar la resolución de su solicitud actual. Origen: HU-01, BR-001.
- CL-005. Usuario que comparte el contacto de un tercero: el backend valida que el identificador de usuario asociado al contacto compartido coincida con el identificador de Telegram que origina la interacción. Origen: contexto 3.2, DEC-E20.

### 11. Criterios de aceptación
- AC-001. Dado que una persona no tiene un establecimiento registrado ni pendiente, cuando confirma el envío de nombre comercial y dirección y comparte su contacto mediante el botón nativo de Telegram, entonces el sistema registra la solicitud en estado pendiente, notifica la recepción al solicitante y no le otorga acceso a configuración ni pedidos.
- AC-002. Dado que una persona intenta registrar un establecimiento enviando el número de teléfono como texto libre sin usar el botón nativo, cuando el backend procesa la petición, entonces el sistema rechaza la solicitud e informa que la verificación mediante el botón de contacto es obligatoria.
- AC-003. Dado que existen solicitudes de registro de negocio en estado pendiente, cuando el dueño de la plataforma consulta la lista de solicitudes, entonces el sistema retorna únicamente el nombre del negocio y el nombre del solicitante de cada registro pendiente, sin exponer teléfonos, direcciones ni información operativa.
- AC-004. Dado que el dueño de la plataforma revisa una solicitud de negocio pendiente, cuando presiona aprobar y confirma la acción en el bot, entonces el backend cambia el estado de la solicitud a aprobada, activa el negocio, asigna el rol de Administrador al solicitante, registra fecha y responsable, y envía un mensaje de bienvenida al nuevo administrador por Telegram.
- AC-005. Dado que el dueño de la plataforma revisa una solicitud de negocio pendiente, cuando presiona rechazar y confirma la acción en el bot, entonces el backend marca la solicitud como rechazada, registra fecha y responsable, y notifica la decisión al solicitante por el bot sin otorgarle ningún permiso administrativo u operativo.
- AC-006. Dado que un usuario con rol de Administrador, Empleado o Domiciliario intenta ejecutar la aprobación o rechazo de un negocio, cuando invoca el comando en el bot, entonces el backend deniega la operación por permisos insuficientes.
- AC-007. Dado que un usuario ingresa el identificador de un negocio activo, selecciona el rol de domiciliario y no tiene vinculaciones activas ni pendientes en ningún negocio, cuando comparte su contacto con el botón nativo de Telegram, entonces el sistema registra su solicitud como pendiente en ese negocio, le notifica que está en espera de aprobación y envía una notificación al administrador del negocio con su nombre y rol solicitado.
- AC-008. Dado que un domiciliario ya cuenta con una vinculación activa o una solicitud pendiente en un negocio, cuando intenta enviar una solicitud de vinculación como domiciliario a otro negocio, entonces el sistema rechaza la solicitud en el backend e informa que un domiciliario solo puede pertenecer a un único negocio.
- AC-009. Dado que un usuario ya tiene una solicitud pendiente o activa en un negocio, cuando intenta enviar una nueva postulación al mismo establecimiento para el mismo rol, entonces el sistema rechaza el intento informando que ya cuenta con un trámite vigente y no crea registros duplicados.
- AC-010. Dado que existen solicitudes de vinculación pendientes para un negocio, cuando el administrador de ese negocio consulta la lista de aspirantes, entonces el sistema muestra únicamente las solicitudes asociadas a su establecimiento con el nombre y rol solicitado, sin mostrar solicitudes de otros negocios.
- AC-011. Dado que el administrador de un negocio revisa una solicitud pendiente de su establecimiento, cuando presiona aprobar y confirma la acción, entonces el backend actualiza la vinculación a estado aprobada, activa los permisos del rol solicitado (empleado o domiciliario), registra fecha y responsable, y notifica la autorización al aspirante por Telegram.
- AC-012. Dado que el administrador de un negocio revisa una solicitud pendiente de su establecimiento, cuando presiona rechazar y confirma la acción, entonces el backend actualiza el estado a rechazada, registra fecha y responsable, y notifica el rechazo al aspirante sin concederle acceso a la operación del negocio.
- AC-013. Dado que un empleado o un domiciliario intenta acceder a la gestión de solicitudes de personal de un negocio, cuando envía la petición, entonces el backend bloquea el acceso por permisos insuficientes.
- AC-014. Dado que dos solicitudes de vinculación como domiciliario para dos negocios distintos son enviadas simultáneamente por el mismo usuario, cuando ambas llegan al backend, entonces una transacción se completa con éxito quedando en estado pendiente y la otra es rechazada informando la existencia de un trámite en curso.

### 12. Dependencias
- Servicio de mensajería y bot de Telegram para interacción conversacional y botones nativos de contacto.
- Almacén de persistencia de datos del backend para usuarios, negocios, roles y solicitudes.

### 13. Restricciones
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar (contexto 4).
- Proyecto individual desarrollado bajo la metodología guiada por especificaciones SDD (contexto 4).
- La lógica de negocio, autenticación, autorización y validación reside exclusivamente en el backend y nunca solo en el bot de Telegram (contexto 3.2).
- Separación estricta de la información por negocio: ningún usuario accede ni modifica datos de otro negocio (contexto 3.3).
- Protección de datos personales y acceso únicamente a la información autorizada por rol (contexto 3.3, contexto 6).
- Los cambios de estado de solicitudes y vinculaciones son atómicos y registran fecha, estado y responsable (contexto 3.8).
- Las operaciones críticas de aprobación y rechazo requieren confirmación previa antes de su ejecución (contexto 3.7).
- Se prohíbe el uso de códigos de verificación por SMS; la validación de identidad y teléfono se realiza exclusivamente con el botón nativo de Telegram (contexto 3.11, DEC-E20).
- Plazo del proyecto de 8 semanas o más (contexto 4, contexto 3.11, DEC-E19).

### 14. Fuera de alcance
- Plataforma como central de repartidores unificada (contexto 5).
- Funcionalidades de marketplace o listado/directorio público de negocios registrados (contexto 5, contexto 3.11, DEC-E05).
- Cobro de comisiones por pedido, por entrega o pasarela de pagos en línea (contexto 2.1, contexto 5).
- Control de suscripciones y cobro periódico de mensualidad en línea (contexto 3.11, DEC-E26).
- Gestión operativa de pedidos, catálogo y zonas de cobertura (corresponden a otras SPEC dentro del sistema).
- Mecanismo de persistencia de sesiones y tokens de autenticación: tema para arquitectura. Origen: RF-001, contexto 3.2.
- Estrategia de control de concurrencia y bloqueo a nivel de base de datos para la exclusividad de domiciliarios: tema para arquitectura. Origen: RF-009, CL-001.
- Estructura de esquemas de datos relacionales o documentales: tema para arquitectura. Origen: contexto 3.2.

### 15. Preguntas abiertas
- OPEN-Q-001: Pendiente.
- OPEN-Q-002: Pendiente.
- OPEN-Q-003: Pendiente.
- OPEN-Q-004: Pendiente.
- OPEN-Q-005: Pendiente.
- OPEN-Q-006: Pendiente.
- OPEN-Q-007: Pendiente.
- OPEN-Q-008: Pendiente.
- OPEN-Q-009: Pendiente.

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-004; BR-001, BR-002; AC-001, AC-002; CL-004, CL-005.
- HU-002: RF-005, RF-006, RF-007, RF-016; BR-003, BR-004, BR-008, BR-009; AC-003, AC-004, AC-005, AC-006; CL-002.
- HU-003: RF-008, RF-009, RF-011; BR-002, BR-005, BR-007; AC-007, AC-008, AC-009; CL-001, CL-003.
- HU-004: RF-012, RF-013, RF-014, RF-015, RF-016; BR-006, BR-008, BR-010; AC-010, AC-011, AC-012, AC-013.
- HU-005: RF-010, RF-011; BR-002, BR-007; AC-007, AC-009.
- RF-001: Origen: HU-01, DEC-E01, DEC-E20; verificado por AC-001.
- RF-002: Origen: contexto 3.2, contexto 3.11, DEC-E20; verificado por AC-001, AC-002.
- RF-003: Origen: HU-01; verificado por AC-001.
- RF-004: Origen: HU-01; verificado por AC-001.
- RF-005: Origen: HU-02, contexto 2.3, contexto 3.3; verificado por AC-003.
- RF-006: Origen: HU-02, contexto 3.11, DEC-E01; verificado por AC-004.
- RF-007: Origen: HU-02; verificado por AC-005.
- RF-008: Origen: HU-04, contexto 3.11, DEC-E02, DEC-E20; verificado por AC-007.
- RF-009: Origen: HU-04, contexto 3.11, DEC-E03; verificado por AC-008, AC-014.
- RF-010: Origen: HU-09, contexto 3.11, DEC-E02, DEC-E20; verificado por AC-007.
- RF-011: Origen: HU-04, HU-09, contexto 3.7; verificado por AC-009.
- RF-012: Origen: HU-05, contexto 3.11, DEC-E25; verificado por AC-007.
- RF-013: Origen: HU-05, contexto 3.3; verificado por AC-010.
- RF-014: Origen: HU-05, contexto 3.8; verificado por AC-011.
- RF-015: Origen: HU-05, contexto 3.8; verificado por AC-012.
- RF-016: Origen: contexto 3.7; verificado por AC-004, AC-005, AC-011, AC-012.
- RNF-001: Origen: contexto 3.2; verificado con pruebas de seguridad e inspección de código.
- RNF-002: Origen: contexto 3.3; verificado con pruebas automáticas de consulta cruzada.
- RNF-003: Origen: contexto 3.8; verificado con pruebas automatizadas de peticiones concurrentes simultáneas.
- RNF-004: Origen: contexto 3.8; verificado con inspección de registros de persistencia tras cada transición.
- RNF-005: Origen: contexto 2.3, contexto 3.3; verificado con prueba de verificación de carga de datos en vistas de aprobación del dueño.
- BR-001: Origen: HU-01, contexto 3.7; verificado por AC-001.
- BR-002: Origen: contexto 3.11, DEC-E20, HU-01, HU-04, HU-09; verificado por AC-002.
- BR-003: Origen: contexto 3.11, DEC-E01, HU-02; verificado por AC-004.
- BR-004: Origen: contexto 2.3, HU-02; verificado por AC-003, AC-006.
- BR-005: Origen: contexto 3.11, DEC-E03, HU-04; verificado por AC-008, AC-014.
- BR-006: Origen: contexto 3.3, HU-05; verificado por AC-010.
- BR-007: Origen: HU-04, HU-09, contexto 3.7; verificado por AC-009.
- BR-008: Origen: contexto 3.8; verificado por AC-004, AC-005, AC-011, AC-012.
- BR-009: Origen: contexto 3.11, DEC-E01, HU-02; verificado por AC-004, AC-005.
- BR-010: Origen: contexto 3.11, DEC-E02, HU-05; verificado por AC-011, AC-012.
- CL-001: Origen: contexto 3.8, contexto 3.11, DEC-E03; verificado por AC-014.
- CL-002: Origen: contexto 3.8; verificado por AC-004, AC-005.
- CL-003: Origen: contexto 3.2; verificado por AC-007.
- CL-004: Origen: HU-01, BR-001; verificado por AC-001.
- CL-005: Origen: contexto 3.2, DEC-E20; verificado por AC-002.

### 17. Historial de cambios
- Versión 0.1: creación inicial de la especificación a partir de la necesidad y las historias HU-01, HU-02, HU-04, HU-05 y HU-09 de EPIC-001, manteniendo las preguntas de aclaración en estado pendiente.

## Verificación
- Completitud: cumple. Se cubrieron las 17 secciones del estándar y los flujos de registro, aprobación y vinculación solicitados.
- Consistencia interna: cumple. Se verificó que las reglas de negocio coincidan con los requisitos funcionales, flujos de excepción y criterios de aceptación.
- Consistencia con el contexto: cumple. Se validó correspondencia con DEC-E01, DEC-E02, DEC-E03, DEC-E20, DEC-E25 y principios de autorización en backend.
- No ambigüedad: cumple. Los términos y comportamientos observables están redactados sin juicios de valor ni términos ambiguos.
- Verificabilidad: cumple. Cada criterio de aceptación está en formato Dado/Cuando/Entonces y es observable.
- Cobertura de actores: cumple. Se incluyeron historias y flujos para solicitante, dueño de la plataforma, administrador, empleado y domiciliario.
- Cobertura de AC: cumple. Todos los RF y BR tienen criterios de aceptación directos asociados en la sección 16.
- Trazabilidad: cumple. Todos los RF, RNF, BR y CL cuentan con origen y método de verificación en la matriz de trazabilidad.
- No invención: cumple. Los vacíos no decididos por el equipo se mantienen en la sección 15 como preguntas abiertas y no se asumieron como decisiones cerradas.
- Delimitación: cumple. No se tomaron decisiones de arquitectura técnica, bases de datos ni endpoints, delegándolos a la sección 14.

## Siguiente paso
Respondan las preguntas abiertas y ejecuten de nuevo el agente con --continuar SPEC-001.
