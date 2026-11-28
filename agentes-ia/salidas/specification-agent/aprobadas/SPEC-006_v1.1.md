<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: ninguno (aprobación sin modelo)
Fecha: 2026-11-21 15:55
Petición: El equipo aprueba la SPEC-006
-->

# SPEC-006. Seguimiento de la entrega, ubicación en tiempo real y Mini App - Versión 1.1
Estado: Aprobada y congelada
Modo: Aprobación
Necesidad original: "Especifica el seguimiento de la entrega: paso a en camino por el domiciliario compartiendo su ubicación en tiempo real de Telegram, obligatoria para ese paso (DEC-E14, DEC-E22) y con su consentimiento de ubicación (DEC-E38); paso a entregado o registro de una novedad que deja el pedido en el estado final con novedad (DEC-E21, DEC-E22); ubicación interrumpida en camino: el pedido sigue, el mapa muestra la última posición con su hora, el bot pide reactivarla y se avisa al administrador y al empleado (DEC-E24); recorrido guardado 30 días (DEC-E15); mapa en la Mini App para el administrador y el empleado con los domiciliarios en ruta de su negocio y para el cliente solo con el domiciliario de su pedido mientras está en camino (DEC-E16); avisos al cliente en cada cambio de estado con acceso al mapa al pasar a en camino (DEC-E17); avisos al negocio de novedades (DEC-E25); el administrador consulta el recorrido de un pedido finalizado (DEC-E33). La ubicación es un dato personal que se protege. Las historias aprobadas están en el archivo adjunto: usa HU-26 a HU-32. Dependencias: SPEC-005 (asignación). Es una sola funcionalidad."
Épica: EPIC-004

## Análisis
- Objetivo: Coordinar el seguimiento en tiempo real del pedido desde su despacho hasta la entrega o registro de novedad, regulando el acceso al mapa en la Mini App según el rol, registrando la confirmación de cobro cuando corresponda y resguardando la privacidad de la ubicación del domiciliario.
- Alcance inicial: Cambio de estado a «en camino» exigiendo ubicación en vivo y consentimiento previo; pasaje a estados finales «entregado» (con confirmación de cobro según forma de pago) o «con novedad» (según catálogo de motivos); gestión de señal GPS interrumpida; visualización de mapa interactivo para negocio y cliente; notificaciones asociadas; conservación y purga del recorrido a los 30 días.
- Actores: Domiciliario, Cliente, Administrador del negocio, Empleado o vendedor.
- Contexto aplicable: 3.2, 3.3, 3.7, 3.8, DEC-E14, DEC-E15, DEC-E16, DEC-E17, DEC-E21, DEC-E22, DEC-E24, DEC-E25, DEC-E30, DEC-E32, DEC-E33, DEC-E38, DEC-E55, DEC-E56, DEC-E57, DEC-E58.

## Modelo de dominio
- Pedido: pertenece a Negocio; cardinalidad 1 a N. Origen: contexto 3.8.
- Domiciliario: pertenece a Negocio; cardinalidad 1 a N. Origen: contexto 3.6, DEC-E03.
- Punto de geolocalización: pertenece a Domiciliario y a Pedido; cardinalidad N puntos por Pedido mientras está en camino. Origen: DEC-E14.
- Recorrido histórico: pertenece a Pedido; conservado durante 30 días. Origen: DEC-E15.
- Consentimiento de ubicación: pertenece a Domiciliario; registrado antes de permitir la transmisión de señal. Origen: DEC-E38.
- Novedad de entrega: pertenece a Pedido; registrada durante el trayecto en camino según catálogo predefinido. Origen: DEC-E21, DEC-E22, DEC-E55.
- Confirmación de cobro: pertenece a Pedido; registrada al entregar si la forma de pago requiere recaudo presencial. Origen: DEC-E56, DEC-E57.

## Contradicciones detectadas
Ninguna.

## Análisis de impacto
- DEC-001 (DEC-E55): Afecta RF-055, AC-055. Todos actualizados para detallar el catálogo exacto de novedades (cliente ausente, dirección no encontrada, cliente rechaza el pedido, otro motivo con texto breve).
- DEC-002 (DEC-E56, DEC-E57): Afecta RF-054, BR-027, AC-054, AC-066. Todos actualizados para requerir la confirmación de «cobrado» cuando el pedido tenga una forma de pago cuyo tipo no sea transferencia.
- DEC-003 (DEC-E58): Afecta RF-056, CL-010, AC-057. Todos actualizados para precisar que ante interrupción de ubicación sin reactivación, el pedido se mantiene en «en camino» hasta que el domiciliario entregue o reporte novedad, gestionando la coordinación fuera del bot.

