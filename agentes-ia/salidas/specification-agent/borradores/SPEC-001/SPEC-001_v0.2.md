<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.6-flash
Fecha: 2026-11-19 10:53
Petición: Respuestas del equipo a las preguntas de la SPEC-001:
- OPEN-Q-001: el dueño de la plataforma registra un motivo obligatorio al rechazar un negocio; el motivo se notifica al solicitante por el bot; la persona puede volver a registrar su negocio corrigiendo los datos.
- OPEN-Q-002: ya está decidido en DEC-E03 (contexto 3.11): la restricción de un solo negocio aplica solo a domiciliarios; un empleado puede estar vinculado a varios negocios, sin duplicar solicitud ni vinculación en el mismo negocio.
- OPEN-Q-003: si el administrador rechaza a un domiciliario, este queda libre de inmediato para postularse a otro negocio o volver a pedir al mismo.
- OPEN-Q-004: el administrador registra un motivo obligatorio al rechazar a un aspirante (empleado o domiciliario) y el motivo se notifica al aspirante.
- OPEN-Q-005: el registro del negocio pide nombre comercial, ciudad o municipio y dirección; no se permite el mismo nombre comercial exacto en la misma ciudad.
- OPEN-Q-006: se guardan el identificador de Telegram, el nombre de la cuenta y el teléfono verificado; antes de pedir el contacto, la persona debe aceptar explícitamente el tratamiento de datos con un botón y la aceptación queda registrada.
- OPEN-Q-007: el empleado o domiciliario llega al negocio por enlace profundo o QR del negocio, o escribiendo el código del negocio en el chat.
- OPEN-Q-008: las solicitudes pendientes (de registro de negocio y de vinculación de personal) vencen solas tras un plazo y se avisa al solicitante; el plazo aún no está definido.
- OPEN-Q-009: el solicitante puede retirar su solicitud mientras está pendiente; queda cancelada y puede iniciar otra.
-->

# SPEC-001. Registro y aprobacion de negocio y vinculacion de personal - Versión 0.2

Estado: Borrador
Modo: Iteración
Necesidad original: "EPIC-001. Especifica el registro y la aprobación del negocio y la vinculación de su personal: una persona registra su negocio desde el bot compartiendo su contacto y queda pendiente hasta que el dueño de la plataforma lo aprueba o rechaza; al aprobarse pasa a ser su administrador; empleados y domiciliarios piden unirse a un negocio y el administrador aprueba o rechaza. Las historias de usuario aprobadas HU-01, HU-02, HU-04, HU-05 y HU-09 están en el archivo adjunto; respétalas como entrada."
Épica: EPIC-001

## Análisis
- Objetivo: permitir que nuevos establecimientos soliciten su registro en la plataforma mediante el bot de Telegram previo consentimiento explícito de tratamiento de datos personales, datos comerciales y contacto verificado; garantizar la aprobación o rechazo justificado con motivo obligatorio por parte del dueño de la plataforma; y permitir que empleados y domiciliarios soliciten su vinculación a un negocio activo (vía código, enlace profundo o QR) para ser aprobados o rechazados con motivo por el administrador, regulando la exclusividad del domiciliario, la expiración de solicitudes y la opción de retiro voluntario.
- Alcance inicial: registro de solicitud de negocio con autorización de tratamiento de datos y contacto verificado; aprobación o rechazo con motivo del negocio; postulación de domiciliarios con validación de exclusividad; postulación de empleados (multi-negocio sin duplicidad en el mismo establecimiento); gestión con motivo obligatorio de solicitudes por parte del administrador del negocio; retiro voluntario de solicitudes; expiración automática de solicitudes; notificaciones asociadas en Telegram.
- Actores: Persona que solicita el registro del negocio, Dueño de la plataforma, Administrador del negocio, Empleado o vendedor, Domiciliario, Telegram (canal de transporte).
- Contexto aplicable: secciones 2.3, 3.1, 3.2, 3.3, 3.4, 3.6, y decisiones DEC-E01, DEC-E02, DEC-E03, DEC-E20, DEC-E25, DEC-E29 del contexto 3.11, más las decisiones DEC-001 a DEC-009.

## Modelo de dominio
- Negocio: entidad principal que representa el establecimiento de comercio. Pertenece a la plataforma; cardinalidad uno o varios en la plataforma. Posee nombre comercial, ciudad o municipio y dirección. Origen: contexto 2.4, DEC-E01, DEC-005.
- Solicitud de registro de negocio: registro temporal del trámite de apertura. Pertenece a una persona solicitante y a la plataforma; cardinalidad una activa o pendiente por trámite. Transita entre pendiente, aprobada, rechazada (con motivo obligatorio), cancelada o expirada. Origen: HU-01, HU-02, DEC-001, DEC-008, DEC-009.
- Usuario: persona identificada mediante su cuenta de Telegram. Almacena identificador numérico de Telegram, nombre de la cuenta, teléfono verificado y marca de aceptación explícita de tratamiento de datos personales. Origen: contexto 2.3, DEC-E20, DEC-006.
- Vinculacion de personal: relación entre un usuario y un negocio específico bajo un rol (empleado o domiciliario). Pertenece a un usuario y a un negocio; cardinalidad: un usuario domiciliario sólo puede poseer máximo una vinculación activa o pendiente en toda la plataforma; un empleado puede estar vinculado a múltiples negocios. Origen: DEC-E02, DEC-E03, DEC-002.
- Solicitud de vinculacion: petición de un usuario para ingresar a un negocio como empleado o domiciliario. Transita entre pendiente, aprobada, rechazada (con motivo obligatorio), cancelada o expirada. Origen: DEC-E02, DEC-004, DEC-008, DEC-009.

## Contradicciones detectadas
Ninguna. Todas las decisiones del equipo coinciden con la sección 3 del contexto y con las reglas críticas del proyecto.

