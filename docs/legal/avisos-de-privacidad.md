# Avisos de privacidad y consentimientos — Domiciliarios Eje

Versión: 0.1 (borrador)
Fecha: 2026-11-19
Estado: Borrador para revisión. No es asesoría jurídica. Antes de tratar datos reales, una persona con formación jurídica debe revisarlo y completar los campos entre corchetes.
Decisiones: DEC-E36, DEC-E37, DEC-E38, DEC-E39, DEC-E15 (contexto 3.11).

## 1. Marco normativo

Colombia (aplica):
- Constitución Política, artículo 15: derecho de habeas data.
- Ley 1581 de 2012 (protección de datos personales): principios, autorización previa, expresa e informada (art. 9), deber de informar al titular (art. 12), derechos de los titulares (art. 8), datos sensibles (art. 5) y de niños, niñas y adolescentes (art. 7), transferencias internacionales (art. 26).
- Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015: aviso de privacidad, política de tratamiento de la información, prueba de la autorización, transmisión de datos a un Encargado mediante contrato.
- Autoridad de control: Superintendencia de Industria y Comercio (SIC). Registro Nacional de Bases de Datos cuando corresponda según la normativa vigente: [verificar si aplica al Responsable].

Referencia internacional (buenas prácticas; no se asume que aplique jurídicamente):
- Principios del Reglamento General de Protección de Datos de la Unión Europea: licitud y transparencia, limitación de la finalidad, minimización, exactitud, limitación del plazo de conservación, integridad y confidencialidad, responsabilidad proactiva.

Precisión de términos: en la Ley 1581 «dato sensible» es una categoría específica (salud, biometría, origen racial o étnico, entre otros). Nombre, teléfono, dirección y ubicación son datos personales; no son sensibles en sentido legal, pero exigen autorización previa, expresa e informada y medidas de seguridad. En el proyecto, «datos sensibles» (proyecto.json) se usa en sentido amplio: datos que no deben exponerse.

## 2. Reglas para todos los consentimientos

1. Se muestran antes de pedir cualquier dato, con dos botones: «Acepto» y «No acepto». Sin aceptar no se recogen datos y no se continúa.
2. El texto corto va en el chat; el texto completo (política de tratamiento) se abre desde un enlace o la Mini App.
3. Se registra: identificador del titular, tipo de consentimiento, versión del texto, fecha y hora, y negocio (si aplica). Ese registro es la prueba de la autorización.
4. El titular puede consultar, actualizar, rectificar, revocar la autorización y pedir la supresión desde el bot (comando `/privacidad`) o por el canal del Responsable.
5. Si cambia la finalidad o el texto, se pide una nueva aceptación.
6. El servicio es solo para mayores de 18 años (DEC-E81). Cada texto incluye «Declaro que soy mayor de 18 años» y, si no se acepta, no se continúa.
7. Los datos se alojan en [proveedor y país del hosting]. Si el servidor está fuera de Colombia, se informa como transferencia o transmisión internacional (art. 26, Ley 1581). Telegram trata los mensajes según su propia política; el aviso lo menciona.

## 3. Textos

### 3.1. Persona que registra un negocio (y administrador)

Responsable: la plataforma Domiciliarios Eje (DEC-E37).

> **Tratamiento de tus datos personales**
> [Razón social de la plataforma], NIT [número], con domicilio en [ciudad] y correo [correo de privacidad], es responsable de tus datos.
> **Qué datos:** identificador y nombre de tu cuenta de Telegram, teléfono que compartas con el botón de Telegram, y los datos de tu negocio (nombre comercial, ciudad, dirección, correo de atención de datos).
> **Para qué:** crear y administrar la cuenta de tu negocio, verificar tu identidad, aprobar tu solicitud, enviarte avisos del servicio y gestionar la suscripción. No los usamos para publicidad ni los vendemos.
> **Tus derechos:** conocer, actualizar y rectificar tus datos; pedir prueba de esta autorización; saber cómo se usan; revocar la autorización o pedir su supresión cuando no exista un deber legal o contractual de conservarlos; y presentar quejas ante la Superintendencia de Industria y Comercio. Escríbenos a [correo] o usa /privacidad.
> **Cuánto tiempo:** mientras tu negocio esté en la plataforma y [plazo posterior por definir].
> Tus datos se guardan en servidores de [proveedor] en [país].
> Política completa: [enlace].
> [Acepto] [No acepto]

