<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-21 15:10
Petición: SPEC-003. EPIC-002. Especifica el catálogo de productos del negocio: el administrador y el empleado crean, modifican y desactivan productos con su precio (DEC-E06, DEC-E27, DEC-E28) y los clientes del negocio lo consultan. Las historias aprobadas están en el archivo adjunto: usa HU-10 como entrada. Dependencias: SPEC-001 y SPEC-002 (candidatas).
-->

# SPEC-003. Gestión y consulta del catálogo de productos del negocio - Versión 0.1

Estado: Borrador
Modo: Iteración
Necesidad original: "EPIC-002. Especifica el catálogo de productos del negocio: el administrador y el empleado crean, modifican y desactivan productos con su precio (DEC-E06, DEC-E27, DEC-E28) y los clientes del negocio lo consultan. Las historias aprobadas están en el archivo adjunto: usa HU-10 como entrada. Dependencias: SPEC-001 y SPEC-002 (candidatas)."
Épica: EPIC-002

## Análisis
- Objetivo: Permitir que el administrador y el empleado o vendedor del negocio configuren la oferta de productos de su establecimiento (creación, modificación de precio y desactivación), y que los clientes del negocio puedan consultar la lista de productos disponibles para realizar pedidos.
- Alcance inicial: Registro de productos con nombre y precio, modificación de precios previa confirmación, desactivación lógica conservando historial en pedidos anteriores, control de autorización por rol y negocio, y consulta del catálogo de productos activos para clientes del negocio.
- Actores: Administrador del negocio, Empleado o vendedor, Cliente.
- Contexto aplicable: Contexto 3.2 (Backend, autenticación y autorización), 3.3 (Separación de información por negocio), 3.7 (Confirmación antes de ejecutar operaciones importantes), 3.11 (DEC-E06, DEC-E27, DEC-E28).

## Modelo de dominio
- Producto: pertenece a Negocio; cardinalidad varios. Origen: contexto 3.11 (DEC-E06).
- Catálogo: pertenece a Negocio; cardinalidad uno. Origen: contexto 3.11 (DEC-E06).

## Contradicciones detectadas
- Ninguna.

## Análisis de impacto
- FASE=RESPUESTAS procesada: Las preguntas abiertas OPEN-Q-001 a OPEN-Q-005 no recibieron respuestas por parte del equipo (permanecen en estado pendiente). No hay decisiones DEC que actualizar en esta versión.

## Preguntas de aclaración
- OPEN-Q-001. ¿El catálogo del negocio soporta organización por categorías (por ejemplo: entradas, platos fuertes, bebidas) o es una lista plana de productos?
  Por qué importa: define el modelo de datos del catálogo, el flujo de creación y la forma en que el cliente explora los productos.
  Crítica: sí
  Propuesta del agente: Manejar una lista plana de productos por defecto en el bot de Telegram para simplificar la interacción conversacional.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-002. ¿Se requiere un estado "agotado" o "no disponible temporalmente" para los productos, o el estado desactivado (DEC-E28) es la única forma de no mostrarlos al cliente?
  Por qué importa: define los estados posibles de un producto en el catálogo y las operaciones que pueden realizar el administrador y el empleado.
  Crítica: sí
  Propuesta del agente: Manejar únicamente los estados "activo" y "desactivado" (DEC-E28). Si un producto no está disponible, se desactiva.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-003. ¿La gestión (crear, editar, desactivar) y la consulta del catálogo se realizan mediante chat conversacional con botones en Telegram o a través de una Telegram Mini App?
  Por qué importa: define los canales y la interfaz de usuario para el personal del negocio y para los clientes.
  Crítica: sí
  Propuesta del agente: Realizar la gestión por chat conversacional con botones nativos de Telegram y dejar la consulta de clientes por chat conversacional.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-004. ¿Un producto del catálogo incluye únicamente nombre y precio (DEC-E06), o puede incluir además una descripción corta y/o una imagen/foto?
  Por qué importa: determina los campos requeridos y opcionales al registrar o modificar un producto.
  Crítica: no
  Propuesta del agente: Permitir nombre y precio como obligatorios, y descripción corta e imagen como opcionales.
  Estado: Pendiente
  Responsable: equipo

- OPEN-Q-005. ¿Se permite que existan dos productos con el mismo nombre exacto dentro del mismo negocio?
  Por qué importa: establece las reglas de validación y unicidad en el registro y actualización de productos.
  Crítica: no
  Propuesta del agente: No permitir nombres duplicados de productos (activos o desactivados) dentro del mismo negocio para evitar confusiones en la administración y en los pedidos.
  Estado: Pendiente
  Responsable: equipo

