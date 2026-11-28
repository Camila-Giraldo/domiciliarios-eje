<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-21 15:36
Petición: Cambio solicitado por el equipo sobre la SPEC-002 (Candidata v1.1): DEC-E57 (contexto 3.11) define que las formas de pago tienen un tipo fijo de la plataforma (efectivo, transferencia o datáfono); el administrador elige cuáles acepta y puede darles un nombre propio (por ejemplo, «Nequi» de tipo transferencia); toda forma cuyo tipo no sea transferencia se cobra al entregar. Precisa RF-020 y BR-010 con esa lista, haz el análisis de impacto y entrega la versión 1.2 en estado Candidata.
-->

# SPEC-002. Configuración operativa del negocio y suscripción - Versión 1.2

Estado: Candidata
Modo: Cambio
Necesidad original: "EPIC-001. Especifica la configuración operativa de un negocio approved: el administrador configura los datos del negocio y sus horarios de atención por día, obtiene el enlace, el QR y el código propios del negocio (para clientes y personal), define el tope de pedidos simultáneos por domiciliario y administra los barrios de cobertura con su tarifa; además, el dueño de la plataforma marca la suscripción del negocio al día o vencida, con la cancelación de pedidos no despachados al vencer (DEC-E26). Las historias de usuario aprobadas HU-03, HU-06, HU-07 y HU-08 están en el archivo adjunto; respétalas como entrada. La SPEC-001 aprobada (registro y vinculación) es una dependencia."
Épica: EPIC-001

## Análisis
- Objetivo: permitir que el administrador configure los datos operativos, horarios de atención, formas de pago aceptadas (con tipo fijo de la plataforma, nombre personalizado y condición de cobro al entregar), valor mínimo de compra, enlace/QR/código de acceso, capacidad operativa de domiciliarios y zonas tarifarias de un negocio aprobado, y que el dueño de la plataforma controle la suscripción del negocio y su impacto en pedidos no despachados.
- Alcance inicial: configuración comercial, horarios de atención por día, formas de pago aceptadas asociadas a tipos fijos de la plataforma (efectivo, transferencia o datáfono) con nombres personalizados y determinación de cobro al entregar para tipos no transferencia, monto mínimo de compra, generación y consulta de enlace/QR/código propio del negocio, parametrización del tope de pedidos por domiciliario, gestión de barrios y tarifas de cobertura, y conmutación de estado de suscripción con cancelación atómica de pedidos no despachados.
- Actores: Administrador del negocio, Dueño de la plataforma, Empleado o vendedor (como actor de control de acceso negativo).
- Contexto aplicable: secciones 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8 y decisiones DEC-E01, DEC-E05, DEC-E07, DEC-E09, DEC-E12, DEC-E13, DEC-E26, DEC-E40, DEC-E41, DEC-E42, DEC-E43, DEC-E44, DEC-E51, DEC-E53, DEC-E57.

## Modelo de dominio
- Negocio: entidad principal aprobada previamente; pertenece a la plataforma y contiene su propia configuración operativa. Origen: contexto 2.4 y DEC-E01.
- Configuración de negocio: pertenece al negocio; cardinalidad uno a uno; almacena nombre comercial, dirección física, horarios de atención, formas de pago aceptadas (asociadas a tipo fijo de plataforma, nombre personalizado y cobro al entregar), valor mínimo de compra y tope de pedidos simultáneos. Origen: contexto 3.4, DEC-E40, DEC-E41, DEC-E51, DEC-E53, DEC-E57 y HU-06, HU-07.
- Horario de atención: pertenece al negocio; cardinalidad un rango HH:MM a HH:MM o cerrado por cada día de la semana. Origen: contexto 3.4, DEC-E41 y HU-06.
- Medio de acceso: pertenece al negocio; cardinalidad dos accesos distintos generados automáticamente al aprobar el negocio: uno para clientes (enlace, QR y código) y otro para personal (enlace, QR y código). Origen: DEC-E05, DEC-E42 y HU-06.
- Zona de cobertura (barrio y tarifa): pertenece al negocio; cardinalidad de una a varias zonas con tarifa de $0 a $50.000 COP y nombres no repetidos dentro del mismo negocio. Origen: contexto 3.5, DEC-E43 y HU-08.
- Suscripción: estado comercial del negocio controlado por la plataforma; cardinalidad uno a uno por negocio; valores al día o vencido. Origen: DEC-E26, DEC-E41 y HU-03.
- Pedido: pertenece al negocio; cardinalidad de cero a muchos por negocio; transiciona a cancelado con motivo suscripción vencida y responsable dueño de la plataforma si no está despachado al vencer la suscripción. Origen: DEC-E13, DEC-E21, DEC-E26.

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
- DEC-E40: afecta RF-005, RF-006, BR-006, AC-005, AC-017 y CL-004. Todos actualizados previamente.
- DEC-E41: afecta RF-002, BR-009, AC-018 y CL-006. Todos actualizados previamente.
- DEC-E26: afecta RF-015, RF-016, BR-004, AC-012, AC-013 y CL-001. Todos actualizados previamente.
- DEC-E42: afecta RF-003, BR-009, AC-004. Todos actualizados previamente.
- DEC-E43: afecta RF-009, BR-008, AC-007, CL-005. Todos actualizados previamente.
- DEC-E44: afecta RF-005, BR-006, CL-004 y AC-005. Todos actualizados previamente.
- DEC-E51: afecta Configuración de negocio en Modelo de dominio, Alcance, HU-001, RF-020, BR-010, pasos 3 y 4 del flujo principal, E7, CL-008 y AC-019. Todos actualizados previamente.
- DEC-E53: afecta Configuración de negocio en Modelo de dominio, Alcance, HU-001, RF-021, BR-011, pasos 3 y 4 del flujo principal, E8, CL-007, AC-020 y AC-021. Todos actualizados previamente.
- DEC-E57: afecta Configuración de negocio en Modelo de dominio, Alcance (sección 3), Decisiones del equipo (sección 2), RF-020, BR-010, pasos 3 y 4 del flujo principal, CL-008 y AC-019. Todos actualizados para explicitar los tres tipos fijos de la plataforma (efectivo, transferencia, datáfono), la capacidad de darle un nombre personalizado y la regla por la cual toda forma de pago cuyo tipo no sea transferencia se registra y marca para cobro al entregar.

