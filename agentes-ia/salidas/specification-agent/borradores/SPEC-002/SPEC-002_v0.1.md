<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.7-flash
Fecha: 2026-11-19 11:16
Petición: EPIC-001. Especifica la configuración operativa de un negocio aprobado: el administrador configura los datos del negocio y sus horarios de atención por día, obtiene el enlace, el QR y el código propios del negocio (para clientes y personal), define el tope de pedidos simultáneos por domiciliario y administra los barrios de cobertura con su tarifa; además, el dueño de la plataforma marca la suscripción del negocio al día o vencida, con la cancelación de pedidos no despachados al vencer (DEC-E26). Las historias de usuario aprobadas HU-03, HU-06, HU-07 y HU-08 están en el archivo adjunto; respétalas como entrada. La SPEC-001 aprobada (registro y vinculación) es una dependencia.
-->

# SPEC-002. Configuración operativa del negocio y suscripción - Versión 0.1

Estado: Borrador
Modo: Inicial
Necesidad original: "EPIC-001. Especifica la configuración operativa de un negocio aprobado: el administrador configura los datos del negocio y sus horarios de atención por día, obtiene el enlace, el QR y el código propios del negocio (para clientes y personal), define el tope de pedidos simultáneos por domiciliario y administra los barrios de cobertura con su tarifa; además, el dueño de la plataforma marca la suscripción del negocio al día o vencida, con la cancelación de pedidos no despachados al vencer (DEC-E26). Las historias de usuario aprobadas HU-03, HU-06, HU-07 y HU-08 están en el archivo adjunto; respétalas como entrada. La SPEC-001 aprobada (registro y vinculación) es una dependencia."
Épica: EPIC-001

## Análisis
- Objetivo: permitir que el administrador configure los datos operativos, horarios de atención, enlace/QR/código de acceso, capacidad operativa de domiciliarios y zonas tarifarias de un negocio aprobado, y que el dueño de la plataforma controle la suscripción del negocio y su impacto en pedidos no despachados.
- Alcance inicial: configuración comercial y horarios de atención por día, generación y consulta de enlace/QR/código propio del negocio, parametrización del tope de pedidos por domiciliario, gestión de barrios y tarifas de cobertura, y conmutación de estado de suscripción con cancelación atómica de pedidos no despachados.
- Actores: Administrador del negocio, Dueño de la plataforma, Empleado o vendedor (como actor de control de acceso negativo).
- Contexto aplicable: secciones 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8 y decisiones DEC-E01, DEC-E05, DEC-E07, DEC-E09, DEC-E12, DEC-E13, DEC-E26.

## Modelo de dominio
- Negocio: entidad principal aprobada previamente; pertenece a la plataforma y contiene su propia configuración operativa. Origen: contexto 2.4 y DEC-E01.
- Configuración de negocio: pertenece a un único negocio; cardinalidad uno a uno; almacena nombre comercial, dirección física, horarios de atención y tope de pedidos simultáneos. Origen: contexto 3.4 y HU-06, HU-07.
- Horario de atención: pertenece a un negocio; cardinalidad uno por día de la semana. Origen: contexto 3.4 y HU-06.
- Medio de acceso (enlace, QR, código único): pertenece a un único negocio; cardinalidad uno a uno. Origen: DEC-E05 y HU-06.
- Zona de cobertura (barrio y tarifa): pertenece a un negocio; cardinalidad de una a varias zonas activas o inactivas por negocio. Origen: contexto 3.5 y HU-08.
- Suscripción: estado comercial del negocio controlado por la plataforma; cardinalidad uno a uno por negocio; valores al día o vencido. Origen: DEC-E26 y HU-03.
- Pedido: pertenece a un negocio; cardinalidad de cero a muchos por negocio; transiciona a cancelado si no está despachado al vencer la suscripción. Origen: DEC-E13, DEC-E21, DEC-E26.

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
No aplica.

