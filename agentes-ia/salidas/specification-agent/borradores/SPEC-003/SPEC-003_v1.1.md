<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: ninguno (corrección manual de la revisión cruzada)
Fecha: 2026-11-21 15:39
Petición: corrección manual de la revisión cruzada de las SPEC, pedida por la estudiante
- OPEN-Q-001: el catálogo se organiza por categorías, que gestionan el administrador y el empleado (DEC-E45).
- OPEN-Q-002: un producto está activo, agotado o desactivado; agotado se muestra como no disponible y no se puede pedir; desactivado no se muestra; un producto desactivado se puede reactivar (DEC-E46).
- OPEN-Q-003: el catálogo se gestiona y se consulta tanto por el chat como por la Mini App, para el personal y para el cliente (DEC-E47).
- OPEN-Q-004: nombre y precio obligatorios; descripción corta e imagen opcionales (DEC-E48).
- OPEN-Q-005: el nombre del producto no se repite en el negocio aunque esté desactivado; para volver a venderlo se reactiva (DEC-E49).
-->

# SPEC-003. Gestión y consulta del catálogo de productos del negocio - Versión 1.1
Estado: Candidata
Modo: Cambio
Necesidad original: "EPIC-002. Especifica el catálogo de productos del negocio: el administrador y el empleado crean, modifican y desactivan productos con su precio (DEC-E06, DEC-E27, DEC-E28) y los clientes del negocio lo consultan. Las historias aprobadas están en el archivo adjunto: usa HU-10 como entrada. Dependencias: SPEC-001 y SPEC-002 (candidatas)."
Épica: EPIC-002

## Análisis
- Objetivo: Permitir que el administrador y el empleado o vendedor del negocio configuren y gestionen la oferta de productos organizada por categorías (crear, modificar precio, definir estado activo/agotado/desactivado y gestionar categorías), así como la consulta del catálogo por parte de los clientes, mediante chat conversacional y Mini App en Telegram.
- Alcance inicial: Gestión de categorías, creación de productos (nombre y precio obligatorios; descripción e imagen opcionales), actualización de estado (activo, agotado, desactivado) y precio, unicidad de nombre de producto por negocio, reactivación de productos desactivados, consulta del catálogo organizado por categorías para clientes (mostrando agotados como no disponibles y ocultando desactivados), canales de chat conversacional y Telegram Mini App, y autorización en sistema por rol y negocio.
- Actores: Administrador del negocio, Empleado o vendedor, Cliente.
- Contexto aplicable: Contexto 3.1, 3.2, 3.3, 3.7, 3.11 (DEC-E06, DEC-E27, DEC-E28, DEC-E45, DEC-E46, DEC-E47, DEC-E48, DEC-E49).

## Modelo de dominio
- Categoria: pertenece a Negocio; cardinalidad varias. Origen: contexto 3.11 (DEC-E45).
- Producto: pertenece a Categoria y a Negocio; cardinalidad varios. Origen: contexto 3.11 (DEC-E06, DEC-E45).
- Catálogo: pertenece a Negocio; contiene Categorías y Productos; cardinalidad uno. Origen: contexto 3.11 (DEC-E06, DEC-E45).

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
- DEC-E45: afecta RF-001, RF-007, BR-005, Flujo principal, AC-001, AC-008, Trazabilidad. Se añade la gestión y organización del catálogo por categorías.
- DEC-E46: afecta RF-003, RF-008, BR-002, BR-006, CL-002, AC-004, AC-009, AC-010, Trazabilidad. Se diferencian los estados activo, agotado y desactivado, especificando que un producto agotado se muestra al cliente como no disponible y no se puede pedir, un producto desactivado no se muestra al cliente y un producto desactivado se puede reactivar.
- DEC-E47: afecta RF-009, BR-007, Flujo principal, A1, AC-011, Trazabilidad. Se especifica la disponibilidad de la gestión y consulta del catálogo tanto en chat conversacional como en Telegram Mini App.
- DEC-E48: afecta RF-001, BR-008, CL-001, AC-001, Trazabilidad. Se define que el nombre y el precio son obligatorios, mientras que la descripción corta y la imagen son opcionales.
- DEC-E49: afecta RF-010, BR-009, CL-003, AC-012, Trazabilidad. Se establece la restricción de que el nombre de un producto no se puede repetir dentro del negocio aunque esté desactivado, exigiendo reactivar el producto existente para volver a venderlo.