## Preguntas de aclaración
- OPEN-Q-001. ¿Cuál es el valor por defecto del tope de pedidos simultáneos por domiciliario si el administrador no lo define, y existe un límite máximo configurable (Contexto 7.1 y HU-07)?
  Por qué importa: define el valor inicial del sistema, la validación de entrada en la interfaz y los criterios de aceptación de HU-07.
  Crítica: sí
  Estado: Respondida (DEC-E40)
  Responsable: equipo
- OPEN-Q-002. Para los horarios de atención por día (HU-06 y DEC-E09), ¿cómo se estructuran los rangos de operación y qué ocurre con los días de descanso?
  Por qué importa: define el formato de almacenamiento y validación de horarios, la regla de negocio para permitir o bloquear pedidos fuera de horario y los criterios de aceptación de configuración.
  Crítica: sí
  Estado: Respondida (DEC-E41)
  Responsable: equipo
- OPEN-Q-003. En la cancelación de pedidos por suscripción vencida (HU-03 y DEC-E26), ¿cuáles estados exactos del ciclo de vida se consideran «no despachados» y qué ocurre con el domiciliario si el pedido ya estaba asignado pero no «en camino»?
  Por qué importa: define la lógica de transición atómica de pedidos al pasar la suscripción a vencida, la notificación al domiciliario asignado y el conteo previo que se le muestra al dueño de la plataforma.
  Crítica: sí
  Estado: Respondida (DEC-E26)
  Responsable: equipo
- OPEN-Q-004. Respecto al enlace, código QR y código único del negocio (HU-06, HU-04, HU-09 y DEC-E05), ¿el código lo genera automáticamente el sistema al aprobar el negocio o lo define el administrador, y es el mismo identificador para clientes y para personal?
  Por qué importa: define los requisitos funcionales de generación y consulta de credenciales de difusión, y cómo el bot identifica el negocio en los comandos de vinculación o compra.
  Crítica: sí
  Estado: Respondida (DEC-E42)
  Responsable: equipo
- OPEN-Q-005. Para la parametrización de zonas de cobertura (HU-08), ¿se permite registrar una tarifa de $0 COP (domicilio gratuito) y qué reglas aplican sobre nombres duplicados o tarifas mínimas/máximas?
  Por qué importa: define las validaciones de entrada para creación y actualización de barrios, evitando registros inconsistentes o cobros negativos.
  Crítica: sí
  Estado: Respondida (DEC-E43)
  Responsable: equipo
- OPEN-Q-006. Si el administrador reduce el tope de pedidos simultáneos a un valor inferior al número de pedidos que un domiciliario tiene asignados en ese momento (HU-07), ¿qué comportamiento debe tener el sistema con las asignaciones vigentes?
  Por qué importa: define si la regla de capacidad afecta retroactivamente la operación en curso o solo restringe nuevas asignaciones.
  Crítica: no
  Estado: Respondida (DEC-E44)
  Responsable: equipo

## Especificación

### 1. Objetivo
Permitir la parametrización operativa integral de un negocio aprobado por parte de su administrador (datos comerciales, horarios de atención por día, formas de pago aceptadas asociadas a tipos fijos de la plataforma con nombres personalizados y marcado automático de cobro al entregar, valor mínimo de compra, dos accesos independientes para clientes y personal, tope de pedidos simultáneos entre 1 y 7, y zonas tarifarias entre $0 y $50.000 COP) y facultar al dueño de la plataforma para controlar la suscripción del negocio, suspendiendo la recepción de pedidos y cancelando de forma atómica los pedidos no despachados al vencer.

### 2. Contexto
En Domiciliarios Eje cada negocio opera de forma aislada. Una vez un negocio es aprobado por el dueño de la plataforma (SPEC-001), el administrador requiere configurar las condiciones de servicio para atender clientes y coordinar repartidores. A su vez, la plataforma opera bajo un modelo de mensualidad fija, por lo que el dueño de la plataforma gestiona el estado de suscripción.

Decisiones del equipo:
- DEC-E40. El tope de pedidos simultáneos por domiciliario es 3 por defecto; el administrador lo puede cambiar entre 1 y 7. Responde a OPEN-Q-001.
- DEC-E41. Cada día de la semana tiene un único rango de atención (HH:MM a HH:MM) o está cerrado. El dueño de la plataforma mantiene una lista única de festivos de Colombia; cada negocio decide si en cada festivo cierra o atiende con un horario propio. Responde a OPEN-Q-002.
- DEC-E26. El sistema guarda el estado de suscripción de cada negocio (al día o vencido), que marca el dueño de la plataforma. Al vencer, los pedidos no despachados (recibido, en preparación, listo para recoger) se cancelan con motivo «suscripción vencida» y el dueño de la plataforma como responsable; si tenían domiciliario asignado, también se le avisa. Responde a OPEN-Q-003.
- DEC-E42. Cada negocio tiene dos accesos distintos generados automáticamente al aprobar el negocio: enlace, QR y código para clientes (pedidos) y enlace, QR y código para personal (solicitudes de unión); el de personal solo lo ve el administrador. Responde a OPEN-Q-004.
- DEC-E43. La tarifa de domicilio va de $0 a $50.000 COP; el nombre del barrio no se repite dentro del mismo negocio. Responde a OPEN-Q-005.
- DEC-E44. Si el administrador baja el tope por debajo de la carga actual de un domiciliario, sus pedidos actuales se respetan y no recibe nuevos hasta quedar por debajo del tope. Responde a OPEN-Q-006.
- DEC-E51. Cada negocio configura las formas de pago que acepta (configuración del negocio, SPEC-002); el cliente elige entre ellas.
- DEC-E53. Cada negocio puede fijar un valor mínimo de compra (0 = sin mínimo) en su configuración (SPEC-002).
- DEC-E57. Las formas de pago tienen un tipo fijo de la plataforma (efectivo, transferencia o datáfono); cada negocio elige cuáles acepta y puede darles un nombre propio (por ejemplo, «Nequi» de tipo transferencia). Toda forma de pago cuyo tipo no sea transferencia se cobra al entregar.