## Preguntas de aclaración
- OPEN-Q-001. ¿Cuál es el valor por defecto del tope de pedidos simultáneos por domiciliario si el administrador no lo define, y existe un límite máximo configurable (Contexto 7.1 y HU-07)?
  Por qué importa: define el valor inicial del sistema, la validación de entrada en la interfaz y los criterios de aceptación de HU-07.
  Crítica: sí
  Propuesta del agente: PROPUESTA: valor por defecto de 3 pedidos simultáneos y límite máximo permitido de 10 por domiciliario.
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-002. Para los horarios de atención por día (HU-06 y DEC-E09), ¿cómo se estructuran los rangos de operación y qué ocurre con los días de descanso?
  Por qué importa: define el formato de almacenamiento y validación de horarios, la regla de negocio para permitir o bloquear pedidos fuera de horario y los criterios de aceptación de configuración.
  Crítica: sí
  Propuesta del agente: PROPUESTA: cada día de la semana (lunes a domingo) puede marcarse como cerrado o con un único rango de hora de apertura y hora de cierre (en formato HH:MM).
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-003. En la cancelación de pedidos por suscripción vencida (HU-03 y DEC-E26), ¿cuáles estados exactos del ciclo de vida se consideran «no despachados» y qué ocurre con el domiciliario si el pedido ya estaba asignado pero no «en camino»?
  Por qué importa: define la lógica de transición atómica de pedidos al pasar la suscripción a vencida, la notificación al domiciliario asignado y el conteo previo que se le muestra al dueño de la plataforma.
  Crítica: sí
  Propuesta del agente: PROPUESTA: los estados considerados «no despachados» son recibido, en preparación y listo para recoger; si un pedido ya tenía domiciliario asignado en esos estados, se cancela y se notifica al domiciliario sobre la cancelación por suscripción vencida.
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-004. Respecto al enlace, código QR y código único del negocio (HU-06, HU-04, HU-09 y DEC-E05), ¿el código lo genera automáticamente el sistema al aprobar el negocio o lo define el administrador, y es el mismo identificador para clientes y para personal?
  Por qué importa: define los requisitos funcionales de generación y consulta de credenciales de difusión, y cómo el bot identifica el negocio en los comandos de vinculación o compra.
  Crítica: sí
  Propuesta del agente: PROPUESTA: el sistema genera automáticamente un código alfanumérico único al aprobar el establecimiento, usado como parámetro en el enlace y QR para clientes; el personal usa ese mismo código para postularse.
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-005. Para la parametrización de zonas de cobertura (HU-08), ¿se permite registrar una tarifa de $0 COP (domicilio gratuito) y qué reglas aplican sobre nombres duplicados o tarifas mínimas/máximas?
  Por qué importa: define las validaciones de entrada para creación y actualización de barrios, evitando registros inconsistentes o cobros negativos.
  Crítica: sí
  Propuesta del agente: PROPUESTA: permitir tarifa de $0 COP o valores enteros positivos hasta un tope razonable (ej. $50.000 COP), exigiendo que el nombre del barrio sea único dentro del mismo negocio.
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-006. Si el administrador reduce el tope de pedidos simultáneos a un valor inferior al número de pedidos que un domiciliario tiene asignados en ese momento (HU-07), ¿qué comportamiento debe tener el sistema con las asignaciones vigentes?
  Por qué importa: define si la regla de capacidad afecta retroactivamente la operación en curso o solo restringe nuevas asignaciones.
  Crítica: no
  Propuesta del agente: PROPUESTA: los pedidos ya asignados se respetan y concluyen su ciclo normal, pero el sistema bloquea cualquier asignación nueva a ese domiciliario hasta que su carga baje por debajo del nuevo tope.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Permitir la parametrización operativa integral de un negocio aprobado por parte de su administrador (datos comerciales, horarios de atención, identificadores de difusión, tope de pedidos simultáneos y zonas tarifarias) y facultar al dueño de la plataforma para controlar la suscripción del negocio, suspendiendo la recepción de pedidos y cancelando de forma atómica los pedidos no despachados al vencer.

### 2. Contexto
En Domiciliarios Eje cada negocio opera de forma aislada. Una vez un negocio es aprobado por el dueño de la plataforma (SPEC-001), el administrador requiere configurar las condiciones de servicio para atender clientes y coordinar repartidores. A su vez, la plataforma opera bajo un modelo de mensualidad fija, por lo que el dueño de la plataforma gestiona manualmente el estado de suscripción.

Decisiones del equipo:
- Ninguna decisión registrada en esta iteración. Todas las preguntas permanecen pendientes.

### 3. Alcance
- Consulta y actualización de datos comerciales del negocio (nombre comercial y dirección).
- Configuración de horarios de atención por cada día de la semana.
- Generación y consulta del enlace directo, código QR y código alfanumérico del negocio para clientes y postulantes.
- Definición y actualización del tope de pedidos simultáneos por domiciliario para el negocio.
- Creación, actualización de tarifa y desactivación de zonas de cobertura (barrios).
- Conmutación del estado de suscripción (al día o vencido) por parte del dueño de la plataforma, incluyendo conteo previo, confirmación obligatoria, cese de recepción de pedidos y cancelación atómica de pedidos no despachados con notificación a clientes y negocio.

