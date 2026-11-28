# Domiciliarios Eje - Contexto para agentes de IA

Versión: 0.1
Estado: Borrador
Fuente: enunciado «Proyecto Final», Ingeniería de Software III, Universidad de Caldas, Aplicativo 1.
Ejemplo de uso del kit SDD: archivo de contexto con la estructura de CONTEXTO_PROYECTO.md.
Propósito: dar a cualquier agente de IA que trabaje en Domiciliarios Eje las reglas de trabajo, el dominio y el contexto del producto, sin importar la tarea que realice.

Todo lo que no aparece en este archivo está sin decidir. La sección 7 lista los vacíos conocidos. Ningún agente los completa por su cuenta.

# 1. Reglas de trabajo

1. Redactar en español de Colombia.
2. Seguir el principio del proyecto: la IA propone, la estudiante decide y valida. La estudiante es responsable de revisar, corregir y justificar todo lo que produzca la IA.
3. Si falta información para cumplir la tarea, preguntar. No completar vacíos con suposiciones ni inventar reglas, cifras, normas, integraciones o comportamientos.
4. En toda respuesta, distinguir tres tipos de contenido:
   - Confirmado: lo que está en este archivo o lo que la estudiante respondió.
   - Inferido: una conclusión propia del agente. Se marca como tal y requiere confirmación.
   - Pendiente: lo que aún no está decidido.
   Una inferencia nunca se convierte en regla sin aprobación.
5. Si una solicitud contradice el contexto del producto (sección 3), señalar la contradicción y preguntar antes de continuar. No resolverla por cuenta propia.
6. Desarrollo guiado por especificaciones (SDD): no se construye nada que no parta de una SPEC aprobada.
7. Cada uso de un agente deja evidencia en `docs/evidencias-ia.md` (skill `registro-de-evidencias-ia`). Es un entregable obligatorio.

# 2. Dominio

## 2.1. Producto

- Nombre: Domiciliarios Eje.
- Tipo: herramienta para que cada negocio administre sus propios pedidos a domicilio desde Telegram.
- Propósito: que cada negocio administre sus pedidos a domicilio, organice sus zonas de cobertura y coordine la entrega con sus domiciliarios.
- Modelo comercial previsto: mensualidad fija por negocio. No cobra comisión por pedido ni por entrega.
- Entregable: aplicativo individual del curso, construido y sustentado por una sola estudiante.

## 2.2. Problema

- Muchos pequeños negocios reciben pedidos por distintos canales y coordinan las entregas de manera manual.
- Esto dificulta saber qué pedidos están pendientes, quién debe entregarlos, cuánto cuesta el domicilio y en qué estado está cada servicio.

## 2.3. Actores

- Administrador del negocio: configura el establecimiento, horarios, zonas, tarifas, usuarios, domiciliarios y reglas de operación.
- Empleado o vendedor: registra pedidos, consulta su estado y coordina la preparación y la entrega según sus permisos.
- Domiciliario: consulta los servicios que le asignaron y actualiza los estados de recogida y entrega.
- Cliente: realiza o confirma un pedido, entrega los datos necesarios y consulta el estado cuando el negocio habilite esta opción.
- Dueño de la plataforma: aprueba o rechaza los negocios que se registran (DEC-E01), marca su suscripción (DEC-E26) y mantiene la lista de festivos de Colombia (DEC-E41). No ve ni opera pedidos, clientes, domiciliarios ni reportes de ningún negocio.
- Telegram: canal real de interacción. Transporta mensajes; no decide permisos.

No existen otros roles. En particular, no hay un rol de «central de repartidores» ni un rol de plataforma con poder sobre los pedidos de los negocios (ver sección 5).

## 2.4. Glosario

- Negocio o establecimiento: unidad que contrata el servicio. Toda la información pertenece a un negocio.
- Pedido: solicitud de un cliente con sus productos o descripción, dirección, observaciones y forma de pago cuando aplique.
- Zona de cobertura: barrio, sector o zona donde el negocio entrega, con su tarifa y condiciones.
- Tarifa de domicilio: valor que cobra el negocio por entregar en una zona.
- Domiciliario: repartidor registrado o vinculado a un negocio.
- Asignación: relación entre un pedido y el domiciliario que lo entrega.
- Despacho: selección del domiciliario, consulta de pendientes y control de la carga de trabajo.
- Estado del pedido: recibido, en preparación, listo para recoger, asignado, en camino, entregado o cancelado.
- Novedad: situación excepcional registrada durante la entrega.