## Preguntas de aclaración
No hay preguntas pendientes.

## Especificación

### 1. Objetivo
Permitir el seguimiento en tiempo real del recorrido del domiciliario desde que el pedido pasa a «en camino» hasta su entrega o registro de novedad, verificando el recaudo presencial en la entrega cuando aplique, visualizando el mapa en la Mini App de Telegram según los permisos de cada actor, enviando notificaciones de estado y conservando la trazabilidad del recorrido durante 30 días.

### 2. Contexto
En Domiciliarios Eje, la fase de entrega requiere coordinar en tiempo real la salida del domiciliario, la recepción de coordenadas de ubicación mediante Telegram y la actualización constante del estado del servicio. Es crucial proteger los datos de geolocalización, de modo que el cliente solo vea al domiciliario asignado a su pedido mientras esté en camino, y que el personal del negocio supervise a sus repartidores en ruta sin cruzar datos entre establecimientos.

Decisiones del equipo:
- DEC-001. Opciones de novedad registrables por el domiciliario: cliente ausente, dirección no encontrada, cliente rechaza el pedido y otro motivo con texto breve. Responde a OPEN-Q-001 (DEC-E55).
- DEC-002. Para pedidos cuya forma de pago implique cobro al entregar (toda forma de pago cuyo tipo no sea transferencia), el domiciliario confirma «cobrado» al marcar el pedido como entregado, lo cual se registra junto con la entrega. Responde a OPEN-Q-002 (DEC-E56, DEC-E57).
- DEC-003. Si el domiciliario no reactiva la ubicación en tiempo real tras la interrupción, el pedido se mantiene en estado «en camino» hasta que finalice por entrega o novedad; el negocio coordina la gestión fuera del bot. Responde a OPEN-Q-003 (DEC-E58).

### 3. Alcance
- Transición del pedido a «en camino» condicionada al envío de ubicación en tiempo real de Telegram y consentimiento previo (DEC-E14, DEC-E38).
- Transición a estados finales «entregado» (con confirmación de «cobrado» si la forma de pago es distinta a transferencia) o «con novedad» (DEC-E21, DEC-E22, DEC-E55, DEC-E56, DEC-E57).
- Gestión de señal GPS interrumpida durante el recorrido sin alterar el flujo del pedido (DEC-E24, DEC-E58).
- Visualización de mapa interactivo en Mini App por rol y por negocio (DEC-E16).
- Notificaciones automáticas de cambio de estado y reporte de novedades (DEC-E17, DEC-E25).
- Almacenamiento y borrado automático del recorrido tras 30 días calendarios, permitiendo la consulta por el administrador (DEC-E15, DEC-E33).

### 4. Actores e historias de usuario
Actores: Domiciliario, Cliente, Administrador del negocio, Empleado o vendedor.
- HU-026. Como domiciliario, quiero cambiar el estado de un pedido asignado a «en camino» compartiendo mi ubicación en tiempo real, para indicar que salí hacia la entrega y permitir el seguimiento del pedido por parte del negocio y del cliente.
- HU-027. Como domiciliario, quiero marcar un pedido en camino como «entregado», confirmando el recaudo de dinero si corresponde, para dar por finalizado el servicio, suspender la transmisión de mi ubicación y liberar mi cupo de carga asignada.
- HU-028. Como domiciliario, quiero registrar una novedad sobre un pedido que llevo en camino seleccionando la causa correspondiente, para reportar oportunamente los impedimentos de la entrega y alertar al negocio para que tome decisiones.
- HU-029. Como empleado o vendedor, quiero recibir una alerta si un domiciliario en ruta deja de compartir su ubicación, para verificar la última posición conocida, solicitarle la reactivación y coordinar el despacho sin cancelar el pedido.
- HU-030. Como cliente, quiero ver en un mapa interactivo la ubicación del domiciliario que transporta mi pedido en camino, para conocer el avance de mi entrega en tiempo real de forma segura.
- HU-031. Como administrador del negocio, quiero ver en un mapa interactivo a todos los domiciliarios de mi establecimiento que se encuentran en camino, para supervisar el avance global de las entregas y balancear la operación.
- HU-032. Como administrador del negocio, quiero consultar el recorrido realizado por un domiciliario en un pedido finalizado durante el tiempo de conservación fijado, para revisar inquietudes o aclaraciones sobre el trayecto de la entrega antes de su borrado.