### 3. Alcance
- Consulta y actualización de datos comerciales del negocio (nombre comercial y dirección).
- Configuración de horarios de atención (único rango HH:MM a HH:MM o cerrado) por cada día de la semana, incluyendo operación en días festivos según decisión del negocio sobre la lista de la plataforma.
- Configuración y selección de las formas de pago aceptadas por el establecimiento, asociando cada una a un tipo fijo de la plataforma (efectivo, transferencia o datáfono) con un nombre personalizado (ej. Nequi de tipo transferencia), identificando de forma automática que toda forma cuyo tipo no sea transferencia se cobra al entregar (el cliente únicamente podrá elegir entre las opciones habilitadas por el negocio).
- Definición del valor mínimo de compra exigido por el negocio para procesar pedidos ($0 COP = sin valor mínimo).
- Generación automática y consulta de dos accesos distintos (enlace, código QR y código) para clientes y para personal.
- Definición y actualización del tope de pedidos simultáneos por domiciliario dentro del rango de 1 a 7, respetando cargas actuales en caso de reducción.
- Creación, actualización de tarifa ($0 a $50.000 COP) y desactivación de zonas de cobertura (barrios con nombres no repetidos).
- Conmutación del estado de suscripción (al día o vencido) por parte del dueño de la plataforma, incluyendo conteo previo, confirmación obligatoria, cese de recepción de pedidos y cancelación atómica de pedidos no despachados con notificación a clientes, administrador y domiciliarios asignados.

### 4. Actores e historias de usuario
Actores:
- Administrador del negocio: gestiona la configuración comercial, horarios, formas de pago aceptadas (tipos fijos, nombres y reglas de cobro), valor mínimo de compra, accesos de difusión, capacidad de domiciliarios y cobertura tarifaria de su establecimiento.
- Dueño de la plataforma: administra el estado de suscripción de los negocios registrados y mantiene la lista de festivos.
- Empleado o vendedor: usuario con permisos operativos que tiene restringida la modificación de la configuración general y suscripción.

Historias de usuario:
- HU-001 (HU-06). Como Administrador del negocio, quiero configurar los datos generales, los horarios de atención, las formas de pago aceptadas (con sus tipos fijos de plataforma, nombres personalizados y marcas de cobro al entregar), el valor mínimo de compra y consultar los accesos de difusión (clientes y personal) de mi establecimiento, para definir las condiciones de servicio y permitir la llegada directa de mis clientes y postulantes sin intermediarios.
- HU-002 (HU-07). Como Administrador del negocio, quiero definir el número máximo de pedidos simultáneos asignables a un domiciliario en mi negocio (entre 1 y 7), para regular la carga de trabajo de los repartidores y la puntualidad del servicio.
- HU-003 (HU-08). Como Administrador del negocio, quiero registrar y actualizar los barrios de cobertura con su tarifa de entrega (de $0 a $50.000 COP y sin nombres repetidos), para determinar dónde entrega mi establecimiento y cuánto se cobrará por cada envío.
- HU-004 (HU-03). Como Dueño de la plataforma, quiero actualizar el estado de suscripción de un negocio entre al día y vencido, para asegurar que solo los establecimientos con mensualidad activa puedan recibir pedidos.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir al administrador del negocio actualizar el nombre comercial y la dirección física de su establecimiento, validando la autorización y pertenencia en el backend. Origen: HU-06 y contexto 3.2.
- RF-002. El sistema debe permitir al administrador del negocio configurar para cada día de la semana un único rango de atención (HH:MM a HH:MM) o marcarlo como cerrado, y definir si el establecimiento atiende o cierra en los días festivos registrados por la plataforma. Origen: HU-06, DEC-E41 y contexto 3.4.
- RF-003. Al aprobar un negocio, el sistema debe generar automáticamente dos accesos distintos compuestos por enlace, código QR y código único: uno exclusivo para clientes y otro exclusivo para personal. Origen: HU-06, DEC-E42 y DEC-E05.
- RF-004. El sistema debe permitir al administrador del negocio consultar los accesos de clientes y personal, asegurando que el acceso de personal solo sea visible para el rol de administrador. Origen: HU-06, DEC-E42 y contexto 3.3.
- RF-005. El sistema debe permitir al administrador del negocio registrar y actualizar el tope de pedidos simultáneos por domiciliario asignándole un valor entero entre 1 y 7. Origen: HU-07, DEC-E40 y DEC-E12.
- RF-006. El sistema debe asignar por defecto un tope de 3 pedidos simultáneos por domiciliario cuando un negocio es aprobado y el administrador no ha definido un valor explícito. Origen: HU-07 y DEC-E40.
- RF-007. El sistema debe rechazar valores fuera del rango permitido (menores a 1 o mayores a 7) o formatos no numéricos al configurar el tope de pedidos simultáneos. Origen: HU-07 y DEC-E40.
- RF-008. El sistema debe restringir la configuración del tope de pedidos simultáneos exclusivamente al rol de Administrador del negocio, rechazando intentos de empleados u otros roles. Origen: HU-07 y contexto 3.2.
- RF-009. El sistema debe permitir al administrador del negocio registrar barrios de cobertura ingresando nombre del sector y valor de tarifa de entrega entre $0 y $50.000 COP. Origen: HU-08, DEC-E43 y contexto 3.5.
- RF-010. El sistema debe validar que el nombre del barrio registrado no esté duplicado dentro del mismo negocio. Origen: DEC-E43 y HU-08.
- RF-011. El sistema debe permitir al administrador del negocio modificar la tarifa de entrega de un barrio existente dentro del rango permitido, aplicando la nueva tarifa únicamente a pedidos futuros. Origen: HU-08 y DEC-E43.
- RF-012. El sistema debe permitir al administrador del negocio desactivar un barrio de cobertura, impidiendo cotizaciones de pedidos futuros hacia ese sector y preservando el histórico anterior. Origen: HU-08.
- RF-013. El sistema debe validar que el registro y modificación de barrios y tarifas solo opere sobre los datos del negocio del administrador autenticado. Origen: contexto 3.3 y HU-08.
- RF-014. El sistema debe permitir al dueño de la plataforma consultar los negocios registrados y su estado de suscripción actual (al día o vencido), sin exponer datos de pedidos, clientes ni domiciliarios. Origen: contexto 2.3, DEC-E01 y HU-03.
- RF-015. Antes de marcar una suscripción como vencida, el sistema debe calcular y mostrar al dueño de la plataforma la cantidad exacta de pedidos no despachados (recibido, en preparación y listo para recoger) que serán cancelados y solicitar confirmación explícita. Origen: DEC-E26, DEC-E13 y HU-03.
- RF-016. Al confirmar el cambio a estado vencido, el sistema debe cambiar atómicamente el estado del negocio a vencido, impedir el ingreso de pedidos nuevos, cancelar todos los pedidos no despachados registrando motivo «suscripción vencida» y responsable Dueño de la plataforma, y notificar al administrador, a los clientes afectados y a los domiciliarios que tenían asignados dichos pedidos. Origen: DEC-E26, DEC-E13, DEC-E25 y HU-03.
- RF-017. El sistema debe permitir que los pedidos que ya se encuentren en estado «en camino» continúen su entrega habitual cuando el negocio pase a suscripción vencida. Origen: DEC-E26 y HU-03.
- RF-018. El sistema debe permitir al dueño de la plataforma reactivar un negocio con suscripción vencida pasándolo a «al día», previa confirmación, habilitando nuevamente la recepción de pedidos. Origen: HU-03 y DEC-E26.
- RF-019. El sistema debe rechazar cualquier intento de modificar el estado de suscripción realizado por administradores, empleados o domiciliarios. Origen: contexto 2.3 y HU-03.
- RF-020. El sistema debe permitir al administrador del negocio seleccionar y gestionar las formas de pago que su establecimiento acepta de los clientes, obligando a asociar cada una a un tipo fijo de la plataforma (efectivo, transferencia o datáfono) y a asignarle un nombre propio (por ejemplo, «Nequi» de tipo transferencia), registrando automáticamente que toda forma cuyo tipo no sea transferencia se cobra al entregar, y asegurando que el negocio mantenga al menos una forma de pago activa. Origen: DEC-E51, DEC-E57 y HU-06.
- RF-021. El sistema debe permitir al administrador del negocio configurar un valor mínimo de compra para los pedidos expresado como un entero mayor o igual a $0 COP, donde $0 COP indica que el negocio no exige monto mínimo. Origen: DEC-E53 y HU-06.