## Preguntas de aclaración
No hay preguntas pendientes.

## Especificación

### 1. Objetivo
Permitir a los administradores y empleados de un negocio gestionar la oferta de productos organizada por categorías (crear, modificar precio, cambiar estado a activo/agotado/desactivado, reactivar y crear categorías) y permitir a los clientes consultar el catálogo mediante chat de Telegram y Telegram Mini App.

### 2. Contexto
Cada negocio administra su propio catálogo de productos organizado en categorías para coordinar sus entregas a domicilio desde Telegram (chat conversacional o Mini App). Únicamente el personal autorizado del negocio (administrador y empleado o vendedor) puede modificar el catálogo y sus categorías. Los clientes sólo pueden consultar los productos de categorías del negocio, visualizando los activos como disponibles y los agotados como no disponibles, mientras que los desactivados quedan totalmente ocultos.

Decisiones del equipo:
- DEC-E45. El catálogo se organiza por categorías, que gestionan el administrador y el empleado. Responde a OPEN-Q-001.
- DEC-E46. Un producto está activo, agotado o desactivado: agotado se muestra al cliente como no disponible y no se puede pedir; desactivado no se muestra. Un producto desactivado se puede reactivar. Responde a OPEN-Q-002.
- DEC-E47. El catálogo se gestiona y se consulta tanto por el chat como por la Mini App, para el personal y para el cliente. Responde a OPEN-Q-003.
- DEC-E48. Un producto tiene nombre y precio obligatorios, y descripción corta e imagen opcionales. Responde a OPEN-Q-004.
- DEC-E49. El nombre del producto no se repite en el negocio aunque esté desactivado; para volver a venderlo se reactiva el mismo producto. Responde a OPEN-Q-005.

### 3. Alcance
- Gestión de categorías de productos (crear, modificar nombre, organizar productos) por el administrador o el empleado.
- Registro de productos asignados a una categoría con nombre y precio obligatorios, y descripción corta e imagen opcionales.
- Manejo de tres estados del producto: activo (disponible para pedir), agotado (visible como no disponible, sin opción de pedido) y desactivado (oculto para clientes).
- Reactivación de productos previamente desactivados.
- Validación de unicidad de nombre de producto dentro del negocio (incluso si está desactivado).
- Modificación de precio y cambios de estado con confirmación previa del usuario.
- Interacción para personal y clientes a través de chat conversacional de Telegram y Telegram Mini App.
- Consulta del catálogo activo y agotado por parte de los clientes del negocio.
- Control estricto de autorización y aislamiento de datos por negocio en el sistema.

### 4. Actores e historias de usuario
Actores: Administrador del negocio, Empleado o vendedor, Cliente.