### 5. Requisitos funcionales
- RF-050. El sistema debe permitir al domiciliario asignado a un pedido en estado «listo para recoger» cambiar el estado a «en camino» únicamente si mantiene activo el consentimiento de ubicación (DEC-E38) y transmite su ubicación en tiempo real de Telegram. Origen: DEC-E14, DEC-E22, DEC-E38, HU-26.
- RF-051. El sistema debe solicitar confirmación previa al domiciliario antes de ejecutar el cambio de estado a «en camino», «entregado» o «con novedad». Origen: contexto 3.7, HU-26, HU-27, HU-28.
- RF-052. El sistema debe actualizar el estado del pedido a «en camino», «entregado» o «con novedad», registrando en el sistema la fecha, hora exacta y responsable de la operación. Origen: contexto 3.2, 3.8, DEC-E21, DEC-E22.
- RF-053. El sistema debe enviar una notificación automática al cliente cuando su pedido cambie de estado, incluyendo en la notificación de «en camino» un enlace seguro de acceso al mapa de seguimiento de su pedido en la Mini App. Origen: DEC-E17, HU-26, HU-30.
- RF-054. El sistema debe permitir al domiciliario asignado pasar un pedido en estado «en camino» a «entregado», finalizando el servicio, deteniendo la transmisión de ubicación para el cliente, liberando 1 cupo de la carga asignada al domiciliario y solicitando la confirmación de «cobrado» cuando la forma de pago asignada no sea de tipo transferencia. Origen: DEC-E14, DEC-E22, DEC-E30, DEC-E56, DEC-E57, HU-27.
- RF-055. El sistema debe permitir al domiciliario asignado registrar una novedad en un pedido en estado «en camino» seleccionando entre las opciones «cliente ausente», «dirección no encontrada», «cliente rechaza el pedido» u «otro motivo» con texto breve, cambiando el pedido al estado final «con novedad», deteniendo el seguimiento en mapa, liberando el cupo de carga del domiciliario y notificando inmediatamente al administrador y al empleado del negocio. Origen: DEC-E21, DEC-E22, DEC-E25, DEC-E55, HU-28.
- RF-056. El sistema debe mantener el pedido en estado «en camino» si el domiciliario interrumpe la transmisión de ubicación en tiempo real sin reactivarla, registrando la última posición conocida con su hora exacta, solicitando al domiciliario reactivar la ubicación, enviando una alerta de pérdida de señal al administrador y al empleado del negocio, y permitiendo que la entrega o el registro de novedad continúen normalmente o mediante gestión fuera del bot. Origen: DEC-E24, DEC-E25, DEC-E58, HU-29.
- RF-057. El sistema debe permitir al cliente visualizar en la Mini App el mapa interactivo con la ubicación en tiempo real del domiciliario asignado únicamente mientras su pedido permanezca en estado «en camino». Origen: DEC-E16, HU-30.
- RF-058. El sistema debe permitir al administrador del negocio y al empleado o vendedor consultar en la Mini App el mapa interactivo con los domiciliarios en ruta (estado «en camino») pertenecientes exclusivamente a su establecimiento. Origen: contexto 3.3, DEC-E16, HU-31.
- RF-059. El sistema debe permitir al administrador del negocio consultar el trazado completo del recorrido realizado en un pedido finalizado de su negocio si la antigüedad del pedido no supera los 30 días calendarios. Origen: DEC-E15, DEC-E33, HU-32.
- RF-060. El sistema debe eliminar de forma permanente la información del recorrido histórico de un pedido transcurridos 30 días calendarios desde su finalización, conservando únicamente la fecha, hora, estado final y responsable. Origen: DEC-E15, HU-32.

### 6. Requisitos no funcionales
- RNF-010. Seguridad y Privacidad. Ninguna vista, notificación o mensaje debe exponer identificadores de Telegram, ubicación en tiempo real ni historial de ubicación a usuarios no autorizados o pertenecientes a otros negocios. Se verifica con: prueba de autorización por rol y aislamiento entre negocios mediante inspección de respuestas de API y mensajes. Origen: contexto 3.2, 3.3, regla crítica 7.
- RNF-011. Integridad y Concurrencia. Las actualizaciones de estado del pedido («en camino», «entregado», «con novedad») y la liberación del cupo de carga del domiciliario deben ejecutarse de forma atómica en el sistema. Se verifica con: prueba de concurrencia simulando solicitudes simultáneas sobre un mismo pedido. Origen: contexto 3.2, 3.8.

