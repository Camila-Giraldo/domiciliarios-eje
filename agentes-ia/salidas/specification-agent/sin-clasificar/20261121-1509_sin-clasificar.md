<!--
Agente: Specification Agent
Proveedor: gemini
Modelo: gemini-3.5-flash
Fecha: 2026-11-21 15:09
Petición: SPEC-004. EPIC-002. Especifica el pedido del cliente de principio a fin hasta antes del despacho: ingreso por el acceso de clientes del negocio con aviso de privacidad y contacto compartido (DEC-E05, DEC-E20, DEC-E29, DEC-E36, DEC-E37, DEC-E42); armado del pedido con productos del catálogo, barrio de la lista y dirección, forma de pago y total con tarifa (DEC-E06 a DEC-E08); rechazo por barrio sin cobertura o negocio cerrado (DEC-E09, DEC-E41); aviso de posible duplicado (DEC-E10); negocio vencido no recibe pedidos (DEC-E26); confirmación (pasa a en preparación) o rechazo por el negocio con aviso al cliente (DEC-E17, DEC-E21, DEC-E22, DEC-E25); cancelación por el cliente o el negocio antes de en camino (DEC-E13). Las historias aprobadas están en el archivo adjunto: usa HU-11 a HU-18 como entrada. Dependencias: SPEC-001, SPEC-002 y SPEC-003 (candidatas). Si es demasiado para una sola SPEC, propón la división.
-->

# Propuesta de división

La necesidad abarca dos funcionalidades distintas con objetivos, actores principales y responsabilidades independientes:

1. **Gestión del catálogo de productos del negocio (HU-10)**
   - **Objetivo:** Permitir al administrador y al empleado del negocio crear, modificar precios y desactivar productos de la oferta del establecimiento (DEC-E27, DEC-E28).
   - **Actores:** Administrador del negocio, Empleado o vendedor.
   - **Alcance:** Administración del catálogo (precondición para la toma de pedidos).

2. **Registro de clientes, toma y gestión inicial del pedido antes del despacho (HU-11 a HU-18)**
   - **Objetivo:** Permitir el ingreso e identificación del cliente con tratamiento de datos (HU-11), el armado y envío del pedido con validación de cobertura, horario, duplicados y suscripción (HU-12, HU-13, HU-14, HU-15), la confirmación o rechazo por el negocio (HU-16) y la cancelación previa a estar «en camino» por parte del cliente o del negocio (HU-17, HU-18).
   - **Actores:** Cliente, Administrador del negocio, Empleado o vendedor.
   - **Alcance:** Flujo conversacional de pedido del cliente y ciclo de vida inicial del pedido hasta pasar a preparación o cancelado/rechazado.

---

### Pregunta de aclaración para continuar

¿Cuál de las dos funcionalidades desean especificar primero en la SPEC-004?
- **Opción A:** Especificar primero la **Gestión del catálogo de productos** (HU-10).
- **Opción B:** Especificar primero el **Registro, toma y gestión inicial de pedidos del cliente** (HU-11 a HU-18), asumiendo un catálogo existente.