### 4. Actores e historias de usuario
Actores:
- Administrador del negocio: gestiona la configuración comercial, horarios, capacidad de domiciliarios y cobertura tarifaria de su establecimiento.
- Dueño de la plataforma: administra el estado de suscripción de los negocios registrados.
- Empleado o vendedor: usuario con permisos operativos que tiene restringida la modificación de la configuración general y suscripción.

Historias de usuario:
- HU-001 (HU-06). Como Administrador del negocio, quiero configurar los datos generales, los horarios de atención y consultar el enlace y código QR de mi establecimiento, para definir las condiciones de servicio y permitir la llegada directa de mis clientes sin intermediarios ni directorios públicos.
- HU-002 (HU-07). Como Administrador del negocio, quiero definir el número máximo de pedidos simultáneos asignables a un domiciliario en mi negocio, para regular la carga de trabajo de los repartidores y la puntualidad del servicio.
- HU-003 (HU-08). Como Administrador del negocio, quiero registrar y actualizar los barrios de cobertura con su tarifa de entrega, para determinar dónde entrega mi establecimiento y cuánto se cobrará por cada envío.
- HU-004 (HU-03). Como Dueño de la plataforma, quiero actualizar el estado de suscripción de un negocio entre al día y vencido, para asegurar que solo los establecimientos con mensualidad activa puedan recibir pedidos.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir al administrador del negocio actualizar el nombre comercial y la dirección física de su establecimiento, validando la autorización y pertenencia en el backend. Origen: HU-06 y contexto 3.2.
- RF-002. El sistema debe permitir al administrador del negocio configurar el horario de atención para cada día de la semana, indicando si abre y los rangos de operación. Origen: HU-06 e inferido, requiere confirmación (OPEN-Q-002).
- RF-003. El sistema debe entregar al administrador del negocio el enlace directo, el código QR y el código alfanumérico identificador de su establecimiento para interacción por Telegram. Origen: HU-06, DEC-E05 y HU-04.
- RF-004. El sistema debe impedir que un usuario consulte o modifique datos comerciales, horarios o enlaces de un negocio distinto al que pertenece. Origen: contexto 3.3 y HU-06.
- RF-005. El sistema debe permitir al administrador del negocio registrar y actualizar el tope de pedidos simultáneos por domiciliario con un número entero positivo. Origen: HU-07 y DEC-E12.
- RF-006. El sistema debe asignar un valor por defecto al tope de pedidos simultáneos cuando el negocio es aprobado y el administrador no ha definido un valor explícito. Origen: HU-07 e inferido, requiere confirmación (OPEN-Q-001).
- RF-007. El sistema debe rechazar valores menores o iguales a cero o formatos no numéricos al configurar el tope de pedidos simultáneos. Origen: HU-07.
- RF-008. El sistema debe restringir la configuración del tope de pedidos simultáneos exclusivamente al rol de Administrador del negocio, rechazando intentos de empleados u otros roles. Origen: HU-07 y contexto 3.2.
- RF-009. El sistema debe permitir al administrador del negocio registrar barrios de cobertura ingresando nombre del sector y valor de tarifa de entrega en pesos colombianos. Origen: HU-08 y contexto 3.5.
- RF-010. El sistema debe permitir al administrador del negocio modificar la tarifa de entrega de un barrio existente, aplicando la nueva tarifa únicamente a pedidos futuros. Origen: HU-08.
- RF-011. El sistema debe permitir al administrador del negocio desactivar un barrio de cobertura, impidiendo cotizaciones de pedidos futuros hacia ese sector y preservando el histórico anterior. Origen: HU-08.
- RF-012. El sistema debe validar que el registro y modificación de barrios y tarifas solo opere sobre los datos del negocio del administrador autenticado. Origen: contexto 3.3 y HU-08.
- RF-013. El sistema debe permitir al dueño de la plataforma consultar los negocios registrados y su estado de suscripción actual (al día o vencido), sin exponer datos de pedidos, clientes ni domiciliarios. Origen: contexto 2.3, DEC-E01 y HU-03.
- RF-014. Antes de marcar una suscripción como vencida, el sistema debe calcular y mostrar al dueño de la plataforma la cantidad exacta de pedidos no despachados que serán cancelados y solicitar confirmación explícita. Origen: DEC-E26 y HU-03.
- RF-015. Al confirmar el cambio a estado vencido, el sistema debe cambiar atómicamente el estado del negocio a vencido, impedir el ingreso de pedidos nuevos y cancelar todos los pedidos no despachados registrando motivo «suscripción vencida» y responsable Dueño de la plataforma. Origen: DEC-E26, DEC-E13 y HU-03.
- RF-016. Al ejecutarse la cancelación de pedidos por suscripción vencida, el sistema debe enviar una notificación por Telegram a los clientes afectados y al administrador del negocio informando la cancelación. Origen: DEC-E26 y HU-03.
- RF-017. El sistema debe permitir que los pedidos que ya se encuentren en estado «en camino» continúen su entrega habitual cuando el negocio pase a suscripción vencida. Origen: DEC-E26 y HU-03.
- RF-018. El sistema debe permitir al dueño de la plataforma reactivar un negocio con suscripción vencida pasándolo a «al día», previa confirmación, habilitando nuevamente la recepción de pedidos. Origen: HU-03 y DEC-E26.
- RF-019. El sistema debe rechazar cualquier intento de modificar el estado de suscripción realizado por administradores, empleados o domiciliarios. Origen: contexto 2.3 y HU-03.

