<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-21 15:29
Petición: SPEC-007. EPIC-005. Especifica el historial y los reportes del negocio: historial de pedidos filtrable por fecha, estado, domiciliario y zona, y trazabilidad de estados de un pedido con fecha, estado y responsable (contexto 3.8, 3.9); reporte de pedidos por fecha y estado, reporte de pedidos y valor de domicilios por zona, y reporte de ventas del catálogo con productos más pedidos (DEC-E18); valores y ventas cuentan solo pedidos entregados y los demás estados se muestran aparte (DEC-E34); productos desactivados siguen en los reportes (DEC-E28); el administrador ve historial, trazabilidad y reportes y el empleado solo historial y trazabilidad (DEC-E33); cada negocio solo ve sus datos (contexto 3.3) y el dueño de la plataforma no ve nada de los negocios. Las historias aprobadas están en el archivo adjunto: usa HU-33 a HU-36. Dependencias: SPEC-003, SPEC-004, SPEC-005 y SPEC-006. Es una sola funcionalidad.
-->

# SPEC-007. Historial y reportes del negocio - Versión 0.1

Estado: Borrador
Modo: Inicial
Necesidad original: "Especifica el historial y los reportes del negocio: historial de pedidos filtrable por fecha, estado, domiciliario y zona, y trazabilidad de estados de un pedido con fecha, estado y responsable (contexto 3.8, 3.9); reporte de pedidos por fecha y estado, reporte de pedidos y valor de domicilios por zona, y reporte de ventas del catálogo con productos más pedidos (DEC-E18); valores y ventas cuentan solo pedidos entregados y los demás estados se muestran aparte (DEC-E34); productos desactivados siguen en los reportes (DEC-E28); el administrador ve historial, trazabilidad y reportes y el empleado solo historial y trazabilidad (DEC-E33); cada negocio solo ve sus datos (contexto 3.3) y el dueño de la plataforma no ve nada de los negocios. Las historias aprobadas están en el archivo adjunto: usa HU-33 a HU-36. Dependencias: SPEC-003, SPEC-004, SPEC-005 y SPEC-006. Es una sola funcionalidad."
Épica: EPIC-005

## Análisis
- Objetivo: Permitir que el administrador y los empleados de un negocio consulten la trazabilidad y el historial filtrable de los pedidos de su negocio, y que el administrador acceda a reportes consolidados operativos y de ventas, garantizando el aislamiento de información entre negocios y la protección de datos personales.
- Alcance inicial: Consulta de la cronología de eventos de un pedido, búsqueda filtrada de pedidos en el historial del negocio, generación de reporte operativo de pedidos por estado, reporte de despachos y recaudo de domicilio por zona, y reporte de ventas del catálogo con productos activos y desactivados.
- Actores: Administrador del negocio, Empleado o vendedor, Domiciliario, Cliente y Dueño de la plataforma.
- Contexto aplicable: Contexto 2.3 (roles y límites del dueño de la plataforma), 3.2 (autenticación y autorización backend), 3.3 (separación de información por negocio y protección de datos), 3.8 (trazabilidad y registros de cambios de estado), 3.9 (historial y reportes básicos), y decisiones DEC-E18, DEC-E28, DEC-E33, DEC-E34.

## Modelo de dominio
- Negocio: entidad principal. A él pertenecen los pedidos, zonas, usuarios y productos. Origen: contexto 2.4.
- Pedido: pertenece a un solo Negocio. Posee historial de estados (trazabilidad) y un Domiciliario asignado opcional. Cardinalidad: un Negocio tiene varios Pedidos. Origen: contexto 2.4, 3.8.
- Cambio de estado (Evento de trazabilidad): pertenece a un Pedido. Contiene fecha, hora, estado alcanzado y usuario responsable. Cardinalidad: un Pedido tiene uno o varios Cambios de estado. Origen: contexto 3.8.
- Zona de cobertura: pertenece a un Negocio. Asociada a los Pedidos entregados o gestionados en ella. Cardinalidad: un Negocio tiene varias Zonas. Origen: contexto 2.4, 3.5.
- Producto del catálogo: pertenece a un Negocio. Puede estar activo, agotado o desactivado. Registrado en los Pedidos. Cardinalidad: un Negocio tiene varios Productos. Origen: contexto 3.11, DEC-E28, DEC-E46.

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
No aplica.