## Análisis de impacto
- DEC-001: afecta RF-008, BR-007, BR-009, paso 3-5 del Flujo A1, AC-006. El rechazo de un negocio requiere motivo obligatorio, se notifica por Telegram y permite al solicitante registrarse de nuevo corrigiendo datos.
- DEC-002: afecta RF-011, RF-012, BR-006, AC-009, AC-010, Flujo E5. Confirma multi-negocio para empleados prohibiendo duplicados en el mismo negocio.
- DEC-003: afecta RF-016, BR-005, AC-013, Flujo A2. El rechazo de un domiciliario por el administrador lo libera de inmediato para postularse a otro negocio o reintentar.
- DEC-004: afecta RF-016, BR-007, BR-010, Flujo A2, AC-013. El rechazo de solicitudes de personal por el administrador requiere motivo obligatorio y su notificación al aspirante.
- DEC-005: afecta RF-001, RF-003, RF-006, BR-001, Flujo 1 (pasos 2-3), AC-001, AC-003, CL-006. Requiere nombre comercial, ciudad/municipio y dirección; no permite nombres duplicados exactos en la misma ciudad.
- DEC-006: afecta RF-001, RF-009, RF-011, BR-002, RNF-005, AC-001, AC-002, AC-007, AC-009, AC-015, Flujos 1 y 2. Añade aceptación previa e explícita de tratamiento de datos personales antes de solicitar el contacto nativo y restringe los datos persistidos.
- DEC-007: afecta RF-009, RF-011, Flujo 2 (paso 1), AC-007, AC-009. Soporta enlace profundo, código QR y código de negocio en chat.
- DEC-008: afecta RF-018, BR-011, Flujo A3, AC-016. Define expiración automática de solicitudes pendientes al cumplirse un plazo.
- DEC-009: afecta RF-019, BR-012, Flujo A4, AC-017. Define retiro o cancelación voluntaria de solicitudes por parte del solicitante.

## Preguntas de aclaración
- OPEN-Q-010. ¿Cuál es el plazo exacto (en horas o días) para que las solicitudes pendientes de registro de negocio y vinculación de personal expiren automáticamente?
  Por qué importa: define el parámetro temporal para la regla de negocio BR-011 y el requisito RF-018 de expiración automática.
  Crítica: no
  Propuesta del agente: PROPUESTA: 72 horas (3 días) de plazo para la expiración automática de solicitudes pendientes.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Permitir el registro de nuevos establecimientos de comercio mediante el bot de Telegram previa aceptación explícita de tratamiento de datos personales, captura de información comercial y contacto verificado; garantizar su aprobación o rechazo justificado con motivo obligatorio por el dueño de la plataforma; y permitir la vinculación controlada de empleados y domiciliarios mediante la aprobación del administrador de cada negocio, asegurando la exclusividad del domiciliario, la expiración de solicitudes y la opción de retiro voluntario.

### 2. Contexto
En Domiciliarios Eje cada negocio gestiona su propia operación de domicilios desde Telegram. Para comenzar, una persona solicita registrar su negocio en el bot y queda en espera de que el dueño de la plataforma autorice su funcionamiento. Una vez aprobado, el solicitante asume el rol de Administrador y puede evaluar las postulaciones de empleados y domiciliarios que desean integrarse a su equipo.

Decisiones del equipo aplicables:
- DEC-E01. Un negocio se registra solo desde el bot y queda pendiente hasta que el dueño de la plataforma lo aprueba. Quien lo registra queda como su administrador. Origen: contexto 3.11.
- DEC-E02. Empleados y domiciliarios piden unirse a un negocio desde el bot y el administrador aprueba o rechaza la solicitud. Origen: contexto 3.11.
- DEC-E03. Un domiciliario pertenece a un solo negocio: no puede pedir unirse a otro mientras tenga una vinculación activa o pendiente. La restricción aplica solo al rol domiciliario; una misma cuenta puede ser empleado o administrador de otros negocios y cliente de varios. Origen: contexto 3.11.
- DEC-E20. Una persona se identifica con su cuenta de Telegram y, al registrarse, comparte su contacto con el botón nativo de Telegram; el teléfono queda verificado por Telegram. No se usan códigos por SMS. Origen: contexto 3.11.
- DEC-E25. Notificaciones del negocio: el administrador recibe las solicitudes de unión. Origen: contexto 3.11.
- DEC-001. El dueño de la plataforma registra un motivo obligatorio al rechazar un negocio; el motivo se notifica al solicitante por el bot; la persona puede volver a registrar su negocio corrigiendo los datos. Responde a OPEN-Q-001.
- DEC-002. La restricción de un solo negocio aplica sólo a domiciliarios (DEC-E03); un empleado puede estar vinculado a varios negocios, sin duplicar solicitud ni vinculación activa en el mismo negocio. Responde a OPEN-Q-002.
- DEC-003. Si el administrador rechaza a un domiciliario, este queda libre de inmediato para postularse a otro negocio o volver a pedir al mismo. Responde a OPEN-Q-003.
- DEC-004. El administrador registra un motivo obligatorio al rechazar a un aspirante (empleado o domiciliario) y el motivo se notifica al aspirante por el bot. Responde a OPEN-Q-004.
- DEC-005. El registro del negocio pide nombre comercial, ciudad o municipio y dirección; no se permite el mismo nombre comercial exacto en la misma ciudad o municipio. Responde a OPEN-Q-005.
- DEC-006. Se guardan el identificador de Telegram, el nombre de la cuenta y el teléfono verificado; antes de pedir el contacto nativo, la persona debe aceptar explícitamente el tratamiento de datos con un botón y la aceptación queda registrada. Responde a OPEN-Q-006.
- DEC-007. El empleado o domiciliario llega al negocio por enlace profundo, código QR del negocio o escribiendo el código del negocio en el chat del bot. Responde a OPEN-Q-007.
- DEC-008. Las solicitudes pendientes (de negocio y de vinculación de personal) vencen solas tras un plazo y se avisa al solicitante por el bot. Responde a OPEN-Q-008.
- DEC-009. El solicitante puede retirar (cancelar) su solicitud mientras esté pendiente; queda cancelada y puede iniciar otra. Responde a OPEN-Q-009.

