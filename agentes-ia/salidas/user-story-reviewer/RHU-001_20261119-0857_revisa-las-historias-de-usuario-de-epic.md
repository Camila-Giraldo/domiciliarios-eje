<!--
Agente: Revisor de historias de usuario
Proveedor: gemini
Modelo: gemini-3.7-flash
Fecha: 2026-11-19 08:57
Petición: Revisa las historias de usuario de EPIC-001 (negocio, usuarios y acceso) adjuntas contra INVEST, el contexto del proyecto y las decisiones DEC-E01 a DEC-E26. Verifica también que cada actor con objetivo propio en esta épica tenga su historia.
-->

A continuación se presenta la revisión detallada de las historias de usuario de la épica **EPIC-001 (Negocio, usuarios y acceso)**.

---

## Historias revisadas

### HU-01 — Solicitud de registro de negocio con contacto verificado
**Estado:** corregida

Como Administrador del negocio,  
quiero registrar mi establecimiento en el bot compartiendo mi contacto verificado de Telegram,  
para solicitar la apertura de mi negocio en la plataforma y quedar a la espera de aprobación.

Está hecho cuando:
- Dado que un administrador del negocio no tiene un establecimiento registrado ni pendiente, cuando confirma el envío de los datos comerciales básicos (nombre comercial y dirección) y comparte su contacto mediante el botón nativo de Telegram, entonces el backend registra la solicitud en estado pendiente y notifica al solicitante la recepción de su trámite.
- Dado que el administrador del negocio intenta registrar el establecimiento sin compartir su número a través del botón nativo de Telegram, cuando presiona enviar, entonces el backend rechaza la solicitud e informa que la verificación del contacto es obligatoria.
- Dado que la solicitud del negocio se encuentra en estado pendiente de aprobación, cuando el solicitante intenta ejecutar acciones de configuración operativa o gestión de pedidos, entonces el backend deniega el acceso informando que su establecimiento aún no ha sido aprobado por el dueño de la plataforma.

---

### HU-02 — Aprobación o rechazo de registro de negocio
**Estado:** corregida

Como Dueño de la plataforma,  
quiero revisar las solicitudes de registro de negocios pendientes para aprobarlas o rechazarlas,  
para controlar qué establecimientos están autorizados a operar en la plataforma sin acceder a su operación interna.

Está hecho cuando:
- Dado que existen negocios en estado pendiente de aprobación, cuando el dueño de la plataforma consulta la lista de solicitudes, entonces el backend presenta únicamente el nombre del negocio y el nombre del solicitante de cada establecimiento pendiente, sin exponer pedidos ni datos operativos.
- Dado que se revisa una solicitud pendiente, cuando el dueño de la plataforma confirma su aprobación, entonces el backend cambia el estado del negocio a activo, habilita al solicitante con el rol de Administrador del negocio y le envía una notificación de bienvenida a través del bot.
- Dado que se revisa una solicitud pendiente, cuando el dueño de la plataforma confirma el rechazo, entonces el backend marca el negocio como rechazado y notifica la decisión al solicitante sin concederle permisos sobre el sistema.
- Dado que un usuario con rol de Administrador del negocio, Empleado o vendedor o Domiciliario intenta acceder a la opción de aprobar negocios, cuando ejecuta la acción, entonces el backend deniega la operación por permisos insuficientes.

---

### HU-03 — Control de estado de suscripción del negocio
**Estado:** corregida

Como Dueño de la plataforma,  
quiero actualizar el estado de suscripción de un negocio entre al día y vencido,  
para asegurar que solo los establecimientos con mensualidad activa puedan recibir pedidos.

Está hecho cuando:
- Dado un negocio con suscripción al día, cuando el dueño de la plataforma selecciona marcarlo como vencido y confirma la acción, entonces el backend actualiza el estado del negocio a vencido e impide inmediatamente el registro de nuevos pedidos para ese establecimiento.
- Dado un negocio con suscripción en estado vencido, cuando el dueño de la plataforma selecciona marcarlo como al día y confirma la acción, entonces el backend habilita nuevamente al establecimiento para recibir pedidos.
- Dado que un usuario con rol de Administrador del negocio o Empleado o vendedor intenta modificar el estado de suscripción de su establecimiento, cuando envía la solicitud, entonces el backend rechaza la operación informando falta de autorización.

---

### HU-04 — Solicitud de vinculación de domiciliario a un negocio
**Estado:** corregida