### 6. Requisitos no funcionales
- RNF-001. Autorización y seguridad. Toda operación de consulta o modificación de configuración y suscripción debe validar identidad, rol, negocio y permisos en el backend. Se verifica con: prueba de integración simulando peticiones con token/rol manipulado hacia el backend. Origen: contexto 3.2.
- RNF-002. Aislamiento multiinquilino. Ninguna consulta de configuración o zonas debe retornar o alterar registros pertenecientes a otro identificador de negocio. Se verifica con: prueba automatizada de acceso cruzado entre identificadores de negocio distintos. Origen: contexto 3.3.
- RNF-003. Atomicidad y consistencia. La transición de suscripción a vencida y la cancelación masiva de pedidos no despachados deben ejecutarse dentro de una transacción atómica para evitar estados inconsistentes. Se verifica con: prueba de carga concurrente simulando fallos durante la conmutación de estado. Origen: contexto 3.8.
- RNF-004. Usabilidad en Telegram. Los menús de configuración de horarios, topes y tarifas deben presentarse mediante formularios y botones en el bot con confirmación previa a la persistencia. Se verifica con: inspección de interfaz y flujos conversacionales en bot de prueba. Origen: contexto 3.1 y contexto 3.7.

### 7. Reglas de negocio
- BR-001. Exclusividad de gestión de configuración. Solo el usuario con rol de Administrador activo del negocio puede modificar datos comerciales, horarios, enlace/código, topes y barrios de cobertura de su negocio. Origen: contexto 3.4 y HU-06, HU-07, HU-08.
- BR-002. Exclusividad de control de suscripción. Solo el usuario con rol de Dueño de la plataforma puede visualizar el panel de suscripciones y conmutar el estado de suscripción de un negocio. Origen: contexto 2.3 y HU-03.
- BR-003. Restricción de pedidos en negocio vencido. Un negocio con suscripción en estado vencido no puede recibir pedidos nuevos de clientes bajo ninguna circunstancia. Origen: DEC-E26 y HU-03.
- BR-004. Cancelación por vencimiento. Todo pedido en estado no despachado (recibido, en preparación o listo para recoger) de un negocio cuya suscripción pasa a vencida debe pasar inmediatamente al estado final cancelado con motivo «suscripción vencida». Origen: DEC-E13, DEC-E26 e inferido, requiere confirmación (OPEN-Q-003).
- BR-005. Continuidad de pedidos en ruta. Los pedidos que se encuentren en estado «en camino» al momento de vencer la suscripción no se cancelan y deben seguir su flujo normal hasta terminar como entregado o con novedad. Origen: DEC-E26 y DEC-E22.
- BR-006. Validación de tope de pedidos. El tope de pedidos simultáneos por domiciliario debe ser un número entero mayor estricto que cero (tope >= 1). Pendiente de valor por defecto y techo máximo por OPEN-Q-001. Origen: HU-07 y DEC-E12.
- BR-007. No eliminación de barrios históricos. Un barrio de cobertura no puede borrarse físicamente del sistema si tiene pedidos asociados; solo puede marcarse como inactivo para no admitir nuevos pedidos. Origen: HU-08.
- BR-008. Unicidad de barrio en el negocio. Un negocio no puede registrar dos zonas de cobertura con el mismo nombre normalizado. Origen: inferido, requiere confirmación (OPEN-Q-005).
- BR-009. Generación de medios de difusión. Cada negocio aprobado tiene asignado un código único permanente que compone su enlace directo de Telegram (`t.me/<bot>?start=<codigo>`) y su respectivo código QR. Origen: DEC-E05, HU-06 e inferido, requiere confirmación (OPEN-Q-004).