# 3. Funcionamiento del producto

Esta sección es la fuente de verdad del funcionamiento. Lo que no está aquí está en la sección 7 (vacíos) o fuera de alcance (sección 5).

## 3.1. Canales

- Telegram es la interfaz principal, mediante un bot con comandos, botones, menús, formularios conversacionales, mensajes, fotografías, documentos y notificaciones.
- Cuando una funcionalidad necesite una experiencia visual más compleja, se puede usar una Telegram Mini App, siempre integrada al flujo de Telegram.
- No se exige una aplicación web ni móvil aparte.

## 3.2. Backend, autenticación y autorización

- El backend concentra la lógica de negocio, las validaciones, las reglas de operación, la autenticación, la autorización, la persistencia y la comunicación con servicios externos.
- No se confían controles críticos solo a la interfaz del bot.
- Cada operación verifica el usuario, su rol, el negocio al que pertenece y los permisos correspondientes.

## 3.3. Separación de la información por negocio

- La información de cada negocio está separada. Un usuario solo accede a la información del negocio al que pertenece y que su rol le permite.
- Protección de datos personales: acceso únicamente a la información autorizada.

## 3.4. Configuración del negocio

- Datos del establecimiento, dirección, contacto, horarios de atención y parámetros de operación.
- Gestión de usuarios, roles y permisos según las responsabilidades reales.

## 3.5. Zonas de cobertura y tarifas

- Definición de barrios, sectores o zonas de cobertura, con tarifas y condiciones de domicilio.
- Al registrar un pedido, el sistema valida la zona de cobertura y calcula la tarifa correspondiente.

## 3.6. Gestión de domiciliarios

- Registro o vinculación de repartidores, disponibilidad, estado y asignación de servicios.

## 3.7. Registro de pedidos

- Datos del cliente, productos o descripción del pedido, dirección, observaciones y forma de pago cuando aplique.
- Validación de datos y prevención de registros duplicados o inconsistentes.
- Confirmación antes de ejecutar operaciones importantes.

## 3.8. Asignación, despacho y seguimiento

- El administrador o el empleado asigna un domiciliario.
- Despacho: selección del domiciliario, consulta de pedidos pendientes y control de la carga de trabajo.
- El domiciliario recibe la notificación y actualiza los estados del servicio.
- Estados: recibido, en preparación, listo para recoger, asignado, en camino, entregado o cancelado.
- El pedido termina como entregado o con la novedad correspondiente.
- Se registran fechas, estados y responsables para la trazabilidad.
- Se manejan errores, cancelaciones y situaciones excepcionales.

Flujo general de operación:

1. El negocio recibe o registra el pedido.
2. El sistema valida la zona de cobertura y calcula la tarifa.
3. El negocio confirma el pedido y lo prepara.
4. El administrador o el empleado asigna un domiciliario.
5. El domiciliario recibe la notificación y actualiza los estados del servicio.
6. El pedido se marca como entregado o se registra la novedad.

## 3.9. Historial y reportes

- Consulta de pedidos por fecha, estado, domiciliario, zona y negocio.
- Reportes básicos para consultar la operación y apoyar decisiones.

## 3.10. Integraciones complementarias

- Puede integrarse con Mi Tienda Express (Aplicativo 6) para coordinar entregas. Es opcional y no es requisito del funcionamiento básico.

## 3.11. Decisiones de la estudiante (2026-11-19)

Confirmadas por la estudiante. Precisan el enunciado; los agentes las citan como «contexto 3.11, DEC-E0x». El registro completo está en `docs/decisiones.md`.

Usuarios y acceso:
- DEC-E01. Un negocio se registra solo desde el bot y queda pendiente hasta que el dueño de la plataforma lo aprueba. Quien lo registra queda como su administrador.
- DEC-E02. Empleados y domiciliarios piden unirse a un negocio desde el bot y el administrador aprueba o rechaza la solicitud.
- DEC-E03. (modificada 2026-11-19) Un domiciliario pertenece a un solo negocio: no puede pedir unirse a otro mientras tenga una vinculación activa o pendiente. La restricción aplica solo al rol domiciliario; una misma cuenta puede ser empleado o administrador de otros negocios y cliente de varios (DEC-E29).