### 6. Requisitos no funcionales
- RNF-001. Autorización y seguridad. Toda operación de consulta o modificación de configuración y suscripción debe validar identidad, rol, negocio y permisos en el backend. Se verifica con: prueba de integración simulando peticiones con token/rol manipulado hacia el backend. Origen: contexto 3.2.
- RNF-002. Aislamiento multiinquilino. Ninguna consulta de configuración o zonas debe retornar o alterar registros pertenecientes a otro identificador de negocio. Se verifica con: prueba automatizada de acceso cruzado entre identificadores de negocio distintos. Origen: contexto 3.3.
- RNF-003. Atomicidad y consistencia. La transición de suscripción a vencida y la cancelación masiva de pedidos no despachados deben ejecutarse dentro de una transacción atómica para evitar estados inconsistentes. Se verifica con: prueba de carga concurrente simulando fallos durante la conmutación de estado. Origen: contexto 3.8.
- RNF-004. Usabilidad en Telegram. Los menús de configuración de horarios, topes, formas de pago, valor mínimo y tarifas deben presentarse mediante formularios y botones en el bot con confirmación previa a la persistencia. Se verifica con: inspección de interfaz y flujos conversacionales en bot de prueba. Origen: contexto 3.1 y contexto 3.7.

### 7. Reglas de negocio
- BR-001. Exclusividad de gestión de configuración. Solo el usuario con rol de Administrador activo del negocio puede modificar datos comerciales, horarios, accesos de difusión, formas de pago aceptadas, valor mínimo de compra, topes y barrios de cobertura de su negocio. Origen: contexto 3.4 y HU-06, HU-07, HU-08.
- BR-002. Exclusividad de control de suscripción. Solo el usuario con rol de Dueño de la plataforma puede visualizar el panel de suscripciones y conmutar el estado de suscripción de un negocio. Origen: contexto 2.3 y HU-03.
- BR-003. Restricción de pedidos en negocio vencido. Un negocio con suscripción en estado vencido no puede recibir pedidos nuevos de clientes bajo ninguna circunstancia. Origen: DEC-E26 y HU-03.
- BR-004. Cancelación por vencimiento. Todo pedido en estado no despachado (recibido, en preparación o listo para recoger) de un negocio cuya suscripción pasa a vencida debe pasar inmediatamente al estado final cancelado con motivo «suscripción vencida» y responsable Dueño de la plataforma, notificando al domiciliario asignado. Origen: DEC-E13, DEC-E25 y DEC-E26.
- BR-005. Continuidad de pedidos en ruta. Los pedidos que se encuentren en estado «en camino» al momento de vencer la suscripción no se cancelan y deben seguir su flujo normal hasta terminar como entregado o con novedad. Origen: DEC-E26 y DEC-E22.
- BR-006. Validación de tope de pedidos. El tope de pedidos simultáneos por domiciliario debe encontrarse estrictamente entre 1 y 7, con un valor por defecto de 3. Origen: HU-07 y DEC-E40.
- BR-007. No eliminación de barrios históricos. Un barrio de cobertura no puede borrarse físicamente del sistema si tiene pedidos asociados; solo puede marcarse como inactivo para no admitir nuevos pedidos. Origen: HU-08.
- BR-008. Unicidad de barrio en el negocio. Un negocio no puede registrar dos zonas de cobertura con el mismo nombre normalizado. Origen: DEC-E43 y HU-08.
- BR-009. Generación de accesos independientes. Cada negocio aprobado cuenta con dos accesos distintos (enlace, QR y código) generados automáticamente por el sistema: uno para clientes y otro para personal (restringido al administrador). Origen: DEC-E42 y HU-06.
- BR-010. Tipos y formas de pago permitidas. Las formas de pago aceptadas por el negocio corresponden a uno de los tres tipos fijos de la plataforma (efectivo, transferencia o datáfono) y llevan un nombre personalizado asignado por el negocio. Toda forma de pago cuyo tipo no sea transferencia (efectivo y datáfono) se clasifica y procesa automáticamente como cobro al entregar. El cliente únicamente puede seleccionar de entre las formas de pago activas en el negocio. Origen: DEC-E51 y DEC-E57.
- BR-011. Valor mínimo de compra. Todo pedido cuyo valor total de productos sea inferior al valor mínimo de compra configurado por el negocio (cuando sea mayor a $0 COP) debe ser rechazado por el sistema. Origen: DEC-E53.