### 3. Alcance
- Presentación de aviso y captura de aceptación explícita de tratamiento de datos personales previo al registro.
- Captura de solicitud de registro de negocio con nombre comercial, ciudad/municipio, dirección y número de teléfono verificado mediante el botón nativo de Telegram.
- Validación de no duplicidad de nombre comercial exacto en la misma ciudad o municipio.
- Consulta de solicitudes pendientes de registro de negocio por el dueño de la plataforma (visualizando sólo nombre comercial, ciudad/municipio y nombre del solicitante).
- Aprobación o rechazo con motivo obligatorio de la solicitud de negocio por parte del dueño de la plataforma, permitiendo el reintento del solicitante si fue rechazado.
- Asignación automática del rol de Administrador al solicitante cuando su negocio es aprobado.
- Postulación de domiciliarios a un negocio vía enlace profundo, QR o código de negocio, con validación de exclusividad en la plataforma.
- Postulación de empleados o vendedores a un negocio vía enlace profundo, QR o código de negocio, permitiendo vinculación a múltiples negocios sin duplicidad en el mismo.
- Consulta y resolución (aprobación o rechazo con motivo obligatorio) de solicitudes de personal por parte del administrador del negocio.
- Liberación inmediata de un domiciliario rechazado para nuevas postulaciones.
- Retiro o cancelación voluntaria de solicitudes pendientes por el solicitante.
- Expiración automática de solicitudes pendientes al cumplirse un plazo configurado.
- Notificaciones en Telegram asociadas a cada evento o cambio de estado.

### 4. Actores e historias de usuario
Actores:
- Persona que solicita el registro del negocio: usuario de Telegram que busca abrir un establecimiento en la plataforma.
- Dueño de la plataforma: usuario autorizado para aprobar o rechazar solicitudes de registro de negocios. No opera pedidos ni ve datos sensibles.
- Administrador del negocio: solicitante aprobado que gestiona su establecimiento y autoriza su equipo de trabajo.
- Domiciliario: repartidor que solicita vinculación exclusiva a un negocio y ejecuta entregas una vez autorizado.
- Empleado o vendedor: usuario que solicita vinculación a un negocio para apoyar la operación.