Como Domiciliario,  
quiero solicitar mi unión a un negocio específico compartiendo mi contacto verificado de Telegram,  
para postularme a realizar entregas para ese establecimiento.

Está hecho cuando:
- Dado que un domiciliario ingresa el código o enlace de un negocio activo, cuando confirma el envío de su solicitud de vinculación compartiendo su contacto mediante el botón nativo de Telegram, entonces el backend registra su solicitud como pendiente en dicho establecimiento y le notifica que está en espera de aprobación.
- Dado que un domiciliario ya se encuentra vinculado a un negocio activo, cuando confirma una solicitud de vinculación a un segundo establecimiento, entonces el backend registra la nueva solicitud sin desvincularlo del negocio anterior ni cruzar información entre ellos.
- Dado que un domiciliario ya tiene una solicitud pendiente o activa en un negocio, cuando intenta enviar una nueva solicitud al mismo establecimiento, entonces el backend le advierte que ya se encuentra registrado y no crea duplicados.
- Dado que un domiciliario intenta postularse sin usar el botón nativo de Telegram, cuando envía los datos, entonces el backend rechaza la postulación exigiendo la verificación obligatoria del contacto.

---

### HU-05 — Gestión de solicitudes de vinculación de personal
**Estado:** corregida

Como Administrador del negocio,  
quiero aprobar o rechazar las solicitudes de vinculación de empleados y domiciliarios,  
para conformar el equipo de trabajo autorizado en mi establecimiento.

Está hecho cuando:
- Dado que existen solicitudes de vinculación pendientes, cuando el administrador del negocio consulta la lista de aspirantes, entonces el backend muestra únicamente las solicitudes asociadas a su propio establecimiento, indicando el nombre y el rol solicitado (empleado o domiciliario).
- Dado que el administrador revisa una solicitud pendiente de su negocio, cuando confirma la aprobación, entonces el backend activa la vinculación del solicitante en el rol respectivo, registra fecha y responsable, y le notifica la autorización a través del bot.
- Dado que el administrador revisa una solicitud pendiente de su negocio, cuando confirma el rechazo, entonces el backend marca la solicitud como rechazada y el solicitante no obtiene acceso a la operación del negocio.
- Dado que un empleado o vendedor, o un domiciliario intenta acceder a la gestión de vinculación de personal, cuando ejecuta la acción, entonces el backend deniega el acceso por permisos insuficientes.

---

### HU-06 — Configuración básica, horarios y enlace de acceso del negocio
**Estado:** corregida

Como Administrador del negocio,  
quiero configurar los datos generales, los horarios de atención y consultar el enlace y código QR de mi establecimiento,  
para definir las condiciones de servicio y permitir la llegada directa de mis clientes sin intermediarios ni directorios públicos.

Está hecho cuando:
- Dado que el administrador accede a la configuración de su establecimiento, cuando actualiza los datos comerciales (nombre, dirección y horarios de atención por día) y confirma los cambios, entonces el backend valida y almacena la información para su negocio.
- Dado que el negocio está activo, cuando el administrador consulta los medios de difusión para clientes, entonces el backend entrega el enlace directo y el código QR exclusivo del establecimiento para interactuar con el bot.
- Dado que un administrador intenta consultar o modificar la configuración de un establecimiento ajeno, cuando envía la solicitud, entonces el backend bloquea la acción garantizando la separación estricta de datos entre negocios.

---

### HU-07 — Configuración del tope de pedidos simultáneos por domiciliario
**Estado:** corregida

Como Administrador del negocio,  
quiero definir el número máximo de pedidos simultáneos asignables a un domiciliario en mi negocio,  
para regular la carga de trabajo de los repartidores y la puntualidad del servicio.

Está hecho cuando:
- Dado que el administrador accede a los parámetros operativos de su negocio, cuando ingresa un número entero positivo (o conserva el valor por defecto de `[por definir con el equipo]`) y confirma la acción, entonces el backend registra el tope de pedidos simultáneos para su establecimiento.
- Dado que el administrador ingresa un valor menor o igual a cero o un formato no numérico, cuando intenta guardar, entonces el backend rechaza el valor e informa que debe ser un número entero positivo.
- Dado que un empleado o vendedor intenta modificar este parámetro, cuando intenta realizar el cambio, entonces el backend rechaza la solicitud indicando que solo el administrador del negocio puede configurarlo.

---