### 7. Reglas de negocio
- BR-020. Restricción de cambio a «en camino» sin ubicación. El sistema debe rechazar cualquier intento de pasar un pedido a «en camino» si el domiciliario no ha iniciado la transmisión de su ubicación en tiempo real o no cuenta con consentimiento de ubicación activo. Origen: DEC-E14, DEC-E38, HU-26.
- BR-021. Autorización de cambio de estado por domiciliario. Solo el domiciliario asignado al pedido puede pasar el estado a «en camino», «entregado» o registrar «con novedad». Intentos por parte del cliente, de otro domiciliario o de personal de otro negocio deben ser rechazados por el sistema. Origen: contexto 3.2, 3.3, 3.8, HU-26.
- BR-022. Inmutabilidad de estados finales. Un pedido en estado final («entregado», «con novedad», «rechazado» o «cancelado») no permite cambios posteriores de estado ni registro de nuevas novedades. Origen: DEC-E21, DEC-E22, HU-28.
- BR-023. Visibilidad de ubicación para cliente restringida al estado «en camino». El cliente solo puede visualizar la posición del domiciliario mientras el pedido esté en estado «en camino». En estados previos o finales («entregado», «con novedad», «cancelado»), la visualización de la posición en vivo se inabilita. Origen: DEC-E14, DEC-E16, HU-30.
- BR-024. Aislamiento multinegocio en mapa de Mini App. El administrador y el empleado solo pueden ver en el mapa la ruta en vivo de los domiciliarios con pedidos en camino del negocio en el que están autenticados; solo el administrador consulta el recorrido de pedidos finalizados (DEC-E33, RF-059). Origen: contexto 3.2, 3.3, DEC-E16, HU-31, HU-32.
- BR-025. Retención de recorrido por 30 días. Los puntos de geolocalización del recorrido se conservan durante 30 días calendarios contados desde la finalización del pedido. Cumplido dicho plazo, las coordenadas de ruta se eliminan automáticamente. Origen: DEC-E15, HU-32.
- BR-026. Liberación de cupo de domiciliario al finalizar. Al cambiar un pedido al estado «entregado» o «con novedad», el sistema descuenta 1 unidad de la carga simultánea actual del domiciliario asignado. Origen: DEC-E12, DEC-E30, HU-27, HU-28.
- BR-027. Registro de recaudo al entregar. Para pedidos cuya forma de pago asignada tenga un tipo distinto a transferencia (cobro presencial en entregas de efectivo o datáfono), el sistema exige la confirmación explícita de «cobrado» por parte del domiciliario para marcar la entrega. Origen: DEC-E56, DEC-E57, HU-27.

### 8. Flujo principal
1. El domiciliario asignado selecciona en el bot de Telegram un pedido de su negocio en estado «listo para recoger».
2. El domiciliario inicia la transmisión de su ubicación en tiempo real en Telegram (si no ha firmado el consentimiento de ubicación DEC-E38, el bot se lo solicita previamente).
3. El domiciliario solicita cambiar el pedido a estado «en camino».
4. El sistema le pide confirmación explícita (contexto 3.7).
5. El domiciliario confirma la operación.
6. El sistema verifica autenticación, rol, pertenencia al negocio, asignación del pedido y recepción activa de coordenadas en vivo.
7. El sistema actualiza el estado del pedido a «en camino», guardando fecha, hora exacta y responsable.
8. El sistema envía un aviso al cliente informando que su pedido va en camino e incluye el enlace seguro a la Mini App con el mapa en tiempo real.
9. Durante el recorrido, el sistema registra los puntos GPS para la trazabilidad y actualiza el mapa para el cliente y para el negocio (administrador y empleados).
10. Al llegar a la dirección de entrega, el domiciliario solicita marcar el pedido como «entregado».
11. Si el pedido tiene una forma de pago cuyo tipo no es transferencia (cobro presencial), el sistema le pide confirmar que ha cobrado el valor del servicio (DEC-E56, DEC-E57).
12. El sistema le pide confirmación explícita de la entrega (contexto 3.7).
13. El domiciliario confirma la entrega y el cobro correspondiente.
14. El sistema actualiza el pedido al estado final «entregado», registra fecha, hora, responsable y la confirmación de cobro, finaliza la visualización de ubicación para el cliente y libera 1 cupo de carga del domiciliario.
15. El sistema notifica al cliente que su entrega concluyó con éxito.

