<!--
Agente: Generador de historias de usuario (INVEST)
Proveedor: gemini
Modelo: gemini-3.7-flash
Fecha: 2026-11-19 08:51
Petición: Épica EPIC-001: Negocio, usuarios y acceso. Cubre: registro del negocio por el bot y su aprobación por el dueño de la plataforma (DEC-E01), identificación con cuenta de Telegram y contacto compartido (DEC-E20), solicitud de unión de empleados y domiciliarios y su aprobación por el administrador (DEC-E02, DEC-E03), configuración del negocio (datos, horarios, enlace o QR propio, tope de pedidos por domiciliario), zonas de cobertura por barrio con su tarifa, y estado de suscripción (DEC-E26). Roles: dueño de la plataforma, administrador, empleado, domiciliario. Genera 8 historias empezando en HU-01.
-->

## Supuestos
- Se asume que el solicitante que registra un nuevo negocio asume el rol de Administrador del negocio en el momento en que dicho establecimiento es aprobado por el Dueño de la plataforma (según DEC-E01).
- Se asume que el proceso de solicitud de unión para un Empleado o vendedor sigue las mismas reglas de vinculación y aprobación que el Domiciliario (DEC-E02), especificando el rol deseado durante el registro.

## Historias de usuario

### HU-01 — Solicitud de registro de negocio con contacto verificado
Yo, como Administrador del negocio,
quiero registrar mi establecimiento en el bot compartiendo mi contacto verificado de Telegram,
para solicitar la apertura de mi negocio en la plataforma y quedar a la espera de aprobación.

Está hecho cuando:
- Dado que un usuario con cuenta de Telegram no tiene un negocio registrado ni pendiente, cuando envía los datos básicos del negocio (nombre comercial y dirección) y comparte su contacto mediante el botón nativo de Telegram, entonces el sistema registra la solicitud en estado pendiente y notifica al usuario la recepción de su trámite.
- Dado que el usuario intenta registrar el establecimiento sin compartir su número a través del botón nativo de Telegram, cuando presiona enviar, entonces el sistema rechaza la solicitud e informa que la verificación del contacto es obligatoria.
- Dado que la solicitud del negocio se encuentra en estado pendiente, cuando el usuario intenta ejecutar acciones de configuración operativa o gestión de pedidos, entonces el sistema le deniega el acceso informando que su establecimiento aún no ha sido aprobado.

Cómo se simula en el prototipo: Se utiliza un evento simulado de contacto de Telegram en memoria para capturar el teléfono verificado ficticio `3001234567`.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es independiente porque permite capturar la solicitud sin depender de la aprobación inmediata. No prescribe bases de datos ni esquemas internos. Es pequeña y comprobable mediante el flujo del bot.

---

### HU-02 — Aprobación o rechazo de registro de negocio
Yo, como Dueño de la plataforma,
quiero revisar las solicitudes de registro de negocios pendientes para aprobarlas o rechazarlas,
para controlar qué establecimientos están autorizados a operar en la plataforma.

Está hecho cuando:
- Dado que existen negocios en estado pendiente de aprobación, cuando el dueño de la plataforma consulta la lista de solicitudes, entonces el sistema presenta únicamente el nombre del negocio y el nombre del solicitante de cada solicitud pendiente.
- Dado que se revisa una solicitud pendiente, cuando el dueño de la plataforma confirma su aprobación, entonces el sistema cambia el negocio a estado activo, habilita al solicitante como Administrador del negocio y le envía una notificación de bienvenida al bot.
- Dado que se revisa una solicitud pendiente, cuando el dueño de la plataforma confirma el rechazo, entonces el sistema marca el negocio como rechazado y notifica la decisión al solicitante sin conceder permisos de administración.
- Dado que un usuario con rol de Administrador del negocio, Empleado o vendedor o Domiciliario intenta acceder a la opción de aprobar negocios, cuando ejecuta la acción, entonces el sistema deniega la operación por permisos insuficientes.

Cómo se simula en el prototipo: Se asocia un identificador de Telegram simulado con permisos de Dueño de la plataforma en las variables de configuración.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Entrega valor administrativo esencial para la gobernanza del sistema (DEC-E01). Cuenta con criterios objetivos de aceptación y validación estricta de autorización en backend.

---

### HU-03 — Control de estado de suscripción del negocio
Yo, como Dueño de la plataforma,
quiero actualizar el estado de suscripción de un negocio entre al día y vencido,
para asegurar que solo los negocios con mensualidad activa puedan recibir pedidos.