Estados y ciclo de vida de la suscripción del negocio:
- Estados posibles de suscripción: al día, vencido.
- Transición 1: al día -> vencido. Provocada por: Dueño de la plataforma tras confirmar cantidad de pedidos a cancelar. Efecto colateral: cancela pedidos no despachados, notifica a domiciliarios asignados y cierra recepción de pedidos.
- Transición 2: vencido -> al día. Provocada por: Dueño de la plataforma tras confirmar reactivación. Efecto colateral: reabre recepción de pedidos.

### 8. Flujo principal
1. El administrador del negocio autenticado en Telegram selecciona el comando de configuración de su establecimiento.
2. El sistema valida en el backend el rol de Administrador y obtiene los datos del negocio asociado.
3. El administrador selecciona la opción deseada: datos generales, horarios de atención, formas de pago aceptadas, valor mínimo de compra, accesos de difusión, tope de pedidos por domiciliario o zonas de cobertura.
4. Para datos comerciales, horarios, formas de pago y valor mínimo de compra: el administrador ingresa los nuevos valores. En el caso de las formas de pago, selecciona el tipo fijo de la plataforma (efectivo, transferencia o datáfono) e ingresa un nombre personalizado (ej. Nequi), ante lo cual el sistema asigna automáticamente la propiedad de cobro al entregar si el tipo no es transferencia. El sistema valida la estructura y almacena los cambios.
5. Para accesos de difusión: el sistema despliega por separado los accesos (enlace, código y QR) para clientes y para personal (restringiendo este último al administrador).
6. Para tope de domiciliarios: el administrador digita un entero entre 1 y 7, el sistema valida el rango y actualiza el parámetro operativo.
7. Para zonas de cobertura: el administrador registra un barrio nuevo con su tarifa entre $0 y $50.000 COP validando nombre único, o actualiza/inactiva un barrio existente; el sistema valida y confirma el cambio.
8. El sistema muestra mensaje de confirmación y resumen de la configuración actualizada.

Flujo principal de control de suscripción (Dueño de la plataforma):
1. El dueño de la plataforma autenticado ingresa al bot y consulta la lista de negocios registrados.
2. El sistema presenta la lista de negocios con su estado de suscripción (al día o vencido) sin mostrar datos operativos internos.
3. El dueño selecciona un negocio con suscripción al día y presiona marcar como vencido.
4. El sistema cuenta los pedidos no despachados (recibido, en preparación, listo para recoger) de ese negocio y presenta mensaje de advertencia solicitando confirmación.
5. El dueño de la plataforma confirma la acción.
6. El sistema, de manera atómica, cambia el estado a vencido, bloquea nuevos pedidos, cancela los pedidos no despachados registrando motivo y responsable, y notifica al administrador, clientes y domiciliarios asignados.

### 9. Flujos alternativos y de excepción
- A1. Reactivación de suscripción: En el paso 3 del flujo de suscripción, el dueño selecciona un negocio en estado vencido y elige marcar al día; el sistema pide confirmación y al aceptar conmuta el estado a al día y habilita la recepción de pedidos sin alterar los pedidos históricos.
- A2. Modificación de tarifa de barrio existente: En el paso 7 del flujo de configuración, el administrador elige un barrio previamente creado e introduce un nuevo valor monetario válido; el sistema actualiza el registro para pedidos futuros.
- A3. Inactivación de barrio: En el paso 7, el administrador selecciona desactivar una zona; el sistema marca el sector como no disponible para nuevos pedidos y notifica éxito.
- E1. Usuario no autorizado intenta configurar negocio: Un usuario con rol de empleado, domiciliario o cliente envía comandos de configuración; el sistema verifica permisos en backend, rechaza la operación y no muestra datos.
- E2. Administrador intenta acceder a otro negocio: Una solicitud intenta modificar parámetros de un negocio ajeno; el sistema detecta inconsistencia en backend y bloquea el acceso.
- E3. Valor de tope fuera de rango: El administrador ingresa un valor menor a 1, mayor a 7 o texto al definir el tope de domiciliarios; el sistema rechaza la entrada, emite mensaje de error y mantiene el valor anterior.
- E4. Usuario no autorizado intenta modificar suscripción: Un administrador o empleado envía instrucción de cambio de suscripción; el backend valida que no es Dueño de la plataforma y deniega la acción.
- E5. Cancelación de acción de vencimiento: El dueño de la plataforma cancela la confirmación tras ver el número de pedidos afectados; el sistema no altera la suscripción ni los pedidos.
- E6. Nombre de barrio duplicado: El administrador intenta registrar un barrio con un nombre ya existente en su negocio; el sistema rechaza el registro informando que el nombre ya está en uso.
- E7. Desactivación de todas las formas de pago: El administrador intenta desmarcar la única forma de pago activa del negocio; el sistema rechaza el cambio indicando que el negocio debe tener al menos una forma de pago habilitada.
- E8. Valor mínimo de compra inválido: El administrador ingresa un número negativo o un texto como valor mínimo de compra; el sistema rechaza la entrada y mantiene el valor previo.