## Especificación

### 1. Objetivo
Permitir a los administradores y empleados de un negocio gestionar el catálogo de productos de su establecimiento (crear, modificar precio y desactivar productos) y permitir a los clientes consultar los productos activos disponibles.

### 2. Contexto
Cada negocio mantiene su propio catálogo de productos para ofrecer sus entregas a domicilio desde Telegram. De acuerdo con las reglas de operación y autorización del producto, únicamente el personal del negocio (administrador y empleado o vendedor) tiene permisos para modificar la oferta, mientras que los clientes únicamente pueden visualizar la lista de productos activos de dicho establecimiento.

Decisiones del equipo:
- Sin decisiones registradas aún (las preguntas OPEN-Q-001 a OPEN-Q-005 están pendientes de respuesta por el equipo).

### 3. Alcance
- Registro de un nuevo producto con su nombre y precio por parte de administradores o empleados del negocio.
- Modificación del precio de un producto existente con solicitud de confirmación previa.
- Desactivación lógica de un producto para excluirlo de la oferta a clientes sin afectar los pedidos históricos.
- Consulta pública del catálogo activo para los clientes registrados o interactuando en el negocio.
- Validación estricta de autorización en el backend para evitar que roles no permitidos o usuarios de otros negocios modifiquen o consulten catálogos ajenos.

### 4. Actores e historias de usuario
Actores: Administrador del negocio, Empleado o vendedor, Cliente.

- HU-001. Como Administrador del negocio, quiero registrar, modificar precios y desactivar productos del catálogo de mi establecimiento, para mantener actualizada la oferta disponible para los clientes.
- HU-002. Como Empleado o vendedor del negocio, quiero registrar, modificar precios y desactivar productos del catálogo de mi establecimiento, para respaldar la gestión operativa de la oferta del negocio.
- HU-003. Como Cliente, quiero consultar el catálogo de productos disponibles del negocio, para seleccionar los productos que deseo pedir a domicilio.

### 5. Requisitos funcionales
- RF-001. El sistema debe permitir al administrador del negocio y al empleado o vendedor registrar un nuevo producto ingresando su nombre y precio en el catálogo de su negocio. Origen: contexto 3.11 (DEC-E06, DEC-E27), HU-10.
- RF-002. El sistema debe solicitar confirmación previa al administrador o al empleado antes de guardar la modificación del precio de un producto existente. Origen: contexto 3.7, HU-10.
- RF-003. El sistema debe permitir al administrador del negocio y al empleado o vendedor desactivar un producto activo previa confirmación. Origen: contexto 3.7, 3.11 (DEC-E27, DEC-E28), HU-10.
- RF-004. El sistema debe permitir únicamente a los clientes vinculados o interactuando con el negocio consultar los productos con estado activo del catálogo de dicho negocio. Origen: contexto 3.11 (DEC-E06, DEC-E27), HU-10.
- RF-005. El sistema debe verificar en el backend la identidad, el rol, el negocio y los permisos del usuario ante cualquier intento de creación, modificación o desactivación del catálogo, rechazando solicitudes no autorizadas. Origen: contexto 3.2, 3.3, HU-10.
- RF-006. El sistema debe impedir que un usuario de un negocio consulte o altere los productos pertenecientes al catálogo de otro negocio. Origen: contexto 3.3, HU-10.

### 6. Requisitos no funcionales
- RNF-001. Seguridad y autorización. Toda operación sobre el catálogo debe validarse exclusivamente en el backend garantizando la separación de datos por negocio. Se verifica con: prueba de autorización con tokens/credenciales de diferentes roles y negocios. Origen: contexto 3.2, 3.3.
- RNF-002. Integridad de historial. La desactivación de un producto no debe eliminar la referencia del producto ni sus datos en los pedidos previamente registrados. Se verifica con: prueba funcional de consulta de historial de pedidos tras desactivar un producto. Origen: contexto 3.11 (DEC-E28).