- HU-001. Como Administrador del negocio, quiero registrar categorías, productos (con nombre, precio, descripción e imagen), modificar sus precios y gestionar su estado (activo, agotado, desactivado y reactivado) desde el chat o la Mini App, para mantener actualizada la oferta disponible del establecimiento.
- HU-002. Como Empleado o vendedor del negocio, quiero registrar categorías, productos (con nombre, precio, descripción e imagen), modificar sus precios y gestionar su estado (activo, agotado, desactivado y reactivado) desde el chat o la Mini App, para respaldar la gestión operativa de la oferta del negocio.
- HU-003. Como Cliente del negocio, quiero consultar el catálogo organizado por categorías desde el chat o la Mini App, identificando los productos disponibles y los agotados, para seleccionar lo que deseo pedir a domicilio.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir al administrador del negocio y al empleado o vendedor registrar un nuevo producto en una categoría del negocio ingresando obligatoriamente su nombre y precio, e ingresando de forma opcional una descripción corta e imagen. Origen: contexto 3.11 (DEC-E06, DEC-E27, DEC-E48), HU-10.
- RF-002. El sistema debe solicitar confirmación previa al administrador o al empleado antes de guardar la modificación del precio de un producto existente. Origen: contexto 3.7, HU-10.
- RF-003. El sistema debe permitir al administrador del negocio y al empleado o vendedor cambiar el estado de un producto a activo, agotado o desactivado, previa confirmación. Origen: contexto 3.7, 3.11 (DEC-E27, DEC-E28, DEC-E46), HU-10.
- RF-004. El sistema debe permitir únicamente a los clientes vinculados o interactuando con el negocio consultar los productos del catálogo con estado activo u agotado, omitiendo totalmente los productos desactivados. Origen: contexto 3.11 (DEC-E06, DEC-E27, DEC-E46), HU-10.
- RF-005. El sistema debe verificar la identidad, el rol, el negocio y los permisos del usuario ante cualquier intento de creación, modificación de precio, gestión de categorías o cambio de estado de productos, rechazando solicitudes no autorizadas. Origen: contexto 3.2, 3.3, HU-10.
- RF-006. El sistema debe impedir que un usuario de un negocio consulte o altere las categorías y productos pertenecientes al catálogo de otro negocio. Origen: contexto 3.3, HU-10.
- RF-007. El sistema debe permitir al administrador y al empleado crear y modificar las categorías para organizar los productos del catálogo de su negocio. Origen: contexto 3.11 (DEC-E45), HU-10.
- RF-008. El sistema debe permitir al administrador y al empleado reactivar un producto desactivado, cambiando su estado a activo o agotado previa confirmación. Origen: contexto 3.11 (DEC-E46), HU-10.
- RF-009. El sistema debe ofrecer la gestión y la consulta del catálogo de productos tanto por medio de chat conversacional con botones como por la Telegram Mini App. Origen: contexto 3.1, 3.11 (DEC-E47), HU-10.
- RF-010. El sistema debe validar que el nombre de un producto sea único dentro del mismo negocio, impidiendo registrar o renombrar un producto con un nombre que ya exista en el negocio, independientemente de si está activo, agotado o desactivado. Origen: contexto 3.11 (DEC-E49), HU-10.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización. Toda operación sobre el catálogo debe validarse exclusivamente en el sistema garantizando la separación de datos por negocio. Se verifica con: prueba de autorización con tokens/credenciales de diferentes roles y negocios. Origen: contexto 3.2, 3.3.
- RNF-002. Integridad de historial. La desactivación o cambio de estado de un producto no debe eliminar ni alterar la referencia del producto ni sus datos en los pedidos previamente registrados. Se verifica con: prueba funcional de consulta de historial de pedidos tras desactivar o agotar un producto. Origen: contexto 3.11 (DEC-E28, DEC-E46).

### 7. Reglas de negocio
- BR-001. Autorización de gestión de catálogo. Únicamente el Administrador del negocio y el Empleado o vendedor tienen permisos para gestionar categorías, registrar productos, editar precios, modificar estados (activo, agotado, desactivado) y reactivar productos. Los clientes y los domiciliarios no poseen permisos de modificación. Origen: contexto 3.11 (DEC-E27, DEC-E45), HU-10.
- BR-002. Manejo de estados de producto. Un producto activo se muestra al cliente y se puede pedir; un producto agotado se muestra al cliente marcado como no disponible y no se puede seleccionar para pedir; un producto desactivado no se muestra al cliente. Desactivar conserva los registros históricos en pedidos anteriores. Origen: contexto 3.11 (DEC-E28, DEC-E46), HU-10.
- BR-003. Aislamiento por negocio. Los usuarios registrados o vinculados a un negocio solo pueden ver o gestionar el catálogo y categorías de ese negocio específico. Ningún usuario puede interactuar con el catálogo de un negocio ajeno. Origen: contexto 3.3.
- BR-004. Confirmación obligatoria. Toda modificación de precio, cambio de estado (a agotado, desactivado o reactivado) o eliminación/modificación crítica de una categoría requiere confirmación explícita por parte del usuario antes de ejecutarse. Origen: contexto 3.7, HU-10.
- BR-005. Organización por categorías. Todo producto pertenece a una categoría del negocio. El personal del negocio gestiona las categorías del establecimiento. Origen: contexto 3.11 (DEC-E45).
- BR-006. Reactivación de productos. Un producto desactivado no se elimina físicamente; el personal del negocio puede reactivarlo pasándolo a estado activo o agotado. Origen: contexto 3.11 (DEC-E46).
- BR-007. Disponibilidad multicanal en Telegram. La consulta y gestión del catálogo están disponibles en el bot de chat mediante botones/comandos y en la Telegram Mini App del negocio. Origen: contexto 3.1, 3.11 (DEC-E47).
- BR-008. Campos obligatorios y opcionales de producto. Nombre y precio son campos obligatorios para registrar un producto; la descripción corta y la imagen son opcionales. Origen: contexto 3.11 (DEC-E48).
- BR-009. Unicidad de nombre de producto dentro del negocio. El nombre de un producto es único por negocio. No se permite crear dos productos con el mismo nombre ni renombrar a uno existente, aun cuando el producto de nombre duplicado esté desactivado. Para reutilizarlo se debe reactivar el producto original. Origen: contexto 3.11 (DEC-E49).