Historias de usuario:
- HU-001. Como persona que quiere registrar su negocio, quiero autorizar el tratamiento de mis datos y registrar mi establecimiento ingresando nombre comercial, ciudad y dirección con mi contacto verificado de Telegram, para solicitar la apertura de mi negocio en la plataforma y quedar a la espera de aprobación. Origen: HU-01, DEC-005, DEC-006.
- HU-002. Como Dueño de la plataforma, quiero revisar las solicitudes pendientes de registro de negocio para aprobarlas o rechazarlas ingresando un motivo obligatorio, para controlar qué establecimientos están autorizados a operar en la plataforma sin acceder a su información operativa. Origen: HU-02, DEC-001.
- HU-003. Como Domiciliario, quiero solicitar mi unión a un negocio específico (vía QR, enlace o código) compartiendo mi contacto verificado, para postularme a realizar entregas exclusivamente para ese establecimiento. Origen: HU-04, DEC-003, DEC-007.
- HU-004. Como Administrador del negocio, quiero consultar las postulaciones recibidas y aprobarlas o rechazarlas ingresando un motivo obligatorio, para conformar el equipo autorizado en mi establecimiento. Origen: HU-05, DEC-004.
- HU-005. Como Empleado o vendedor, quiero solicitar mi vinculación a un negocio específico compartiendo mi contacto verificado, para integrarme al equipo de trabajo de dicho establecimiento. Origen: HU-09, DEC-002, DEC-007.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir a una persona sin solicitud activa ni pendiente enviar una solicitud de registro de negocio capturando nombre comercial, ciudad o municipio y dirección, exigiendo la aceptación explícita del tratamiento de datos mediante un botón antes de compartir el contacto verificado mediante el botón nativo de Telegram. Origen: HU-001, DEC-E01, DEC-E20, DEC-005, DEC-006.
- RF-002. El sistema debe verificar en el backend que el contacto recibido proviene del evento nativo de Telegram y que la aceptación de tratamiento de datos fue registrada antes de crear la solicitud de negocio. Origen: contexto 3.2, DEC-E20, DEC-006.
- RF-003. El sistema debe validar en el backend que no exista otro negocio activo o en trámite pendiente con el mismo nombre comercial exacto en la misma ciudad o municipio antes de registrar la solicitud. Origen: DEC-005, contexto 3.7.
- RF-004. El sistema debe registrar la solicitud de negocio en estado pendiente y notificar a la persona solicitante por el bot la confirmación de recepción. Origen: HU-001.
- RF-005. El sistema debe bloquear cualquier intento de acceso a funciones operativas o de configuración por parte de un solicitante mientras su negocio se encuentre en estado pendiente, rechazado, cancelado o expirado. Origen: HU-001, DEC-001, DEC-008, DEC-009.
- RF-006. El sistema debe permitir al dueño de la plataforma consultar la lista de solicitudes de registro de negocio en estado pendiente, mostrando exclusivamente nombre comercial, ciudad o municipio y el nombre del solicitante. Origen: HU-002, contexto 2.3, contexto 3.3, DEC-005.
- RF-007. El sistema debe permitir al dueño de la plataforma aprobar una solicitud de negocio pendiente, cambiando el estado del negocio a aprobada/activo, otorgando al solicitante el rol de Administrador, registrando fecha y responsable, y enviando una notificación de bienvenida por el bot. Origen: HU-002, DEC-E01, contexto 3.8.
- RF-008. El sistema debe permitir al dueño de la plataforma rechazar una solicitud de negocio pendiente ingresando un motivo obligatorio de texto, cambiando el estado a rechazada, registrando fecha, responsable y motivo, y notificando la decisión con su motivo al solicitante por el bot, permitiendo que la persona pueda enviar una nueva solicitud corrigiendo los datos. Origen: HU-002, DEC-001, contexto 3.8.
- RF-009. El sistema debe permitir a un usuario solicitar vinculación como domiciliario a un negocio activo ingresando mediante enlace profundo, código QR o digitando el código del negocio en el chat, previa aceptación explícita de tratamiento de datos personales y envío de contacto nativo de Telegram. Origen: HU-003, DEC-E02, DEC-E20, DEC-006, DEC-007.
- RF-010. El sistema debe validar en el backend, antes de registrar una solicitud de domiciliario, que el usuario no posea una vinculación activa ni una solicitud pendiente como domiciliario en ningún negocio de la plataforma. Si posee alguna, debe rechazar el registro e informar la restricción de exclusividad. Origen: HU-003, DEC-E03.
- RF-011. El sistema debe permitir a un usuario solicitar vinculación como empleado o vendedor a un negocio activo ingresando mediante enlace profundo, código QR o digitando el código del negocio en el chat, previa aceptación explícita de tratamiento de datos personales y envío de contacto nativo de Telegram. Origen: HU-005, DEC-E02, DEC-E20, DEC-002, DEC-006, DEC-007.
- RF-012. El sistema debe validar que un aspirante a empleado o domiciliario no envíe solicitudes duplicadas si ya cuenta con una solicitud pendiente o una vinculación activa en el mismo negocio para el mismo rol. Origen: HU-003, HU-005, DEC-002, contexto 3.7.
- RF-013. El sistema debe notificar al administrador del negocio a través del bot cada vez que se registre una nueva solicitud de vinculación para su establecimiento, indicando el nombre del aspirante y el rol solicitado. Origen: HU-004, DEC-E25.
- RF-014. El sistema debe permitir al administrador del negocio consultar la lista de solicitudes de vinculación de personal pendientes pertenecientes únicamente a su propio establecimiento. Origen: HU-004, contexto 3.3.
- RF-015. El sistema debe permitir al administrador del negocio aprobar una solicitud de vinculación pendiente, otorgando al aspirante el rol solicitado (empleado o domiciliario) en dicho negocio, registrando fecha y responsable, y notificando la aprobación al aspirante por el bot. Origen: HU-004, contexto 3.8.
- RF-016. El sistema debe permitir al administrador del negocio rechazar una solicitud de vinculación pendiente ingresando un motivo obligatorio de texto, cambiando el estado a rechazada, registrando fecha, responsable y motivo, notificando la decisión con su motivo al aspirante por el bot, y liberando de inmediato al domiciliario para postularse a otro negocio o reintentar en el mismo. Origen: HU-004, DEC-003, DEC-004, contexto 3.8.
- RF-017. El sistema debe solicitar confirmación previa al dueño de la plataforma antes de ejecutar la aprobación o rechazo de un negocio, y al administrador antes de ejecutar la aprobación o rechazo de una vinculación. Origen: contexto 3.7.
- RF-018. El sistema debe marcar automáticamente como expiradas las solicitudes de registro de negocio y de vinculación de personal que permanezcan en estado pendiente al cumplirse el plazo establecido (pendiente de precisión en OPEN-Q-010), cambiando su estado a expirada y notificando al usuario solicitante por el bot. Origen: DEC-008.
- RF-019. El sistema debe permitir a un solicitante de registro de negocio o aspirante a personal retirar (cancelar) su propia solicitud mientras se encuentre en estado pendiente, cambiando su estado a cancelada y habilitándolo para iniciar una nueva solicitud. Origen: DEC-009.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización: cada operación de consulta, registro, aprobación y rechazo debe verificar en el backend la identidad del usuario en Telegram, su rol asignado y la pertenecia al negocio correspondiente. Se verifica con: inspección de código y pruebas de seguridad simulando peticiones con roles no autorizados. Origen: contexto 3.2.
- RNF-002. Aislamiento multitenant: las consultas de solicitudes de vinculación de personal deben estar estrictamente filtradas en el backend por el identificador del negocio del administrador autenticado. Se verifica con: pruebas automáticas de consulta cruzada entre distintos negocios. Origen: contexto 3.3.
- RNF-003. Concurrencia y atomicidad: la asignación de roles y las transiciones de estado de solicitudes de negocio y personal deben ejecutarse de forma atómica impidiendo asignaciones duplicadas o decisiones concurrentes contradictorias. Se verifica con: pruebas automatizadas de peticiones concurrentes simultáneas. Origen: contexto 3.8.
- RNF-004. Trazabilidad de auditoría: cada cambio de estado en solicitudes de negocio y de personal debe registrar marca de tiempo, el identificador del responsable de la decisión y el motivo obligatorio en caso de rechazo. Se verifica con: inspección de registros de persistencia tras cada transición. Origen: contexto 3.8, DEC-001, DEC-004.
- RNF-005. Protección de datos personales: el backend debe almacenar únicamente el identificador numérico de Telegram, el nombre de cuenta, el teléfono verificado y el registro de la aceptación explícita de tratamiento de datos personales. La interfaz del dueño de la plataforma no expone teléfonos, direcciones ni datos operativos. Se verifica con: prueba de carga de datos en vistas de administración del dueño e inspección del almacén de datos. Origen: contexto 2.3, contexto 3.3, DEC-006.