Estados y ciclo de vida de la suscripción del negocio:
- Estados posibles de suscripción: al día, vencido.
- Transición 1: al día -> vencido. Provocada por: Dueño de la plataforma tras confirmar cantidad de pedidos a cancelar. Efecto colateral: cancela pedidos no despachados y cierra recepción de pedidos.
- Transición 2: vencido -> al día. Provocada por: Dueño de la plataforma tras confirmar reactivación. Efecto colateral: reabre recepción de pedidos.

### 8. Flujo principal
1. El administrador del negocio autenticado en Telegram selecciona el comando de configuración de su establecimiento.
2. El sistema valida en el backend el rol de Administrador y obtiene los datos del negocio asociado.
3. El administrador selecciona la opción deseada: datos generales, horarios de atención, medios de difusión (enlace/QR/código), tope de pedidos por domiciliario o zonas de cobertura.
4. Para datos comerciales y horarios: el administrador ingresa los nuevos valores, el sistema valida estructura y almacena los cambios.
5. Para medios de difusión: el sistema genera y despliega el enlace directo, el código alfanumérico y la imagen del código QR para compartir a clientes y personal.
6. Para tope de domiciliarios: el administrador digita un entero positivo, el sistema valida que sea mayor a cero y actualiza el parámetro operativo.
7. Para zonas de cobertura: el administrador registra un barrio nuevo con su tarifa en pesos o actualiza/inactiva un barrio existente; el sistema valida y confirma el cambio.
8. El sistema muestra mensaje de confirmación y resumen de la configuración actualizada.

Flujo principal de control de suscripción (Dueño de la plataforma):
1. El dueño de la plataforma autenticado ingresa al bot y consulta la lista de negocios registrados.
2. El sistema presenta la lista de negocios con su estado de suscripción (al día o vencido) sin mostrar datos operativos internos.
3. El dueño selecciona un negocio con suscripción al día y presiona marcar como vencido.
4. El sistema cuenta los pedidos no despachados de ese negocio y presenta mensaje de advertencia solicitando confirmación.
5. El dueño de la plataforma confirma la acción.
6. El sistema, de manera atómica, cambia el estado a vencido, bloquea nuevos pedidos, cancela los pedidos no despachados registrando motivo y responsable, y notifica a clientes y al negocio.

### 9. Flujos alternativos y de excepción
- A1. Reactivación de suscripción: En el paso 3 del flujo de suscripción, el dueño selecciona un negocio en estado vencido y elige marcar al día; el sistema pide confirmación y al aceptar conmuta el estado a al día y habilita la recepción de pedidos sin alterar los pedidos históricos.
- A2. Modificación de tarifa de barrio existente: En el paso 7 del flujo de configuración, el administrador elige un barrio previamente creado e introduce un nuevo valor monetario; el sistema actualiza el registro para pedidos futuros.
- A3. Inactivación de barrio: En el paso 7, el administrador selecciona desactivar una zona; el sistema marca el sector como no disponible para nuevos pedidos y notifica éxito.
- E1. Usuario no autorizado intenta configurar negocio: Un usuario con rol de empleado, domiciliario o cliente envía comandos de configuración; el sistema verifica permisos en backend, rechaza la operación y no muestra datos.
- E2. Administrador intenta acceder a otro negocio: Una solicitud intenta modificar parámetros de un negocio ajeno; el sistema detecta inconsistencia en backend y bloquea el acceso.
- E3. Valor de tope inválido: El administrador ingresa cero, un número negativo o caracteres alfanuméricos al definir el tope de domiciliarios; el sistema rechaza la entrada, emite mensaje de error y mantiene el valor anterior.
- E4. Usuario no autorizado intenta modificar suscripción: Un administrador o empleado envía instrucción de cambio de suscripción; el backend valida que no es Dueño de la plataforma y deniega la acción.
- E5. Cancelación de acción de vencimiento: El dueño de la plataforma cancela la confirmación tras ver el número de pedidos afectados; el sistema no altera la suscripción ni los pedidos.

