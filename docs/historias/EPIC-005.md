# EPIC-005. Historial y reportes — Historias de usuario

Estado: Aprobada por Camila (2026-11-19)
Fecha: 2026-11-19

Origen y validación:
- Generadas por `generador-hu-invest` (agentes-ia/salidas/generador-hu-invest/HU-004_20261119-0942_user-stories_epic-005_hu-33.md).
- Revisadas por `user-story-reviewer` (agentes-ia/salidas/user-story-reviewer/RHU-004_20261119-0944_story-review_epic-005.md).
- Correcciones elegidas por la estudiante y aplicadas por el asistente Claude Code (revisión de conflictos, 2026-11-19); aprobadas por Camila:
  1. HU-33 y HU-34: el administrador también consulta la trazabilidad y el historial (DEC-E33).
  2. HU-35 y HU-36: los valores y las ventas cuentan solo pedidos entregados; los demás estados se muestran aparte (DEC-E34).
  3. HU-35 y HU-36: el empleado no ve los reportes (DEC-E33).

---

### HU-33 — Consulta de trazabilidad de estados de un pedido

Yo, como empleado o vendedor,
quiero consultar la cronología completa de cambios de estado de un pedido específico,
para verificar qué ocurrió en el servicio y atender cualquier reclamo o duda con información fehaciente.

Está hecho cuando:
- Dado un pedido registrado en el negocio al que pertenece el empleado o vendedor, cuando este solicita ver su trazabilidad, entonces el sistema presenta en orden cronológico cada cambio de estado, registrando la fecha, la hora exacta, el estado alcanzado y el responsable de la acción (contexto 3.8).
- Dado un pedido que contiene registros de entrega o novedades, cuando el empleado o vendedor visualiza su historial, entonces el sistema muestra el detalle de la novedad registrada o la confirmación de entrega sin exponer datos personales no autorizados.
- Dado un pedido que pertenece a otro negocio, cuando el empleado o vendedor intenta consultar su trazabilidad mediante su identificador, entonces el sistema le deniega el acceso indicando que el pedido no fue encontrado (contexto 3.3).
- Dado el dueño de la plataforma, cuando intenta consultar la trazabilidad o los eventos del pedido de un negocio, entonces el sistema bloquea la operación y no entrega información (contexto 2.3).
- Dado el administrador del negocio, cuando consulta la trazabilidad de un pedido de su negocio, entonces el sistema le muestra la misma cronología que al empleado (DEC-E33).

Cómo se simula en el prototipo: Se consultan pedidos precargados con registros simulados de cambio de estado en memoria vinculados a identificadores ficticios.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Es independiente porque evalúa la consulta puntual de eventos de un pedido sin requerir pantallas complejas de analítica. Su valor radica en la atención de reclamos y es testeable verificando los datos obligatorios de auditoría (fecha, estado y responsable).

---

### HU-34 — Filtrado y consulta del historial de pedidos del negocio

Yo, como empleado o vendedor,
quiero filtrar el historial de pedidos de mi negocio por fecha, estado, domiciliario y zona,
para ubicar rápidamente entregas anteriores y revisar la operación diaria.

Está hecho cuando:
- Dado que el empleado o vendedor ingresa a la consulta de historial de su negocio, cuando aplica filtros por rango de fechas, estado del pedido, domiciliario asignado o zona de cobertura, entonces el sistema muestra exclusivamente los pedidos que cumplen con dichos criterios (contexto 3.9).
- Dado el listado de resultados obtenido, cuando el empleado o vendedor examina los pedidos, entonces el sistema presenta un resumen de cada servicio sin exhibir datos personales no autorizados del cliente.
- Dado que en la plataforma existen pedidos registrados por otros negocios, cuando el empleado o vendedor ejecuta la búsqueda, entonces el sistema aísla la información y muestra únicamente los pedidos pertenecientes a su negocio (contexto 3.3).
- Dado una persona que no se ha identificado en Telegram o que no tiene una vinculación activa como empleado o vendedor en el negocio, cuando intenta consultar el historial de pedidos, entonces el sistema rechaza la consulta y exige autenticación previa (contexto 3.2).
- Dado el administrador del negocio, cuando aplica los mismos filtros, entonces el sistema le muestra el historial de su negocio con las mismas reglas (DEC-E33).

