# EPIC-001. Negocio, usuarios y acceso — Historias de usuario

Estado: Aprobada por Camila (2026-11-19)
Fecha: 2026-11-19

Origen y validación:
- Generadas por `generador-hu-invest` (agentes-ia/salidas/generador-hu-invest/HU-001_…md).
- Revisadas por `user-story-reviewer` (agentes-ia/salidas/user-story-reviewer/RHU-001_…md), que agregó HU-09.
- Correcciones elegidas por la estudiante y aplicadas por el asistente Claude Code sobre la revisión; aprobadas por Camila:
  1. HU-01: el rol pasa a «persona que quiere registrar su negocio»; al ser aprobada pasa a Administrador (DEC-E01).
  2. HU-05: nuevo criterio de aviso al administrador cuando llega una solicitud de unión (DEC-E25).
  3. Se reemplazó «el backend» por «el sistema» en todos los criterios: la validación en backend es una regla crítica del proyecto y se especifica en la SPEC, no en la historia.
  4. Se recuperaron la línea «Cómo se simula» y la tabla INVEST del generador; HU-09 queda sin autoevaluación.
  5. Revisión de conflictos (2026-11-19): HU-03 confirma y cancela pedidos al vencer el negocio (DEC-E26); HU-04 rechaza la unión a un segundo negocio (DEC-E03).
  6. Protección de datos (2026-11-19): HU-04 exige aceptar el aviso general y el consentimiento de ubicación (DEC-E36, DEC-E38).
---

### HU-01 — Solicitud de registro de negocio con contacto verificado

Como persona que quiere registrar su negocio,
quiero registrar mi establecimiento en el bot compartiendo mi contacto verificado de Telegram,
para solicitar la apertura de mi negocio en la plataforma y quedar a la espera de aprobación.

Nota: al ser aprobado (DEC-E01), el solicitante pasa a ser Administrador del negocio.

Está hecho cuando:
- Dado que una persona no tiene un establecimiento registrado ni pendiente, cuando confirma el envío de los datos comerciales básicos (nombre comercial y dirección) y comparte su contacto mediante el botón nativo de Telegram, entonces el sistema registra la solicitud en estado pendiente y notifica al solicitante la recepción de su trámite.
- Dado que la persona intenta registrar el establecimiento sin compartir su número a través del botón nativo de Telegram, cuando presiona enviar, entonces el sistema rechaza la solicitud e informa que la verificación del contacto es obligatoria.
- Dado que la solicitud del negocio se encuentra en estado pendiente de aprobación, cuando el solicitante intenta ejecutar acciones de configuración operativa o gestión de pedidos, entonces el sistema deniega el acceso informando que su establecimiento aún no ha sido aprobado por el dueño de la plataforma.

Cómo se simula en el prototipo: Se utiliza un evento simulado de contacto de Telegram en memoria para capturar el teléfono verificado ficticio `3001234567`.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-02 — Aprobación o rechazo de registro de negocio

Como Dueño de la plataforma,
quiero revisar las solicitudes de registro de negocios pendientes para aprobarlas o rechazarlas,
para controlar qué establecimientos están autorizados a operar en la plataforma sin acceder a su operación interna.

Está hecho cuando:
- Dado que existen negocios en estado pendiente de aprobación, cuando el dueño de la plataforma consulta la lista de solicitudes, entonces el sistema presenta únicamente el nombre del negocio y el nombre del solicitante de cada establecimiento pendiente, sin exponer pedidos ni datos operativos.
- Dado que se revisa una solicitud pendiente, cuando el dueño de la plataforma confirma su aprobación, entonces el sistema cambia el estado del negocio a activo, habilita al solicitante con el rol de Administrador del negocio y le envía una notificación de bienvenida a través del bot.
- Dado que se revisa una solicitud pendiente, cuando el dueño de la plataforma confirma el rechazo, entonces el sistema marca el negocio como rechazado y notifica la decisión al solicitante sin concederle permisos sobre el sistema.
- Dado que un usuario con rol de Administrador del negocio, Empleado o vendedor o Domiciliario intenta acceder a la opción de aprobar negocios, cuando ejecuta la acción, entonces el sistema deniega la operación por permisos insuficientes.

Cómo se simula en el prototipo: Se asocia un identificador de Telegram simulado con permisos de Dueño de la plataforma en las variables de configuración.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-03 — Control de estado de suscripción del negocio

Como Dueño de la plataforma,
quiero actualizar el estado de suscripción de un negocio entre al día y vencido,
para asegurar que solo los establecimientos con mensualidad activa puedan recibir pedidos.

