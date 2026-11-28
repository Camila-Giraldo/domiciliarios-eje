<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-19 11:25
Petición: Cambio solicitado por el equipo sobre la SPEC-001 aprobada: DEC-E42 (contexto 3.11) define que cada negocio tiene dos accesos distintos, uno para clientes y otro para personal. Precisa en la SPEC-001 que empleados y domiciliarios piden unirse mediante el enlace, QR o código de personal del negocio (no el de clientes), que ese acceso solo lo ve el administrador, y que si alguien usa el acceso de clientes no entra al flujo de vinculación de personal. Haz el análisis de impacto y entrega la versión 1.1 en estado Candidata.
-->

# SPEC-001. Registro y aprobacion de negocio y vinculacion de personal - Versión 1.1

Estado: Candidata
Modo: Cambio
Necesidad original: "EPIC-001. Especifica el registro y la aprobación del negocio y la vinculación de su personal: una persona registra su negocio desde el bot compartiendo su contacto y queda pendiente hasta que el dueño de la plataforma lo aprueba o rechaza; al aprobarse pasa a ser su administrador; empleados y domiciliarios piden unirse a un negocio y el administrador aprueba o rechaza. Las historias de usuario aprobadas HU-01, HU-02, HU-04, HU-05 y HU-09 están en el archivo adjunto; respétalas como entrada."
Épica: EPIC-001

## Análisis
- Objetivo: permitir que nuevos establecimientos soliciten su registro en la plataforma mediante el bot de Telegram previo consentimiento explícito de tratamiento de datos personales, términos del servicio, acuerdo de transmisión, correo de atención de habeas data, datos comerciales y contacto verificado; garantizar la aprobación o rechazo justificado con motivo obligatorio por parte del dueño de la plataforma; y permitir que empleados y domiciliarios soliciten su vinculación a un negocio activo utilizando exclusivamente el acceso de personal del negocio (enlace profundo, QR o código de personal) visible únicamente para el administrador, impidiendo el ingreso al flujo de vinculación a través del acceso de clientes, regulando la exclusividad del domiciliario, el consentimiento de ubicación, la expiración de solicitudes a los 7 días y la opción de retiro voluntario.
- Alcance inicial: registro de solicitud de negocio con autorización de tratamiento de datos, términos, acuerdo de transmisión, correo de atención y contacto verificado; aprobación o rechazo con motivo del negocio; postulación de domiciliarios vía acceso exclusivo de personal con validación de exclusividad y consentimiento específico de ubicación y recorrido; postulación de empleados vía acceso exclusivo de personal (multi-negocio sin duplicidad en el mismo establecimiento); restricción del acceso de personal para ser visible únicamente por el administrador del negocio; rechazo de solicitudes de vinculación intentadas desde el acceso de clientes; gestión con motivo obligatorio de solicitudes por parte del administrador del negocio; retiro voluntario de solicitudes; expiración automática de solicitudes tras 7 días; notificaciones asociadas en Telegram.
- Actores: Persona que solicita el registro del negocio, Dueño de la plataforma, Administrador del negocio, Empleado o vendedor, Domiciliario, Telegram (canal de transporte).
- Contexto aplicable: secciones 2.3, 3.1, 3.2, 3.3, 3.4, 3.6, y decisiones DEC-E01, DEC-E02, DEC-E03, DEC-E15, DEC-E20, DEC-E25, DEC-E29, DEC-E35, DEC-E36, DEC-E37, DEC-E38, DEC-E39 y DEC-E42 del contexto 3.11, más las decisiones DEC-001 a DEC-015.

## Modelo de dominio
- Negocio: entidad principal que representa el establecimiento de comercio. Pertenece a la plataforma; cardinalidad uno o varios en la plataforma. Posee nombre comercial, ciudad o municipio, dirección, correo de atención para datos personales y dos tipos de acceso diferenciados: accesos de cliente (para pedidos) y accesos de personal (enlace, QR y código de personal, visibles solo para el administrador). Origen: contexto 2.4, DEC-E01, DEC-E42, DEC-005, DEC-014, DEC-015.
- Solicitud de registro de negocio: registro del trámite de apertura. Pertenece a una persona solicitante y a la plataforma; cardinalidad una activa o pendiente por trámite. Transita entre pendiente, aprobada, rechazada (con motivo obligatorio), cancelada o expirada. Origen: HU-01, HU-02, DEC-001, DEC-008, DEC-009, DEC-010.
- Usuario: persona identificada mediante su cuenta de Telegram. Almacena identificador numérico de Telegram, nombre de la cuenta y teléfono verificado. Origen: contexto 2.3, DEC-E20, DEC-006.
- Autorización de datos: registro probatorio de consentimiento legal. Pertenece a un usuario. Contiene tipo de autorización, versión del texto legal, fecha y hora de aceptación, y estado de revocabilidad. Origen: DEC-E36, DEC-011, DEC-013, DEC-014.
- Vinculación de personal: relación entre un usuario y un negocio específico bajo un rol (empleado o domiciliario). Pertenece a un usuario y a un negocio; cardinalidad: un usuario domiciliario sólo puede poseer máximo una vinculación activa o pendiente en toda la plataforma; un empleado puede estar vinculado a múltiples negocios. Origen: DEC-E02, DEC-E03, DEC-002.
- Solicitud de vinculación: petición de un usuario para ingresar a un negocio como empleado o domiciliario iniciada únicamente desde el acceso exclusivo de personal del establecimiento. Transita entre pendiente, aprobada, rechazada (con motivo obligatorio), cancelada o expirada. Origen: DEC-E02, DEC-E42, DEC-004, DEC-008, DEC-009, DEC-010, DEC-015.

## Contradicciones detectadas
Ninguna. Todas las decisiones del equipo coinciden con la sección 3 del contexto, las decisiones del contexto 3.11, el marco legal de la sección 6 y las reglas críticas del proyecto.

## Análisis de impacto
- DEC-015 (DEC-E42): afecta Contexto (sección 2), Alcance (sección 3), HU-003, HU-005, RF-009, RF-011, nuevo RF-020, BR-013, Flujo 2 (paso 1), Flujo de excepción E7, CL-003, AC-007, AC-010, nuevo AC-019 y nuevo AC-020. Establece que cada negocio posee dos accesos diferenciados (cliente y personal), que el acceso de personal (enlace, QR o código) es visible únicamente para el administrador del negocio, que las solicitudes de vinculación de empleados y domiciliarios deben originarse obligatoriamente desde el acceso de personal, y que el uso del acceso de clientes rechaza el ingreso al flujo de vinculación de personal.

## Preguntas de aclaración
No hay preguntas pendientes.

## Especificación

### 1. Objetivo
Permitir el registro de nuevos establecimientos de comercio mediante el bot de Telegram previa aceptación explícita de tratamiento de datos personales, términos del servicio, acuerdo de transmisión, correo de atención para habeas data y contacto verificado; garantizar su aprobación o rechazo justificado con motivo obligatorio por el dueño de la plataforma; y permitir la vinculación de empleados y domiciliarios mediante la aprobación del administrador de cada negocio a través de un acceso exclusivo de personal visible únicamente para el administrador, garantizando la imposibilidad de vincularse desde el acceso de clientes, la exclusividad del domiciliario, el consentimiento de ubicación, la expiración de solicitudes a los 7 días y la opción de retiro voluntario.