Está hecho cuando:
- Dado un negocio con suscripción al día, cuando el dueño de la plataforma selecciona marcarlo como vencido y confirma la acción, entonces el sistema actualiza el estado del negocio a vencido e impide inmediatamente el registro de nuevos pedidos para ese establecimiento.
- Dado un negocio con suscripción en estado vencido, cuando el dueño de la plataforma selecciona marcarlo como al día y confirma la acción, entonces el sistema habilita nuevamente al establecimiento para recibir pedidos.
- Dado que un usuario con rol de Administrador del negocio o Empleado o vendedor intenta modificar el estado de suscripción de su negocio, cuando envía la solicitud, entonces el sistema rechaza la operación informando falta de autorización.

Cómo se simula en el prototipo: Se conmuta el valor de suscripción en una estructura de datos en memoria para el negocio ficticio `NEG-01`.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple con DEC-E26 manteniendo fuera de alcance la pasarela de pagos en línea. Es concisa, estimable y con resultados verificables en el estado operativo del negocio.

---

### HU-04 — Solicitud de vinculación de domiciliario a un negocio
Yo, como Domiciliario,
quiero solicitar mi unión a un negocio específico compartiendo mi contacto verificado de Telegram,
para postularme a realizar entregas para ese establecimiento.

Está hecho cuando:
- Dado que un domiciliario ingresa el código o enlace de un negocio activo, cuando envía la solicitud de unión compartiendo su número mediante el botón nativo de Telegram, entonces el sistema registra su solicitud como pendiente en dicho negocio y le notifica que está en espera de aprobación.
- Dado que un domiciliario ya se encuentra vinculado a un negocio existente, cuando envía una solicitud de vinculación a un segundo negocio, entonces el sistema registra la nueva solicitud sin desvincularlo del negocio anterior.
- Dado que un domiciliario ya tiene una solicitud pendiente o activa en el mismo negocio, cuando intenta enviar una nueva solicitud al mismo establecimiento, entonces el sistema le advierte que ya se encuentra registrado y no crea duplicados.

Cómo se simula en el prototipo: Se utiliza una cuenta de Telegram secundaria simulada que envía el comando de adhesión con el identificador de negocio ficticio `NEG-01`.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Responde a DEC-E02, DEC-E03 y DEC-E20. Es independiente de la aprobación (HU-05) y comprueba la capacidad multinegocio del domiciliario sin cruce de información.

---

### HU-05 — Gestión de solicitudes de vinculación de personal
Yo, como Administrador del negocio,
quiero aprobar o rechazar las solicitudes de vinculación de empleados y domiciliarios,
para conformar el equipo de trabajo autorizado en mi establecimiento.

Está hecho cuando:
- Dado que existen solicitudes de vinculación pendientes, cuando el administrador del negocio consulta la bandeja de aspirantes, entonces el sistema muestra únicamente las solicitudes asociadas a su propio negocio, indicando el nombre y el rol solicitado (empleado o domiciliario).
- Dado que el administrador revisa una solicitud pendiente de su negocio, cuando confirma la aprobación, entonces el sistema activa la vinculación del usuario en el rol respectivo y le notifica al usuario por el bot.
- Dado que el administrador revisa una solicitud pendiente de su negocio, cuando confirma el rechazo, entonces el sistema marca la solicitud como rechazada y el usuario no obtiene acceso a la operación del negocio.
- Dado que un empleado o domiciliario intenta acceder a la gestión de vinculación de personal, cuando ejecuta la acción, entonces el sistema deniega el acceso por falta de permisos.

Cómo se simula en el prototipo: Se procesan solicitudes pendientes almacenadas en una lista simulada para el negocio del administrador autenticado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es valiosa y delimita claramente el aislamiento por negocio (3.3). Los criterios abordan los caminos de aprobación, rechazo y restricción de permisos para otros roles.

---

### HU-06 — Configuración básica, horarios y enlace de acceso del negocio
Yo, como Administrador del negocio,
quiero configurar los datos generales, los horarios de atención y consultar el enlace y código QR de mi establecimiento,
para definir las condiciones de servicio y permitir la llegada directa de mis clientes.