Pedidos del cliente:
- DEC-E04. (modificada 2026-11-27, ver DEC-E66) El cliente hace pedidos por el bot.
- DEC-E05. El cliente llega a un negocio por el enlace o QR propio de ese negocio. No hay listado ni buscador de negocios (para no ser un marketplace, sección 5).
- DEC-E06. Cada negocio tiene un catálogo simple de productos con precio; el cliente elige productos y cantidades y el sistema calcula el total (productos más tarifa del domicilio).
- DEC-E07. El cliente elige el barrio de la lista de zonas del negocio (define la tarifa) y escribe la dirección y las referencias.
- DEC-E08. El sistema solo registra la forma de pago; el cobro ocurre fuera del sistema.
- DEC-E09. (modificada 2026-11-19) Un barrio sin cobertura se rechaza con un mensaje. Fuera del horario de atención el bot le informa al cliente que el negocio está cerrado y no le deja hacer el pedido; no hay pedidos programados.
- DEC-E10. Un pedido del mismo cliente al mismo negocio, con los mismos productos y la misma dirección, hecho poco tiempo después de otro, se considera posible duplicado: el bot pide confirmar antes de registrarlo.

Asignación y estados:
- DEC-E11. El administrador o el empleado asigna el pedido a un domiciliario; el domiciliario acepta o rechaza en el bot.
- DEC-E12. Cada negocio configura un tope de pedidos simultáneos por domiciliario; el sistema no permite asignar por encima del tope.
- DEC-E13. (modificada 2026-11-27, ver DEC-E69) (modificada 2026-11-19) El cliente y el negocio pueden cancelar un pedido antes de que pase a «en camino». También se cancela al marcar el negocio como vencido (DEC-E26). Desde «en camino», lo que ocurra se registra como novedad.

Ubicación y mapa:
- DEC-E14. El domiciliario comparte su ubicación en tiempo real de Telegram para pasar a «en camino»; sin ubicación no puede pasar a ese estado. Se deja de usar al entregar.
- DEC-E15. (modificada 2026-11-19) Se guarda el recorrido de cada pedido durante 30 días; después se borra.
- DEC-E16. (modificada 2026-11-27, ver DEC-E73) (modificada 2026-11-19) En la Mini App ven el mapa: el administrador y el empleado (los domiciliarios en ruta de su negocio) y el cliente (solo el domiciliario de su pedido, mientras está «en camino»).

Notificaciones y reportes:
- DEC-E17. El cliente recibe: pedido confirmado o rechazado (con el total) y cada cambio de estado; el aviso de «en camino» incluye el acceso al mapa.
- DEC-E18. Reportes para la demostración: pedidos por fecha y estado, pedidos y valor de domicilios por zona, y ventas del catálogo.

Proyecto:
- DEC-E19. (modificada 2026-11-27, ver DEC-E80) Plazo disponible: unas 8 semanas o más.

Segunda ronda (2026-11-19):
- DEC-E20. Una persona se identifica con su cuenta de Telegram y, al registrarse, comparte su contacto con el botón nativo de Telegram; el teléfono queda verificado por Telegram. No se usan códigos por SMS.
- DEC-E21. (modificada 2026-11-27, ver DEC-E69) (modificada 2026-11-19) Ciclo de vida del pedido: recibido → en preparación → listo para recoger → en camino → entregado. Confirmar el pedido es pasarlo de «recibido» a «en preparación»; desde «recibido» el negocio también puede rechazarlo. Una novedad registrada en camino deja el pedido en el estado final «con novedad». Cancelado aplica según DEC-E13. La asignación del domiciliario se puede hacer desde «en preparación»: «asignado» es un dato del pedido, no un estado.
- DEC-E22. (modificada 2026-11-27, ver DEC-E69) (modificada 2026-11-19) El administrador o el empleado confirma (pasa a «en preparación») o rechaza el pedido y lo marca «listo para recoger». El domiciliario lo pasa a «en camino» y a «entregado», o registra una novedad (pasa a «con novedad»). Entregado, con novedad, rechazado y cancelado son estados finales.
- DEC-E23. Si el domiciliario rechaza la asignación o no responde a tiempo, el pedido queda sin domiciliario y se avisa a quien asignó para que elija otro.
- DEC-E24. (modificada 2026-11-19) Si el domiciliario deja de compartir la ubicación en «en camino», el pedido sigue; el mapa muestra la última posición con su hora, el bot le pide reactivarla y se avisa al administrador y al empleado.
- DEC-E25. Notificaciones del negocio: administrador y empleado reciben pedidos nuevos para confirmar, rechazos o falta de respuesta de domiciliarios, novedades y cancelaciones del cliente; el domiciliario recibe asignaciones y cancelaciones de sus pedidos; el administrador recibe las solicitudes de unión.
- DEC-E26. (modificada 2026-11-19) El sistema guarda el estado de suscripción de cada negocio (al día o vencido), que marca el dueño de la plataforma. Antes de marcarlo vencido, el sistema le muestra cuántos pedidos se cancelarán y pide confirmar. Al confirmar: el negocio no recibe pedidos nuevos, los pedidos no despachados se cancelan con motivo «suscripción vencida» y el dueño de la plataforma como responsable, se avisa a los clientes y al negocio, y los pedidos que van «en camino» terminan normalmente. No hay cobro en línea.