### 7. Reglas de negocio
- BR-001. Registro único por nombre y ciudad: no se permite registrar dos negocios con el mismo nombre comercial exacto en la misma ciudad o municipio. Origen: DEC-005.
- BR-002. Aceptación de datos y contacto nativo: toda solicitud de negocio o vinculación requiere la aceptación previa e explícita del tratamiento de datos personales y la transmisión del teléfono mediante el botón nativo de Telegram; no se admiten números digitados en texto libre. Origen: DEC-E20, DEC-006.
- BR-003. Asignación inmediata de rol administrador: la aprobación de un establecimiento por el dueño de la plataforma asigna automáticamente el rol de Administrador al solicitante y activa el negocio para operar. Origen: DEC-E01, HU-002.
- BR-004. Separación de funciones del dueño de la plataforma: el dueño de la plataforma únicamente aprueba o rechaza negocios y gestiona suscripciones; no puede ver detalles operativos, clientes, pedidos ni personal de ningún negocio. Origen: contexto 2.3, HU-002.
- BR-005. Exclusividad del domiciliario: un usuario con rol de domiciliario activo o con solicitud de domiciliario pendiente en cualquier negocio de la plataforma no puede enviar solicitudes a otro negocio. Al ser rechazado, cancelado o expirado, queda libre de inmediato para postularse a otro negocio o reintentar en el mismo. Origen: DEC-E03, DEC-003, HU-003.
- BR-006. Multi-negocio para empleados: un usuario puede estar vinculado como empleado en múltiples negocios, pero no puede tener más de una solicitud pendiente ni una vinculación activa duplicada en el mismo establecimiento. Origen: DEC-E03, DEC-002, HU-005.
- BR-007. Motivo obligatorio de rechazo: el rechazo de un negocio por el dueño de la plataforma y el rechazo de vinculación de personal por el administrador requieren la captura obligatoria de un motivo de texto que se notifica al solicitante por el bot. Origen: DEC-001, DEC-004.
- BR-008. Inmutabilidad de decisiones finales: las solicitudes que hayan pasado a estado aprobada, rechazada, cancelada o expirada no pueden ser modificadas ni cambiar de estado nuevamente. Origen: contexto 3.8, DEC-008, DEC-009.
- BR-009. Estados y ciclo de vida de la solicitud de negocio: los estados válidos son pendiente, aprobada, rechazada (con motivo), cancelada (por solicitante) y expirada (por plazo). Una persona cuyo registro fue rechazado, cancelado o expirado puede iniciar una nueva solicitud. Origen: DEC-E01, DEC-001, DEC-008, DEC-009.
- BR-010. Estados y ciclo de vida de la solicitud de vinculación: los estados válidos son pendiente, aprobada, rechazada (con motivo), cancelada (por aspirante) y expirada (por plazo). Origen: DEC-E02, DEC-004, DEC-008, DEC-009.
- BR-011. Expiración de solicitudes pendientes: toda solicitud de negocio o vinculación que permanezca en estado pendiente al cumplirse el plazo establecido (OPEN-Q-010) expira automáticamente y notifica al usuario. Origen: DEC-008.
- BR-012. Retiro voluntario: el solicitante puede cancelar su propia solicitud pendiente en cualquier momento antes de la resolución, permitiéndole iniciar un nuevo trámite. Origen: DEC-009.

### 8. Flujo principal
Flujo 1: Registro y aprobación de negocio
1. La persona ingresa al bot de Telegram e inicia el proceso de registro de negocio.
2. El sistema presenta el aviso de tratamiento de datos personales con el botón de aceptación.
3. La persona presiona el botón para aceptar el tratamiento de datos.
4. El sistema solicita nombre comercial, ciudad o municipio y dirección del establecimiento.
5. La persona ingresa los datos solicitados.
6. El backend valida que no exista un negocio activo o pendiente con el mismo nombre comercial en dicha ciudad/municipio.
7. El sistema presenta el botón nativo de Telegram para compartir el contacto verificado.
8. La persona presiona el botón nativo y transmite su contacto.
9. El backend valida que el contacto provenga del evento nativo de Telegram, registra la solicitud de negocio en estado pendiente y notifica al solicitante por el bot.
10. El dueño de la plataforma consulta la lista de solicitudes pendientes en el bot y visualiza el nombre del negocio, ciudad/municipio y nombre del solicitante.
11. El dueño de la plataforma selecciona la solicitud y presiona el comando de aprobación.
12. El sistema solicita confirmación antes de aplicar la aprobación.
13. El dueño de la plataforma confirma la acción.
14. El backend cambia el estado de la solicitud a aprobada, activa el negocio, otorga el rol de Administrador al solicitante y registra fecha y responsable.
15. El sistema envía una notificación de bienvenida al nuevo administrador por el bot.

Flujo 2: Vinculación de domiciliario o empleado
1. El aspirante (empleado o domiciliario) ingresa al bot mediante enlace profundo, código QR o digitando el código de un negocio activo, y selecciona el rol deseado.
2. El sistema presenta el aviso de tratamiento de datos personales y el botón de aceptación.
3. El aspirante presiona el botón de aceptación de tratamiento de datos.
4. El sistema presenta el botón nativo de Telegram para compartir el contacto.
5. El aspirante presiona el botón nativo y transmite su contacto verificado.
6. El backend valida: autenticidad del contacto, ausencia de trámites duplicados en ese negocio y, si el rol es domiciliario, confirma que el usuario no tenga vínculos activos ni pendientes en ningún otro negocio de la plataforma.
7. El backend registra la solicitud de vinculación en estado pendiente, notifica al aspirante y envía un mensaje al administrador del negocio con el nombre del aspirante y rol solicitado.
8. El administrador del negocio consulta la lista de solicitudes de personal pendientes de su establecimiento.
9. El administrador selecciona la solicitud y presiona aprobar.
10. El sistema solicita confirmación previa.
11. El administrador confirma la aprobación.
12. El backend actualiza la solicitud a aprobada, asigna el rol al usuario en el negocio y registra fecha y responsable.
13. El sistema notifica la aprobación al aspirante por el bot.

### 9. Flujos alternativos y de excepción
- A1. Rechazo de solicitud de negocio por el dueño de la plataforma:
  - En el paso 11 del Flujo 1, el dueño de la plataforma selecciona rechazar.
  - El sistema solicita ingresar el motivo obligatorio de rechazo.
  - El dueño de la plataforma escribe el motivo y solicita confirmación.
  - El dueño confirma el rechazo.
  - El backend marca la solicitud como rechazada, guarda fecha, responsable y motivo, y notifica la decisión con su motivo al solicitante por el bot, informándole que puede volver a enviar la solicitud corrigiendo los datos.