Está hecho cuando:
- Dado un negocio con suscripción al día, cuando el dueño de la plataforma selecciona marcarlo como vencido, entonces el sistema le muestra cuántos pedidos no despachados se cancelarán y le pide confirmar (DEC-E26).
- Dado que el dueño de la plataforma confirma el cambio a vencido, cuando el sistema lo aplica, entonces el negocio deja de recibir pedidos nuevos, los pedidos no despachados quedan cancelados con motivo «suscripción vencida» y el dueño como responsable, se avisa a los clientes y al negocio, y los pedidos que van en camino siguen hasta terminar (DEC-E26, DEC-E13).
- Dado un negocio con suscripción en estado vencido, cuando el dueño de la plataforma selecciona marcarlo como al día y confirma la acción, entonces el sistema habilita nuevamente al establecimiento para recibir pedidos.
- Dado que un usuario con rol de Administrador del negocio o Empleado o vendedor intenta modificar el estado de suscripción de su establecimiento, cuando envía la solicitud, entonces el sistema rechaza la operación informando falta de autorización.

Cómo se simula en el prototipo: Se conmuta el valor de suscripción en una estructura de datos en memoria para el negocio ficticio `NEG-01`.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-04 — Solicitud de vinculación de domiciliario a un negocio

Como Domiciliario,
quiero solicitar mi unión a un negocio específico compartiendo mi contacto verificado de Telegram,
para postularme a realizar entregas para ese establecimiento.

Está hecho cuando:
- Dado que un domiciliario ingresa el código o enlace de un negocio activo, cuando confirma el envío de su solicitud de vinculación compartiendo su contacto mediante el botón nativo de Telegram, entonces el sistema registra su solicitud como pendiente en dicho establecimiento y le notifica que está en espera de aprobación.
- Dado que un domiciliario ya tiene una vinculación activa o una solicitud pendiente en un negocio, cuando intenta solicitar la unión a otro establecimiento, entonces el sistema rechaza la solicitud e informa que un domiciliario solo puede pertenecer a un negocio (DEC-E03).
- Dado que un domiciliario ya tiene una solicitud pendiente o activa en un negocio, cuando intenta enviar una nueva solicitud al mismo establecimiento, entonces el sistema le advierte que ya se encuentra registrado y no crea duplicados.
- Dado que un domiciliario intenta postularse sin usar el botón nativo de Telegram, cuando envía los datos, entonces el sistema rechaza la postulación exigiendo la verificación obligatoria del contacto.
- Dado que un domiciliario inicia su solicitud de unión, cuando el sistema le presenta el aviso de tratamiento de datos y el consentimiento específico de ubicación en tiempo real y recorrido, entonces solo puede continuar si acepta ambos; la aceptación queda registrada con fecha y versión del texto (DEC-E36, DEC-E38).

Cómo se simula en el prototipo: Se utiliza una cuenta de Telegram secundaria simulada que envía el comando de adhesión con el identificador de negocio ficticio `NEG-01`.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-05 — Gestión de solicitudes de vinculación de personal

Como Administrador del negocio,
quiero aprobar o rechazar las solicitudes de vinculación de empleados y domiciliarios,
para conformar el equipo de trabajo autorizado en mi establecimiento.

Está hecho cuando:
- Dado que existen solicitudes de vinculación pendientes, cuando el administrador del negocio consulta la lista de aspirantes, entonces el sistema muestra únicamente las solicitudes asociadas a su propio establecimiento, indicando el nombre y el rol solicitado (empleado o domiciliario).
- Dado que el administrador revisa una solicitud pendiente de su negocio, cuando confirma la aprobación, entonces el sistema activa la vinculación del solicitante en el rol respectivo, registra fecha y responsable, y le notifica la autorización a través del bot.
- Dado que el administrador revisa una solicitud pendiente de su negocio, cuando confirma el rechazo, entonces el sistema marca la solicitud como rechazada y el solicitante no obtiene acceso a la operación del negocio.
- Dado que un empleado o vendedor, o un domiciliario intenta acceder a la gestión de vinculación de personal, cuando ejecuta la acción, entonces el sistema deniega el acceso por permisos insuficientes.
- Dado que una persona envía una solicitud de unión al negocio, cuando la solicitud queda pendiente, entonces el sistema notifica al administrador por el bot con el nombre y el rol solicitado y un acceso directo para aprobarla o rechazarla (DEC-E25).

Cómo se simula en el prototipo: Se procesan solicitudes pendientes almacenadas en una lista simulada para el negocio del administrador autenticado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-06 — Configuración básica, horarios y enlace de acceso del negocio

Como Administrador del negocio,
quiero configurar los datos generales, los horarios de atención y consultar el enlace y código QR de mi establecimiento,
para definir las condiciones de servicio y permitir la llegada directa de mis clientes sin intermediarios ni directorios públicos.