Revisión de HU de EPIC-002 (2026-11-19):
- DEC-E27. El administrador y el empleado o vendedor gestionan el catálogo del negocio (crear, modificar y desactivar productos). Los clientes del negocio solo lo consultan.
- DEC-E28. Un producto se desactiva, no se borra: deja de mostrarse a los clientes y se conserva en los pedidos anteriores.
- DEC-E29. El cliente se registra en cada negocio: al entrar por el enlace o QR de un negocio nuevo vuelve a compartir su contacto.

Revisión de HU de EPIC-003 a EPIC-005 (2026-11-19):
- DEC-E30. Una asignación pendiente de respuesta cuenta para el tope de pedidos simultáneos del domiciliario, igual que las aceptadas y las que van en camino.
- DEC-E31. El domiciliario se marca disponible o no disponible en el bot; solo los disponibles se ofrecen para asignar. Al marcarse no disponible, sus pedidos asignados que aún no van en camino se liberan con aviso a quien los asignó; los que van en camino los termina.
- DEC-E32. Mientras un pedido está activo y asignado a él, el domiciliario ve el nombre, la dirección, las referencias y el teléfono del cliente; al terminar, cancelarse o reasignarse el pedido deja de verlos.
- DEC-E33. El administrador ve historial, trazabilidad, reportes y recorridos de su negocio; el empleado ve historial y trazabilidad, pero no los reportes.
- DEC-E34. Los valores de domicilios por zona y las ventas del catálogo cuentan solo pedidos entregados; los demás estados se muestran aparte.

SPEC-001 y protección de datos (2026-11-19):
- DEC-E35. Las solicitudes pendientes de registro de negocio y de vinculación de personal vencen a los 7 días; se avisa al solicitante.
- DEC-E36. Todo actor cuyos datos personales se traten (persona que registra un negocio, administrador, empleado, domiciliario y cliente) da una autorización previa, expresa e informada con un botón antes de compartir sus datos; la aceptación queda registrada con fecha y versión del texto, y se puede revocar. Base: Ley 1581 de 2012 y Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015).
- DEC-E37. Responsables del tratamiento: la plataforma es Responsable de los datos de los negocios, de quienes los registran y de su personal; cada negocio es Responsable de los datos de sus clientes y la plataforma actúa como Encargada.
- DEC-E38. El domiciliario acepta, además del general, un consentimiento propio para su ubicación en tiempo real y su recorrido; sin él no puede vincularse como domiciliario (DEC-E14).
- DEC-E39. Al registrar un negocio se pide también un correo de atención de datos personales (canal para que sus clientes ejerzan sus derechos), y quien lo registra acepta los términos de la plataforma y el acuerdo de transmisión de datos.

