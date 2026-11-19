# Domiciliarios Eje - Contexto para agentes de IA

Versión: 0.1
Estado: Borrador (pendiente de revisión de la estudiante)
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
- Telegram: canal real de interacción. Transporta mensajes; no decide permisos.

No existen otros roles. En particular, no hay un rol de «central de repartidores» ni de administrador de una plataforma de varios negocios con poder sobre sus pedidos (ver sección 5).

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

# 4. Restricciones del proyecto

- Proyecto individual, guiado por especificaciones (SDD): comprensión del problema, especificación funcional, especificación técnica, planificación, desarrollo guiado por especificaciones, pruebas y validación, documentación y demostración.
- Se reutilizan los agentes de IA del primer proyecto, con evidencia de su uso: agente, tarea, instrucciones o contexto, resultado y validación de la estudiante.
- La solución funciona de manera independiente. Las integraciones con otros aplicativos son complementarias, nunca condición para operar.
- Entregables: especificación funcional y criterios de aceptación; especificación técnica y arquitectura; modelo de datos y componentes; evidencias de uso de los agentes; código fuente organizado y ejecutable; plan y evidencias de pruebas funcionales; manual breve de uso y documentación técnica; demostración de los flujos principales.
- Criterios de valoración: calidad, claridad y trazabilidad de las especificaciones; correspondencia entre requisitos, implementación y criterios de aceptación; funcionamiento de los procesos principales y reglas de negocio; calidad técnica y mantenibilidad; uso crítico, documentado y verificable de los agentes; pruebas, documentación y demostración.
- Plazo: pendiente (ver sección 7).

# 5. Fuera de alcance

- No es una central de repartidores.
- No es un marketplace.
- No cobra comisión por pedido ni por entrega.
- No depende de otro aplicativo para su funcionamiento básico.

# 6. Contexto normativo

- El enunciado exige protección de datos personales y acceso únicamente a la información autorizada (3.3). No nombra una norma específica: ver sección 7.

# 7. Vacíos conocidos (pendientes por decidir)

El enunciado no los define. Cualquier agente que los necesite crea una pregunta (`OPEN-Q` en la SPEC o `docs/preguntas/PREG-xxx.md`) y no los resuelve solo.

1. Cómo se autentica cada rol en Telegram y cómo se vincula una persona a un negocio (por ejemplo, invitación del administrador).
2. Si el cliente usa el bot directamente o solo el negocio registra sus pedidos; y qué significa «cuando el negocio habilite» la consulta de estado.
3. Qué transiciones de estado están permitidas, quién puede hacer cada una y si un pedido cancelado o entregado puede cambiar.
4. Si un domiciliario puede pertenecer a varios negocios.
5. Cómo se mide la carga de trabajo y si existe un tope de pedidos simultáneos por domiciliario.
6. Qué pasa con un pedido fuera de toda zona de cobertura o fuera del horario de atención.
7. Qué formas de pago existen y si el sistema registra el cobro o solo la forma de pago.
8. Qué se considera un pedido duplicado.
9. Qué notificaciones recibe cada rol y con qué contenido.
10. Qué reportes son obligatorios para la demostración.
11. Qué datos personales del cliente se guardan, cuánto tiempo y qué norma de protección de datos aplica.
12. Fecha de entrega y plazo disponible.