## Preguntas de aclaración
- OPEN-Q-001. ¿Cuál es el rango de fechas por defecto cuando el administrador o el empleado ingresan al historial o a los reportes sin especificar un rango explícito?
  Por qué importa: define el comportamiento inicial de la consulta de historial (HU-34) y de la generación de reportes (HU-35, HU-36) cuando el usuario no envía parámetros de fecha.
  Crítica: sí
  Propuesta del agente: Mostrar los registros del día actual (desde las 00:00 hasta las 23:59 del día de la consulta).
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-002. En el reporte de pedidos por fecha y estado (HU-35 / DEC-E18), ¿los resultados dentro del rango de fechas seleccionado se agrupan por cada día (desglose diario) o se presentan únicamente como un total consolidado por estado de todo el período?
  Por qué importa: define la estructura del consolidado y la forma exacta en que se deben calcular y presentar las cifras en la HU-35.
  Crítica: sí
  Propuesta del agente: Presentar el total consolidado por estado para todo el período consultado y, si el rango es mayor a 1 día, incluir el desglose por día.
  Estado: Pendiente
  Responsable: equipo
- OPEN-Q-003. En el reporte de ventas del catálogo (HU-36), cuando dos productos tienen exactamente la misma cantidad de unidades entregadas en el período, ¿cuál es el criterio secundario para desempatar el ordenamiento?
  Por qué importa: permite definir criterios de aceptación deterministas y verificables para el ordenamiento de productos más vendidos.
  Crítica: no
  Propuesta del agente: Ordenar alfabéticamente por el nombre del producto en forma ascendente como criterio secundario.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Proporcionar a los usuarios autorizados del negocio (administrador y empleado) la capacidad de auditar la trazabilidad detallada y consultar el historial filtrable de sus pedidos, y permitir exclusivamente al administrador generar reportes operativos de servicio y de ventas del catálogo para respaldar la toma de decisiones.

### 2. Contexto
Cada negocio opera sus domicilios en Telegram de forma autónoma. Para controlar la operación y atender reclamos, el personal necesita auditar qué ocurrió con cada pedido (trazabilidad de fechas, estados y responsables) y buscar pedidos pasados. Asimismo, la administración requiere evaluar el desempeño por zona y el volumen de ventas por producto. La plataforma garantiza que ningún negocio acceda a los datos de otro y que el dueño de la plataforma no tenga visibilidad sobre la operación comercial de los negocios.

Decisiones del equipo:
- DEC-E18. Reportes para la demostración: pedidos por fecha y estado, pedidos y valor de domicilios por zona, y ventas del catálogo.
- DEC-E28. Un producto se desactiva, no se borra: deja de mostrarse a los clientes y se conserva en los pedidos anteriores y reportes.
- DEC-E33. El administrador ve historial, trazabilidad, reportes y recorridos de su negocio; el empleado ve historial y trazabilidad, pero no los reportes.
- DEC-E34. Los valores de domicilios por zona y las ventas del catálogo cuentan solo pedidos entregados; los demás estados se muestran aparte.

### 3. Alcance
- Consulta de trazabilidad de un pedido individual (fecha, hora, estado alcanzado, responsable y detalles de entregas o novedades).
- Consulta de historial de pedidos del negocio con filtros por rango de fechas, estado, domiciliario asignado y zona de cobertura.
- Reporte operativo consolidado de pedidos por fecha y estado en un rango seleccionado.
- Reporte operativo de despachos y recaudo por tarifas de domicilio desglosado por zona de cobertura.
- Reporte de ventas del catálogo con ordenamiento de productos por unidades entregadas y montos totales, conservando la visibilidad de productos desactivados.
- Controles de autorización backend para restringir los reportes al administrador y aislar los datos entre negocios.