### 9. Flujos alternativos y de excepción
- A1. Registro de novedad durante la entrega:
  1. Durante el trayecto en camino (paso 9 del flujo principal), el domiciliario selecciona registrar novedad.
  2. El sistema despliega las opciones: «cliente ausente», «dirección no encontrada», «cliente rechaza el pedido» u «otro motivo» (DEC-E55).
  3. Si elige «otro motivo», el domiciliario ingresa un texto breve explicativo.
  4. El domiciliario confirma la novedad tras el mensaje de confirmación del sistema (contexto 3.7).
  5. El sistema cambia el pedido al estado final «con novedad», revoca el seguimiento en mapa para el cliente, libera el cupo de carga del domiciliario y registra fecha, hora, responsable y la novedad explicativa.
  6. El sistema envía una alerta inmediata al administrador y al empleado del negocio con los detalles del suceso.
- E1. Intento de pasar a «en camino» sin compartir ubicación:
  1. En el paso 3 del flujo principal, el domiciliario solicita pasar a «en camino» sin transmitir ubicación en tiempo real.
  2. El sistema invalida la solicitud (BR-020).
  3. El bot notifica al domiciliario que compartir la ubicación en directo es obligatorio para iniciar el recorrido y mantiene el pedido en «listo para recoger».
- E2. Interrupción de transmisión de ubicación en ruta:
  1. En estado «en camino», el domiciliario detiene o pierde la transmisión de ubicación en Telegram.
  2. El sistema mantiene el pedido en estado «en camino» y fija la última posición reportada con su fecha y hora exacta (DEC-E24, DEC-E58).
  3. El bot solicita al domiciliario reactivar el envío de ubicación.
  4. El sistema notifica al administrador y al empleado del negocio sobre la pérdida de señal y la última posición registrada.
  5. El pedido continúa en «en camino» sin alteración; el negocio coordina la reactivación fuera del bot y el domiciliario puede marcar «entregado» o registrar novedad cuando corresponda.
  6. Si el domiciliario reactiva la ubicación, el sistema reanuda la actualización en tiempo real en el mapa.
- E3. Intento de cambio de estado por usuario no autorizado:
  1. Un cliente, otro domiciliario o un usuario de otro establecimiento intenta cambiar el estado de un pedido en camino.
  2. El sistema verifica las credenciales y la pertenencia al negocio (contexto 3.2, 3.3).
  3. El sistema rechaza la operación sin modificar la información del pedido.

### 10. Casos límite
- CL-010. Interrupción prolongada de señal GPS sin reactivación: El pedido permanece en estado «en camino» mostrando en el mapa la última ubicación conocida con su fecha y hora exacta, permitiendo al domiciliario entregar el pedido o registrar novedad, mientras la coordinación de la reactivación se gestiona fuera del bot por el administrador o empleado. Origen: DEC-E24, DEC-E58, HU-29.
- CL-011. Consulta de recorrido en el límite exacto de 30 días calendarios: El sistema permite la visualización del mapa de recorrido si la consulta ocurre dentro de los 30 días calendarios (720 horas) posteriores a la finalización; transcurrido el segundo posterior a las 720 horas, las coordenadas son depuradas y el sistema responde que el historial fue eliminado por política de privacidad. Origen: DEC-E15, BR-025.