SPEC-002, configuración del negocio (2026-11-19):
- DEC-E40. El tope de pedidos simultáneos por domiciliario es 3 por defecto; el administrador lo puede cambiar entre 1 y 7.
- DEC-E41. Cada día de la semana tiene un único rango de atención (HH:MM a HH:MM) o está cerrado. El dueño de la plataforma mantiene una lista única de festivos de Colombia; cada negocio decide si en cada festivo cierra o atiende con un horario propio.
- DEC-E42. Cada negocio tiene dos accesos distintos: enlace, QR y código para clientes (pedidos) y enlace, QR y código para personal (solicitudes de unión); el de personal solo lo ve el administrador.
- DEC-E43. La tarifa de domicilio va de $0 a $50.000 COP; el nombre del barrio no se repite dentro del mismo negocio.
- DEC-E44. Si el administrador baja el tope por debajo de la carga actual de un domiciliario, sus pedidos actuales se respetan y no recibe nuevos hasta quedar por debajo del tope.

SPEC-003 y SPEC-004, catálogo y pedidos (2026-11-21):
- DEC-E45. El catálogo se organiza por categorías, que gestionan el administrador y el empleado (DEC-E27).
- DEC-E46. Un producto está activo, agotado o desactivado: agotado se muestra al cliente como no disponible y no se puede pedir; desactivado no se muestra. Un producto desactivado se puede reactivar.
- DEC-E47. El catálogo se gestiona y se consulta tanto por el chat como por la Mini App, para el personal y para el cliente. La Mini App ya no es solo el mapa.
- DEC-E48. Un producto tiene nombre y precio obligatorios, y descripción corta e imagen opcionales.
- DEC-E49. El nombre del producto no se repite dentro del negocio, aunque esté desactivado; para volver a venderlo se reactiva el mismo producto.
- DEC-E50. Un posible duplicado (DEC-E10) es un pedido igual del mismo cliente al mismo negocio dentro de 5 minutos.
- DEC-E51. Cada negocio configura las formas de pago que acepta (configuración del negocio, SPEC-002); el cliente elige entre ellas.
- DEC-E52. Al enviar el pedido se revalida el catálogo; si un producto quedó agotado o desactivado, se avisa al cliente para que lo quite o lo cambie.
- DEC-E53. Cada negocio puede fijar un valor mínimo de compra (0 = sin mínimo) en su configuración (SPEC-002).

SPEC-005 a SPEC-007, despacho, seguimiento y reportes (2026-11-21):
- DEC-E54. El domiciliario tiene 3 minutos para aceptar o rechazar una asignación; si no responde, se libera (DEC-E23).
- DEC-E55. Novedades que puede reportar el domiciliario en camino: cliente ausente, dirección no encontrada, cliente rechaza el pedido y otro motivo con texto breve.
- DEC-E56. Al entregar un pedido cuya forma de pago se cobra al entregar, el domiciliario confirma «cobrado» y queda registrado.
- DEC-E57. Las formas de pago tienen un tipo fijo de la plataforma (efectivo, transferencia o datáfono); cada negocio elige cuáles acepta y puede darles un nombre propio (por ejemplo, «Nequi» de tipo transferencia). Toda forma de pago cuyo tipo no sea transferencia se cobra al entregar.
- DEC-E58. Si el domiciliario no reactiva la ubicación, el pedido sigue «en camino» hasta que lo entregue o registre una novedad; el negocio coordina fuera del bot.
- DEC-E59. Historial y reportes muestran por defecto el día actual. El reporte por fecha y estado da el total del período y, si abarca más de un día, el desglose diario. En ventas del catálogo, a igual cantidad de unidades se ordena por valor vendido y luego alfabéticamente.

Revisión cruzada de SPEC (2026-11-21):
- DEC-E60. La detección de desvíos de ruta o geocercas (geofencing) queda fuera de alcance.

ARQ-001, decisiones técnicas (2026-11-21):
- DEC-E61. (modificada 2026-11-27, ver DEC-E78 y DEC-E79) Las tareas programadas (3 minutos, 7 días y 30 días) usan pg-boss sobre PostgreSQL.
- DEC-E62. (modificada 2026-11-27, ver DEC-E78) La ubicación en vivo llega a la Mini App por SSE.
- DEC-E63. (modificada 2026-11-27, ver DEC-E78) Imágenes de productos: file_id de Telegram si se suben por el bot y disco local del servidor si se suben por la Mini App; los QR se generan al vuelo.
- DEC-E64. La asignación atómica se resuelve solo con transacciones y UPDATE condicional en PostgreSQL, sin bloqueos externos.