### 4. Actores e historias de usuario
Actores: Administrador del negocio, Empleado o vendedor, Domiciliario, Cliente, Dueño de la plataforma.

- HU-33. Como empleado o vendedor, quiero consultar la cronología completa de cambios de estado de un pedido específico, para verificar qué ocurrió en el servicio y atender cualquier reclamo o duda con información fehaciente.
- HU-34. Como empleado o vendedor, quiero filtrar el historial de pedidos de mi negocio por fecha, estado, domiciliario y zona, para ubicar rápidamente entregas anteriores y revisar la operación diaria.
- HU-35. Como administrador del negocio, quiero generar un reporte consolidado de pedidos por estado y por zona de cobertura en un período seleccionado, para evaluar el volumen de entregas y el recaudo por tarifas de domicilio en cada sector.
- HU-36. Como administrador del negocio, quiero consultar el reporte de ventas del catálogo identificando los productos más pedidos en un rango de fechas, para analizar las preferencias de los clientes y el rendimiento de mis productos sin perder el histórico de los que ya no vendo.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir a los usuarios con rol Administrador o Empleado consultar la trazabilidad cronológica de un pedido perteneciente a su negocio, mostrando la secuencia de cambios de estado con fecha, hora exacta, estado resultante y usuario responsable de cada evento. Origen: contexto 3.8, DEC-E33, HU-33.
- RF-002. En la consulta de trazabilidad e historial, el sistema debe presentar el resumen del servicio sin exponer datos personales del cliente que no estén autorizados para el rol del usuario solicitante. Origen: contexto 3.3, Regla crítica 7, HU-33, HU-34.
- RF-003. El sistema debe permitir a los usuarios con rol Administrador o Empleado consultar el historial de pedidos de su negocio aplicando filtros individuales o combinados por rango de fechas, estado del pedido, domiciliario asignado y zona de cobertura. Origen: contexto 3.9, DEC-E33, HU-34.
- RF-004. El sistema debe permitir al Administrador del negocio generar un reporte consolidado de pedidos dentro de un rango de fechas especificado, contabilizando el total de pedidos agrupados por cada estado. Origen: DEC-E18, DEC-E33, HU-35.
- RF-005. El sistema debe permitir al Administrador del negocio consultar el desglose de despachos por zona de cobertura dentro de un rango de fechas, detallando la cantidad total de pedidos y el valor acumulado por tarifa de domicilio. Origen: DEC-E18, DEC-E33, HU-35.
- RF-006. El sistema debe permitir al Administrador del negocio generar un reporte de ventas del catálogo dentro de un rango de fechas, listando los productos ordenados de mayor a menor según la cantidad de unidades entregadas, e indicando las unidades vendidas y el valor total generado por producto. Origen: DEC-E18, DEC-E33, HU-36.
- RF-007. El sistema debe incluir en el reporte de ventas del catálogo los productos que hayan registrado ventas en el período consultado aunque se encuentren actualmente en estado desactivado, marcándolos explícitamente como desactivados. Origen: DEC-E28, HU-36.
- RF-008. El sistema debe denegar el acceso a la generación de reportes (RF-004, RF-005, RF-006) cuando la solicitud provenga de un Empleado, Domiciliario, Cliente o Dueño de la plataforma. Origen: contexto 2.3, DEC-E33, HU-33, HU-35, HU-36.
- RF-009. El sistema debe aislar en el backend la información de historial, trazabilidad y reportes de modo que cada usuario solo acceda a los registros pertenecientes a su negocio autenticado. Origen: contexto 3.2, contexto 3.3, Regla crítica 6, HU-33, HU-34, HU-35, HU-36.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización backend: Toda operación de consulta de historial, trazabilidad y reportes debe validar en el backend la identidad de la cuenta de Telegram, el rol activo y la pertenencia al negocio del usuario que realiza la solicitud. Se verifica con: prueba de autorización en el backend intentando consultar datos con usuarios no autorizados o de otros negocios. Origen: contexto 3.2, Regla crítica 6.
- RNF-002. Protección de datos sensibles: Las respuestas de consulta de historial y trazabilidad no deben exponer datos de clientes (nombre, teléfono, dirección) a roles no autorizados ni fuera del contexto del pedido activo. Se verifica con: inspección automatizada de estructuras de respuesta y pruebas de interfaz. Origen: contexto 3.3, Regla crítica 7.