### 10. Casos límite
- CL-001. Suscripción vencida sin pedidos pendientes: El dueño de la plataforma marca como vencido un negocio que tiene cero pedidos no despachados; el sistema muestra 0 pedidos a cancelar, pide confirmación, pasa a vencido y bloquea nuevos pedidos sin generar errores. Origen: HU-03 y DEC-E26.
- CL-002. Pedidos en camino al vencer suscripción: Existen pedidos en estado «en camino» cuando se confirma el vencimiento; dichos pedidos permanecen en su estado y no son cancelados, completando su ciclo normalmente. Origen: DEC-E26 y HU-03.
- CL-003. Concurrencia al conmutar suscripción y recibir pedido: Un cliente intenta confirmar un pedido en el mismo instante en que el dueño de la plataforma confirma el vencimiento; la transacción atómica rechaza el pedido del cliente informando que el negocio no está disponible. Origen: contexto 3.8 y RNF-003.
- CL-004. Reducción de tope de pedidos con domiciliarios saturados: El administrador reduce el tope a un valor menor a la cantidad de pedidos que un repartidor tiene actualmente en curso; los pedidos vigentes se respetan y concluyen su ciclo, pero no se permite asignarle ningún pedido nuevo hasta quedar por debajo del nuevo tope. Origen: DEC-E44 y HU-07.
- CL-005. Configuración de tarifa en cero pesos ($0 COP): El administrador ingresa una tarifa de 0 pesos para un barrio céntrico; el sistema valida que está dentro del rango permitido ($0 a $50.000 COP) y registra el domicilio como gratuito. Origen: DEC-E43 y HU-08.
- CL-006. Operación en día festivo: El sistema evalúa la lista de festivos de la plataforma y aplica la regla de atención específica configurada por el negocio para permitir o rechazar nuevos pedidos. Origen: DEC-E41 y contexto 3.4.
- CL-007. Configuración de valor mínimo de compra en cero pesos ($0 COP): El administrador establece el valor mínimo de compra en $0 COP; el sistema valida el registro e indica que el negocio no exige monto mínimo para registrar un pedido. Origen: DEC-E53 y HU-06.
- CL-008. Intento de dejar el negocio sin formas de pago o ingresar tipo no reconocido: El administrador intenta desactivar la última forma de pago disponible o seleccionar un tipo distinto a los tres fijos (efectivo, transferencia o datáfono); el sistema bloquea la acción exigiendo mantener al menos una activa y restringiendo a los tipos fijos definidos. Origen: DEC-E51, DEC-E57 y HU-06.

### 11. Criterios de aceptación
- AC-001. Autorización de datos comerciales: Dado un usuario autenticado con rol de Administrador del negocio A, cuando actualiza el nombre comercial y la dirección de su establecimiento, entonces el sistema almacena los datos y confirma la operación.
- AC-002. Aislamiento de configuración: Dado un usuario autenticado como Administrador del negocio A, cuando intenta modificar la configuración comercial o de zonas del negocio B, entonces el sistema rechaza la petición y los datos de B no sufren modificaciones.
- AC-003. Bloqueo de configuración a otros roles: Dado un usuario con rol de Empleado o Domiciliario, cuando intenta acceder o enviar cambios a la configuración operativa del negocio, entonces el sistema deniega el acceso informando permisos insuficientes.
- AC-004. Consulta de accesos independientes: Dado un negocio en estado activo, cuando su administrador consulta los medios de difusión en el bot, entonces el sistema retorna por separado el enlace, código y QR para clientes, y muestra el enlace, código y QR de personal únicamente al administrador.
- AC-005. Configuración válida de tope de domiciliarios: Dado un administrador configurando el tope operativo, cuando ingresa un número entero entre 1 y 7, entonces el sistema actualiza el valor de capacidad máxima por domiciliario del negocio.
- AC-006. Rechazo de tope fuera de rango: Dado un administrador configurando el tope operativo, cuando ingresa un valor menor a 1, mayor a 7 o texto, entonces el sistema rechaza la actualización y muestra un mensaje indicando que debe ser un entero entre 1 y 7.
- AC-007. Registro de barrio nuevo con tarifa válida: Dado un administrador configurando zonas, cuando ingresa un barrio con nombre único en su negocio y una tarifa entre $0 y $50.000 COP, entonces el sistema guarda la zona como activa.
- AC-008. Rechazo de barrio duplicado: Dado un negocio con un barrio registrado, cuando el administrador intenta crear otro barrio con el mismo nombre, entonces el sistema rechaza el registro por duplicidad.
- AC-009. Actualización de tarifa en zona existente: Dado un barrio previamente configurado en el negocio, cuando el administrador actualiza su tarifa dentro del rango permitido, entonces los pedidos cotizados a partir de ese momento calculan la nueva tarifa y los anteriores no se modifican.
- AC-010. Suspensión de cobertura de barrio: Dado un barrio activo en el negocio, cuando el administrador cambia su estado a inactivo, entonces el sistema impide cotizar domicilios hacia ese barrio en nuevos pedidos y preserva el registro histórico.
- AC-011. Consulta de suscripción sin datos sensibles: Dado el dueño de la plataforma autenticado en el bot, cuando consulta el estado de los negocios, entonces el sistema muestra el listado con nombre de establecimiento y estado de suscripción sin exponer pedidos, clientes ni repartidores.
- AC-012. Conteo y advertencia antes de vencer suscripción: Dado un negocio con suscripción al día que posee pedidos en estado recibido, en preparación o listo para recoger, cuando el dueño de la plataforma selecciona marcar como vencido, entonces el sistema presenta el número exacto de pedidos que serán cancelados y solicita confirmación.
- AC-013. Confirmación de vencimiento y cancelación atómica: Dado que el dueño de la plataforma confirma marcar como vencido un negocio, cuando el sistema procesa el cambio, entonces la suscripción pasa a vencida, los pedidos en recibido, en preparación y listo para recoger quedan en estado cancelado con motivo «suscripción vencida» y responsable Dueño de la plataforma, el negocio no admite pedidos nuevos, y se notifica al administrador, clientes y domiciliarios asignados.
- AC-014. Continuidad de pedidos en camino: Dado un pedido en estado «en camino» perteneciente a un negocio que pasa a suscripción vencida, cuando se aplica el vencimiento, entonces el pedido permanece en estado «en camino» y permite al domiciliario finalizarlo como entregado o con novedad.
- AC-015. Reactivación de suscripción: Dado un negocio en estado vencido, cuando el dueño de la plataforma selecciona marcar al día y confirma, entonces el sistema actualiza el estado a al día y el bot vuelve a admitir pedidos en el horario de atención configurado.
- AC-016. Rechazo de control de suscripción a no administradores de plataforma: Dado un usuario con rol de Administrador del negocio o Empleado, cuando intenta ejecutar el comando de conmutación de suscripción, entonces el sistema rechaza la solicitud por falta de autorización.
- AC-017. Asignación de tope por defecto: Dado un negocio recientemente aprobado que no ha configurado su tope, cuando se consulta su capacidad máxima de asignación, entonces el sistema aplica el valor por defecto de 3 pedidos simultáneos.
- AC-018. Bloqueo de pedidos fuera de horario configurado: Dado un horario configurado por día o una regla de cierre en festivos, cuando un cliente intenta iniciar un pedido fuera de la franja horaria establecida, entonces el bot le informa que el establecimiento se encuentra cerrado y no permite el registro.
- AC-019. Configuración de formas de pago aceptadas y reglas de cobro: Dado un administrador configurando su negocio, cuando selecciona una forma de pago indicando uno de los tipos fijos de la plataforma (efectivo, transferencia o datáfono) y le asigna un nombre propio (por ejemplo, «Nequi» de tipo transferencia), entonces el sistema la registra en la configuración del negocio, la marca automáticamente para cobro al entregar si su tipo es efectivo o datáfono, y restringe la selección del cliente únicamente a las formas de pago configuradas y activas.
- AC-020. Configuración de valor mínimo de compra válido: Dado un administrador configurando el valor mínimo de compra, cuando ingresa un entero mayor o igual a $0 COP, entonces el sistema actualiza la regla del monto mínimo para pedidos de ese negocio.
- AC-021. Rechazo de valor mínimo de compra inválido: Dado un administrador configurando el valor mínimo de compra, cuando ingresa un entero negativo o texto, entonces el sistema rechaza la solicitud y mantiene la configuración previa.