### HU-08 — Parametrización de zonas de cobertura y tarifas de domicilio
**Estado:** corregida

Como Administrador del negocio,  
quiero registrar y actualizar los barrios de cobertura con su tarifa de entrega,  
para determinar dónde entrega mi establecimiento y cuánto se cobrará por cada envío.

Está hecho cuando:
- Dado que el administrador desea habilitar un sector, cuando ingresa el nombre del barrio y el valor de la tarifa de domicilio en pesos colombianos y confirma, entonces el backend almacena la zona como activa para su negocio.
- Dado que un barrio ya existe en la cobertura del establecimiento, cuando el administrador modifica el valor de la tarifa y confirma, entonces el backend actualiza el valor para los pedidos futuros de esa zona.
- Dado que el administrador decide suspender la entrega en un barrio, cuando cambia el estado de la zona a inactiva y confirma, entonces el backend impide que se coticen nuevos domicilios para ese sector sin alterar el histórico de pedidos.
- Dado que un usuario intenta modificar las zonas o tarifas de otro establecimiento, cuando envía la petición, entonces el backend bloquea la acción garantizando la separación de información por negocio.

---

### HU-09 — Solicitud de vinculación de empleado o vendedor a un negocio
**Estado:** nueva (incorporada para cubrir al actor faltante según DEC-E02)

Como Empleado o vendedor,  
quiero solicitar mi vinculación a un negocio específico compartiendo mi contacto verificado de Telegram,  
para integrarme al equipo de trabajo y coordinar pedidos en dicho establecimiento.

Está hecho cuando:
- Dado que un empleado o vendedor ingresa el enlace o código de un negocio activo, cuando confirma el envío de su solicitud de vinculación compartiendo su contacto mediante el botón nativo de Telegram, entonces el backend registra la solicitud en estado pendiente para ese establecimiento y le notifica que se encuentra en espera de aprobación.
- Dado que un empleado o vendedor intenta enviar la solicitud sin compartir su contacto por el botón nativo de Telegram, cuando presiona enviar, entonces el backend rechaza la solicitud e informa que la verificación de contacto es obligatoria.
- Dado que un empleado o vendedor ya tiene una solicitud pendiente o una vinculación activa en ese negocio, cuando intenta enviar una nueva solicitud al mismo establecimiento, entonces el backend le advierte que ya tiene un trámite vigente y no genera registros duplicados.
- Dado que la solicitud de vinculación está pendiente o ha sido rechazada, cuando el empleado o vendedor intenta acceder a las funciones operativas del negocio, entonces el backend deniega el acceso informando que no tiene una vinculación autorizada.

---

## Resumen

- **Historias revisadas:** 8
- **Historias corregidas:** 8 (HU-01 a HU-08)
- **Historias eliminadas:** 0
- **Historias pendientes:** 0
- **Historias nuevas agregadas:** 1 (HU-09)

### Hallazgo sobre los actores de la épica
Al revisar los actores con objetivo propio en EPIC-001 (DEC-E01 a DEC-E26, contexto 2.3), se identificó que el actor **Empleado o vendedor** no tenía su propia historia de usuario para postularse o solicitar unirse a un negocio (DEC-E02). En el archivo original, la HU-04 cubría únicamente al **Domiciliario**, dejando por fuera el flujo de ingreso del empleado. Por tal razón, se redactó e integró la **HU-09**, asegurando cobertura completa de actores.

### Correcciones principales
1. **Formato INVEST y redacción:** Se retiró la fórmula inicial «Yo, como» para dejar estrictamente la estructura estándar «Como [rol], quiero [objetivo], para [beneficio]».
2. **Eliminación de términos genéricos:** Se reemplazó el término genérico «el usuario» en los criterios de aceptación por los roles exactos definidos en la sección 2.3 del contexto (`Administrador del negocio`, `Empleado o vendedor`, `Domiciliario`, `Dueño de la plataforma`).
3. **Validación en backend y confirmaciones:** Se especificó en los criterios que las validaciones de identidad, roles, permisos y aislamiento multi-inquilino ocurren en el backend (contexto 3.2 y 3.3), y se incorporó el paso explícito de confirmación antes de registrar o modificar datos sensibles (contexto 3.7).
4. **Respeto a decisiones y vacíos:** Se mantuvo el marcador `[por definir con el equipo]` en la HU-07 para el tope por defecto de pedidos simultáneos (Vacío conocido 1 / DEC-E12), sin inventar cifras.