### 7. Reglas de negocio
- BR-001. Registro de trazabilidad: Cada cambio de estado de un pedido debe registrar obligatoriamente fecha, hora, estado resultante y el identificador o nombre del usuario/actor responsable del cambio. Origen: contexto 3.8.
- BR-002. Exclusividad de reportes para el Administrador: El acceso a los reportes consolidados (pedidos por estado, recaudo de domicilio por zona y ventas del catálogo) es exclusivo del Administrador del negocio. Los empleados sólo pueden acceder a la trazabilidad y al historial filtrable. Origen: DEC-E33.
- BR-003. Inclusión financiera exclusiva para pedidos entregados: Para el cálculo del valor monetario acumulado por tarifas de domicilio en cada zona y del monto total generado por venta de productos del catálogo, el sistema debe contabilizar única y exclusivamente los pedidos en estado "entregado". Origen: DEC-E34.
- BR-004. Contabilización separada de estados no entregados: Los pedidos que finalicen o se encuentren en estados diferentes a "entregado" (recibido, en preparación, listo para recoger, en camino, cancelado, rechazado, con novedad) no deben sumar valor monetario en los reportes de recaudo ni en el valor de ventas del catálogo; se contabilizan únicamente en la cantidad de pedidos por su respectivo estado. Origen: DEC-E34.
- BR-005. Conservación de históricos de productos desactivados: La desactivación de un producto no elimina sus datos históricos de venta. Si un producto desactivado registró entregas en el período consultado, debe aparecer en el reporte de ventas conservando su nombre histórico y con un indicador explícito de su estado actual. Origen: DEC-E28.
- BR-006. Aislamiento estricto y denegación de visibilidad externa: Ningún usuario puede consultar historial, trazabilidad o reportes de un negocio distinto al suyo. El Dueño de la plataforma no tiene permiso de acceso a ningún dato operativo, historial ni reporte de los negocios. Origen: contexto 2.3, contexto 3.3.

### 8. Flujo principal
1. El Administrador o Empleado autenticado solicita consultar el historial o la trazabilidad de un pedido en la interfaz del bot o Mini App de su negocio.
2. El sistema valida en el backend la identidad, el rol y la vinculación del usuario con el negocio.
3. Para la consulta de trazabilidad de un pedido (RF-001): el usuario ingresa el identificador del pedido; el sistema recupera la lista cronológica de eventos con fecha, hora, estado y responsable, y la presenta respetando la protección de datos sensibles.
4. Para la consulta del historial filtrado (RF-003): el usuario define los criterios de búsqueda (rango de fechas, estado, domiciliario o zona); el sistema filtra los pedidos pertenecientes al negocio y retorna el listado de resultados.
5. Para la generación de reportes (RF-004, RF-005, RF-006): el Administrador selecciona el tipo de reporte deseado y el rango de fechas. El sistema calcula las cifras de pedidos y montos (aplicando BR-003 y BR-004) y presenta el consolidado en pantalla.

### 9. Flujos alternativos y de excepción
- A1. Consulta de historial sin aplicar filtros:
  1. El usuario no especifica filtros al ingresar al historial.
  2. El sistema aplica el rango de fechas por defecto (pendiente de OPEN-Q-001) y presenta los pedidos del negocio en ese período.
- E1. Usuario no autenticado o sin vinculación activa:
  1. Una persona no registrada en Telegram o sin rol de Administrador/Empleado intenta consultar la trazabilidad o el historial.
  2. El backend deniega la consulta y retorna un mensaje indicando requerimiento de autenticación previa.