### 2. Contexto
En Domiciliarios Eje cada negocio gestiona su propia operación de pedidos a domicilio desde Telegram. Una persona solicita registrar su negocio en el bot y queda en espera de que el dueño de la plataforma evalúe y apruebe su solicitud. Al ser aprobada, el solicitante asume el rol de Administrador y puede visualizar el acceso exclusivo de personal de su negocio para recibir y resolver las postulaciones de empleados y domiciliarios. Conforme a DEC-E42, cada negocio cuenta con accesos separados para clientes (pedidos) y para personal (unión de trabajadores), asegurando que el acceso de personal solo sea visible para el administrador y que el acceso de clientes no permita iniciar trámites de vinculación laboral. Conforme al régimen de protección de datos personales de Colombia (Ley 1581 de 2012 y Decreto 1377 de 2013), la plataforma actúa como Responsable del tratamiento de los datos de negocios, solicitantes y personal vinculado, exigiendo autorizaciones previas, expresas, informadas y revocables antes de solicitar cualquier dato personal.

Decisiones del equipo aplicables:
- DEC-E01. Un negocio se registra solo desde el bot y queda pendiente hasta que el dueño de la plataforma lo aprueba. Quien lo registra queda como su administrador. Origen: contexto 3.11.
- DEC-E02. Empleados y domiciliarios piden unirse a un negocio desde el bot y el administrador aprueba o rechaza la solicitud. Origen: contexto 3.11.
- DEC-E03. Un domiciliario pertenece a un solo negocio: no puede pedir unirse a otro mientras tenga una vinculación activa o pendiente. La restricción aplica solo al rol domiciliario; una misma cuenta puede ser empleado o administrador de otros negocios y cliente de varios. Origen: contexto 3.11.
- DEC-E20. Una persona se identifica con su cuenta de Telegram y, al registrarse, comparte su contacto con el botón nativo de Telegram; el teléfono queda verificado por Telegram. No se usan códigos por SMS. Origen: contexto 3.11.
- DEC-E25. Notificaciones del negocio: el administrador recibe las solicitudes de unión. Origen: contexto 3.11.
- DEC-E35. Las solicitudes pendientes de registro de negocio y de vinculación de personal vencen a los 7 días; se avisa al solicitante. Origen: contexto 3.11.
- DEC-E36. Todo actor cuyos datos personales se traten da una autorización previa, expresa e informada con un botón antes de compartir sus datos; la aceptación queda registrada con fecha, hora y versión del texto, y se puede revocar. Origen: contexto 3.11.
- DEC-E37. Responsables del tratamiento: la plataforma es Responsable de los datos de los negocios, de quienes los registran y de su personal. Origen: contexto 3.11.
- DEC-E38. El domiciliario acepta, además del general, un consentimiento propio para su ubicación en tiempo real y su recorrido; sin él no puede vincularse como domiciliario. Origen: contexto 3.11.
- DEC-E39. Al registrar un negocio se pide también un correo de atención de datos personales y quien lo registra acepta los términos de la plataforma y el acuerdo de transmisión de datos. Origen: contexto 3.11.
- DEC-E42. Cada negocio tiene dos accesos distintos: enlace, QR y código para clientes (pedidos) y enlace, QR y código para personal (solicitudes de unión); el de personal solo lo ve el administrador. Origen: contexto 3.11.
- DEC-001. El dueño de la plataforma registra un motivo obligatorio al rechazar un negocio; el motivo se notifica al solicitante por el bot; la persona puede volver a registrar su negocio corrigiendo los datos. Responde a OPEN-Q-001.
- DEC-002. La restricción de un solo negocio aplica sólo a domiciliarios (DEC-E03); un empleado puede estar vinculado a varios negocios, sin duplicar solicitud ni vinculación activa en el mismo negocio. Responde a OPEN-Q-002.
- DEC-003. Si el administrador rechaza a un domiciliario, este queda libre de inmediato para postularse a otro negocio o volver a pedir al mismo. Responde a OPEN-Q-003.
- DEC-004. El administrador registra un motivo obligatorio al rechazar a un aspirante (empleado o domiciliario) y el motivo se notifica al aspirante por el bot. Responde a OPEN-Q-004.
- DEC-005. El registro del negocio pide nombre comercial, ciudad o municipio y dirección; no se permite el mismo nombre comercial exacto en la misma ciudad o municipio. Responde a OPEN-Q-005.
- DEC-006. Se guardan el identificador de Telegram, el nombre de la cuenta y el teléfono verificado; antes de pedir el contacto nativo, la persona debe aceptar explícitamente el tratamiento de datos con un botón y la aceptación queda registrada. Responde a OPEN-Q-006.
- DEC-007. El empleado o domiciliario llega al negocio por enlace profundo, código QR del negocio o escribiendo el código del negocio en el chat del bot. Responde a OPEN-Q-007.
- DEC-008. Las solicitudes pendientes (de negocio y de vinculación de personal) vencen solas tras un plazo y se avisa al solicitante por el bot. Responde a OPEN-Q-008.
- DEC-009. El solicitante puede retirar (cancelar) su solicitud mientras esté pendiente; queda cancelada y puede iniciar otra. Responde a OPEN-Q-009.
- DEC-010. Las solicitudes pendientes de registro de negocio y de vinculación de personal expiran automáticamente a los 7 días (168 horas) calendario y se envía notificación al solicitante. Responde a OPEN-Q-010.
- DEC-011. Toda autorización de tratamiento de datos personales se otorga de manera previa, expresa e informada con un botón específico, registrando fecha, hora, identificador de usuario y versión del texto legal exhibido, manteniendo su condición revocable.
- DEC-012. La plataforma asume el rol de Responsable del tratamiento de datos personales de negocios, solicitantes y personal vinculado.
- DEC-013. El aspirante a domiciliario debe aceptar de forma obligatoria un consentimiento complementario para el uso de su ubicación en tiempo real y el almacenamiento de su recorrido durante 30 días; sin dicha autorización no puede solicitar vinculación como domiciliario.
- DEC-014. El registro de un negocio exige capturar un correo electrónico de atención de datos personales para la atención de los clientes del establecimiento, y exige la aceptación explícita de los términos del servicio y del acuerdo de transmisión de datos.
- DEC-015. El personal (empleados y domiciliarios) sólo puede solicitar su vinculación utilizando el acceso exclusivo de personal (enlace profundo, código QR o código de personal del negocio), el cual sólo es visible para el administrador. Si un usuario intenta usar el acceso de clientes (enlace, QR o código para pedidos), el sistema deniega el acceso y no le permite iniciar el flujo de vinculación de personal. Origen: DEC-E42.

### 3. Alcance
- Presentación de avisos de privacidad y captura de autorizaciones expresas previas al registro de negocio y de personal.
- Captura y registro de términos del servicio y acuerdo de transmisión de datos para la persona que registra un establecimiento.
- Captura obligatoria de correo electrónico de atención de datos personales del establecimiento.
- Captura de solicitud de registro de negocio con nombre comercial, ciudad o municipio, dirección y teléfono verificado mediante botón nativo de Telegram.
- Validación de no duplicidad de nombre comercial exacto en la misma ciudad o municipio.
- Generación y consulta de dos accesos diferenciados por negocio: accesos de cliente (pedidos) y accesos de personal (enlace profundo, QR y código de personal), restringiendo la visibilidad del acceso de personal únicamente al administrador del negocio.
- Denegación automática del flujo de vinculación de personal cuando un usuario intente ingresar utilizando el acceso de clientes.
- Consulta de solicitudes pendientes de registro de negocio por el dueño de la plataforma (visualizando únicamente nombre comercial, ciudad o municipio y nombre de cuenta del solicitante).
- Aprobación o rechazo justificado con motivo obligatorio de solicitudes de negocio por el dueño de la plataforma, habilitando la corrección y reintento.
- Asignación automática del rol de Administrador al solicitante una vez aprobado su negocio.
- Postulación de aspirantes a domiciliario únicamente vía enlace profundo, QR o código de personal del negocio, validando exclusividad en la plataforma y requiriendo consentimiento general y consentimiento específico de ubicación y recorrido.
- Postulación de aspirantes a empleado únicamente vía enlace profundo, QR o código de personal del negocio, permitiendo vinculación a múltiples negocios sin duplicidad en el mismo.
- Consulta y resolución (aprobación o rechazo justificado con motivo obligatorio) de solicitudes de personal por parte del administrador del negocio.
- Liberación inmediata del aspirante a domiciliario rechazado para nuevas postulaciones.
- Retiro voluntario de solicitudes pendientes por el propio solicitante.
- Expiración automática de solicitudes pendientes al cumplirse el plazo de 7 días, con notificación al usuario.
- Notificaciones en Telegram asociadas a cada evento y cambio de estado.