### 12. Dependencias
- SPEC-001: Registro y vinculación (establece el alta de negocios aprobados, roles y autenticación de usuarios).
- Telegram Bot API: canal de interacción conversacional y entrega de enlaces y códigos QR.
- Repositorio de configuración y suscripción: almacenamiento persistente de horarios, parámetros de carga, formas de pago, monto mínimo de compra y tarifas por negocio.

### 13. Restricciones
- Cada operación verifica en el backend el usuario, su rol, el negocio al que pertenece y sus permisos; nunca solo en el bot (Contexto 3.2).
- La información de cada negocio está separada: ningún usuario ve ni modifica datos de otro negocio (Contexto 3.3).
- La asignación de un domiciliario y cada cambio de estado de un pedido son atómicos: dos acciones simultáneas no dejan un pedido asignado dos veces ni en un estado imposible (Contexto 3.8).
- Cada cambio de estado registra fecha, estado y responsable (Contexto 3.8).
- Las operaciones importantes piden confirmación antes de ejecutarse (Contexto 3.7).
- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración (Contexto 4).
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante (Contexto 4).
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar (Contexto 4).
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales (Contexto 4).
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración (Contexto 4).
- Plazo: unas 8 semanas o más (DEC-E19 y Contexto 4).
- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada (Contexto 3.3 y Contexto 6).
- Colombia: artículo 15 de la Constitución (habeas data), Ley 1581 de 2012 y Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015 (autorización previa, expresa e informada; aviso de privacidad; política de tratamiento; derechos de los titulares; transmisión y transferencia de datos). Autoridad: Superintendencia de Industria y Comercio (Contexto 6).
- Referencia internacional de buenas prácticas (no se asume que aplique jurídicamente): principios del Reglamento General de Protección de Datos de la Unión Europea (minimización, limitación de finalidad y de plazo de conservación, transparencia) (Contexto 6).
- Textos de los avisos: docs/legal/avisos-de-privacidad.md (borrador; requiere revisión de una persona con formación jurídica antes de usarse con datos reales) (Contexto 6).

### 14. Fuera de alcance
- No es una central de repartidores (Contexto 5).
- No es un marketplace ni ofrece listados públicos o directorios de negocios (Contexto 5 y DEC-E05).
- No cobra comisión por pedido ni por entrega (Contexto 5).
- No depende de otro aplicativo para su funcionamiento básico (Contexto 5).
- Cobro en línea o pasarelas de pago para la suscripción mensual o los pedidos (DEC-E08, DEC-E26).
- Pedidos programados para entrega diferida fuera de horario (DEC-E09).
- Edición gráfica o generación interactiva de polígonos geoespaciales sobre mapa para zonas de cobertura.
- [Mecanismo de generación de imagen QR]: tema para arquitectura. Origen: RF-003.
- [Estrategia de transacción distribuida o bloqueo para cancelación atómica de pedidos]: tema para arquitectura. Origen: RF-016 y RNF-003.