### 7. Reglas de negocio
- BR-001. Autorización de gestión de catálogo. Únicamente el Administrador del negocio y el Empleado o vendedor tienen permisos para registrar, editar precio o desactivar productos. Los clientes y los domiciliarios no poseen permisos de modificación. Origen: contexto 3.11 (DEC-E27), HU-10.
- BR-002. Conservación del historial de productos desactivados. Desactivar un producto modifica su estado a desactivado y lo oculta de la vista del cliente, pero conserva intactos los registros de pedidos históricos que incluyan dicho producto. Origen: contexto 3.11 (DEC-E28), HU-10.
- BR-003. Aislamiento por negocio. Los usuarios registrados o vinculados a un negocio solo pueden ver o gestionar el catálogo de ese negocio específico. Ningún usuario puede interactuar con el catálogo de un negocio ajeno. Origen: contexto 3.3.
- BR-004. Confirmación obligatoria de cambios de precio y desactivación. Toda modificación de precio o desactivación de un producto requiere confirmación explícita por parte del usuario antes de guardarse en el sistema. Origen: contexto 3.7, HU-10.

### 8. Flujo principal
1. El administrador o el empleado inicia la gestión del catálogo de su negocio en el bot de Telegram.
2. El sistema valida en el backend la identidad del usuario, su rol (Administrador o Empleado) y la vinculación con el negocio.
3. El usuario selecciona la acción a realizar: registrar producto, modificar precio o desactivar producto.
4. Si es registro: el usuario ingresa el nombre y el precio del producto.
5. Si es modificación de precio: el usuario selecciona un producto existente, ingresa el nuevo precio y el sistema solicita confirmación.
6. Si es desactivación: el usuario selecciona un producto activo y el sistema solicita confirmación.
7. El usuario confirma la operación de modificación o desactivación (si aplica).
8. El backend ejecuta la operación, actualiza el catálogo del negocio y emite un mensaje de confirmación.

### 9. Flujos alternativos y de excepción
- A1. Consulta de catálogo por parte del cliente:
  1. El cliente inicia la consulta del catálogo en el bot del negocio.
  2. El sistema valida que el cliente esté interactuando en el contexto de ese negocio.
  3. El sistema muestra la lista de productos que tienen estado activo, con sus nombres y precios.
- E1. Intento de modificación por rol no autorizado (Cliente o Domiciliario):
  1. Un cliente o domiciliario envía una instrucción para crear, modificar o desactivar un producto.
  2. El backend valida el rol y deniega la operación.
  3. El sistema responde con un mensaje indicando que no cuenta con permisos para gestionar el catálogo.
- E2. Intento de acceso al catálogo de otro negocio:
  1. Un usuario intenta acceder a la gestión o consulta del catálogo de un negocio al cual no pertenece.
  2. El backend valida la separación de información por negocio y rechaza la solicitud.
  3. El sistema informa el rechazo por falta de autorización sobre ese negocio.
- E3. Cancelación de confirmación en modificación de precio o desactivación:
  1. El usuario solicita modificar el precio o desactivar un producto.
  2. El sistema solicita confirmación previa.
  3. El usuario decide cancelar la acción.
  4. El sistema interrumpe la operación sin alterar el producto.

### 10. Casos límite
- CL-001. Intentar modificar el precio de un producto a un valor no numérico o menor a cero: el backend rechaza la operación e informa que el precio debe ser un valor numérico válido mayor o igual a cero. Origen: inferido, requiere confirmación (OPEN-Q-004).
- CL-002. Intentar desactivar un producto que ya se encuentra en estado desactivado: el sistema informa que el producto ya está desactivado y no ejecuta ningún cambio. Origen: inferido.

### 11. Criterios de aceptación
- AC-001. Dado que el administrador o el empleado del negocio ingresa un nuevo producto con su nombre y precio, cuando solicita guardar, entonces el sistema registra el producto en la lista de oferta de ese negocio con estado activo.
- AC-002. Dado que el administrador o el empleado selecciona modificar el precio de un producto, cuando ingresa el nuevo valor, entonces el sistema le solicita confirmación previa antes de hacer efectiva la actualización.
- AC-003. Dado que el administrador o el empleado confirma la actualización del precio de un producto, cuando el sistema lo procesa, entonces actualiza el precio en el catálogo del negocio y emite un mensaje de éxito.
- AC-004. Dado un producto en estado activo, cuando el administrador o el empleado selecciona desactivarlo y confirma la acción, entonces el sistema cambia el estado del producto a desactivado, dejando de mostrarlo a los clientes pero conservándolo en los pedidos anteriores.
- AC-005. Dado un usuario con rol Cliente o Domiciliario, cuando intenta crear, modificar o desactivar un producto del catálogo, entonces el sistema rechaza la solicitud en el backend e informa la falta de permisos.
- AC-006. Dado un usuario perteneciente al Negocio A, cuando intenta modificar o visualizar el catálogo del Negocio B, entonces el sistema rechaza la solicitud por aislamiento de información entre negocios.
- AC-007. Dado un cliente del negocio, cuando solicita consultar el catálogo, entonces el sistema le muestra únicamente los productos del negocio que tienen estado activo con su nombre y precio.