- E2. Intento de consulta sobre un pedido de otro negocio:
  1. Un Empleado o Administrador intenta consultar la trazabilidad o datos de un pedido mediante un identificador que pertenece a otro negocio.
  2. El backend rechaza la solicitud y retorna una respuesta indicando que el pedido no fue encontrado (aislamiento multi-inquilino).
- E3. Empleado intenta acceder a reportes consolidados:
  1. Un Empleado o vendedor solicita generar alguno de los reportes consolidados.
  2. El backend identifica el rol de Empleado y deniega la operación por falta de permisos.
- E4. Intentos de acceso por el Dueño de la plataforma, Cliente o Domiciliario:
  1. El Dueño de la plataforma, un Cliente o un Domiciliario intentan ejecutar la consulta de reportes o trazabilidad general del negocio.
  2. El backend bloquea la petición inmediatamente sin entregar información.

### 10. Casos límite
- CL-001. Consulta de historial o reportes en un rango de fechas donde no existen pedidos registrados: El sistema retorna una respuesta exitosa con contador en cero y listas vacías, sin fallos ni errores. Origen: inferido, requiere confirmación (OPEN-Q-001).
- CL-002. Reporte de ventas del catálogo cuando dos o más productos registran la misma cantidad de unidades entregadas: El sistema aplica un criterio secundario de ordenamiento (pendiente de OPEN-Q-003). Origen: inferido, requiere confirmación (OPEN-Q-003).
- CL-003. Consulta de trazabilidad de un pedido cancelado automáticamente por suscripción vencida del negocio: El sistema muestra en la cronología el cambio de estado a cancelado, registrando como responsable al Dueño de la plataforma y el motivo "suscripción vencida". Origen: contexto 3.11, DEC-E26.

### 11. Criterios de aceptación
- AC-001. Dado un pedido registrado en el negocio A, cuando un Empleado o Administrador del negocio A solicita su trazabilidad, entonces el backend devuelve la lista en orden cronológico de cada cambio de estado especificando fecha, hora exacta, estado alcanzado y nombre/identificador del responsable.
- AC-002. Dado un pedido en el cual se registraron novedades o la entrega, cuando un Empleado o Administrador del negocio A visualiza la trazabilidad o el historial, entonces el sistema muestra el detalle de la novedad o la confirmación sin exponer datos sensibles del cliente no autorizados.
- AC-003. Dado un pedido que pertenece al negocio B, cuando un Empleado o Administrador del negocio A intenta consultar su trazabilidad mediante su identificador, entonces el sistema deniega el acceso indicando que el pedido no fue encontrado.
- AC-004. Dado el Dueño de la plataforma, cuando intenta consultar la trazabilidad, el historial o los reportes de cualquier negocio, entonces el sistema bloquea la operación y deniega el acceso.
- AC-005. Dado que un Empleado o Administrador ingresa al historial de pedidos, cuando aplica un filtro por rango de fechas, estado, domiciliario asignado o zona de cobertura, entonces el sistema muestra únicamente los pedidos de su negocio que cumplen con todos los criterios seleccionados.
- AC-006. Dado una persona no identificada en Telegram o sin vinculación activa como Empleado o Administrador del negocio, cuando intenta consultar el historial o la trazabilidad, entonces el sistema rechaza la solicitud indicando que requiere autenticación previa.
- AC-007. Dado un Administrador de negocio que selecciona un rango de fechas para el reporte operativo, cuando confirma la consulta, entonces el sistema presenta el total de pedidos de su negocio agrupados por cada estado dentro de ese período.
- AC-008. Dado un Administrador que consulta el reporte de recaudo por zonas en un rango de fechas, cuando el sistema genera el desglose, entonces muestra para cada zona la cantidad de pedidos y la sumatoria del valor de la tarifa de domicilio contabilizando únicamente los pedidos en estado "entregado".
- AC-009. Dado un conjunto de pedidos en un período que incluye pedidos cancelados, rechazados o con novedad, cuando el Administrador genera el reporte de zonas o de ventas del catálogo, entonces el sistema excluye el valor de dichos pedidos de la sumatoria monetaria y contabiliza sus cantidades por separado según su estado.
- AC-010. Dado un Empleado o vendedor del negocio, cuando intenta solicitar la generación de un reporte operativo o de ventas del catálogo, entonces el sistema deniega la operación notificando que no posee permisos.
- AC-011. Dado un Administrador que solicita el reporte de ventas del catálogo en un rango de fechas, cuando el sistema genera la respuesta, entonces entrega la lista de productos ordenados de mayor a menor por cantidad de unidades en pedidos "entregados", indicando unidades vendidas y valor total por producto.
- AC-012. Dado un producto que generó ventas en el período pero fue desactivado posteriormente, cuando el Administrador genera el reporte de ventas, entonces el sistema incluye el producto con sus ventas históricas e indica explícitamente que el producto está desactivado.
- AC-013. Dado un Cliente o Domiciliario, cuando intenta acceder al reporte de ventas del catálogo o a los reportes operativos del negocio, entonces el sistema deniega el acceso por falta de permisos.