Está hecho cuando:
- Dado que el administrador accede al menú de configuración de su negocio, cuando actualiza los datos comerciales (nombre de atención, dirección y horarios por día de la semana) y confirma, entonces el sistema valida y almacena la nueva información para su establecimiento.
- Dado que el negocio está configurado, cuando el administrador solicita el medio de difusión para clientes, entonces el sistema genera y muestra un enlace directo y un código QR único que dirigen al bot con la identificación exclusiva de su negocio.
- Dado que un administrador intenta acceder a la configuración de un negocio ajeno, cuando ejecuta la solicitud, entonces el sistema deniega la acción y no revela información de otros establecimientos.

Cómo se simula en el prototipo: Se genera una URL profunda ficticia `https://t.me/DomiciliariosEjeBot?start=NEG01` y su representación en código QR simulado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cubre DEC-E05 y 3.4. Garantiza que el negocio cuente con su canal de entrada propio sin depender de directorios públicos o marketplaces.

---

### HU-07 — Configuración del tope de pedidos simultáneos por domiciliario
Yo, como Administrador del negocio,
quiero definir el número máximo de pedidos simultáneos asignables a un domiciliario en mi negocio,
para regular la carga de trabajo de los repartidores y la puntualidad del servicio.

Está hecho cuando:
- Dado que el administrador accede a los parámetros de despacho de su negocio, cuando ingresa un número entero positivo (o conserva el valor predeterminado de `[por definir con el equipo]`) y confirma la acción, entonces el sistema guarda el nuevo tope de pedidos simultáneos para su negocio.
- Dado que el administrador ingresa un valor menor o igual a cero o un formato no numérico, cuando intenta guardar, entonces el sistema rechaza el valor e informa que debe ser un número entero positivo.
- Dado que un empleado o vendedor intenta modificar este parámetro, cuando intenta realizar el cambio, entonces el sistema rechaza la solicitud indicando que solo el administrador puede configurarlo.

Cómo se simula en el prototipo: Se actualiza el parámetro de capacidad operativa en la configuración en memoria del negocio evaluado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Responde puntualmente a DEC-E12. Es sumamente pequeña, precisa y comprobable, facilitando la estimación y posterior verificación en el módulo de asignaciones.

---

### HU-08 — Parametrización de zonas de cobertura y tarifas de domicilio
Yo, como Administrador del negocio,
quiero registrar y actualizar los barrios de cobertura con su tarifa de entrega,
para determinar dónde entrega mi establecimiento y cuánto se cobrará por cada envío.

Está hecho cuando:
- Dado que el administrador desea habilitar un sector, cuando ingresa el nombre del barrio y el valor de la tarifa de domicilio en pesos colombianos y confirma, entonces el sistema almacena la zona como activa para su negocio.
- Dado que un barrio ya existe en la lista de cobertura del negocio, cuando el administrador modifica el valor de la tarifa y confirma, entonces el sistema actualiza el precio para las futuras órdenes de esa zona.
- Dado que el administrador decide retirar la cobertura de un barrio, cuando cambia el estado de la zona a inactiva y confirma, entonces el sistema impide que se coticen nuevos domicilios para ese sector sin borrar registros históricos.
- Dado que un usuario intenta modificar zonas pertenecientes a otro negocio, cuando envía la petición, entonces el sistema bloquea la acción asegurando la separación de datos entre establecimientos.

Cómo se simula en el prototipo: Se administra un catálogo de barrios ficticios como "Centro", "Palogrande" y "Chipre" con tarifas fijadas en memoria para el negocio de prueba.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple con 3.5 y DEC-E07. Establece la base tarifaria sin acoplarse aún a la selección del cliente en el pedido, permitiendo desarrollo y pruebas desacopladas.

## Resumen
| Historia | Rol | I | N | V | E | S | T | Puntaje |
|---|---|---|---|---|---|---|---|---|
| HU-01 | Administrador del negocio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-02 | Dueño de la plataforma | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-03 | Dueño de la plataforma | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-04 | Domiciliario | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-05 | Administrador del negocio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-06 | Administrador del negocio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-07 | Administrador del negocio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |
| HU-08 | Administrador del negocio | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/6 |

Observaciones para el equipo:
- Queda marcado como `[por definir con el equipo]` el tope numérico predeterminado de pedidos simultáneos por domiciliario en la HU-07 (Vacío conocido 1 / DEC-E12).
- Se recomienda priorizar en el primer sprint las historias HU-01, HU-02 y HU-06, ya que constituyen la base de identidad, enlace propio y tenencia requerida para operar el resto del bot.
- Se debe validar en la implementación técnica de Telegram que la captura del teléfono provenga estrictamente del objeto `contact` generado por el botón nativo para cumplir con DEC-E20 y evitar suplantaciones de número por texto manual.