### 12. Dependencias
- SPEC-001. Registro y vinculación de usuarios y negocios (para la autenticación, roles de Administrador, Empleado y Cliente, y vinculación al negocio).
- SPEC-002. Configuración general del negocio (para verificar que el negocio exista y esté activo).

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
- [Manejo de imágenes de productos]: tema para arquitectura. Origen: OPEN-Q-004.

### 15. Preguntas abiertas
- OPEN-Q-001: Pendiente.
- OPEN-Q-002: Pendiente.
- OPEN-Q-003: Pendiente.
- OPEN-Q-004: Pendiente.
- OPEN-Q-005: Pendiente.

### 16. Trazabilidad
- HU-001: RF-001, RF-002, RF-003, RF-005; BR-001, BR-002, BR-004; AC-001, AC-002, AC-003, AC-004; CL-001, CL-002.
- HU-002: RF-001, RF-002, RF-003, RF-005; BR-001, BR-002, BR-004; AC-001, AC-002, AC-003, AC-004; CL-001, CL-002.
- HU-003: RF-004, RF-006; BR-003; AC-007.
- RF-001: Origen: contexto 3.11 (DEC-E06, DEC-E27), HU-10; verificado por AC-001.
- RF-002: Origen: contexto 3.7, HU-10; verificado por AC-002, AC-003.
- RF-003: Origen: contexto 3.7, 3.11 (DEC-E27, DEC-E28), HU-10; verificado por AC-004.
- RF-004: Origen: contexto 3.11 (DEC-E06, DEC-E27), HU-10; verificado por AC-007.
- RF-005: Origen: contexto 3.2, 3.3, HU-10; verificado por AC-005.
- RF-006: Origen: contexto 3.3, HU-10; verificado por AC-006.
- RNF-001: Origen: contexto 3.2, 3.3; verificado con prueba de autorización con tokens/credenciales de diferentes roles y negocios.
- RNF-002: Origen: contexto 3.11 (DEC-E28); verificado con prueba funcional de consulta de historial de pedidos tras desactivar un producto.
- BR-001: Origen: contexto 3.11 (DEC-E27), HU-10; verificado por AC-005.
- BR-002: Origen: contexto 3.11 (DEC-E28), HU-10; verificado por AC-004.
- BR-003: Origen: contexto 3.3; verificado por AC-006.
- BR-004: Origen: contexto 3.7, HU-10; verificado por AC-002, AC-004.
- CL-001: Origen: inferido, requiere confirmación (OPEN-Q-004); verificado por AC-002.
- CL-002: Origen: inferido; verificado por AC-004.

### 17. Historial de cambios
- Versión 0.1: creación inicial a partir de HU-10 (EPIC-002) y decisiones del contexto (DEC-E06, DEC-E27, DEC-E28).

## Verificación
- Completitud: cumple. Se han especificado todas las secciones requeridas conforme al estándar.
- Consistencia interna: cumple. Se compararon los requisitos funcionales, reglas de negocio, flujos y criterios de aceptación, asegurando total coherencia sobre la gestión y consulta del catálogo.
- Consistencia con el contexto: cumple. Se constató la alineación con la sección 3 del contexto, respetando DEC-E06, DEC-E27 y DEC-E28.
- No ambigüedad: cumple. Los términos y comportamientos del sistema están definidos claramente.
- Verificabilidad: cumple. Todos los RF y BR cuentan con criterios de aceptación o métodos de verificación formal en formato Dado/Cuando/Entonces.
- Cobertura de actores: cumple. Se contemplan los tres actores relevantes (Administrador del negocio, Empleado o vendedor, Cliente) asignando a cada uno una historia de usuario explícita.
- Cobertura de AC: cumple. Todos los RF y BR son verificados por al menos un criterio de aceptación.
- Trazabilidad: cumple. Cada RF, RNF, BR y CL aparece en la sección 16 con su origen y su correspondiente criterio o método de verificación.
- No invención: cumple. Se respetaron las decisiones confirmadas del proyecto. Lo que no está decidido se mantiene como OPEN-Q.
- Delimitación: cumple. No se incluyeron decisiones de diseño técnico ni arquitectura.

## Siguiente paso
Respondan las preguntas abiertas (OPEN-Q-001 a OPEN-Q-005) y ejecuten de nuevo el agente con --continuar SPEC-003.