### 4. Actores e historias de usuario
Actores:
- Persona que solicita el registro del negocio: usuario de Telegram que tramita la apertura de un establecimiento en la plataforma.
- Dueño de la plataforma: usuario autorizado para aprobar o rechazar solicitudes de registro de negocios. No opera pedidos ni accede a información operativa.
- Administrador del negocio: solicitante aprobado que gestiona su establecimiento, accede de forma exclusiva a los enlaces y códigos de personal y autoriza las solicitudes de su personal.
- Domiciliario: repartidor que solicita vinculación exclusiva a un negocio mediante su acceso de personal, autoriza el uso de su ubicación y realiza entregas una vez aprobado.
- Empleado o vendedor: usuario que solicita vinculación a un negocio mediante su acceso de personal para integrarse al equipo operativo.

Historias de usuario:
- HU-001. Como persona que quiere registrar su negocio, quiero aceptar el aviso de privacidad, los términos y el acuerdo de transmisión, e ingresar el nombre comercial, ciudad, dirección, correo de atención de datos y mi contacto verificado de Telegram, para solicitar la apertura de mi negocio en la plataforma y quedar en espera de aprobación. Origen: HU-01, DEC-005, DEC-006, DEC-011, DEC-014.
- HU-002. Como Dueño de la plataforma, quiero revisar las solicitudes pendientes de registro de negocio para aprobarlas o rechazarlas ingresando un motivo obligatorio, para controlar qué establecimientos operan en la plataforma sin acceder a su información operativa ni datos sensibles. Origen: HU-02, DEC-001, DEC-012.
- HU-003. Como Domiciliario, quiero autorizar el tratamiento de mis datos y el uso de mi ubicación y recorrido, y postularme a un negocio específico ingresando mediante su acceso exclusivo de personal (enlace, QR o código de personal) compartiendo mi contacto verificado, para solicitar realizar entregas de forma exclusiva para dicho establecimiento. Origen: HU-04, DEC-E42, DEC-003, DEC-007, DEC-011, DEC-013, DEC-015.
- HU-004. Como Administrador del negocio, quiero consultar de forma exclusiva los accesos de personal de mi negocio y gestionar las solicitudes recibidas en mi establecimiento aprobándolas o rechazándolas con un motivo obligatorio, para conformar el equipo de trabajo autorizado en mi negocio. Origen: HU-05, DEC-E42, DEC-004, DEC-015.
- HU-005. Como Empleado o vendedor, quiero autorizar el tratamiento de mis datos y solicitar mi vinculación a un negocio específico ingresando mediante su acceso exclusivo de personal (enlace, QR o código de personal) compartiendo mi contacto verificado, para integrarme al equipo operativo de dicho establecimiento. Origen: HU-09, DEC-E42, DEC-002, DEC-007, DEC-011, DEC-015.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir a una persona sin solicitud activa ni pendiente tramitar el registro de su negocio, presentando de forma previa y obligatoria la aceptación explícita de la política de datos personales, los términos del servicio y el acuerdo de transmisión de datos mediante botones nativos, antes de solicitar los datos del establecimiento y el contacto verificado de Telegram. Origen: HU-001, DEC-E01, DEC-E36, DEC-E39, DEC-006, DEC-011, DEC-014.
- RF-002. El sistema debe validar que el número de teléfono recibido provenga exclusivamente del evento nativo de contacto de Telegram correspondiente al usuario en sesión, y que se haya registrado la aceptación expresa de las autorizaciones legales requeridas antes de crear la solicitud. Origen: contexto 3.2, DEC-E20, DEC-006, DEC-011.
- RF-003. El sistema debe capturar el nombre comercial, ciudad o municipio, dirección y correo electrónico de atención de datos personales del negocio, validando que no exista otro negocio activo o en trámite con el mismo nombre comercial exacto en la misma ciudad o municipio. Origen: DEC-005, DEC-014, contexto 3.7.
- RF-004. El sistema debe registrar la solicitud de negocio en estado pendiente, almacenar el registro probatorio de la autorización con fecha, hora y versión del texto legal, y notificar al solicitante por el bot la confirmación de recepción. Origen: HU-001, DEC-E36, DEC-011.
- RF-005. El sistema debe bloquear el acceso a cualquier función de configuración u operación del negocio a todo usuario cuya solicitud permanezca en estado pendiente, rechazada, cancelada o expirada. Origen: HU-001, DEC-001, DEC-008, DEC-009, DEC-010.
- RF-006. El sistema debe permitir al dueño de la plataforma consultar la lista de solicitudes de registro de negocio pendientes, mostrando únicamente nombre comercial, ciudad o municipio y nombre de cuenta de Telegram del solicitante. Origen: HU-002, contexto 2.3, contexto 3.3, DEC-005.
- RF-007. El sistema debe permitir al dueño de la plataforma aprobar una solicitud de negocio pendiente, cambiando su estado a aprobada, activando el negocio, asignando al solicitante el rol de Administrador, registrando fecha, hora y responsable, y enviando un mensaje de bienvenida por el bot. Origen: HU-002, DEC-E01, contexto 3.8.
- RF-008. El sistema debe permitir al dueño de la plataforma rechazar una solicitud de negocio pendiente exigiendo la captura obligatoria de un motivo de texto, cambiando su estado a rechazada, registrando fecha, hora, responsable y motivo, y notificando la decisión con su motivo al solicitante por el bot, habilitándolo para iniciar una nueva solicitud corregida. Origen: HU-002, DEC-001, contexto 3.8.
- RF-009. El sistema debe permitir a un usuario solicitar vinculación como domiciliario a un negocio activo únicamente mediante el acceso exclusivo de personal (enlace profundo, código QR o digitación del código de personal del negocio), exigiendo la aceptación previa de la autorización general de datos y del consentimiento específico de ubicación en tiempo real y conservación de recorrido durante 30 días, antes de transmitir su contacto nativo de Telegram. Origen: HU-003, DEC-E02, DEC-E20, DEC-E36, DEC-E38, DEC-E42, DEC-006, DEC-007, DEC-011, DEC-013, DEC-015.
- RF-010. El sistema debe verificar que el aspirante a domiciliario no posea una vinculación activa ni una solicitud pendiente como domiciliario en ningún negocio de la plataforma, y que haya otorgado ambos consentimientos requeridos; ante el incumplimiento de cualquiera de estas condiciones, el sistema debe denegar el registro e informar el motivo correspondiente. Origen: HU-003, DEC-E03, DEC-E38, DEC-013.
- RF-011. El sistema debe permitir a un usuario solicitar vinculación como empleado a un negocio activo únicamente mediante el acceso exclusivo de personal (enlace profundo, código QR o digitación del código de personal del negocio), exigiendo la aceptación previa de la autorización de tratamiento de datos personales antes de transmitir su contacto nativo de Telegram. Origen: HU-005, DEC-E02, DEC-E20, DEC-E36, DEC-E42, DEC-002, DEC-006, DEC-007, DEC-011, DEC-015.
- RF-012. El sistema debe validar que un aspirante a empleado o domiciliario no envíe solicitudes duplicadas si ya posee una solicitud pendiente o una vinculación activa en el mismo negocio para el mismo rol. Origen: HU-003, HU-005, DEC-002, contexto 3.7.
- RF-013. El sistema debe notificar al administrador del negocio por el bot cada vez que se registre una nueva solicitud de vinculación en su establecimiento, indicando el nombre del aspirante y el rol solicitado. Origen: HU-004, DEC-E25.
- RF-014. El sistema debe permitir al administrador del negocio consultar la lista de solicitudes de vinculación de personal pendientes pertenecientes exclusivamente a su propio establecimiento. Origen: HU-004, contexto 3.3.
- RF-015. El sistema debe permitir al administrador del negocio aprobar una solicitud de vinculación pendiente, otorgando al aspirante el rol solicitado en dicho negocio, registrando fecha, hora y responsable, y enviando una notificación de confirmación al usuario por el bot. Origen: HU-004, contexto 3.8.
- RF-016. El sistema debe permitir al administrador del negocio rechazar una solicitud de vinculación pendiente exigiendo la captura obligatoria de un motivo de texto, cambiando su estado a rechazada, registrando fecha, hora, responsable y motivo, notificando la decisión con su motivo al aspirante por el bot, y liberando de inmediato al domiciliario para postularse a otro negocio o reintentar. Origen: HU-004, DEC-003, DEC-004, contexto 3.8.
- RF-017. El sistema debe solicitar confirmación explícita antes de ejecutar la aprobación o rechazo de una solicitud de negocio o de vinculación de personal. Origen: contexto 3.7.
- RF-018. El sistema debe marcar automáticamente como expiradas las solicitudes de registro de negocio y de vinculación de personal que permanezcan en estado pendiente tras cumplirse el plazo exacto de 7 días (168 horas), registrando marca de tiempo y notificando al solicitante por el bot. Origen: DEC-E35, DEC-008, DEC-010.
- RF-019. El sistema debe permitir a un solicitante de negocio o aspirante a personal cancelar voluntariamente su solicitud mientras se encuentre en estado pendiente, cambiando su estado a cancelada y habilitándolo para iniciar un nuevo trámite. Origen: DEC-009.
- RF-020. El sistema debe mostrar el acceso de personal (enlace profundo, código QR y código de personal del negocio) únicamente al usuario con rol de Administrador del negocio, y debe rechazar cualquier intento de iniciar el flujo de vinculación de personal cuando el usuario ingrese mediante el acceso de clientes (enlace, QR o código para pedidos). Origen: DEC-E42, DEC-015, contexto 3.2, contexto 3.3.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización: cada operación de consulta, registro, aprobación y rechazo debe validar en la lógica de negocio la identidad del usuario en Telegram, su rol y la correspondencia al negocio gestionado. Se verifica con: inspección de código y pruebas automáticas simulando accesos con roles y usuarios no autorizados. Origen: contexto 3.2.
- RNF-002. Aislamiento de información por negocio: las consultas y gestiones de personal deben estar estrictamente restringidas a los datos del negocio del administrador solicitante. Se verifica con: pruebas automáticas de consulta cruzada entre diferentes identificadores de negocio. Origen: contexto 3.3.
- RNF-003. Concurrencia y atomicidad: las transiciones de estado de solicitudes y la asignación de roles deben ejecutarse de forma atómica evitando dobles aprobaciones, estados contradictorios o vinculaciones duplicadas concurrentes. Se verifica con: pruebas de concurrencia automatizadas con solicitudes simultáneas. Origen: contexto 3.8.
- RNF-004. Trazabilidad de auditoría y autorizaciones: cada cambio de estado debe registrar marca de tiempo, identificador del responsable y motivo en caso de rechazo. Todo consentimiento legal debe almacenar marca de tiempo, identificador de usuario y versión del documento aceptado. Se verifica con: inspección de registros en el almacén de datos tras cada transacción. Origen: contexto 3.8, DEC-E36, DEC-001, DEC-004, DEC-011.
- RNF-005. Protección de datos personales y minimización: el sistema debe almacenar únicamente el identificador numérico de Telegram, nombre de cuenta, teléfono verificado, correo de atención de datos del negocio y pruebas de autorización. La interfaz del dueño de la plataforma no debe exhibir teléfonos, direcciones, correos ni datos operativos. Se verifica con: auditoría de respuestas en las vistas del dueño de la plataforma e inspección de esquemas de almacenamiento. Origen: contexto 2.3, contexto 3.3, DEC-E37, DEC-006, DEC-012.