### 8. Flujo principal
1. El administrador o el empleado accede a la gestión del catálogo en el bot de Telegram o en la Telegram Mini App del negocio.
2. El sistema valida en cada petición la identidad del usuario, su rol (Administrador o Empleado) y la pertenencia al negocio.
3. El usuario selecciona la acción: crear categoría, registrar producto, modificar precio, cambiar estado de producto (activo, agotado, desactivado) o reactivar producto desactivado.
4. Si es creación de categoría: ingresa el nombre de la categoría y el sistema la registra.
5. Si es registro de producto: selecciona la categoría, ingresa nombre y precio obligatorios, y opcionalmente descripción corta e imagen. El sistema valida que el nombre no exista en el negocio y registra el producto con estado activo.
6. Si es modificación de precio: selecciona el producto, ingresa el nuevo valor de precio y el sistema pide confirmación explícita antes de aplicar.
7. Si es cambio de estado (a agotado, desactivado o reactivado): selecciona el producto, elige el nuevo estado y el sistema pide confirmación explícita.
8. El usuario confirma la acción requerida.
9. El sistema ejecuta la actualización y notifica al usuario el resultado de la operación.

### 9. Flujos alternativos y de excepción
- A1. Consulta de catálogo por parte del cliente (chat o Mini App):
  1. El cliente inicia la consulta del catálogo en el bot del negocio o abre la Mini App.
  2. El sistema valida el contexto del negocio.
  3. El sistema presenta el catálogo organizado por categorías.
  4. Para cada categoría, muestra los productos activos (disponibles con precio) y los productos agotados (visibles con etiqueta "No disponible", sin botón de agregar al pedido). Los productos desactivados no aparecen.
- A2. Reactivación de producto desactivado por el personal del negocio:
  1. El administrador o el empleado selecciona ver productos desactivados en la gestión del catálogo.
  2. Selecciona un producto desactivado y elige reactivarlo (a estado activo o agotado).
  3. El sistema solicita confirmación previa.
  4. El usuario confirma y el sistema cambia el estado del producto, volviendo a mostrarlo en la consulta de clientes según el estado seleccionado.
- E1. Intento de gestión del catálogo por rol no autorizado (Cliente o Domiciliario):
  1. Un cliente o domiciliario solicita crear, modificar, cambiar estado o gestionar categorías.
  2. El sistema verifica el rol y deniega la operación.
  3. El sistema responde informando que no posee permisos para gestionar el catálogo.
- E2. Intento de acceso o modificación al catálogo de un negocio ajeno:
  1. Un usuario intenta consultar o alterar categorías o productos de un negocio distinto al suyo.
  2. El sistema rechaza la solicitud por aislamiento de datos.
  3. El sistema emite un mensaje de error por falta de autorización sobre ese negocio.
- E3. Intento de registrar un producto con un nombre ya existente en el negocio:
  1. El usuario intenta crear un producto o modificar su nombre usando una denominación que ya pertenece a otro producto del negocio (activo, agotado o desactivado).
  2. El sistema detecta la duplicidad de nombre.
  3. El sistema rechaza el registro e informa que el nombre ya existe en el negocio, sugiriendo reactivar el producto en caso de estar desactivado.