### 12. Dependencias
- SPEC-003: Gestión del catálogo del negocio (definición de productos, precios y estado activo/desactivado).
- SPEC-004: Registro de pedidos por clientes y cálculo de tarifas por zona.
- SPEC-005: Asignación y gestión de domiciliarios.
- SPEC-006: Ciclo de vida del pedido, transiciones de estado y registro de novedades/cancelaciones.

### 13. Restricciones
- Las operaciones se ejecutan a través de la interfaz del bot o Mini App de Telegram integrada al flujo del negocio. Origen: contexto 3.1.
- El backend concentra la lógica de autorización y persistencia; no se confían controles de acceso al bot. Origen: contexto 3.2.
- La información de cada negocio está separada; ningún usuario ve ni modifica datos de otro negocio. Origen: contexto 3.3.
- Protección de datos sensibles del cliente: nombre, teléfono, dirección e identificadores personales no deben exponerse salvo autorización expresa. Origen: contexto 3.3, Regla crítica 7.
- Restricciones generales del proyecto: proyecto individual, guiado por especificaciones (SDD). Origen: contexto 4.
- Solución independiente que no condiciona su funcionamiento básico a aplicativos externos. Origen: contexto 4.
- Cumplimiento de la Ley 1581 de 2012 y Decreto 1377 de 2013 de Colombia en el tratamiento y acceso a datos personales. Origen: contexto 6.

### 14. Fuera de alcance
- Funcionalidades de analítica predictiva o gráficos complejos exportables a formatos externos (PDF/Excel). Origen: contexto 3.9.
- Acceso a reportes o consolas administrativas para el Dueño de la plataforma sobre pedidos de los negocios. Origen: contexto 2.3, sección 5.
- Central de repartidores o visibilidad cruzada de domiciliarios entre negocios. Origen: sección 5.
- [Mecanismo de agregación y optimización de consultas de reportes]: tema para arquitectura. Origen: RF-004, RF-005, RF-006.

### 15. Preguntas abiertas
- OPEN-Q-001: Pendiente.
- OPEN-Q-002: Pendiente.
- OPEN-Q-003: Pendiente.