### 15. Preguntas abiertas
- OPEN-Q-001: Respondida (DEC-E40).
- OPEN-Q-002: Respondida (DEC-E41).
- OPEN-Q-003: Respondida (DEC-E26).
- OPEN-Q-004: Respondida (DEC-E42).
- OPEN-Q-005: Respondida (DEC-E43).
- OPEN-Q-006: Respondida (DEC-E44).

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-004, RF-020, RF-021; BR-001, BR-009, BR-010, BR-011; AC-001, AC-002, AC-003, AC-004, AC-018, AC-019, AC-020, AC-021; CL-006, CL-007, CL-008.
- HU-002: RF-005, RF-006, RF-007, RF-008; BR-006; AC-005, AC-006, AC-017; CL-004.
- HU-003: RF-009, RF-010, RF-011, RF-012, RF-013; BR-007, BR-008; AC-007, AC-008, AC-009, AC-010; CL-005.
- HU-004: RF-014, RF-015, RF-016, RF-017, RF-018, RF-019; BR-002, BR-003, BR-004, BR-005; AC-011, AC-012, AC-013, AC-014, AC-015, AC-016; CL-001, CL-002, CL-003.
- RF-001: Origen: HU-06 y contexto 3.2; verificado por AC-001.
- RF-002: Origen: HU-06, DEC-E41 y contexto 3.4; verificado por AC-018.
- RF-003: Origen: HU-06, DEC-E42 y DEC-E05; verificado por AC-004.
- RF-004: Origen: HU-06, DEC-E42 y contexto 3.3; verificado por AC-004.
- RF-005: Origen: HU-07, DEC-E40 y DEC-E12; verificado por AC-005.
- RF-006: Origen: HU-07 y DEC-E40; verificado por AC-017.
- RF-007: Origen: HU-07 y DEC-E40; verificado por AC-006.
- RF-008: Origen: HU-07 y contexto 3.2; verificado por AC-003.
- RF-009: Origen: HU-08, DEC-E43 y contexto 3.5; verificado por AC-007.
- RF-010: Origen: DEC-E43 y HU-08; verificado por AC-008.
- RF-011: Origen: HU-08 y DEC-E43; verificado por AC-009.
- RF-012: Origen: HU-08; verificado por AC-010.
- RF-013: Origen: contexto 3.3 y HU-08; verificado por AC-002.
- RF-014: Origen: contexto 2.3, DEC-E01 y HU-03; verificado por AC-011.
- RF-015: Origen: DEC-E26, DEC-E13 y HU-03; verificado por AC-012.
- RF-016: Origen: DEC-E26, DEC-E13, DEC-E25 y HU-03; verificado por AC-013.
- RF-017: Origen: DEC-E26 y HU-03; verificado por AC-014.
- RF-018: Origen: HU-03 y DEC-E26; verificado por AC-015.
- RF-019: Origen: contexto 2.3 y HU-03; verificado por AC-016.
- RF-020: Origen: DEC-E51, DEC-E57 y HU-06; verificado por AC-019.
- RF-021: Origen: DEC-E53 y HU-06; verificado por AC-020, AC-021.
- RNF-001: Origen: contexto 3.2; verificado con prueba de integración simulando peticiones con token/rol manipulado hacia el backend.
- RNF-002: Origen: contexto 3.3; verificado con prueba automatizada de acceso cruzado entre identificadores de negocio distintos.
- RNF-003: Origen: contexto 3.8; verificado con prueba de carga concurrente simulando fallos durante la conmutación de estado.
- RNF-004: Origen: contexto 3.1 y contexto 3.7; verificado con inspección de interfaz y flujos conversacionales en bot de prueba.
- BR-001: Origen: contexto 3.4 y HU-06, HU-07, HU-08; verificado por AC-001, AC-003.
- BR-002: Origen: contexto 2.3 y HU-03; verificado por AC-011, AC-016.
- BR-003: Origen: DEC-E26 y HU-03; verificado por AC-013.
- BR-004: Origen: DEC-E13, DEC-E25 y DEC-E26; verificado por AC-013.
- BR-005: Origen: DEC-E26 y DEC-E22; verificado por AC-014.
- BR-006: Origen: HU-07 y DEC-E40; verificado por AC-005, AC-006.
- BR-007: Origen: HU-08; verificado por AC-010.
- BR-008: Origen: DEC-E43 y HU-08; verificado por AC-008.
- BR-009: Origen: DEC-E42 y HU-06; verificado por AC-004.
- BR-010: Origen: DEC-E51 y DEC-E57; verificado por AC-019.
- BR-011: Origen: DEC-E53; verificado por AC-020, AC-021.
- CL-001: Origen: HU-03 y DEC-E26; verificado por AC-012.
- CL-002: Origen: DEC-E26 y HU-03; verificado por AC-014.
- CL-003: Origen: contexto 3.8 y RNF-003; verificado por AC-013.
- CL-004: Origen: DEC-E44 y HU-07; verificado por AC-005.
- CL-005: Origen: DEC-E43 y HU-08; verificado por AC-007.
- CL-006: Origen: DEC-E41 y contexto 3.4; verificado por AC-018.
- CL-007: Origen: DEC-E53 y HU-06; verificado por AC-020.
- CL-008: Origen: DEC-E51, DEC-E57 y HU-06; verificado por AC-019.

### 17. Historial de cambios
- Versión 0.1: creación de la especificación a partir de la necesidad y las historias de usuario HU-03, HU-06, HU-07 y HU-08 de EPIC-001.
- Versión 1.0: incorporación de las respuestas del equipo a OPEN-Q-001 a OPEN-Q-006 (DEC-E40 a DEC-E44 y DEC-E26). Se actualizan los requisitos funcionales, reglas de negocio, flujos y criterios de aceptación, pasando el documento a estado Candidata.
- Versión 1.1: incorporación de decisiones DEC-E51 (formas de pago configurables) y DEC-E53 (valor mínimo de compra). Se agregan RF-020, RF-021, BR-010, BR-011, CL-007, CL-008, AC-019, AC-020 y AC-021. Documento en estado Candidata.
- Versión 1.2: incorporación de la decisión DEC-E57 que precisa los tres tipos fijos de la plataforma (efectivo, transferencia o datáfono), el uso de nombres propios personalizados y la condición de cobro al entregar para tipos distintos a transferencia. Se actualizan el Modelo de dominio, Alcance, RF-020, BR-010, flujo principal, CL-008 y AC-019. Documento en estado Candidata.

## Verificación
- Completitud: cumple. Se cubrieron todas las operaciones descritas en la necesidad, en las historias aprobadas HU-03, HU-06, HU-07 y HU-08 y las decisiones DEC-E51, DEC-E53 y DEC-E57, conservando las 17 secciones completas.
- Consistencia interna: cumple. Se verificó la alineación estricta entre RF-020, BR-010, el paso 4 del flujo principal, CL-008 y AC-019 garantizando que los tipos fijos (efectivo, transferencia, datáfono), el nombre propio y la marca de cobro al entregar concuerden plenamente.
- Consistencia con el contexto: cumple. Se compararon las adiciones con la sección 3.11 del contexto, confirmando la concordancia exacta con DEC-E57 y la ausencia de cobro en línea o pasarelas integradas.
- No ambigüedad: cumple. No existen términos indeterminados; los tipos de forma de pago de la plataforma son exactamente tres (efectivo, transferencia o datáfono) y su comportamiento de cobro al entregar queda explícitamente determinado por su tipo.
- Verificabilidad: cumple. El criterio de aceptación AC-019 redactado en estructura Dado/Cuando/Entonces es totalmente medible y ejecutable por pruebas automatizadas o manuales.
- Cobertura de actores: cumple. Se mantuvo la correspondencia de las historias de usuario para Administrador del negocio y Dueño de la plataforma, así como las restricciones de acceso para Empleados y Domiciliarios.
- Cobertura de AC: cumple. Todos los requisitos funcionales (RF-001 a RF-021) y reglas de negocio (BR-001 a BR-011) poseen al menos un criterio de aceptación asignado en la sección 16.
- Trazabilidad: cumple. Todos los elementos (RF, RNF, BR, CL) están citados en la sección 16 con su origen exacto y su mecanismo o AC de verificación.
- No invención: cumple. Se respetaron al pie de la letra las declaraciones de DEC-E57 sin presuponer pasarelas externas ni comisiones.
- Delimitación: cumple. Las decisiones de arquitectura sobre la implementación técnica de datos persisten en la sección 14 sin contaminar los requisitos funcionales.

## Siguiente paso
La SPEC-002 versión 1.2 está lista para revisión. Confirmen el objetivo y el alcance, las reglas de negocio, los criterios de aceptación críticos, las restricciones y lo que está fuera de alcance. Si la aprueban, queda congelada y lista para el Architecture Agent.