### 11. Criterios de aceptación
- AC-050. Dado un pedido en estado «listo para recoger» asignado al domiciliario D1 del negocio N1, cuando D1 comparte su ubicación en tiempo real en Telegram con consentimiento de ubicación activo e inicia el cambio a «en camino», entonces el sistema le solicita confirmación previa antes de ejecutar la operación (Verifica RF-050, BR-020, BR-021, HU-26).
- AC-051. Dado que el domiciliario D1 confirma pasar el pedido a «en camino», cuando el sistema procesa la solicitud, entonces actualiza el estado del pedido a «en camino», registra la fecha, la hora exacta y el responsable D1, y envía un aviso al cliente informándole que su pedido va en camino con el enlace de acceso a la Mini App (Verifica RF-051, RF-052, RF-053, HU-26).
- AC-052. Dado un pedido listo para recoger asignado al domiciliario D1, cuando D1 intenta cambiar el estado a «en camino» sin transmitir su ubicación en tiempo real, entonces el sistema rechaza la operación, mantiene el pedido en «listo para recoger» e informa que la ubicación en tiempo real es obligatoria (Verifica BR-020, HU-26).
- AC-053. Dado un pedido del negocio N1 asignado al domiciliario D1, cuando un usuario con rol de cliente o un domiciliario D2 intenta cambiar el estado a «en camino», entonces el sistema rechaza la solicitud y no modifica los datos del pedido (Verifica BR-021, HU-26).
- AC-054. Dado un pedido en estado «en camino» asignado al domiciliario D1 con una forma de pago de tipo transferencia, cuando D1 elige marcar el pedido como «entregado» y confirma la acción, entonces el sistema actualiza el estado al estado final «entregado», registra fecha, hora y responsable, suspende la transmisión de ubicación para el cliente, libera 1 cupo de carga de D1 y notifica al cliente la entrega exitosa (Verifica RF-054, BR-022, BR-026, HU-27).
- AC-055. Dado un pedido en estado «en camino» asignado al domiciliario D1, cuando D1 selecciona registrar novedad, elige una opción del catálogo («cliente ausente», «dirección no encontrada», «cliente rechaza el pedido» u «otro motivo» con texto breve) y confirma, entonces el sistema actualiza el pedido al estado final «con novedad», detiene el seguimiento para el cliente, libera la carga de D1 y envía una alerta con los detalles al administrador y al empleado del negocio (Verifica RF-055, BR-022, BR-026, HU-28).
- AC-056. Dado un pedido que ya se encuentra en estado final («entregado», «con novedad» o «cancelado»), cuando un usuario intenta modificar su estado o registrar una novedad, entonces el sistema rechaza la acción informando que el servicio finalizó (Verifica BR-022, HU-28).
- AC-057. Dado un pedido en estado «en camino», cuando el domiciliario interrumpe la transmisión de ubicación en directo y no la reactiva, entonces el sistema mantiene el pedido en estado «en camino» registrando la última posición con su hora, notifica al administrador y al empleado para coordinar fuera del bot, y permite al domiciliario culminar el servicio como entregado o con novedad (Verifica RF-056, CL-010, HU-29).
- AC-058. Dado un pedido con señal de ubicación interrumpida, cuando el domiciliario reactiva la transmisión en Telegram, entonces el sistema detecta la señal, reanuda la actualización en vivo en la Mini App y continúa el seguimiento sin reiniciar el pedido (Verifica RF-056, HU-29).
- AC-059. Dado un cliente C1 con un pedido propio en estado «en camino», cuando abre el enlace de seguimiento en la Mini App, entonces el sistema muestra el mapa interactivo presentando únicamente la posición del domiciliario asignado a su pedido y la dirección de entrega (Verifica RF-057, BR-023, HU-30).
- AC-060. Dado un cliente C1 cuyo pedido cambia a estado «entregado» o «con novedad», cuando accede al enlace de seguimiento en la Mini App, entonces el sistema inhabilita el mapa en tiempo real y presenta un aviso de servicio finalizado (Verifica BR-023, HU-30).
- AC-061. Dado un cliente C1 autenticado, cuando intenta abrir el enlace de seguimiento de un pedido perteneciente a otro cliente C2 o a otro negocio N2, entonces el sistema niega el acceso y no expone datos de ubicación ni identificadores (Verifica RNF-010, BR-024, HU-30).
- AC-062. Dado un administrador A1 o un empleado E1 del negocio N1 autenticado, cuando abre la Mini App en la vista de monitoreo de negocio, entonces el sistema muestra en el mapa interactivo a todos los domiciliarios de N1 que tienen pedidos en estado «en camino» (Verifica RF-058, BR-024, HU-31).
- AC-063. Dado un usuario con rol de domiciliario o cliente, cuando intenta ingresar a la vista de monitoreo general del negocio en la Mini App, entonces el sistema rechaza el acceso por falta de permisos (Verifica BR-024, HU-31).
- AC-064. Dado el administrador A1 del negocio N1, cuando consulta el detalle de un pedido finalizado de N1 con antigüedad menor o igual a 30 días calendarios, entonces el sistema presenta el mapa con el trazado histórico del recorrido realizado (Verifica RF-059, BR-025, HU-32).
- AC-065. Dado el administrador A1 del negocio N1, cuando consulta un pedido finalizado con antigüedad mayor a 30 días calendarios, entonces el sistema informa que el historial de recorrido fue eliminado por política de privacidad, conservando fecha, hora, estado final y responsable (Verifica RF-060, BR-025, HU-32).
- AC-066. Dado un pedido en estado «en camino» asignado al domiciliario D1 cuya forma de pago es cobrada al entregar (tipo efectivo o datáfono), cuando D1 selecciona marcar como «entregado», entonces el sistema le exige confirmar «cobrado», y al confirmar, el sistema registra el estado final «entregado» con la marca de cobrado registrada, libera la carga de D1 y notifica al cliente (Verifica RF-054, BR-027, HU-27).