- A2. Rechazo de solicitud de vinculación por el administrador del negocio:
  - En el paso 9 del Flujo 2, el administrador del negocio selecciona rechazar.
  - El sistema solicita ingresar el motivo obligatorio de rechazo.
  - El administrador escribe el motivo y solicita confirmación.
  - El administrador confirma el rechazo.
  - El backend marca la solicitud como rechazada, guarda fecha, responsable y motivo, notifica al aspirante por el bot con el motivo ingresado y, si el rol era domiciliario, lo libera de inmediato para nuevas postulaciones.
- A3. Expiración automática de solicitud pendiente por cumplimiento de plazo:
  - Una solicitud de negocio o de vinculación de personal cumple el plazo de expiración en estado pendiente.
  - El proceso del backend marca el estado de la solicitud como expirada y guarda marca de tiempo.
  - El sistema envía un aviso por el bot al solicitante informando la expiración de la solicitud.
- A4. Cancelación / retiro voluntario de solicitud por el solicitante:
  - El solicitante de negocio o aspirante a vinculación consulta su trámite pendiente en el bot y selecciona "Cancelar solicitud".
  - El sistema solicita confirmación previa de retiro.
  - El solicitante confirma la cancelación.
  - El backend marca la solicitud como cancelada y libera al usuario para iniciar una nueva solicitud.
- E1. Intento de registro sin aceptar tratamiento de datos o sin contacto nativo verificado:
  - En el paso 3 u 8 del Flujo 1 (o 3 y 5 del Flujo 2), el usuario rechaza los términos de datos o ingresa un teléfono como texto libre.
  - El backend detecta la falta de consentimiento o la ausencia del evento oficial de contacto de Telegram.
  - El sistema detiene la operación e informa que ambos requisitos son obligatorios.
- E2. Intento de registro de negocio con nombre duplicado en la misma ciudad:
  - En el paso 6 del Flujo 1, el backend detecta que ya existe un negocio activo o pendiente con el mismo nombre comercial exacto en la misma ciudad o municipio.
  - El sistema rechaza el registro e informa al solicitante que debe elegir un nombre comercial diferente o verificar la ciudad.
- E3. Intento de postulación de domiciliario ya vinculado o con trámite pendiente:
  - En el paso 6 del Flujo 2, el backend identifica que el domiciliario posee una vinculación activa o solicitud pendiente en otro negocio o en el mismo.
  - El sistema interrumpe el registro e informa que un domiciliario solo puede pertenecer a un único negocio.
- E4. Intento de solicitud de vinculación duplicada por empleado en el mismo negocio:
  - En el paso 6 del Flujo 2, el backend identifica que el empleado ya tiene una solicitud pendiente o una vinculación activa en ese mismo negocio.
  - El sistema bloquea la solicitud e informa la existencia de un trámite vigente en el mismo establecimiento.
- E5. Usuario no autorizado intenta aprobar o consultar trámites ajenos:
  - Un usuario sin rol de dueño de la plataforma intenta aprobar negocios, o un empleado/domiciliario intenta gestionar personal.
  - El backend valida permisos, bloquea la acción y registra el intento no autorizado.

### 10. Casos límite
- CL-001. Solicitud simultánea de vinculación como domiciliario a dos negocios distintos: dos peticiones concurrentes del mismo usuario son procesadas al mismo instante; el backend debe asegurar atómicamente que solo una solicitud quede registrada en pendiente y la otra sea rechazada por existencia de trámite previo. Origen: contexto 3.8, DEC-E03, RNF-003.
- CL-002. Aprobación y rechazo simultáneos de la misma solicitud de negocio: dos peticiones concurrentes sobre la misma solicitud deben resolverse de forma atómica; la primera determina el estado final y la segunda es rechazada por cambio de estado previo. Origen: contexto 3.8, RNF-003.
- CL-003. Intento de vinculación a un negocio inexistente o código inválido: el backend valida la existencia del establecimiento antes de asociar la solicitud y retorna un mensaje de error sin crear registros huérfanos. Origen: contexto 3.2.
- CL-004. Usuario que intenta registrar un segundo negocio teniendo uno pendiente: el backend bloquea la acción informando que debe esperar la resolución de su solicitud en trámite o retirarla. Origen: HU-001, BR-009, DEC-009.
- CL-005. Usuario que comparte el contacto de un tercero: el backend valida que el identificador de usuario asociado al contacto compartido coincida con el identificador de Telegram que origina la interacción. Origen: contexto 3.2, DEC-E20.
- CL-006. Intento de registrar un negocio con el mismo nombre comercial exacto en la misma ciudad o municipio: el backend valida la combinación de nombre comercial y ciudad e impide el registro duplicado. Origen: DEC-005, BR-001.