Además, al registrar el negocio (DEC-E39):

> **Términos del servicio y acuerdo de transmisión de datos**
> Al registrar tu negocio aceptas los términos del servicio [enlace]. Tu negocio será responsable de los datos personales de sus clientes y Domiciliarios Eje los tratará por cuenta de tu negocio, solo para gestionar sus pedidos, con las medidas de seguridad descritas en el acuerdo de transmisión [enlace], conforme al Decreto 1377 de 2013. Debes indicar un correo de atención para que tus clientes ejerzan sus derechos.
> [Acepto] [No acepto]

### 3.2. Empleado o vendedor

Responsable: la plataforma (DEC-E37).

> **Tratamiento de tus datos personales**
> [Razón social de la plataforma] es responsable de tus datos. **Qué datos:** identificador y nombre de tu cuenta de Telegram, tu teléfono, el negocio al que te vinculas y las acciones que registras (confirmaciones, cambios de estado). **Para qué:** vincularte al negocio, controlar tus permisos y dejar trazabilidad de la operación. **Tus derechos:** los de la Ley 1581 de 2012 (ver arriba), por [correo] o /privacidad. **Cuánto tiempo:** mientras estés vinculado y [plazo posterior por definir]. El administrador del negocio verá tu nombre y tu rol.
> [Acepto] [No acepto]

### 3.3. Domiciliario — tratamiento general

Responsable: la plataforma (DEC-E37).

> **Tratamiento de tus datos personales**
> [Razón social de la plataforma] es responsable de tus datos. **Qué datos:** identificador y nombre de tu cuenta de Telegram, tu teléfono, el negocio al que te vinculas, tu disponibilidad y los pedidos que aceptas y entregas. **Para qué:** vincularte al negocio, asignarte pedidos y dejar trazabilidad de las entregas. **Tus derechos:** los de la Ley 1581 de 2012, por [correo] o /privacidad. **Cuánto tiempo:** mientras estés vinculado y [plazo posterior por definir].
> [Acepto] [No acepto]

### 3.4. Domiciliario — ubicación en tiempo real y recorrido (consentimiento aparte, DEC-E38)

> **Uso de tu ubicación**
> Para pasar un pedido a «en camino» debes compartir tu ubicación en tiempo real de Telegram.
> **Cuándo:** solo desde que pasas un pedido a «en camino» hasta que lo entregas o registras una novedad. Fuera de eso no usamos tu ubicación.
> **Quién la ve:** el administrador y los empleados de tu negocio, y el cliente de ese pedido mientras está en camino.
> **Qué guardamos:** el recorrido de cada pedido, durante 30 días; luego se borra (DEC-E15).
> **Para qué:** seguir la entrega y atender reclamos sobre ella. No la usamos para otra finalidad.
> Puedes revocar este permiso por /privacidad; sin él no podrás llevar pedidos como domiciliario.
> [Acepto] [No acepto]

### 3.5. Cliente (por cada negocio, DEC-E29)

Responsable: el negocio. Encargada: la plataforma (DEC-E37).

> **Tratamiento de tus datos personales**
> [Nombre comercial del negocio] es responsable de tus datos; Domiciliarios Eje los trata por su cuenta para gestionar tus pedidos. **Qué datos:** identificador y nombre de tu cuenta de Telegram, tu teléfono, tus direcciones de entrega con su barrio y referencias, y tus pedidos. **Para qué:** recibir, preparar y entregar tus pedidos, avisarte su estado y atender reclamos. El domiciliario que lleve tu pedido verá tu nombre, dirección y teléfono solo mientras el pedido esté activo (DEC-E32). **Tus derechos:** conocer, actualizar, rectificar, revocar la autorización, pedir la supresión y presentar quejas ante la Superintendencia de Industria y Comercio, escribiendo a [correo de atención del negocio] o con /privacidad. **Cuánto tiempo:** [plazo por definir]. Tus datos se guardan en servidores de [proveedor] en [país].
> [Acepto] [No acepto]