### 7. Reglas de negocio
- BR-001. Unicidad de nombre y correo de atención: no se permite registrar un negocio con el mismo nombre comercial exacto en la misma ciudad o municipio que otro negocio activo o pendiente. Todo negocio debe suministrar un correo electrónico válido para la atención de habeas data de sus clientes. Origen: DEC-005, DEC-014.
- BR-002. Consentimiento previo y verificación obligatoria: toda solicitud de registro o vinculación requiere la aceptación previa e informada del tratamiento de datos personales y la transmisión del teléfono verificado mediante el botón nativo de Telegram. El aspirante a domiciliario debe aceptar además el consentimiento específico de ubicación y conservación de recorrido por 30 días. No se aceptan teléfonos ingresados en texto libre ni postulaciones de domiciliarios sin autorización de ubicación. Origen: DEC-E20, DEC-E36, DEC-E38, DEC-006, DEC-011, DEC-013.
- BR-003. Asignación inmediata de rol administrador: la aprobación de un negocio por el dueño de la plataforma confiere inmediatamente el rol de Administrador al solicitante y habilita la operación del establecimiento. Origen: DEC-E01, HU-002.
- BR-004. Limitación de funciones del dueño de la plataforma: el dueño de la plataforma es Responsable del tratamiento respecto a negocios y personal, pero su facultad operativa se restringe a aprobar o rechazar establecimientos y gestionar el estado de suscripción; no puede acceder a clientes, pedidos ni detalles internos de ningún negocio. Origen: contexto 2.3, DEC-E37, HU-002, DEC-012.
- BR-005. Exclusividad del domiciliario: un usuario con vinculación activa o solicitud pendiente de domiciliario en cualquier negocio de la plataforma no puede enviar solicitudes a otro establecimiento. Si es rechazado, cancela su solicitud o esta expira, queda libre de inmediato para postularse a cualquier negocio. Origen: DEC-E03, DEC-003, HU-003.
- BR-006. Multi-negocio para empleados: un usuario puede estar vinculado como empleado en múltiples negocios, pero no puede tener más de una solicitud pendiente ni vinculación activa duplicada en un mismo establecimiento. Origen: DEC-E03, DEC-002, HU-005.
- BR-007. Motivo obligatorio de rechazo: todo rechazo de una solicitud de negocio por el dueño de la plataforma o de vinculación por el administrador requiere capturar un motivo de texto obligatorio que se transmite al solicitante por el bot. Origen: DEC-001, DEC-004.
- BR-008. Inmutabilidad de estados terminales: las solicitudes en estado aprobada, rechazada, cancelada o expirada son definitivas y no admiten cambios de estado posteriores. Origen: contexto 3.8, DEC-008, DEC-009, DEC-010.
- BR-009. Ciclo de vida de la solicitud de negocio: los estados válidos son pendiente, aprobada, rechazada, cancelada y expirada. Una persona cuya solicitud finalice en rechazada, cancelada o expirada queda habilitada para iniciar un nuevo trámite. Origen: DEC-E01, DEC-001, DEC-008, DEC-009, DEC-010.
- BR-010. Ciclo de vida de la solicitud de vinculación: los estados válidos son pendiente, aprobada, rechazada, cancelada y expirada. Origen: DEC-E02, DEC-004, DEC-008, DEC-009, DEC-010.
- BR-011. Expiración de solicitudes a los 7 días: toda solicitud de negocio o vinculación de personal que permanezca en estado pendiente durante 7 días continuos (168 horas) expira de forma automática y notifica al usuario por el bot. Origen: DEC-E35, DEC-008, DEC-010.
- BR-012. Retiro voluntario: el solicitante puede cancelar su trámite pendiente en cualquier momento antes de que sea resuelto, liberando su cuenta para iniciar una nueva postulación. Origen: DEC-009.
- BR-013. Accesos diferenciados de personal y clientes: cada negocio posee accesos independientes para clientes (pedidos) y para personal (enlace profundo, QR y código de personal). La visibilidad del acceso de personal está restringida únicamente al administrador del negocio. El flujo de vinculación de personal exige obligatoriamente el uso del acceso de personal; si se utiliza el acceso de clientes, el sistema rechaza la operación sin iniciar el trámite. Origen: DEC-E42, DEC-015.