Mapa (2026-11-21):
- DEC-E65. (modificada 2026-11-27, ver DEC-E74) El mapa de la Mini App usa OpenStreetMap.

Respuestas del profesor (reunión 2026-11-24, registradas 2026-11-27):
- DEC-E66. El administrador o el empleado también registra los pedidos que le llegan al negocio por otros canales: tipo (a domicilio o en el local), fecha, valor (productos del catálogo o un valor libre con descripción), tarifa del domicilio si es a domicilio, dirección de entrega y teléfono de contacto. Los pedidos a domicilio se asignan y se siguen como los demás. Siguen existiendo los pedidos que hace el cliente por el bot (DEC-E04).
- DEC-E67. En un pedido registrado por el negocio, la dirección y el teléfono de contacto quedan en el pedido como registro del negocio y no se borran con el recorrido. El empleado marca obligatoriamente que el cliente autorizó el tratamiento, con fecha y versión del aviso que le leyó; el negocio es el Responsable (DEC-E37). Si el cliente no usa Telegram, no recibe avisos ni ve el mapa.
- DEC-E68. Cada negocio activa o desactiva la consulta de estado para sus clientes: un comando «ver estado» a demanda en el bot. Los avisos de cambio de estado (DEC-E17) y el mapa no dependen de esta opción.
- DEC-E69. Nuevo estado «recogido» entre «listo para recoger» y «en camino». Lo marca el domiciliario y no exige ubicación; la ubicación en tiempo real se exige para pasar a «en camino» (DEC-E14). El cliente y el negocio pueden cancelar hasta antes de «recogido».
- DEC-E70. El administrador puede suspender o eliminar empleados y domiciliarios, siempre con un motivo que queda registrado. Suspender bloquea el acceso y se puede revertir; eliminar desvincula de forma definitiva, y el historial y los pedidos conservan su nombre. No se puede hacer mientras el domiciliario tenga un pedido «en camino»; sus pedidos asignados que no han salido se liberan con aviso a quien los asignó (como DEC-E31).
- DEC-E71. El rol «dueño de la plataforma» se mantiene como está.
- DEC-E72. En las evidencias, lo que hizo un asistente o agente de IA dice que fue aprobado por la estudiante. Nada se hace sin aprobación humana.
- DEC-E73. El domiciliario ve en la Mini App una ruta dibujada desde su ubicación actual (la de su ubicación en tiempo real de Telegram) hasta el punto de entrega. El administrador, el empleado y el cliente siguen el recorrido de dos formas: una ubicación en tiempo real que el bot les envía y actualiza en su chat de Telegram, y el mapa de la Mini App (DEC-E16).
- DEC-E74. Mapa y rutas con Mapbox. El cliente comparte, además de la dirección escrita, un pin de ubicación de Telegram como punto de entrega; no se usa la geocodificación de Mapbox (sus resultados gratuitos no se pueden guardar).
- DEC-E75. Un domiciliario tiene un solo pedido «en camino» a la vez, para que ningún cliente vea el camino a la casa de otro.
- DEC-E76. El catálogo se mantiene completo (categorías, precios, agotados e imágenes, por chat y Mini App).
- DEC-E77. Cada autorización de datos se puede leer completa antes de aceptarla: el bot ofrece «Leer autorización» antes de «Acepto», y el texto también se puede abrir en la Mini App.
- DEC-E78. La solución se despliega públicamente, toda en el plan gratuito de Vercel: la API, el webhook del bot y la Mini App. Sin pg-boss ni procesos de fondo; el mapa de la Mini App se actualiza con consultas periódicas en lugar de SSE; las imágenes subidas por la Mini App no van a disco local. La base de datos y el almacenamiento de imágenes los propone ARQ-001 entre servicios gratuitos.
- DEC-E79. Las revisiones frecuentes (asignación vencida a los 3 minutos y ubicación interrumpida) las dispara cada minuto un servicio externo gratuito de cron que llama un endpoint protegido; las diarias (7 y 30 días) usan el cron de Vercel. El retraso máximo de un aviso es de un minuto aproximadamente.
- DEC-E80. Todo lo especificado debe quedar construido. No hay fecha de entrega exacta.
- DEC-E81. El servicio es solo para mayores de 18 años, en todos los roles. Cada autorización incluye la declaración «soy mayor de 18 años»; quien no la acepta no puede continuar (Ley 1581 art. 7).