## 4. Pendientes antes de usar con datos reales

1. Razón social, NIT, domicilio y correo de privacidad de la plataforma.
2. Proveedor y país del hosting (lo decide la arquitectura).
3. Plazos de conservación después de terminar la relación (vacío 5 del contexto).
4. Política de tratamiento de la información completa (documento aparte exigido por el Decreto 1377 de 2013) y términos del servicio.
5. ~~Si el servicio se limita a mayores de edad.~~ Resuelto: solo mayores de 18 (DEC-E81).
6. Revisión jurídica de este borrador.

## 5. Verificación contra la norma (2026-11-27)

Contrastado con los textos de la Ley 1581 de 2012 y el Decreto 1377 de 2013 (resumen en el contexto, sección 6) y con DEC-E66 a DEC-E80. Los textos de la sección 3 aún no se han cambiado.

Cumple:
- Botones «Acepto» y «No acepto», sin datos antes de aceptar (conducta inequívoca; el silencio no cuenta, Decreto art. 7).
- Registro con versión, fecha y hora como prueba (Ley art. 9; Decreto art. 8) y nueva aceptación si cambia la finalidad (Decreto art. 5).
- Qué datos y para qué en cada texto (Decreto art. 5) y la lista de derechos (Ley art. 8).
- La ubicación no es dato sensible (Ley art. 5); el texto de la sección 1 es correcto.

Falta:
1. Teléfono y dirección del Responsable en todos los textos; hoy solo el 3.1 tiene domicilio y correo (Ley art. 12 d). Para el 3.5 el negocio debe dar teléfono y dirección, no solo el correo de DEC-E39.
2. Cómo consultar la política de tratamiento en 3.2 a 3.5 (Decreto art. 15). Con DEC-E77, «Leer autorización» abre el texto completo antes de aceptar.
3. La política de tratamiento completa (Decreto art. 13): incluye el área que atiende peticiones, el procedimiento, la fecha de vigencia y el período de vigencia de la base de datos.
4. En /privacidad: ver las autorizaciones aceptadas (copia, Ley art. 12 parágrafo), consultar los propios datos gratis (Decreto art. 21) y presentar reclamos de corrección, supresión o revocación con sus plazos: 10 + 5 días hábiles para consultas, 15 + 8 para reclamos, y la marca «reclamo en trámite» en 2 días hábiles (Ley art. 14 y 15). Ninguna SPEC lo especifica todavía.
5. Cuánto tiempo: la norma no fija días; exige un plazo razonable según la finalidad y los aspectos contables o fiscales (Decreto art. 11). Sigue siendo el vacío 1 del contexto.
6. Proveedores fuera de Colombia (Vercel, base de datos gratuita, Mapbox, Telegram): con contrato de Encargado no hay que informarlo (Decreto art. 24 y 25), pero se recomienda decirlo. Mapbox recibe la posición del domiciliario y el pin del cliente para dibujar la ruta (DEC-E73, DEC-E74).
7. 3.4: decir que la ubicación también se muestra en el chat de Telegram de administrador, empleado y cliente, y que esos mensajes quedan en sus chats (DEC-E73).
8. Pedido registrado por el negocio (DEC-E67): la autorización oral es válida (Decreto art. 7), pero el negocio debe poder probarla (Decreto art. 8). La marca del empleado registra quién, cuándo y qué versión leyó, y el negocio sigue respondiendo por esa prueba. Falta un texto corto para leer por teléfono.
9. Menores de edad: resuelto con DEC-E81 (solo mayores de 18, con declaración en cada autorización). Falta agregar la frase a los textos de la sección 3.
10. Registro Nacional de Bases de Datos: depende del Decreto 886 de 2014, no revisado.