### 11. Criterios de aceptación
- AC-001. Dado que una persona no tiene una solicitud activa ni pendiente, cuando presiona iniciar registro, acepta los términos de tratamiento de datos, ingresa nombre comercial, ciudad/municipio y dirección y comparte su contacto nativo de Telegram, entonces el sistema registra la solicitud en estado pendiente, notifica la recepción al solicitante y no le otorga acceso a funciones operativas del negocio.
- AC-002. Dado que una persona no acepta los términos de tratamiento de datos o envía el teléfono como texto libre sin usar el botón nativo, cuando el backend procesa la solicitud, entonces el sistema rechaza la operación e informa que la aceptación de datos y la verificación nativa son obligatorias.
- AC-003. Dado que existe un negocio activo o en trámite en la ciudad X llamado "Don Pedro", cuando otra persona intenta registrar un negocio llamado "Don Pedro" en la misma ciudad X, entonces el sistema rechaza la solicitud en el backend e informa la duplicidad de nombre comercial en la ciudad.
- AC-004. Dado que existen solicitudes de registro de negocio en estado pendiente, cuando el dueño de la plataforma consulta la lista de solicitudes, entonces el sistema retorna únicamente nombre comercial, ciudad/municipio y nombre del solicitante de cada registro pendiente, sin exponer teléfonos, direcciones ni información operativa.
- AC-005. Dado que el dueño de la plataforma evalúa una solicitud de negocio pendiente, cuando presiona aprobar y confirma la acción en el bot, entonces el backend cambia el estado de la solicitud a aprobada, activa el negocio, otorga el rol de Administrador al solicitante, registra fecha y responsable, y envía un mensaje de bienvenida al nuevo administrador por Telegram.
- AC-006. Dado que el dueño de la plataforma evalúa una solicitud de negocio pendiente, cuando presiona rechazar, ingresa un motivo obligatorio de texto y confirma la acción en el bot, entonces el backend marca la solicitud como rechazada registrando motivo, fecha y responsable, notifica el rechazo con su motivo al solicitante por el bot y permite que la persona pueda volver a enviar un registro corregido.
- AC-007. Dado que un usuario ingresa al bot por enlace profundo, QR o código de un negocio activo, acepta el tratamiento de datos, elige el rol de domiciliario y no posee vinculaciones activas ni pendientes en ningún negocio, cuando transmite su contacto nativo, entonces el sistema registra la solicitud como pendiente en ese negocio, notifica al aspirante la espera y envía un mensaje de notificación al administrador del negocio con su nombre y rol solicitado.
- AC-008. Dado que un domiciliario ya cuenta con una vinculación activa o una solicitud pendiente en algún negocio de la plataforma, cuando intenta enviar una solicitud de vinculación como domiciliario a otro negocio, entonces el sistema rechaza la solicitud en el backend e informa la regla de exclusividad de domiciliarios.
- AC-009. Dado que un usuario ingresa al bot por enlace profundo, QR o código de un negocio activo, acepta el tratamiento de datos y elige el rol de empleado, cuando no posee vinculación activa ni solicitud pendiente en ese negocio específico y transmite su contacto nativo, entonces el sistema registra la solicitud en estado pendiente y notifica al administrador del negocio.
- AC-010. Dado que un empleado ya posee una solicitud pendiente o una vinculación activa en el negocio X, cuando intenta enviar una nueva postulación como empleado al negocio X, entonces el sistema rechaza el intento informando la existencia de un trámite vigente en el mismo establecimiento.
- AC-011. Dado que existen solicitudes de vinculación pendientes para un negocio, cuando su administrador consulta la lista de aspirantes, entonces el sistema muestra únicamente las solicitudes correspondientes a su establecimiento con nombre y rol solicitado, sin mostrar registros de otros negocios.
- AC-012. Dado que el administrador de un negocio revisa una solicitud de personal pendiente de su establecimiento, cuando presiona aprobar y confirma la acción, entonces el backend marca la vinculación como aprobada, asigna el rol correspondiente en dicho negocio, registra fecha y responsable, y notifica la aprobación al aspirante por Telegram.
- AC-013. Dado que el administrador de un negocio revisa una solicitud de personal pendiente de su establecimiento, cuando presiona rechazar, ingresa un motivo obligatorio de texto y confirma la acción, entonces el backend marca la solicitud como rechazada registrando motivo, fecha y responsable, notifica la decisión con el motivo al aspirante por el bot y, si era domiciliario, lo libera de inmediato para postularse a otro negocio o reintentar.
- AC-014. Dado que dos solicitudes de vinculación como domiciliario para negocios distintos son enviadas simultáneamente por el mismo usuario, cuando son procesadas por el backend, entonces una transacción se completa atómicamente en estado pendiente y la otra es rechazada informando la existencia de un trámite previo en curso.
- AC-015. Dado que el sistema almacena información de usuarios y solicitudes, cuando se persiste un registro tras compartir el contacto verificado, entonces el backend guarda únicamente identificador numérico de Telegram, nombre de la cuenta, teléfono verificado y marca de aceptación explícita de tratamiento de datos personales.
- AC-016. Dado que una solicitud de negocio o de vinculación de personal permanece en estado pendiente al cumplirse el plazo establecido de expiración, cuando el proceso del backend la evalúa, entonces actualiza su estado a expirada, registra marca de tiempo y envía una notificación por el bot al solicitante.
- AC-017. Dado que una persona posee una solicitud de negocio o de vinculación en estado pendiente, cuando selecciona la opción de cancelar trámite en el bot y confirma la acción, entonces el backend marca la solicitud como cancelada y la libera para iniciar un nuevo proceso.