### 10. Casos límite
- CL-001. Suscripción vencida sin pedidos pendientes: El dueño de la plataforma marca como vencido un negocio que tiene cero pedidos no despachados; el sistema muestra 0 pedidos a cancelar, pide confirmación, pasa a vencido y bloquea nuevos pedidos sin generar errores. Origen: HU-03.
- CL-002. Pedidos en camino al vencer suscripción: Existen pedidos en estado «en camino» cuando se confirma el vencimiento; dichos pedidos permanecen en su estado y no son cancelados, completando su ciclo normalmente. Origen: DEC-E26 y HU-03.
- CL-003. Concurrencia al conmutar suscripción y recibir pedido: Un cliente intenta confirmar un pedido en el mismo instante en que el dueño de la plataforma confirma el vencimiento; la transacción atómica rechaza el pedido del cliente informando que el negocio no está disponible. Origen: contexto 3.8 y RNF-003.
- CL-004. Reducción de tope de pedidos con domiciliarios saturados: El administrador reduce el tope a un valor menor a la cantidad de pedidos que un repartidor tiene actualmente en curso; los pedidos vigentes continúan, pero no se permite asignarle ninguno más hasta quedar por debajo del nuevo tope. Origen: inferido, requiere confirmación (OPEN-Q-006).
- CL-005. Configuración de tarifa en cero pesos ($0 COP): El administrador ingresa una tarifa de 0 pesos para un barrio céntrico; el sistema valida si el costo cero es permitido como domicilio gratuito. Pendiente de confirmación por OPEN-Q-005. Origen: HU-08.
- CL-006. Cambio de horario durante la operación: El administrador adelanta la hora de cierre a una hora anterior a la hora actual mientras hay pedidos en preparación; los pedidos existentes continúan su curso y los nuevos pedidos de clientes se bloquean por estar fuera de horario. Origen: DEC-E09 y contexto 3.4.

### 11. Criterios de aceptación
- AC-001. Autorización de datos comerciales: Dado un usuario autenticado con rol de Administrador del negocio A, cuando actualiza el nombre comercial y la dirección de su establecimiento, entonces el sistema almacena los datos y confirma la operación.
- AC-002. Aislamiento de configuración: Dado un usuario autenticado como Administrador del negocio A, cuando intenta modificar la configuración comercial o de zonas del negocio B, entonces el sistema rechaza la petición y los datos de B no sufren modificaciones.
- AC-003. Bloqueo de configuración a otros roles: Dado un usuario con rol de Empleado o Domiciliario, cuando intenta acceder o enviar cambios a la configuración operativa del negocio, entonces el sistema deniega el acceso informando permisos insuficientes.
- AC-004. Consulta de enlace, QR y código: Dado un negocio en estado activo, cuando su administrador consulta los medios de difusión en el bot, entonces el sistema retorna el enlace exclusivo, el código alfanumérico y la imagen QR con el parámetro del establecimiento.
- AC-005. Configuración válida de tope de domiciliarios: Dado un administrador en la opción de tope operativo, cuando ingresa un número entero positivo mayor a cero, entonces el sistema actualiza el valor de capacidad máxima por domiciliario del negocio.
- AC-006. Rechazo de tope menor o igual a cero: Dado un administrador configurando el tope operativo, cuando ingresa el valor 0, un número negativo o texto, entonces el sistema rechaza la actualización y muestra un mensaje indicando que debe ser un entero positivo.
- AC-007. Registro de barrio nuevo: Dado un administrador configurando zonas, cuando ingresa el nombre de un barrio no registrado previamente y una tarifa monetaria válida, entonces el sistema guarda la zona como activa para su establecimiento.
- AC-008. Actualización de tarifa en zona existente: Dado un barrio previamente configurado en el negocio, cuando el administrador actualiza su tarifa de domicilio, entonces los pedidos cotizados a partir de ese momento calculan la nueva tarifa y los anteriores no se modifican.
- AC-009. Suspensión de cobertura de barrio: Dado un barrio activo en el negocio, cuando el administrador cambia su estado a inactivo, entonces el sistema impide cotizar domicilios hacia ese barrio en nuevos pedidos y preserva el registro histórico.
- AC-010. Consulta de suscripción sin datos sensibles: Dado el dueño de la plataforma autenticado en el bot, cuando consulta el estado de los negocios, entonces el sistema muestra el listado con nombre de establecimiento y estado de suscripción sin exponer pedidos, clientes ni repartidores.
- AC-011. Conteo y advertencia antes de vencer suscripción: Dado un negocio con suscripción al día que posee pedidos en estado recibido, en preparación o listo para recoger, cuando el dueño de la plataforma selecciona marcar como vencido, entonces el sistema presenta el número exacto de pedidos que serán cancelados y solicita confirmación.
- AC-012. Confirmación de vencimiento y cancelación atómica: Dado que el dueño de la plataforma confirma marcar como vencido un negocio, cuando el sistema procesa el cambio, entonces la suscripción pasa a vencida, los pedidos en recibido, en preparación y listo para recoger quedan en estado cancelado con motivo «suscripción vencida» y responsable Dueño de la plataforma, y el negocio no admite pedidos nuevos.
- AC-013. Notificación de cancelación por suscripción: Dado un pedido cancelado por paso de suscripción a vencida, cuando se ejecuta la cancelación masiva, entonces el sistema envía un mensaje por Telegram al cliente informando la cancelación del pedido por vencimiento de suscripción del negocio.
- AC-014. Continuidad de pedidos en camino: Dado un pedido en estado «en camino» perteneciente a un negocio que pasa a suscripción vencida, cuando se aplica el vencimiento, entonces el pedido permanece en estado «en camino» y permite al domiciliario finalizarlo como entregado o con novedad.
- AC-015. Reactivación de suscripción: Dado un negocio en estado vencido, cuando el dueño de la plataforma selecciona marcar al día y confirma, entonces el sistema actualiza el estado a al día y el bot vuelve a admitir pedidos en el horario de atención configurado.
- AC-016. Rechazo de control de suscripción a no administradores de plataforma: Dado un usuario con rol de Administrador del negocio o Empleado, cuando intenta ejecutar el comando de conmutación de suscripción, entonces el sistema rechaza la solicitud por falta de autorización.
- AC-017. Asignación de tope por defecto: Dado un negocio recientemente aprobado que no ha configurado su tope, cuando se consulta su capacidad máxima de asignación, entonces el sistema aplica el valor por defecto configurado a nivel de plataforma.
- AC-018. Bloqueo de pedidos fuera de horario configurado: Dado un horario configurado para el día actual, cuando un cliente intenta iniciar un pedido fuera de la franja horaria establecida, entonces el bot le informa que el establecimiento se encuentra cerrado y no permite el registro.