- E4. Cancelación de confirmación en cambios de precio o de estado:
  1. El usuario solicita cambiar el precio o el estado de un producto.
  2. El sistema pide confirmación.
  3. El usuario rechaza o cancela la confirmación.
  4. El sistema cancela la operación sin modificar el producto.

### 10. Casos límite
- CL-001. Intentar registrar o modificar un precio con un valor no numérico o menor a cero: el sistema rechaza la operación e informa que el precio debe ser un número mayor o igual a cero. Origen: contexto 3.11 (DEC-E48).
- CL-002. Intentar cambiar el estado de un producto al mismo estado en el que ya se encuentra (por ejemplo, marcar como agotado un producto que ya está agotado): el sistema informa que el producto ya se encuentra en ese estado y no realiza ninguna acción. Origen: contexto 3.11 (DEC-E46).
- CL-003. Intentar crear un producto cuyo nombre difiere solo en mayúsculas/minúsculas o espacios extra respecto a uno existente en el negocio: el sistema normaliza la comparación de nombres dentro del mismo negocio y rechaza el duplicado. Origen: contexto 3.11 (DEC-E49).

### 11. Criterios de aceptación
- AC-001. Dado que el administrador o el empleado ingresa una categoría, el nombre obligatorio, el precio obligatorio y opcionalmente descripción/imagen de un producto nuevo, cuando solicita registrarlo, entonces el sistema valida la unicidad del nombre en el negocio y lo guarda en la categoría especificada con estado activo.
- AC-002. Dado que el administrador o el empleado ingresa un nuevo precio para un producto existente, cuando presiona guardar, entonces el sistema le solicita confirmación explícita indicando el precio actual y el nuevo precio.
- AC-003. Dado que el administrador o el empleado confirma el cambio de precio de un producto, cuando el sistema procesa la acción, entonces el precio se actualiza en el catálogo y se emite mensaje de confirmación.
- AC-004. Dado un producto en estado activo, cuando el administrador o el empleado selecciona cambiar su estado a desactivado y confirma la acción, entonces el sistema actualiza su estado a desactivado, omitiéndolo de las consultas del cliente y conservándolo en el historial de pedidos anteriores.
- AC-005. Dado un usuario con rol Cliente o Domiciliario, cuando intenta realizar cualquier operación de creación, edición, cambio de estado o eliminación de categorías/productos, entonces el sistema deniega la acción y retorna error de autorización.
- AC-006. Dado un usuario perteneciente al Negocio A, cuando intenta consultar o modificar categorías o productos pertenecientes al Negocio B, entonces el sistema deniega la acción por separación estricta de información por negocio.
- AC-007. Dado un cliente del negocio consultando el catálogo por chat o Mini App, cuando visualiza los productos, entonces observa únicamente los productos pertenecientes a categorías del negocio que estén en estado activo (disponibles para pedir) o agotado (visibles como no disponibles, sin opción de compra), sin visualizar ningún producto desactivado.
- AC-008. Dado el administrador o el empleado del negocio, cuando registra una nueva categoría en su establecimiento, entonces el sistema la guarda y la deja disponible para asociarle productos.
- AC-009. Dado un producto en estado activo, cuando el administrador o el empleado lo marca como agotado y confirma, entonces el sistema cambia su estado a agotado y en las consultas de clientes pasa a mostrarse como no disponible sin permitir su selección en pedidos.
- AC-010. Dado un producto en estado desactivado, cuando el administrador o el empleado selecciona reactivarlo y confirma, entonces el sistema cambia su estado a activo o agotado según corresponda y vuelve a ser visible para los clientes del negocio.
- AC-011. Dado un personal del negocio o un cliente, cuando interactúa con el catálogo desde el chat conversacional de Telegram o desde la Telegram Mini App, entonces puede acceder a las mismas funciones de gestión o consulta del catálogo respectivamente según sus permisos.
- AC-012. Dado un producto en estado desactivado con nombre "Hamburguesa Clásica" en el Negocio A, cuando el administrador intenta registrar un nuevo producto con el nombre "Hamburguesa Clásica" en el mismo Negocio A, entonces el sistema rechaza la creación notificando que el nombre ya existe y que puede reactivarse el producto existente.

### 12. Dependencias
- SPEC-001. Registro y vinculación de usuarios y negocios (autenticación, validación de roles Administrador, Empleado y Cliente, y vinculación al negocio).
- SPEC-002. Configuración general del negocio (existencia y estado activo del negocio).