### 8. Flujo principal
Flujo 1: Registro y aprobación de negocio
1. La persona ingresa al bot de Telegram y selecciona la opción de registrar un nuevo negocio.
2. El sistema presenta el aviso de privacidad de la plataforma para registro de negocio con el botón de aceptación.
3. La persona presiona el botón de aceptar el tratamiento de datos personales.
4. El sistema presenta el aviso de términos del servicio y acuerdo de transmisión de datos con su botón de aceptación.
5. La persona presiona el botón de aceptar términos y acuerdo de transmisión.
6. El sistema solicita el nombre comercial, ciudad o municipio, dirección y correo electrónico de atención de datos personales del negocio.
7. La persona envía la información comercial solicitada.
8. El sistema valida que el correo tenga formato válido y que no exista un negocio activo o pendiente con el mismo nombre comercial en dicha ciudad o municipio.
9. El sistema presenta el botón nativo de Telegram para compartir el contacto verificado.
10. La persona presiona el botón nativo y transmite su contacto.
11. El sistema valida que el contacto provenga del evento nativo de Telegram, registra las autorizaciones con fecha, hora y versión de textos, registra la solicitud de negocio en estado pendiente y envía un mensaje de confirmación al solicitante.
12. El dueño de la plataforma consulta la lista de solicitudes de negocio pendientes en el bot y visualiza el nombre comercial, ciudad o municipio y nombre de cuenta del solicitante.
13. El dueño de la plataforma selecciona la solicitud y presiona el comando de aprobación.
14. El sistema solicita confirmación antes de aplicar la decisión.
15. El dueño de la plataforma confirma la aprobación.
16. El sistema cambia el estado de la solicitud a aprobada, activa el negocio, asigna el rol de Administrador al solicitante y registra fecha, hora y responsable.
17. El sistema envía una notificación de bienvenida y confirmación al nuevo administrador por el bot, incluyendo los accesos exclusivos de personal de su negocio.

Flujo 2: Vinculación de personal (empleado o domiciliario)
1. El aspirante ingresa al bot mediante el acceso exclusivo de personal del negocio activo (enlace profundo, código QR o digitando el código de personal del negocio, el cual es visible únicamente para el administrador del establecimiento), y selecciona el rol deseado (empleado o domiciliario).
2. El sistema presenta el aviso de tratamiento de datos personales correspondiente al rol y su botón de aceptación.
3. Si el rol es domiciliario, el sistema presenta además el aviso de consentimiento de ubicación en tiempo real y almacenamiento de recorrido por 30 días con su botón de aceptación.
4. El aspirante presiona los botones de aceptación requeridos para su rol.
5. El sistema presenta el botón nativo de Telegram para compartir el contacto.
6. El aspirante presiona el botón nativo y transmite su contacto verificado.
7. El sistema valida la autenticidad del contacto, la vigencia de los consentimientos legales, que el acceso corresponda a personal del negocio, la no duplicidad de trámites en ese negocio y, si el rol es domiciliario, comprueba que el usuario no tenga vínculos activos ni pendientes en ningún otro negocio de la plataforma.
8. El sistema registra las autorizaciones otorgadas con fecha, hora y versión de textos, registra la solicitud de vinculación en estado pendiente, notifica al aspirante la confirmación de envío y envía un mensaje al administrador del negocio con el nombre del aspirante y rol solicitado.
9. El administrador del negocio consulta las solicitudes de personal pendientes de su establecimiento.
10. El administrador selecciona la solicitud y presiona aprobar.
11. El sistema solicita confirmación previa.
12. El administrador confirma la aprobación.
13. El sistema actualiza la solicitud a estado aprobada, asigna el rol correspondiente al usuario en el negocio y registra fecha, hora y responsable.
14. El sistema notifica la aprobación al aspirante por el bot.

### 9. Flujos alternativos y de excepción
- A1. Rechazo de solicitud de negocio por el dueño de la plataforma:
  - En el paso 13 del Flujo 1, el dueño de la plataforma selecciona la opción de rechazar.
  - El sistema solicita ingresar el motivo obligatorio de rechazo.
  - El dueño escribe el motivo y solicita confirmación.
  - El dueño confirma el rechazo.
  - El sistema marca la solicitud como rechazada, registra fecha, hora, responsable y motivo, y notifica la decisión con su motivo al solicitante por el bot, indicándole que puede iniciar un nuevo registro corrigiendo la información.
- A2. Rechazo de solicitud de vinculación por el administrador del negocio:
  - En el paso 10 del Flujo 2, el administrador selecciona rechazar.
  - El sistema solicita ingresar el motivo obligatorio de rechazo.
  - El administrador escribe el motivo y solicita confirmación.
  - El administrador confirma el rechazo.
  - El sistema marca la solicitud como rechazada, registra fecha, hora, responsable y motivo, envía la notificación con el motivo al aspirante por el bot y, si el rol era domiciliario, lo libera inmediatamente para postularse a otro negocio o reintentar.
- A3. Expiración automática de solicitud pendiente a los 7 días:
  - Una solicitud de negocio o vinculación cumple 7 días (168 horas) en estado pendiente sin ser resuelta.
  - El sistema actualiza automáticamente el estado de la solicitud a expirada y registra la marca de tiempo.
  - El sistema envía un mensaje por el bot al solicitante informando la expiración de la solicitud por vencimiento del plazo.
- A4. Cancelación o retiro voluntario de solicitud por el solicitante:
  - El solicitante consulta su trámite pendiente en el bot y selecciona la opción de cancelar solicitud.
  - El sistema solicita confirmación previa de cancelación.
  - El solicitante confirma el retiro.
  - El sistema cambia el estado a cancelada y habilita al usuario para iniciar una nueva solicitud.
- E1. Registro sin aceptar consentimientos legales obligatorios o sin contacto nativo:
  - En el paso 3 o 5 del Flujo 1 (o 4 del Flujo 2), el usuario rechaza los términos de datos, o intenta enviar un número telefónico en texto libre.
  - El sistema detecta la falta de aceptación expresa o la ausencia del evento oficial de contacto de Telegram.
  - El sistema detiene el proceso e informa que las autorizaciones y la verificación nativa son obligatorias para continuar.
- E2. Nombre de negocio duplicado en la misma ciudad:
  - En el paso 8 del Flujo 1, el sistema identifica que ya existe un negocio activo o pendiente con el mismo nombre comercial exacto en la misma ciudad o municipio.
  - El sistema rechaza el registro e informa al solicitante que debe seleccionar un nombre diferente o verificar la ciudad ingresada.
- E3. Postulación de domiciliario que incumple exclusividad:
  - En el paso 7 del Flujo 2, el sistema detecta que el aspirante a domiciliario ya posee una vinculación activa o trámite pendiente en otro negocio o en el mismo.
  - El sistema rechaza la postulación e informa que los domiciliarios solo pueden pertenecer a un único negocio.