Cómo se simula en el prototipo: Se utiliza una colección simulada de 10 pedidos con diferentes zonas, domiciliarios asignados y estados para verificar los filtros.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: La historia es estimable y pequeña al centrarse en la búsqueda y listado filtrado. No impone detalles técnicos de implementación y garantiza el aislamiento de datos entre negocios.

---

### HU-35 — Reporte operativo de pedidos por estado y zonas de entrega

Yo, como administrador del negocio,
quiero generar un reporte consolidado de pedidos por estado y por zona de cobertura en un período seleccionado,
para evaluar el volumen de entregas y el recaudo por tarifas de domicilio en cada sector.

Está hecho cuando:
- Dado que el administrador del negocio selecciona un rango de fechas para el reporte operativo, cuando confirma la consulta, entonces el sistema muestra el consolidado con el total de pedidos agrupados por cada estado dentro de ese rango (DEC-E18).
- Dado el mismo período consultado, cuando el administrador del negocio solicita el desglose por zonas, entonces el sistema detalla para cada zona de cobertura la cantidad de pedidos gestionados y el valor monetario total acumulado por concepto de tarifa de domicilio (DEC-E18).
- Dado pedidos cancelados, rechazados o con novedad en el período, cuando el sistema calcula el valor de domicilios por zona, entonces solo suma los pedidos entregados y muestra la cantidad de los demás estados por separado (DEC-E34).
- Dado que existen datos de despachos de otros negocios en la plataforma, cuando el administrador del negocio genera el reporte, entonces el sistema garantiza que los cálculos incluyan únicamente los despachos de su negocio (contexto 3.3).
- Dado el dueño de la plataforma, cuando intenta generar o consultar el reporte operativo de un negocio, entonces el sistema rechaza la solicitud (contexto 2.3).
- Dado un empleado o vendedor, cuando intenta generar un reporte operativo o de ventas, entonces el sistema deniega el acceso: los reportes son solo del administrador (DEC-E33).

Cómo se simula en el prototipo: Se calculan sumatorias a partir de un conjunto de datos estáticos con montos de flete entre $3.000 y $8.000 distribuidos en dos zonas.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Aporta valor de gestión directa al administrador del negocio al consolidar el comportamiento operativo y el recaudo por domicilio sin acoplarse al catálogo de productos. Es testeable mediante sumatorias sobre pedidos del rango.

---

### HU-36 — Reporte de ventas del catálogo con productos activos y desactivados

Yo, como administrador del negocio,
quiero consultar el reporte de ventas del catálogo identificando los productos más pedidos en un rango de fechas,
para analizar las preferencias de los clientes y el rendimiento de mis productos sin perder el histórico de los que ya no vendo.

Está hecho cuando:
- Dado un rango de fechas especificado por el administrador del negocio, cuando solicita el reporte de ventas, entonces el sistema lista los productos ordenados de mayor a menor según la cantidad de unidades entregadas (DEC-E34), indicando las unidades vendidas y el valor total generado por producto (DEC-E18).
- Dado un producto que generó ventas en el período consultado pero que actualmente se encuentra desactivado en el catálogo, cuando el administrador del negocio genera el reporte, entonces el sistema incluye el producto y sus ventas históricas, indicando de forma clara que el producto está desactivado (DEC-E28).
- Dado que un producto fue registrado y vendido en otro negocio bajo el mismo nombre, cuando el administrador del negocio emite el reporte, entonces el sistema cuantifica únicamente las ventas generadas dentro de su propio negocio (contexto 3.3).
- Dado un cliente o un domiciliario, cuando intenta acceder a este reporte de ventas del catálogo, entonces el sistema deniega el acceso por falta de permisos.

Cómo se simula en el prototipo: Se procesa una lista de pedidos simulados donde un producto desactivado ("Hamburguesa Especial") mantiene sus ventas registradas en el consolidado.

Evaluación INVEST:
| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Comentario INVEST: Cumple con la regla de negocio DEC-E28 respecto a productos desactivados. Es comprobable mediante criterios objetivos de ordenamiento y montos finales, aportando valor analítico al administrador.