### 13. Restricciones
- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración. (Contexto 4).
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante. (Contexto 4).
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar. (Contexto 4).
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales. (Contexto 4).
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración. (Contexto 4).
- Plazo: unas 8 semanas o más. (Contexto 4, DEC-E19).
- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada. (Contexto 6).
- Colombia: artículo 15 de la Constitución (habeas data), Ley 1581 de 2012 y Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015 (autorización previa, expresa e informada; aviso de privacidad; política de tratamiento; derechos de los titulares; transmisión y transferencia de datos). Autoridad: Superintendencia de Industria y Comercio. (Contexto 6).
- Referencia internacional de buenas prácticas: principios del Reglamento General de Protección de Datos de la Unión Europea (minimización, limitación de finalidad y de plazo de conservación, transparencia). (Contexto 6).

### 14. Fuera de alcance
- No es una central de repartidores. (Contexto 5).
- No es un marketplace. (Contexto 5).
- No cobra comisión por pedido ni por entrega. (Contexto 5).
- No depende de otro aplicativo para su funcionamiento básico. (Contexto 5).
- [Estructura de almacenamiento de catálogo]: tema para arquitectura. Origen: RF-001.
- [Manejo de imágenes de productos]: tema para arquitectura. Origen: DEC-E48.

### 15. Preguntas abiertas
- OPEN-Q-001: Respondida (DEC-E45).
- OPEN-Q-002: Respondida (DEC-E46).
- OPEN-Q-003: Respondida (DEC-E47).
- OPEN-Q-004: Respondida (DEC-E48).
- OPEN-Q-005: Respondida (DEC-E49).

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-005, RF-007, RF-008, RF-009, RF-010; BR-001, BR-002, BR-004, BR-005, BR-006, BR-007, BR-008, BR-009; AC-001, AC-002, AC-003, AC-004, AC-005, AC-008, AC-009, AC-010, AC-011, AC-012; CL-001, CL-002, CL-003.
- HU-002: RF-001, RF-002, RF-003, RF-005, RF-007, RF-008, RF-009, RF-010; BR-001, BR-002, BR-004, BR-005, BR-006, BR-007, BR-008, BR-009; AC-001, AC-002, AC-003, AC-004, AC-005, AC-008, AC-009, AC-010, AC-011, AC-012; CL-001, CL-002, CL-003.
- HU-003: RF-004, RF-006, RF-009; BR-002, BR-003, BR-007; AC-006, AC-007, AC-011.
- RF-001: Origen: contexto 3.11 (DEC-E06, DEC-E27, DEC-E48), HU-10; verificado por AC-001.
- RF-002: Origen: contexto 3.7, HU-10; verificado por AC-002, AC-003.
- RF-003: Origen: contexto 3.7, 3.11 (DEC-E27, DEC-E28, DEC-E46), HU-10; verificado por AC-004, AC-009.
- RF-004: Origen: contexto 3.11 (DEC-E06, DEC-E27, DEC-E46), HU-10; verificado por AC-007.
- RF-005: Origen: contexto 3.2, 3.3, HU-10; verificado por AC-005.
- RF-006: Origen: contexto 3.3, HU-10; verificado por AC-006.
- RF-007: Origen: contexto 3.11 (DEC-E45), HU-10; verificado por AC-008.
- RF-008: Origen: contexto 3.11 (DEC-E46), HU-10; verificado por AC-010.
- RF-009: Origen: contexto 3.1, 3.11 (DEC-E47), HU-10; verificado por AC-011.
- RF-010: Origen: contexto 3.11 (DEC-E49), HU-10; verificado por AC-001, AC-012.
- RNF-001: Origen: contexto 3.2, 3.3; verificado con prueba de autorización con tokens/credenciales de diferentes roles y negocios.
- RNF-002: Origen: contexto 3.11 (DEC-E28, DEC-E46); verificado con prueba funcional de consulta de historial de pedidos tras desactivar o agotar un producto.
- BR-001: Origen: contexto 3.11 (DEC-E27, DEC-E45), HU-10; verificado por AC-005.
- BR-002: Origen: contexto 3.11 (DEC-E28, DEC-E46), HU-10; verificado por AC-004, AC-007, AC-009.
- BR-003: Origen: contexto 3.3; verificado por AC-006.
- BR-004: Origen: contexto 3.7, HU-10; verificado por AC-002, AC-004, AC-009, AC-010.
- BR-005: Origen: contexto 3.11 (DEC-E45); verificado por AC-001, AC-008.
- BR-006: Origen: contexto 3.11 (DEC-E46); verificado por AC-010.
- BR-007: Origen: contexto 3.1, 3.11 (DEC-E47); verificado por AC-011.
- BR-008: Origen: contexto 3.11 (DEC-E48); verificado por AC-001.
- BR-009: Origen: contexto 3.11 (DEC-E49); verificado por AC-012.
- CL-001: Origen: contexto 3.11 (DEC-E48); verificado por AC-002.
- CL-002: Origen: contexto 3.11 (DEC-E46); verificado por AC-009.
- CL-003: Origen: contexto 3.11 (DEC-E49); verificado por AC-012.