Está hecho cuando:
- Dado que el administrador accede a la configuración de su establecimiento, cuando actualiza los datos comerciales (nombre, dirección y horarios de atención por día) y confirma los cambios, entonces el sistema valida y almacena la información para su negocio.
- Dado que el negocio está activo, cuando el administrador consulta los medios de difusión para clientes, entonces el sistema entrega el enlace directo y el código QR exclusivo del establecimiento para interactuar con el bot.
- Dado que un administrador intenta consultar o modificar la configuración de un establecimiento ajeno, cuando envía la solicitud, entonces el sistema bloquea la acción garantizando la separación estricta de datos entre negocios.

Cómo se simula en el prototipo: Se genera una URL profunda ficticia `https://t.me/DomiciliariosEjeBot?start=NEG01` y su representación en código QR simulado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-07 — Configuración del tope de pedidos simultáneos por domiciliario

Como Administrador del negocio,
quiero definir el número máximo de pedidos simultáneos asignables a un domiciliario en mi negocio,
para regular la carga de trabajo de los repartidores y la puntualidad del servicio.

Está hecho cuando:
- Dado que el administrador accede a los parámetros operativos de su negocio, cuando ingresa un número entero positivo (o conserva el valor por defecto de `[por definir con el equipo]`) y confirma la acción, entonces el sistema registra el tope de pedidos simultáneos para su establecimiento.
- Dado que el administrador ingresa un valor menor o igual a cero o un formato no numérico, cuando intenta guardar, entonces el sistema rechaza el valor e informa que debe ser un número entero positivo.
- Dado que un empleado o vendedor intenta modificar este parámetro, cuando intenta realizar el cambio, entonces el sistema rechaza la solicitud indicando que solo el administrador del negocio puede configurarlo.

Cómo se simula en el prototipo: Se actualiza el parámetro de capacidad operativa en la configuración en memoria del negocio evaluado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-08 — Parametrización de zonas de cobertura y tarifas de domicilio

Como Administrador del negocio,
quiero registrar y actualizar los barrios de cobertura con su tarifa de entrega,
para determinar dónde entrega mi establecimiento y cuánto se cobrará por cada envío.

Está hecho cuando:
- Dado que el administrador desea habilitar un sector, cuando ingresa el nombre del barrio y el valor de la tarifa de domicilio en pesos colombianos y confirma, entonces el sistema almacena la zona como activa para su negocio.
- Dado que un barrio ya existe en la cobertura del establecimiento, cuando el administrador modifica el valor de la tarifa y confirma, entonces el sistema actualiza el valor para los pedidos futuros de esa zona.
- Dado que el administrador decide suspender la entrega en un barrio, cuando cambia el estado de la zona a inactiva y confirma, entonces el sistema impide que se coticen nuevos domicilios para ese sector sin alterar el histórico de pedidos.
- Dado que un usuario intenta modificar las zonas o tarifas de otro establecimiento, cuando envía la petición, entonces el sistema bloquea la acción garantizando la separación de información por negocio.

Cómo se simula en el prototipo: Se administra un catálogo de barrios ficticios como "Centro", "Palogrande" y "Chipre" con tarifas fijadas en memoria para el negocio de prueba.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

### HU-09 — Solicitud de vinculación de empleado o vendedor a un negocio

Como Empleado o vendedor,
quiero solicitar mi vinculación a un negocio específico compartiendo mi contacto verificado de Telegram,
para integrarme al equipo de trabajo y coordinar pedidos en dicho establecimiento.

Está hecho cuando:
- Dado que un empleado o vendedor ingresa el enlace o código de un negocio activo, cuando confirma el envío de su solicitud de vinculación compartiendo su contacto mediante el botón nativo de Telegram, entonces el sistema registra la solicitud en estado pendiente para ese establecimiento y le notifica que se encuentra en espera de aprobación.
- Dado que un empleado o vendedor intenta enviar la solicitud sin compartir su contacto por el botón nativo de Telegram, cuando presiona enviar, entonces el sistema rechaza la solicitud e informa que la verificación de contacto es obligatoria.
- Dado que un empleado o vendedor ya tiene una solicitud pendiente o una vinculación activa en ese negocio, cuando intenta enviar una nueva solicitud al mismo establecimiento, entonces el sistema le advierte que ya tiene un trámite vigente y no genera registros duplicados.
- Dado que la solicitud de vinculación está pendiente o ha sido rechazada, cuando el empleado o vendedor intenta acceder a las funciones operativas del negocio, entonces el sistema deniega el acceso informando que no tiene una vinculación autorizada.

Cómo se simula en el prototipo: no definido (historia nueva del revisor).

Evaluación INVEST: pendiente (historia nueva del revisor; no autoevaluada).