### 12. Dependencias
- SPEC-002: Configuración del negocio (usuarios, personal, roles, formas de pago).
- SPEC-004: Registro y gestión de pedidos (creación y estados iniciales).
- SPEC-005: Asignación y despacho de domiciliarios (pedido en estado listo para recoger asignado a un repartidor).

### 13. Restricciones
- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración. (Contexto sección 4)
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante. (Contexto sección 4)
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar. (Contexto sección 4)
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales. (Contexto sección 4)
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración. (Contexto sección 4)
- Plazo: unas 8 semanas o más (DEC-E19). (Contexto sección 4)
- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada (3.3). (Contexto sección 6)
- Colombia: artículo 15 de la Constitución (habeas data), Ley 1581 de 2012 y Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015 (autorización previa, expresa e informada; aviso de privacidad; política de tratamiento; derechos de los titulares; transmisión y transferencia de datos). Autoridad: Superintendencia de Industria y Comercio. (Contexto sección 6)
- Referencia internacional de buenas prácticas: principios del Reglamento General de Protección de Datos de la Unión Europea (minimización, limitación de finalidad y de plazo de conservación, transparencia). (Contexto sección 6)
- Textos de los avisos: docs/legal/avisos-de-privacidad.md. (Contexto sección 6)

### 14. Fuera de alcance
- No es una central de repartidores (Contexto sección 5).
- No es un marketplace (Contexto sección 5).
- No cobra comisión por pedido ni por entrega (Contexto sección 5).
- No depende de otro aplicativo para su funcionamiento básico (Contexto sección 5).
- El sistema no detecta desvíos de ruta ni usa geocercas (geofencing). Origen: DEC-E60.
- [Librería o proveedor de renderizado de mapas en Mini App]: tema para arquitectura. Origen: RF-057, RF-058.
- [Mecanismo de depuración periódica de recorridos de más de 30 días en base de datos]: tema para arquitectura. Origen: RF-060.

### 15. Preguntas abiertas
- OPEN-Q-001: Respondida (DEC-001).
- OPEN-Q-002: Respondida (DEC-002).
- OPEN-Q-003: Respondida (DEC-003).

### 16. Trazabilidad
- HU-026: RF-050, RF-051, RF-052, RF-053; BR-020, BR-021; AC-050, AC-051, AC-052, AC-053.
- HU-027: RF-051, RF-052, RF-054; BR-021, BR-022, BR-026, BR-027; AC-054, AC-066.
- HU-028: RF-051, RF-052, RF-055; BR-021, BR-022, BR-026; AC-055, AC-056.
- HU-029: RF-056; BR-024; AC-057, AC-058; CL-010.
- HU-030: RF-053, RF-057; BR-023, BR-024; AC-059, AC-060, AC-061.
- HU-031: RF-058; BR-024; AC-062, AC-063.
- HU-032: RF-059, RF-060; BR-025; AC-064, AC-065; CL-011.
- RF-050: Origen: DEC-E14, DEC-E22, DEC-E38, HU-26; verificado por AC-050.
- RF-051: Origen: contexto 3.7, HU-26, HU-27, HU-28; verificado por AC-051, AC-054, AC-055.
- RF-052: Origen: contexto 3.2, 3.8, DEC-E21, DEC-E22; verificado por AC-051, AC-054, AC-055.
- RF-053: Origen: DEC-E17, HU-26, HU-30; verificado por AC-051, AC-059.
- RF-054: Origen: DEC-E14, DEC-E22, DEC-E30, DEC-E56, DEC-E57, HU-27; verificado por AC-054, AC-066.
- RF-055: Origen: DEC-E21, DEC-E22, DEC-E25, DEC-E55, HU-28; verificado por AC-055.
- RF-056: Origen: DEC-E24, DEC-E25, DEC-E58, HU-29; verificado por AC-057, AC-058.
- RF-057: Origen: DEC-E16, HU-30; verificado por AC-059.
- RF-058: Origen: contexto 3.3, DEC-E16, HU-31; verificado por AC-062.
- RF-059: Origen: DEC-E15, DEC-E33, HU-32; verificado por AC-064.
- RF-060: Origen: DEC-E15, HU-32; verificado por AC-065.
- RNF-010: Origen: contexto 3.2, 3.3, regla crítica 7; verificado con prueba de autorización por rol y aislamiento entre negocios mediante inspección de respuestas de API y mensajes.
- RNF-011: Origen: contexto 3.2, 3.8; verificado con prueba de concurrencia simulando solicitudes simultáneas sobre un mismo pedido.
- BR-020: Origen: DEC-E14, DEC-E38, HU-26; verificado por AC-050, AC-052.
- BR-021: Origen: contexto 3.2, 3.3, 3.8, HU-26; verificado por AC-050, AC-053.
- BR-022: Origen: DEC-E21, DEC-E22, HU-28; verificado por AC-054, AC-055, AC-056.
- BR-023: Origen: DEC-E14, DEC-E16, HU-30; verificado por AC-059, AC-060.
- BR-024: Origen: contexto 3.2, 3.3, DEC-E16, HU-31, HU-32; verificado por AC-061, AC-062, AC-063.
- BR-025: Origen: DEC-E15, HU-32; verificado por AC-064, AC-065.
- BR-026: Origen: DEC-E12, DEC-E30, HU-27, HU-28; verificado por AC-054, AC-055.
- BR-027: Origen: DEC-E56, DEC-E57, HU-27; verificado por AC-066.
- CL-010: Origen: DEC-E24, DEC-E58, HU-29; verificado por AC-057.
- CL-011: Origen: DEC-E15, BR-025; verificado por AC-064, AC-065.