### 12. Dependencias
- SPEC-001: Registro y vinculación (establece el alta de negocios aprobados, roles y autenticación de usuarios).
- Telegram Bot API: canal de interacción conversacional y entrega de enlaces y códigos QR.
- Repositorio de configuración y suscripción: almacenamiento persistente de horarios, parámetros de carga y tarifas por negocio.

### 13. Restricciones
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
- [Estrategia de transacción distribuida o bloqueo para cancelación atómica de pedidos]: tema para arquitectura. Origen: RF-015 y RNF-003.

### 15. Preguntas abiertas
- OPEN-Q-001: Pendiente.
- OPEN-Q-002: Pendiente.
- OPEN-Q-003: Pendiente.
- OPEN-Q-004: Pendiente.
- OPEN-Q-005: Pendiente.
- OPEN-Q-006: Pendiente.

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-004; BR-001, BR-009; AC-001, AC-002, AC-003, AC-004, AC-018; CL-006.
- HU-002: RF-005, RF-006, RF-007, RF-008; BR-006; AC-005, AC-006, AC-017; CL-004.
- HU-003: RF-009, RF-010, RF-011, RF-012; BR-007, BR-008; AC-007, AC-008, AC-009; CL-005.
- HU-004: RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019; BR-002, BR-003, BR-004, BR-005; AC-010, AC-011, AC-012, AC-013, AC-014, AC-015, AC-016; CL-001, CL-002, CL-003.
- RF-001: Origen: HU-06 y contexto 3.2; verificado por AC-001.
- RF-002: Origen: HU-06 e inferido, requiere confirmación (OPEN-Q-002); verificado por AC-018.
- RF-003: Origen: HU-06, DEC-E05 y HU-04; verificado por AC-004.
- RF-004: Origen: contexto 3.3 y HU-06; verificado por AC-002.
- RF-005: Origen: HU-07 y DEC-E12; verificado por AC-005.
- RF-006: Origen: HU-07 e inferido, requiere confirmación (OPEN-Q-001); verificado por AC-017.
- RF-007: Origen: HU-07; verificado por AC-006.
- RF-008: Origen: HU-07 y contexto 3.2; verificado por AC-003.
- RF-009: Origen: HU-08 y contexto 3.5; verificado por AC-007.
- RF-010: Origen: HU-08; verificado por AC-008.
- RF-011: Origen: HU-08; verificado por AC-009.
- RF-012: Origen: contexto 3.3 y HU-08; verificado por AC-002.
- RF-013: Origen: contexto 2.3, DEC-E01 y HU-03; verificado por AC-010.
- RF-014: Origen: DEC-E26 y HU-03; verificado por AC-011.
- RF-015: Origen: DEC-E26, DEC-E13 y HU-03; verificado por AC-012.
- RF-016: Origen: DEC-E26 y HU-03; verificado por AC-013.
- RF-017: Origen: DEC-E26 y HU-03; verificado por AC-014.
- RF-018: Origen: HU-03 y DEC-E26; verificado por AC-015.
- RF-019: Origen: contexto 2.3 y HU-03; verificado por AC-016.
- RNF-001: Origen: contexto 3.2; verificado con prueba de integración simulando peticiones con token/rol manipulado hacia el backend.
- RNF-002: Origen: contexto 3.3; verificado con prueba automatizada de acceso cruzado entre identificadores de negocio distintos.
- RNF-003: Origen: contexto 3.8; verificado con prueba de carga concurrente simulando fallos durante la conmutación de estado.
- RNF-004: Origen: contexto 3.1 y contexto 3.7; verificado con inspección de interfaz y flujos conversacionales en bot de prueba.
- BR-001: Origen: contexto 3.4 y HU-06, HU-07, HU-08; verificado por AC-001, AC-003.
- BR-002: Origen: contexto 2.3 y HU-03; verificado por AC-010, AC-016.
- BR-003: Origen: DEC-E26 y HU-03; verificado por AC-012.
- BR-004: Origen: DEC-E13, DEC-E26 e inferido, requiere confirmación (OPEN-Q-003); verificado por AC-012.
- BR-005: Origen: DEC-E26 y DEC-E22; verificado por AC-014.
- BR-006: Origen: HU-07 y DEC-E12; verificado por AC-005, AC-006.
- BR-007: Origen: HU-08; verificado por AC-009.
- BR-008: Origen: inferido, requiere confirmación (OPEN-Q-005); verificado por AC-007.
- BR-009: Origen: DEC-E05, HU-06 e inferido, requiere confirmación (OPEN-Q-004); verificado por AC-004.
- CL-001: Origen: HU-03; verificado por AC-011.
- CL-002: Origen: DEC-E26 y HU-03; verificado por AC-014.
- CL-003: Origen: contexto 3.8 y RNF-003; verificado por AC-012.
- CL-004: Origen: inferido, requiere confirmación (OPEN-Q-006); verificado por AC-005.
- CL-005: Origen: HU-08; verificado por AC-007.
- CL-006: Origen: DEC-E09 y contexto 3.4; verificado por AC-018.