### 16. Trazabilidad
- HU-33: RF-001, RF-002, RF-008, RF-009; BR-001, BR-006; AC-001, AC-002, AC-003, AC-004; CL-003.
- HU-34: RF-002, RF-003, RF-009; BR-006; AC-002, AC-005, AC-006; CL-001.
- HU-35: RF-004, RF-005, RF-008, RF-009; BR-002, BR-003, BR-004, BR-006; AC-004, AC-007, AC-008, AC-009, AC-010; CL-001.
- HU-36: RF-006, RF-007, RF-008, RF-009; BR-002, BR-003, BR-004, BR-005, BR-006; AC-011, AC-012, AC-013; CL-002.
- RF-001: Origen: contexto 3.8, DEC-E33, HU-33; verificado por AC-001.
- RF-002: Origen: contexto 3.3, Regla crítica 7, HU-33, HU-34; verificado por AC-002.
- RF-003: Origen: contexto 3.9, DEC-E33, HU-34; verificado por AC-005.
- RF-004: Origen: DEC-E18, DEC-E33, HU-35; verificado por AC-007.
- RF-005: Origen: DEC-E18, DEC-E33, HU-35; verificado por AC-008, AC-009.
- RF-006: Origen: DEC-E18, DEC-E33, HU-36; verificado por AC-011.
- RF-007: Origen: DEC-E28, HU-36; verificado por AC-012.
- RF-008: Origen: contexto 2.3, DEC-E33, HU-33, HU-35, HU-36; verificado por AC-010, AC-013.
- RF-009: Origen: contexto 3.2, contexto 3.3, Regla crítica 6, HU-33, HU-34, HU-35, HU-36; verificado por AC-003, AC-004.
- RNF-001: Origen: contexto 3.2, Regla crítica 6; verificado con: prueba de autorización en el backend intentando consultar datos con usuarios no autorizados o de otros negocios.
- RNF-002: Origen: contexto 3.3, Regla crítica 7; verificado con: inspección automatizada de estructuras de respuesta y pruebas de interfaz.
- BR-001: Origen: contexto 3.8; verificado por AC-001.
- BR-002: Origen: DEC-E33; verificado por AC-010.
- BR-003: Origen: DEC-E34; verificado por AC-008, AC-011.
- BR-004: Origen: DEC-E34; verificado por AC-009.
- BR-005: Origen: DEC-E28; verificado por AC-012.
- BR-006: Origen: contexto 2.3, contexto 3.3; verificado por AC-003, AC-004, AC-006, AC-013.
- CL-001: Origen: inferido, requiere confirmación (OPEN-Q-001); verificado por AC-005.
- CL-002: Origen: inferido, requiere confirmación (OPEN-Q-003); verificado por AC-011.
- CL-003: Origen: contexto 3.11, DEC-E26; verificado por AC-001.

### 17. Historial de cambios
- Versión 0.1: creación a partir de la necesidad y de las historias de usuario aprobadas HU-33 a HU-36 (EPIC-005).

## Verificación
- Completitud: cumple. Se incluyeron todas las secciones obligatorias del formato de SPEC y las 4 HUs aprobadas.
- Consistencia interna: cumple. Se compararon los RF, BR y AC sobre trazabilidad, filtros de historial y reportes del negocio sin detectar discrepancias.
- Consistencia con el contexto: cumple. Se verificaron las decisiones DEC-E18, DEC-E28, DEC-E33, DEC-E34 y los límites de roles con las secciones 2.3, 3.2, 3.3 y 3.8 del contexto.
- No ambigüedad: cumple. Los casos pendientes de definición por el equipo se registraron explícitamente en OPEN-Q-001, OPEN-Q-002 y OPEN-Q-003.
- Verificabilidad: cumple. Cada AC está redactado en formato Dado/Cuando/Entonces con resultados observables.
- Cobertura de actores: cumple. Se especificaron HUs para Empleado y Administrador, y se definieron reglas y ACs de autorización explícitos para Cliente, Domiciliario y Dueño de la plataforma.
- Cobertura de AC: cumple. Todos los RF y BR cuentan con al menos un AC que los verifica.
- Trazabilidad: cumple. La sección 16 registra cada HU, RF, RNF, BR y CL con su origen y AC/método de verificación correspondiente.
- No invención: cumple. No se inventaron reglas técnicas ni parámetros no confirmados; los vacíos se elevaron como OPEN-Q.
- Delimitación: cumple. No se incluyeron decisiones de arquitectura ni tecnología en los requisitos de negocio; los aspectos técnicos se marcaron en la sección 14.

## Siguiente paso
Respondan las preguntas abiertas y ejecuten de nuevo el agente con --continuar SPEC-007.