- E4. Aspirante a domiciliario que rechaza el consentimiento de ubicación:
  - En el paso 4 del Flujo 2, el aspirante a domiciliario no acepta el aviso de uso de ubicación en tiempo real y conservación de recorrido.
  - El sistema bloquea el registro e informa que dicho consentimiento es condición indispensable para operar como domiciliario.
- E5. Postulación de empleado duplicada en el mismo negocio:
  - En el paso 7 del Flujo 2, el sistema detecta que el empleado ya posee una solicitud pendiente o una vinculación activa en ese mismo negocio.
  - El sistema bloquea el registro e informa que ya cuenta con un trámite vigente en dicho establecimiento.
- E6. Intento de acceso no autorizado a funciones de aprobación o consulta ajena:
  - Un usuario sin permisos de dueño de plataforma intenta aprobar negocios, o un empleado o domiciliario intenta consultar los accesos de personal o resolver solicitudes de personal.
  - El sistema deniega el acceso e informa la falta de autorización.
- E7. Intento de vinculación mediante acceso de clientes:
  - En el paso 1 del Flujo 2, un usuario intenta iniciar la vinculación de personal utilizando el enlace profundo, código QR o código de clientes del negocio.
  - El sistema detecta que se utilizó el acceso de clientes y no el de personal.
  - El sistema bloquea el ingreso al flujo de vinculación e informa que el acceso de clientes es exclusivo para realizar pedidos y no permite solicitar vinculación de personal.

### 10. Casos límite
- CL-001. Postulación simultánea como domiciliario a dos negocios distintos: si dos peticiones de un mismo usuario son enviadas concurrentemente, el sistema debe procesarlas de forma atómica garantizando que solo una quede en estado pendiente y la otra sea rechazada por existencia de trámite previo. Origen: contexto 3.8, DEC-E03, RNF-003.
- CL-002. Aprobación y rechazo simultáneos sobre la misma solicitud: dos peticiones concurrentes para resolver la misma solicitud deben manejarse de forma atómica; la primera determina el estado definitivo y la segunda es rechazada por haberse resuelto previamente. Origen: contexto 3.8, RNF-003.
- CL-003. Postulación a un negocio mediante código de clientes o código inexistente: el sistema verifica que el código o enlace corresponda al acceso de personal activo del establecimiento; si se usa el acceso de clientes o un código inexistente, emite un mensaje de error y no permite iniciar el trámite. Origen: DEC-E42, DEC-015, contexto 3.2.
- CL-004. Solicitante que intenta registrar un segundo negocio teniendo uno en trámite: el sistema bloquea la acción informando que debe aguardar la resolución de su solicitud pendiente o cancelarla. Origen: HU-001, BR-009, DEC-009.
- CL-005. Contacto compartido correspondiente a una cuenta distinta: el sistema valida que el identificador del usuario propietario del contacto compartido coincida con el identificador del usuario que interactúa en el bot. Origen: contexto 3.2, DEC-E20.
- CL-006. Nombre comercial idéntico con diferente puntuación o mayúsculas en la misma ciudad: el sistema normaliza la comparación de cadenas e impide el registro duplicado. Origen: DEC-005, BR-001.

### 11. Criterios de aceptación
- AC-001. Dado que una persona no tiene una solicitud activa ni pendiente en la plataforma, cuando presiona iniciar registro de negocio, acepta la política de datos personales, acepta los términos y acuerdo de transmisión, ingresa nombre comercial, ciudad o municipio, dirección, correo de atención de datos y comparte su contacto nativo de Telegram, entonces el sistema registra la solicitud en estado pendiente, guarda la prueba de autorización con fecha, hora y versión de textos, envía mensaje de confirmación al solicitante y no le otorga acceso a funciones operativas del negocio.
- AC-002. Dado que una persona rechaza el tratamiento de datos o envía el teléfono mediante texto libre sin el botón nativo, cuando el sistema evalúa la solicitud, entonces rechaza la operación e informa que el consentimiento previo y la verificación nativa son obligatorios.
- AC-003. Dado que existe un negocio activo o pendiente en la ciudad de Armenia llamado "Arepas del Eje", cuando otra persona intenta registrar un negocio con el nombre "Arepas del Eje" en Armenia, entonces el sistema rechaza la solicitud e informa la duplicidad de nombre comercial en la ciudad.
- AC-004. Dado que existen solicitudes de registro de negocio en estado pendiente, cuando el dueño de la plataforma consulta la lista de solicitudes, entonces el sistema presenta únicamente nombre comercial, ciudad o municipio y nombre de cuenta de Telegram de cada solicitante, sin mostrar teléfonos, direcciones, correos ni datos operativos.
- AC-005. Dado que el dueño de la plataforma evalúa una solicitud de negocio pendiente, cuando presiona aprobar y confirma la acción en el bot, entonces el sistema cambia el estado a aprobada, activa el negocio, asigna el rol de Administrador al solicitante, registra fecha, hora y responsable, y envía un mensaje de bienvenida y confirmación al nuevo administrador por el bot, incluyendo la visualización exclusiva de los accesos de personal de su negocio.
- AC-006. Dado que el dueño de la plataforma evalúa una solicitud de negocio pendiente, cuando presiona rechazar, ingresa un motivo obligatorio de texto y confirma la acción en el bot, entonces el sistema cambia el estado a rechazada, registra motivo, fecha, hora y responsable, notifica el rechazo con su motivo al solicitante por el bot y permite que la persona pueda iniciar una nueva solicitud corregida.
- AC-007. Dado que un usuario accede al bot mediante el acceso exclusivo de personal (enlace, QR o código de personal) de un negocio activo, no posee solicitudes ni vínculos de domiciliario en la plataforma, cuando acepta la autorización general de datos, acepta el consentimiento específico de ubicación y recorrido, selecciona el rol de domiciliario y transmite su contacto nativo, entonces el sistema registra la solicitud de vinculación como pendiente en dicho negocio, guarda las autorizaciones y notifica al aspirante y al administrador del establecimiento.
- AC-008. Dado que un usuario ya cuenta con una vinculación activa o una solicitud pendiente como domiciliario en algún negocio de la plataforma, cuando intenta enviar una solicitud de domiciliario a otro negocio, entonces el sistema rechaza la solicitud e informa la restricción de exclusividad de domiciliarios.
- AC-009. Dado que un aspirante a domiciliario rechaza el consentimiento de uso de ubicación en tiempo real y almacenamiento de recorrido por 30 días, cuando intenta postularse, entonces el sistema rechaza el trámite e informa que dicho consentimiento es obligatorio para vincularse como domiciliario.
- AC-010. Dado que un usuario accede al bot por el acceso exclusivo de personal (enlace, QR o código de personal) de un negocio activo, acepta el tratamiento de datos y elige el rol de empleado, cuando no posee trámites vigentes en ese negocio específico y comparte su contacto nativo, entonces el sistema registra la solicitud en estado pendiente, guarda la autorización y notifica al administrador del negocio.
- AC-011. Dado que un empleado ya posee una solicitud pendiente o una vinculación activa en el negocio X, cuando intenta enviar una nueva postulación como empleado al negocio X, entonces el sistema bloquea el registro informando la existencia de un trámite vigente en el mismo establecimiento.
- AC-012. Dado que existen solicitudes de vinculación pendientes para un negocio, cuando su administrador consulta la lista de aspirantes, entonces el sistema muestra únicamente las solicitudes correspondientes a su propio establecimiento, sin exponer registros de otros negocios.
- AC-013. Dado que el administrador de un negocio evalúa una solicitud de personal pendiente de su establecimiento, cuando presiona aprobar y confirma la acción, entonces el sistema cambia el estado a aprobada, asigna el rol al aspirante en dicho negocio, registra fecha, hora y responsable, y envía una notificación de aprobación al usuario por el bot.
- AC-014. Dado que el administrador de un negocio evalúa una solicitud de personal pendiente de su establecimiento, cuando presiona rechazar, ingresa un motivo obligatorio de texto y confirma la acción, entonces el sistema cambia el estado a rechazada registrando motivo, fecha, hora y responsable, notifica la decisión con el motivo al aspirante por el bot y, si era domiciliario, lo libera de inmediato para postularse a otro negocio o reintentar.
- AC-015. Dado que dos solicitudes de vinculación como domiciliario para negocios distintos son enviadas simultáneamente por el mismo usuario, cuando el sistema las procesa, entonces una sola solicitud se registra en estado pendiente y la otra es rechazada informando la existencia de un trámite previo en curso.
- AC-016. Dado que el sistema almacena información de usuarios y solicitudes, cuando se persiste un registro tras compartir el contacto verificado, entonces se guardan únicamente identificador numérico de Telegram, nombre de cuenta, teléfono verificado y el registro probatorio de las autorizaciones legales otorgadas.
- AC-017. Dado que una solicitud de negocio o vinculación de personal cumple 7 días (168 horas) en estado pendiente, cuando el sistema evalúa los trámites, entonces actualiza automáticamente el estado a expirada, registra marca de tiempo y envía una notificación al solicitante por el bot.
- AC-018. Dado que una persona posee una solicitud de negocio o de vinculación en estado pendiente, cuando selecciona la opción de cancelar trámite en el bot y confirma la acción, entonces el sistema cambia el estado a cancelada y la habilita para iniciar un nuevo proceso.
- AC-019. Dado que un usuario intenta iniciar la vinculación de personal (empleado o domiciliario) utilizando el enlace, código QR o código de clientes de un negocio, cuando el sistema evalúa el acceso, entonces rechaza la operación, no ingresa al flujo de vinculación de personal e informa que el acceso de clientes es exclusivo para pedidos.
- AC-020. Dado un negocio activo, cuando su administrador consulta la información del establecimiento, entonces el sistema le muestra únicamente a él los accesos de personal (enlace, QR y código de personal), impidiendo que empleados, domiciliarios o clientes puedan visualizarlos.