Cambios a decisiones anteriores (2026-11-19, revisión de conflictos):
- DEC-E03: se quita el multi-negocio para domiciliarios (evitaba superar la carga real y mostrar su ubicación a otro negocio).
- DEC-E09: se quitan los pedidos programados; fuera de horario no se reciben pedidos.
- DEC-E13 y DEC-E26: un negocio vencido cancela sus pedidos no despachados, con confirmación del dueño de la plataforma.
- DEC-E16: el administrador también ve el mapa (puede asignar, DEC-E11).
- DEC-E21 y DEC-E22: confirmar es pasar a «en preparación»; nuevo estado final «con novedad».
- DEC-E24: el aviso de ubicación interrumpida llega también al administrador.
- DEC-E15: el recorrido se guarda 30 días.

Cambios a decisiones anteriores (2026-11-27, respuestas del profesor):
- DEC-E04: el negocio también registra pedidos (DEC-E66).
- DEC-E13, DEC-E21 y DEC-E22: nuevo estado «recogido»; se cancela hasta antes de él (DEC-E69).
- DEC-E16: además del mapa, el recorrido se ve en el chat de Telegram (DEC-E73).
- DEC-E19: sin fecha exacta; todo debe quedar construido (DEC-E80).
- DEC-E61, DEC-E62 y DEC-E63: despliegue en Vercel sin pg-boss, sin SSE y sin disco local (DEC-E78, DEC-E79).
- DEC-E65: Mapbox en lugar de OpenStreetMap (DEC-E74).

# 4. Restricciones del proyecto

- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración.
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante.
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar.
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales.
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración.
- Plazo: sin fecha exacta; todo lo especificado debe quedar construido (DEC-E80).
- Despliegue público obligatorio, en el plan gratuito de Vercel (DEC-E78).

# 5. Fuera de alcance

- No es una central de repartidores.
- No es un marketplace.
- No cobra comisión por pedido ni por entrega.
- No depende de otro aplicativo para su funcionamiento básico.
- No detecta desvíos de ruta ni usa geocercas (geofencing) (DEC-E60).

# 6. Contexto normativo

- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada (3.3).
- Colombia: artículo 15 de la Constitución (habeas data), Ley 1581 de 2012 y Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015 (autorización previa, expresa e informada; aviso de privacidad; política de tratamiento; derechos de los titulares; transmisión y transferencia de datos). Autoridad: Superintendencia de Industria y Comercio.
- Verificado el 2026-11-27 sobre los textos de la Ley 1581 de 2012 y el Decreto 1377 de 2013 (Gestor Normativo de Función Pública, copias aportadas por la estudiante). Lo que obliga al diseño:
  - Autorización previa, expresa e informada, obtenida por un medio que permita consultarla después (Ley art. 3 a, 4 c y 9). Vale por escrito, oral o por conducta inequívoca; el silencio nunca cuenta (Decreto art. 7). El Responsable conserva la prueba y entrega copia si el titular la pide (Ley art. 12 parágrafo; Decreto art. 8).
  - Al pedirla se informa: los datos que se recogen y cada finalidad (Decreto art. 5), el tratamiento, los derechos del titular y la identificación, dirección física o electrónica y teléfono del Responsable (Ley art. 12). Si cambia la finalidad, se pide una nueva autorización (Decreto art. 5).
  - Aviso de privacidad mínimo: Responsable y contacto, tratamiento y finalidad, derechos, y cómo consultar la política de tratamiento (Decreto art. 15). Se conserva el modelo de cada aviso usado (Decreto art. 16).
  - Política de tratamiento, en lenguaje claro: Responsable con domicilio, dirección, correo y teléfono; tratamiento y finalidad; derechos; persona o área que atiende peticiones; procedimiento para ejercer los derechos y revocar; fecha de vigencia y período de vigencia de la base de datos (Decreto art. 13 y 18).
  - Derechos: conocer, actualizar, rectificar, pedir prueba de la autorización, saber el uso dado, quejarse ante la SIC, revocar o pedir supresión y acceder gratis (Ley art. 8). Consulta gratuita al menos una vez al mes (Decreto art. 21).
  - Revocación y supresión en todo momento mediante reclamo, con mecanismos gratuitos y de fácil acceso; no proceden si hay un deber legal o contractual de permanecer en la base de datos (Decreto art. 9).
  - Plazos: consulta 10 días hábiles, prorrogables 5 (Ley art. 14). Reclamo 15 días hábiles, prorrogables 8; si está incompleto se pide corregir en 5 días y se entiende desistido a los 2 meses; en 2 días hábiles se marca el dato con la leyenda «reclamo en trámite» hasta decidirlo (Ley art. 15).
  - Responsable y Encargado designan una persona o área de protección de datos (Decreto art. 23). Transmisión a un Encargado con contrato que fije alcance, actividades y obligaciones (tratar según los principios, seguridad y confidencialidad); con ese contrato, la transmisión internacional no requiere informar ni pedir consentimiento (Decreto art. 24 y 25). La transferencia internacional a países sin nivel adecuado está prohibida salvo autorización expresa e inequívoca u otras excepciones (Ley art. 26).
  - Conservación: solo el tiempo razonable y necesario para la finalidad, teniendo en cuenta aspectos administrativos, contables, fiscales, jurídicos e históricos; después se suprime, salvo obligación legal o contractual, y el procedimiento se documenta (Decreto art. 11). La norma no fija un número de días.
  - Datos sensibles (Ley art. 5; Decreto art. 3): origen racial o étnico, orientación política, convicciones, pertenencia a sindicatos u organizaciones, salud, vida sexual y biometría. La ubicación no está en la lista; es dato personal y necesita autorización y seguridad.
  - Menores: tratamiento proscrito salvo datos públicos (Ley art. 7); excepción con autorización del representante legal (Decreto art. 12).
  - Recolección limitada a datos pertinentes y adecuados (Decreto art. 4). Los datos personales no se ponen en internet salvo acceso técnicamente controlado para los autorizados (Ley art. 4 f). Incidentes de seguridad se informan a la SIC (Ley art. 17 n y 18 k).
  - Registro Nacional de Bases de Datos (Ley art. 25): lo reglamenta el Decreto 886 de 2014, que no se ha revisado; queda por verificar si aplica.
- Referencias internacionales leídas el 2026-11-27: RGPD art. 7, 13, 17, 25 y 28 (retirar el consentimiento debe ser tan fácil como darlo; informar el plazo de conservación) y LGPD de Brasil art. 8, 9 y 18 (cláusula de consentimiento destacada; informar las consecuencias de no aceptar).
- Referencia internacional de buenas prácticas (no se asume que aplique jurídicamente): principios del Reglamento General de Protección de Datos de la Unión Europea (minimización, limitación de finalidad y de plazo de conservación, transparencia).
- Textos de los avisos: docs/legal/avisos-de-privacidad.md (borrador; requiere revisión de una persona con formación jurídica antes de usarse con datos reales).

# 7. Vacíos conocidos (pendientes por decidir)

El enunciado no los define. Cualquier agente que los necesite crea una pregunta (`OPEN-Q` en la SPEC o `docs/preguntas/PREG-xxx.md`) y no los resuelve solo.

Resueltos el 2026-11-21 y el 2026-11-27 (ver 3.11, DEC-E01 a DEC-E80): acceso e identidad, vinculación, uso del bot por el cliente, multi-negocio, ciclo de vida y responsables de cada estado, asignación y rechazo, tope de carga, ubicación, quién ve el mapa, notificaciones, cobertura y horario, pago, duplicados, suscripción, reportes y plazo.

Siguen abiertos (los resuelve el agente de especificación con preguntas en cada SPEC):

1. Cuánto tiempo se conservan los datos personales de clientes y personal después de terminar la relación con el negocio (la norma aplicable y los consentimientos ya están decididos: DEC-E36 a DEC-E39).
2. En un pedido a domicilio registrado por el negocio (DEC-E66), cómo se fijan la tarifa (¿zona de la lista?) y el punto de entrega para la ruta, si el cliente no comparte un pin de Telegram.
3. Si se puede suspender o eliminar a un domiciliario que tiene un pedido «recogido» que aún no va en camino (DEC-E70).
4. Si la licencia de Mapbox exige un permiso aparte para una aplicación de domicilios («vehicle usage» en sus términos); los términos de producto no se pudieron leer (DEC-E74).