### 17. Historial de cambios
- Versión 0.1: creación de la especificación a partir de la necesidad y las historias de usuario HU-03, HU-06, HU-07 y HU-08 de EPIC-001. Se mantienen las 6 preguntas abiertas en estado pendiente y el documento en estado Borrador.

## Verificación
- Completitud: cumple. Se cubrieron todas las operaciones descritas en la necesidad y en las historias aprobadas HU-03, HU-06, HU-07 y HU-08, con sus 17 secciones completas.
- Consistencia interna: cumple. Los requisitos funcionales, reglas de negocio, flujos y criterios de aceptación coinciden en el comportamiento ante cambios de suscripción, asignación de topes y cobertura de zonas.
- Consistencia con el contexto: cumple. Se verificaron las decisiones DEC-E01, DEC-E05, DEC-E07, DEC-E09, DEC-E12, DEC-E13, DEC-E26 y los principios de separación multiinquilino (3.3) y validación en backend (3.2).
- No ambigüedad: cumple. Los vacíos de valores concretos y detalles de implementación no definidos por el equipo se formularon explícitamente como preguntas abiertas (OPEN-Q-001 a OPEN-Q-006).
- Verificabilidad: cumple. Cada criterio de aceptación está redactado en formato Dado/Cuando/Entonces con resultados observables y métodos definidos para requisitos no funcionales.
- Cobertura de actores: cumple. Se especificaron historias de usuario y criterios de autorización para el Administrador del negocio y el Dueño de la plataforma, incluyendo casos de denegación para Empleados y Domiciliarios.
- Cobertura de AC: cumple. Todos los requisitos funcionales y reglas de negocio cuentan con al menos un criterio de aceptación asociado.
- Trazabilidad: cumple. Todos los RF, RNF, BR y CL cuentan con su identificador de origen y enlace de verificación en la sección 16.
- No invención: cumple. No se inventaron valores por defecto, pasarelas de pago ni integraciones no mencionadas; los puntos abiertos se marcaron como inferencias con preguntas pendientes.
- Delimitación: cumple. Los aspectos técnicos de persistencia distribuida y codificación de imágenes QR se remitieron a la sección 14 para arquitectura, y se mantuvieron las exclusiones de la sección 5 del contexto.

## Siguiente paso
Respondan las preguntas abiertas y ejecuten de nuevo el agente con --continuar SPEC-002.