### 17. Historial de cambios
- Versión 0.1: creación inicial a partir de HU-10 (EPIC-002) y decisiones del contexto (DEC-E06, DEC-E27, DEC-E28).
- Versión 1.0: incorporación de las decisiones DEC-E45, DEC-E46, DEC-E47, DEC-E48 y DEC-E49 aprobadas por el equipo. Se definen las categorías del catálogo, los tres estados de producto (activo, agotado, desactivado), la reactivación, la unicidad de nombre de producto dentro del negocio, la obligatoriedad de nombre/precio con campos opcionales de descripción/imagen, y la disponibilidad en chat conversacional y Telegram Mini App. Transición a versión Candidata.
- Versión 1.1: corrección manual de la revisión cruzada de las SPEC (2026-11-21), sin modelo, aprobada por la estudiante: se reemplaza «backend» por «el sistema» (21 menciones; la validación en el servidor es una restricción de arquitectura del contexto 3.2). Sin otros cambios de contenido.

## Verificación
- Completitud: cumple. Todas las preguntas de aclaración fueron resueltas por el equipo y registradas como decisiones DEC-E45 a DEC-E49. No quedan contenidos inferidos ni vacíos pendientes.
- Consistencia interna: cumple. Se verificó que los requisitos funcionales, reglas de negocio, historias de usuario, flujos y criterios de aceptación mantienen coherencia absoluta respecto a las categorías, estados de producto (activo, agotado, desactivado), unicidad de nombres y canales de Telegram.
- Consistencia con el contexto: cumple. Toda la especificación concuerda estrictamente con la sección 3 del contexto y con las decisiones DEC-E06, DEC-E27, DEC-E28, DEC-E45, DEC-E46, DEC-E47, DEC-E48 y DEC-E49.
- No ambigüedad: cumple. Todos los comportamientos del sistema y las condiciones de error o límites están explícitamente formulados.
- Verificabilidad: cumple. Cada requisito funcional, regla de negocio y caso límite posee al menos un criterio de aceptación en formato Dado/Cuando/Entonces o un método de verificación formal.
- Cobertura de actores: cumple. Se especificaron historias de usuario y criterios de autorización diferenciados para Administrador del negocio, Empleado o vendedor y Cliente del negocio.
- Cobertura de AC: cumple. Todos los RF-001 a RF-010 y BR-001 a BR-009 están asociados a criterios de aceptación verificables.
- Trazabilidad: cumple. Cada elemento de la especificación (RF, RNF, BR, CL) está trazado en la sección 16 con su origen exacto y sus correspondientes AC.
- No invención: cumple. Se incorporaron únicamente las reglas del contexto y las decisiones ratificadas por el equipo.
- Delimitación: cumple. No se incluyeron soluciones técnicas de arquitectura ni de base de datos; los temas correspondientes se registraron adecuadamente en la sección 14.

## Siguiente paso
La SPEC-003 versión 1.0 está lista para revisión. Confirmen el objetivo y el alcance, las reglas de negocio, los criterios de aceptación críticos, las restricciones y lo que está fuera de alcance. Si la aprueban, queda congelada y lista para el Architecture Agent.