### 12. Dependencias
- Bot de Telegram e interfaz conversacional para la recepción de comandos, botones nativos de confirmación y eventos de contacto nativo.
- Documento de avisos de privacidad y consentimientos (docs/legal/avisos-de-privacidad.md, secciones 3.1 a 3.4) para los textos legales de las autorizaciones.
- Componente de persistencia y lógica de negocio para la gestión de identidades, autorizaciones legales, solicitudes, accesos diferenciados y establecimientos.

### 13. Restricciones
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar (contexto 4).
- Proyecto individual desarrollado bajo la metodología guiada por especificaciones SDD (contexto 4).
- Cada operación verifica en la lógica central el usuario, su rol, el negocio al que pertenece y sus permisos; nunca solo en el bot de Telegram (contexto 3.2).
- Separación estricta de la información por negocio: ningún usuario accede ni modifica datos de otro negocio (contexto 3.3).
- Protección de datos personales y acceso únicamente a la información autorizada por rol, cumpliendo con la Ley 1581 de 2012 y el Decreto 1377 de 2013 (contexto 3.3, contexto 6, DEC-E36).
- Los cambios de estado de solicitudes y vinculaciones son atómicos y registran fecha, estado y responsable (contexto 3.8).
- Las operaciones críticas de aprobación y rechazo requieren confirmación previa antes de su ejecución (contexto 3.7).
- Se prohíbe el uso de códigos de verificación por SMS; la validación de identidad y teléfono se realiza exclusivamente con el botón nativo de Telegram (contexto 3.11, DEC-E20).
- Plazo del proyecto de 8 semanas o más (contexto 4, contexto 3.11, DEC-E19).

### 14. Fuera de alcance
- Plataforma como central de repartidores unificada (contexto 5).
- Funcionalidades de marketplace o listado/directorio público de negocios registrados (contexto 5, contexto 3.11, DEC-E05).
- Cobro de comisiones por pedido, por entrega o pasarela de pagos en línea (contexto 2.1, contexto 5).
- Control de suscripciones y cobro periódico de mensualidad en línea (contexto 3.11, DEC-E26).
- Gestión operativa de pedidos, catálogo y zonas de cobertura.
- [mecanismo de persistencia de sesiones y tokens]: tema para arquitectura. Origen: RF-001, contexto 3.2.
- [control de concurrencia y aislamiento en base de datos para exclusividad de domiciliario]: tema para arquitectura. Origen: RF-010, CL-001.
- [modelo fisico de datos y esquemas relacionales o documentales]: tema para arquitectura. Origen: contexto 3.2.
- [mecanismo de ejecucion en segundo plano para expiracion automatica a los 7 dias]: tema para arquitectura. Origen: RF-018, DEC-E35, DEC-010.
- [servicio de almacenamiento y estructura de registro probatorio de autorizaciones legales]: tema para arquitectura. Origen: RF-004, DEC-E36, DEC-011.
- [generación y resolución de enlaces profundos y códigos QR diferenciados]: tema para arquitectura. Origen: RF-009, RF-011, RF-020, DEC-E42, DEC-015.