### 17. Historial de cambios
- Versión 0.1: creación inicial a partir de la necesidad y las historias aprobadas HU-26 a HU-32 de EPIC-004.
- Versión 1.0: versión Candidata. Se incorporan las respuestas del equipo DEC-001 (catalogo de novedades DEC-E55), DEC-002 (confirmación de cobro presencial al entregar DEC-E56, DEC-E57) y DEC-003 (permanencia del estado en camino ante perdida de GPS DEC-E58).
- Versión 1.1: corrección manual de la revisión cruzada de las SPEC (2026-11-21), sin modelo, aprobada por la estudiante: se reemplaza «backend» por «el sistema» (24 menciones; la validación en el servidor es una restricción de arquitectura del contexto 3.2); BR-024 se precisa según DEC-E33 y la detección de desvíos de ruta pasa a fuera de alcance (DEC-E60). Sin otros cambios de contenido.
- Versión 1.1 (aprobación): aprobada y congelada por el equipo, sin cambios de contenido.

## Verificación
- Completitud: cumple. Se respondieron todas las preguntas abiertas de la versión 0.1 y no quedan dudas ni vacíos pendientes en la especificacion.
- Consistencia interna: cumple. Se verificaron las transiciones de estado, la confirmación previa (3.7), los permisos de cada rol y el comportamiento del recaudo según la forma de pago.
- Consistencia con el contexto: cumple. Se compararon todas las decisiones aplicables (DEC-E14 a DEC-E17, DEC-E21, DEC-E22, DEC-E24, DEC-E25, DEC-E30, DEC-E32, DEC-E33, DEC-E38, DEC-E55 a DEC-E58) con las secciones 3 y 6 del contexto.
- No ambigüedad: cumple. Todos los requisitos expresan comportamientos del sistema observables y verificables sin suposiciones técnicas.
- Verificabilidad: cumple. Todos los RF, BR y CL cuentan con criterios de aceptación estructurados en Dado/Cuando/Entonces y los RNF detallan su método de verificación.
- Cobertura de actores: cumple. Se mantiene la asignación de historias por actor (Domiciliario: HU-026 a HU-028, Empleado: HU-029, Cliente: HU-030, Administrador: HU-031 y HU-032).
- Cobertura de AC: cumple. Todos los RF y BR se encuentran cubiertos por al menos un criterio de aceptación.
- Trazabilidad: cumple. La sección 16 correlaciona sin omisiones cada HU, RF, RNF, BR y CL con su origen y su AC o método de prueba correspondiente.
- No invención: cumple. Se incorporaron únicamente las definiciones provistas por la estudiante en sus decisiones oficiales.
- Delimitación: cumple. Los aspectos sobre tecnología de renderizado de mapas y esquemas de depuración en base de datos están derivados a la sección 14 para el agente de arquitectura.

## Siguiente paso
La SPEC-006 versión 1.1 quedó aprobada y congelada.