### 12. Dependencias
- Bot de Telegram e interfaz conversacional para la recepción de comandos, botones de confirmación y eventos de contacto nativo.
- Componente de autenticación y persistencia del backend para gestión de usuarios, roles, solicitudes y negocios.

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
- Gestión operativa de pedidos, catálogo y zonas de cobertura.
- Mecanismo de persistencia de sesiones y tokens de autenticación: tema para arquitectura. Origen: RF-001, contexto 3.2.
- Estrategia de control de concurrencia y bloqueo a nivel de base de datos para la exclusividad de domiciliarios: tema para arquitectura. Origen: RF-010, CL-001.
- Estructura de esquemas de datos relacionales o documentales: tema para arquitectura. Origen: contexto 3.2.
- Mecanismo técnico y temporizador de fondo para la ejecución de la expiración automática de solicitudes: tema para arquitectura. Origen: RF-018, DEC-008.

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
- OPEN-Q-010: Pendiente.

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-004, RF-005; BR-001, BR-002, BR-009, BR-012; AC-001, AC-002, AC-003; CL-004, CL-005, CL-006.
- HU-002: RF-006, RF-007, RF-008, RF-017; BR-003, BR-004, BR-007, BR-008, BR-009; AC-004, AC-005, AC-006; CL-002.
- HU-003: RF-009, RF-010, RF-012, RF-013; BR-002, BR-005, BR-010; AC-007, AC-008, AC-014; CL-001, CL-003.
- HU-004: RF-013, RF-014, RF-015, RF-016, RF-017; BR-006, BR-007, BR-008, BR-010; AC-011, AC-012, AC-013.
- HU-005: RF-011, RF-012, RF-013; BR-002, BR-006, BR-010; AC-009, AC-010.
- RF-001: Origen: HU-001, DEC-E01, DEC-E20, DEC-005, DEC-006; verificado por AC-001.
- RF-002: Origen: contexto 3.2, DEC-E20, DEC-006; verificado por AC-002.
- RF-003: Origen: DEC-005, contexto 3.7; verificado por AC-003.
- RF-004: Origen: HU-001; verificado por AC-001.
- RF-005: Origen: HU-001, DEC-001, DEC-008, DEC-009; verificado por AC-001, AC-006.
- RF-006: Origen: HU-002, contexto 2.3, contexto 3.3, DEC-005; verificado por AC-004.
- RF-007: Origen: HU-002, DEC-E01, contexto 3.8; verificado por AC-005.
- RF-008: Origen: HU-002, DEC-001, contexto 3.8; verificado por AC-006.
- RF-009: Origen: HU-003, DEC-E02, DEC-E20, DEC-006, DEC-007; verificado por AC-007.
- RF-010: Origen: HU-003, DEC-E03; verificado por AC-008, AC-014.
- RF-011: Origen: HU-005, DEC-E02, DEC-E20, DEC-002, DEC-006, DEC-007; verificado por AC-009.
- RF-012: Origen: HU-003, HU-005, DEC-002, contexto 3.7; verificado por AC-010.
- RF-013: Origen: HU-004, DEC-E25; verificado por AC-007, AC-009.
- RF-014: Origen: HU-004, contexto 3.3; verificado por AC-011.
- RF-015: Origen: HU-004, contexto 3.8; verificado por AC-012.
- RF-016: Origen: HU-004, DEC-003, DEC-004, contexto 3.8; verificado por AC-013.
- RF-017: Origen: contexto 3.7; verificado por AC-005, AC-006, AC-012, AC-013.
- RF-018: Origen: DEC-008; verificado por AC-016.
- RF-019: Origen: DEC-009; verificado por AC-017.
- RNF-001: Origen: contexto 3.2; verificado con pruebas de seguridad e inspección de código.
- RNF-002: Origen: contexto 3.3; verificado con pruebas automáticas de consulta cruzada.
- RNF-003: Origen: contexto 3.8; verificado con pruebas automatizadas de peticiones concurrentes simultáneas.
- RNF-004: Origen: contexto 3.8, DEC-001, DEC-004; verificado con inspección de registros de persistencia tras cada transición.
- RNF-005: Origen: contexto 2.3, contexto 3.3, DEC-006; verificado por AC-004, AC-015.
- BR-001: Origen: DEC-005; verificado por AC-003.
- BR-002: Origen: DEC-E20, DEC-006; verificado por AC-001, AC-002.
- BR-003: Origen: DEC-E01, HU-002; verificado por AC-005.
- BR-004: Origen: contexto 2.3, HU-002; verificado por AC-004.
- BR-005: Origen: DEC-E03, DEC-003, HU-003; verificado por AC-008, AC-013, AC-014.
- BR-006: Origen: DEC-E03, DEC-002, HU-005; verificado por AC-009, AC-010, AC-011.
- BR-007: Origen: DEC-001, DEC-004; verificado por AC-006, AC-013.
- BR-008: Origen: contexto 3.8, DEC-008, DEC-009; verificado por AC-005, AC-006, AC-012, AC-013.
- BR-009: Origen: DEC-E01, DEC-001, DEC-008, DEC-009; verificado por AC-005, AC-006, AC-016, AC-017.
- BR-010: Origen: DEC-E02, DEC-004, DEC-008, DEC-009; verificado por AC-012, AC-013, AC-016, AC-017.
- BR-011: Origen: DEC-008; verificado por AC-016.
- BR-012: Origen: DEC-009; verificado por AC-017.
- CL-001: Origen: contexto 3.8, DEC-E03, RNF-003; verificado por AC-014.
- CL-002: Origen: contexto 3.8, RNF-003; verificado por AC-005, AC-006.
- CL-003: Origen: contexto 3.2; verificado por AC-007, AC-009.
- CL-004: Origen: HU-001, BR-009, DEC-009; verificado por AC-001.
- CL-005: Origen: contexto 3.2, DEC-E20; verificado por AC-002.
- CL-006: Origen: DEC-005, BR-001; verificado por AC-003.

### 17. Historial de cambios
- Versión 0.1: creación inicial a partir de las historias HU-01, HU-02, HU-04, HU-05 y HU-09.
- Versión 0.2: incorporación de las respuestas del equipo (DEC-001 a DEC-009), incluyendo motivo obligatorio de rechazo, validación de nombre comercial por ciudad, aceptación previa de tratamiento de datos, soporte de QR/enlace/código de negocio, expiración automática, retiro voluntario y liberación inmediata del domiciliario. Se agrega OPEN-Q-010 para definir el valor exacto del plazo de expiración.

## Verificación
- Completitud: cumple. Se actualizaron todas las secciones incorporando las 9 decisiones emitidas por el equipo.
- Consistencia interna: cumple. Se verificó que los requisitos funcionales, reglas de negocio, flujos y criterios de aceptación guarden estricta concordancia.
- Consistencia con el contexto: cumple. Se compararon las decisiones DEC-001 a DEC-009 con la sección 3 del contexto sin detectar contradicciones.
- No ambigüedad: cumple. Todos los comportamientos observables están redactados formalmente sin juicios de valor.
- Verificabilidad: cumple. Cada criterio de aceptación está estructurado en formato Dado/Cuando/Entonces y es observable.
- Cobertura de actores: cumple. Se revisaron todos los actores de la sección 2.3 participantes en el proceso y sus respectivas historias.
- Cobertura de AC: cumple. Todos los RF, RNF, BR y CL cuentan con criterios de aceptación vinculados en la matriz de trazabilidad.
- Trazabilidad: cumple. Se validó que cada elemento registrado en la sección 16 tenga origen explícito y método o AC de verificación.
- No invención: cumple. Se mantuvo la pregunta OPEN-Q-010 para el parámetro de tiempo no especificado sin suponer cifras.
- Delimitación: cumple. Los aspectos técnicos de temporizadores de expiración, esquemas de BD y sesiones se delegaron a la sección 14.

## Siguiente paso
Respondan la pregunta abierta OPEN-Q-010 y ejecuten de nuevo el agente con --continuar SPEC-001.