### 15. Preguntas abiertas
- OPEN-Q-001: Respondida (DEC-001).
- OPEN-Q-002: Respondida (DEC-002).
- OPEN-Q-003: Respondida (DEC-003).
- OPEN-Q-004: Respondida (DEC-004).
- OPEN-Q-005: Respondida (DEC-005).
- OPEN-Q-006: Respondida (DEC-006).
- OPEN-Q-007: Respondida (DEC-007).
- OPEN-Q-008: Respondida (DEC-008).
- OPEN-Q-009: Respondida (DEC-009).
- OPEN-Q-010: Respondida (DEC-010).

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-004, RF-005; BR-001, BR-002, BR-009, BR-012; AC-001, AC-002, AC-003; CL-004, CL-005, CL-006.
- HU-002: RF-006, RF-007, RF-008, RF-017; BR-003, BR-004, BR-007, BR-008, BR-009; AC-004, AC-005, AC-006; CL-002.
- HU-003: RF-009, RF-010, RF-012, RF-013, RF-020; BR-002, BR-005, BR-010, BR-013; AC-007, AC-008, AC-009, AC-015, AC-019; CL-001, CL-003.
- HU-004: RF-013, RF-014, RF-015, RF-016, RF-017, RF-020; BR-006, BR-007, BR-008, BR-010, BR-013; AC-012, AC-013, AC-014, AC-020.
- HU-005: RF-011, RF-012, RF-013, RF-020; BR-002, BR-006, BR-010, BR-013; AC-010, AC-011, AC-019.
- RF-001: Origen: HU-001, DEC-E01, DEC-E36, DEC-E39, DEC-006, DEC-011, DEC-014; verificado por AC-001.
- RF-002: Origen: contexto 3.2, DEC-E20, DEC-006, DEC-011; verificado por AC-002.
- RF-003: Origen: DEC-005, DEC-014, contexto 3.7; verificado por AC-003.
- RF-004: Origen: HU-001, DEC-E36, DEC-011; verificado por AC-001.
- RF-005: Origen: HU-001, DEC-001, DEC-008, DEC-009, DEC-010; verificado por AC-001, AC-006.
- RF-006: Origen: HU-002, contexto 2.3, contexto 3.3, DEC-005; verificado por AC-004.
- RF-007: Origen: HU-002, DEC-E01, contexto 3.8; verificado por AC-005.
- RF-008: Origen: HU-002, DEC-001, contexto 3.8; verificado por AC-006.
- RF-009: Origen: HU-003, DEC-E02, DEC-E20, DEC-E36, DEC-E38, DEC-E42, DEC-006, DEC-007, DEC-011, DEC-013, DEC-015; verificado por AC-007, AC-019.
- RF-010: Origen: HU-003, DEC-E03, DEC-E38, DEC-013; verificado por AC-008, AC-009, AC-015.
- RF-011: Origen: HU-005, DEC-E02, DEC-E20, DEC-E36, DEC-E42, DEC-002, DEC-006, DEC-007, DEC-011, DEC-015; verificado por AC-010, AC-019.
- RF-012: Origen: HU-003, HU-005, DEC-002, contexto 3.7; verificado por AC-011.
- RF-013: Origen: HU-004, DEC-E25; verificado por AC-007, AC-010.
- RF-014: Origen: HU-004, contexto 3.3; verificado por AC-012.
- RF-015: Origen: HU-004, contexto 3.8; verificado por AC-013.
- RF-016: Origen: HU-004, DEC-003, DEC-004, contexto 3.8; verificado por AC-014.
- RF-017: Origen: contexto 3.7; verificado por AC-005, AC-006, AC-013, AC-014.
- RF-018: Origen: DEC-E35, DEC-008, DEC-010; verificado por AC-017.
- RF-019: Origen: DEC-009; verificado por AC-018.
- RF-020: Origen: DEC-E42, DEC-015, contexto 3.2, contexto 3.3; verificado por AC-019, AC-020.
- RNF-001: Origen: contexto 3.2; verificado con pruebas de seguridad e inspección de código.
- RNF-002: Origen: contexto 3.3; verificado con pruebas automáticas de consulta cruzada.
- RNF-003: Origen: contexto 3.8; verificado con pruebas de concurrencia automatizadas con solicitudes simultáneas.
- RNF-004: Origen: contexto 3.8, DEC-E36, DEC-001, DEC-004, DEC-011; verificado con inspección de registros en el almacén de datos tras cada transacción.
- RNF-005: Origen: contexto 2.3, contexto 3.3, DEC-E37, DEC-006, DEC-012; verificado por AC-004, AC-016.
- BR-001: Origen: DEC-005, DEC-014; verificado por AC-003.
- BR-002: Origen: DEC-E20, DEC-E36, DEC-E38, DEC-006, DEC-011, DEC-013; verificado por AC-001, AC-002, AC-007, AC-009.
- BR-003: Origen: DEC-E01, HU-002; verificado por AC-005.
- BR-004: Origen: contexto 2.3, DEC-E37, HU-002, DEC-012; verificado por AC-004.
- BR-005: Origen: DEC-E03, DEC-003, HU-003; verificado por AC-008, AC-014, AC-015.
- BR-006: Origen: DEC-E03, DEC-002, HU-005; verificado por AC-010, AC-011, AC-012.
- BR-007: Origen: DEC-001, DEC-004; verificado por AC-006, AC-014.
- BR-008: Origen: contexto 3.8, DEC-008, DEC-009, DEC-010; verificado por AC-005, AC-006, AC-013, AC-014.
- BR-009: Origen: DEC-E01, DEC-001, DEC-008, DEC-009, DEC-010; verificado por AC-005, AC-006, AC-017, AC-018.
- BR-010: Origen: DEC-E02, DEC-004, DEC-008, DEC-009, DEC-010; verificado por AC-013, AC-014, AC-017, AC-018.
- BR-011: Origen: DEC-E35, DEC-008, DEC-010; verificado por AC-017.
- BR-012: Origen: DEC-009; verificado por AC-018.
- BR-013: Origen: DEC-E42, DEC-015; verificado por AC-019, AC-020.
- CL-001: Origen: contexto 3.8, DEC-E03, RNF-003; verificado por AC-015.
- CL-002: Origen: contexto 3.8, RNF-003; verificado por AC-005, AC-006.
- CL-003: Origen: DEC-E42, DEC-015, contexto 3.2; verificado por AC-007, AC-010, AC-019.
- CL-004: Origen: HU-001, BR-009, DEC-009; verificado por AC-001.
- CL-005: Origen: contexto 3.2, DEC-E20; verificado por AC-002.
- CL-006: Origen: DEC-005, BR-001; verificado por AC-003.

### 17. Historial de cambios
- Versión 0.1: creación inicial a partir de las historias HU-01, HU-02, HU-04, HU-05 y HU-09.
- Versión 0.2: incorporación de las respuestas del equipo (DEC-001 a DEC-009), incluyendo motivo obligatorio de rechazo, validación de nombre comercial por ciudad, aceptación previa de datos, soporte de QR/enlace/código de negocio, expiración automática y retiro voluntario.
- Versión 1.0: resolución de OPEN-Q-010 fijando expiración a los 7 días (DEC-010 / DEC-E35); incorporación de requisitos de protección de datos personales DEC-011 a DEC-014 (DEC-E36, DEC-E37, DEC-E38, DEC-E39), incluyendo consentimiento previo revocable, consentimiento específico de ubicación para domiciliarios, captura de correo de atención de datos del negocio y aceptación de términos y transmisión de datos, citando docs/legal/avisos-de-privacidad.md como dependencia; remoción de referencias técnicas de arquitectura en los requisitos trasladándolas a la sección 14; paso a estado Candidata.
- Versión 1.0 (aprobación): aprobada y congelada por el equipo, sin cambios de contenido.
- Versión 1.1: actualización por cambio solicitado (DEC-E42 / DEC-015). Se especifican los dos accesos diferenciados por negocio (personal vs clientes), la restricción de visualización del acceso de personal exclusivamente para el administrador del negocio, la prohibición de iniciar vinculación de personal desde el acceso de clientes y se actualizan HU-003, HU-004, HU-005, RF-009, RF-011, nuevo RF-020, BR-013, Flujo 2, Flujo de excepción E7, CL-003, AC-007, AC-010, nuevo AC-019 y nuevo AC-020; paso a estado Candidata.

## Verificación
- Completitud: cumple. Se realizaron todas las modificaciones asociadas a DEC-E42 y DEC-015, incorporando accesos diferenciados y restricciones sin dejar vacíos ni datos inferidos sin confirmar.
- Consistencia interna: cumple. Se compararon todos los RF con sus respectivas BR, pasos de flujos y AC, asegurando coincidencia exacta en las reglas de accesos diferenciados de personal y clientes.
- Consistencia con el contexto: cumple. Se verificaron las reglas contra las secciones 2.3, 3.2, 3.3, 3.7, 3.8, 3.11 (DEC-E01 a DEC-E42) y la sección 6 del contexto normativo.
- No ambigüedad: cumple. Todos los comportamientos observables están redactados sin términos vagos ni condicionales indefinidos.
- Verificabilidad: cumple. Cada criterio de aceptación está estructurado en formato Dado/Cuando/Entonces y es observable mediante pruebas de sistema.
- Cobertura de actores: cumple. Se definieron historias de usuario específicas para la Persona que solicita registro, Dueño de la plataforma, Administrador del negocio, Domiciliario y Empleado/vendedor sin consolidar actores.
- Cobertura de AC: cumple. Todos los RF, BR y CL disponen de al menos un criterio de aceptación asignado.
- Trazabilidad: cumple. La sección 16 contiene cada HU, RF, RNF, BR y CL con su origen y método o AC de verificación.
- No invención: cumple. Se respetaron taxativamente las decisiones DEC-E42 y DEC-015 y la solicitud del equipo, sin agregar supuestos.
- Delimitación: cumple. Los aspectos de implementación técnica como persistencia de sesiones, modelos de base de datos y la generación/resolución técnica de QR/enlaces se trasladaron a la sección 14 con el formato requerido.

## Siguiente paso
La SPEC-001 versión 1.1 está lista para revisión. Confirmen el objetivo y el alcance, las reglas de negocio, los criterios de aceptación críticos, las restricciones y lo que está fuera de alcance. Si la aprueban, queda congelada y lista para el Architecture Agent.
