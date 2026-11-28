# Domiciliarios Eje: preguntas para el profesor

Reunión: martes 24 de noviembre de 2026
Estudiante: Camila Giraldo
Aplicativo 1, Ingeniería de Software III

**Estado actual:** 5 épicas con 37 historias de usuario, 7 SPEC aprobadas, arquitectura en borrador avanzado (ARQ-001 Candidata, con correcciones pendientes) y construcción sin empezar. Nada de lo que se pregunta aquí está cambiado todavía.

## Si solo hay cinco minutos

1. ¿El negocio también debe registrar pedidos que le llegan por teléfono u otros canales? (pregunta 1)
2. ¿Cómo declaro el asistente de IA que usé además de mis agentes? (pregunta 6)
3. ¿Espera una ruta dibujada, o basta con destino, navegación externa y seguimiento en vivo? (pregunta 7)
4. ¿El catálogo y el pedido en Mini App se salen del Aplicativo 1? (pregunta 10)
5. ¿Cuál es la fecha de entrega y qué es lo mínimo que debe funcionar ese día? (pregunta 13)

---

## A. Diferencias entre el enunciado y mis SPEC

**1. Pedidos registrados por el negocio.**
El enunciado parte de negocios que reciben pedidos por varios canales y le da al empleado la tarea de registrarlos. En mis SPEC solo el cliente crea pedidos, desde Telegram.

- [ ] Deben existir los dos caminos
- [ ] Solo los registra el negocio
- [ ] Basta con que pida el cliente

Si los registra el negocio: ¿qué pasa con un cliente sin Telegram (confirmación, seguimiento, autorización de datos)?

Respuesta:

**2. Consulta del estado por el cliente.**
El enunciado dice que el negocio puede habilitarla. En mis SPEC el seguimiento está siempre activo y no hay una consulta de estado aparte de los avisos y el mapa.

- [ ] Debe poder activarse o desactivarse por negocio
- [ ] Puede quedar siempre activa

Respuesta:

**3. Estados del pedido.**
El enunciado lista «asignado» como estado y habla de actualizar la recogida. Yo dejé «asignado» como dato del pedido (se asigna durante la preparación), no tengo un paso de recogida y agregué «rechazado» y «con novedad».

- [ ] Se acepta así
- [ ] «Asignado» debe ser un estado
- [ ] Falta un paso «recogido»

Respuesta:

**4. Administración del personal.**
Hoy el administrador aprueba empleados y domiciliarios, pero ninguna SPEC le permite retirarlos. ¿Qué gestión de usuarios y permisos espera como mínimo?

Respuesta:

**5. Rol «dueño de la plataforma».**
Lo agregué para aprobar negocios, marcar la mensualidad al día o vencida y cargar festivos. No ve los pedidos. ¿Es válido o amplía demasiado el alcance?

Respuesta:

## B. Uso y evidencia de los agentes de IA

**6. Asistente adicional.**
Los agentes del primer proyecto generaron las historias, las SPEC y la arquitectura, con modelos de Gemini. Además usé Claude Code para:

- generalizar esos agentes en un kit reutilizable;
- ejecutarlos y cruzar sus resultados;
- proponerme preguntas y opciones, que yo respondí;
- aplicar correcciones sobre historias y SPEC, y redactar la HU-37;
- redactar el borrador de los avisos de privacidad y los textos de validación, que yo aprobé.

¿Se acepta? ¿Cómo debo declararlo en las evidencias? ¿La validación debe estar redactada por mí?

Respuesta:

## C. Mapa, ruta y ubicación

Idea actual, sin confirmar: el domiciliario no sale sin compartir su ubicación en tiempo real de Telegram, y administrador, empleado y cliente lo ven avanzar hacia la entrega. Solo el administrador consulta recorridos pasados.

**7. Ruta hasta la entrega.**

- [ ] Enlace a Google Maps para navegar, más destino y avance en vivo en la Mini App
- [ ] Ruta dibujada dentro de la Mini App (requiere un servicio de rutas)
- [ ] Basta con el avance en vivo, sin ruta

¿Abrir una aplicación externa contradice que Telegram sea la interfaz principal?

Respuesta:

**8. Punto de entrega.**
Una dirección escrita no siempre se ubica bien en OpenStreetMap. ¿Puedo exigir al cliente un pin de Telegram además de la dirección?

Respuesta:

**9. Privacidad con varios pedidos.**
Si un domiciliario lleva varios, un cliente podría ver el camino a la casa de otro. Propongo un solo pedido «en camino» a la vez. ¿Le parece suficiente?

Respuesta:

## D. Alcance

**10. Catálogo y pedido.**
Incluí catálogo con categorías, precios, agotados e imágenes, disponible en el chat y en la Mini App.

- [ ] Se acepta completo
- [ ] Reducirlo (solo chat, o sin categorías ni imágenes)
- [ ] Quitarlo y usar una descripción del pedido, porque se cruza con Mi Tienda Express

Respuesta:

**11. Protección de datos (Ley 1581 de 2012).**
Tengo especificada la autorización de cada actor y un borrador de avisos, pero no la revocación ni la supresión. ¿Qué espera implementado y qué puede quedar solo documentado?

Respuesta:

**12. Infraestructura.**
Propongo NestJS, PostgreSQL (puede alojarse en Supabase), pg-boss para tareas programadas, bot con grammY y Mini App en React con OpenStreetMap. ¿Hay restricciones? ¿La demostración exige despliegue público o sirve local con un túnel HTTPS?

Respuesta:

**13. Entrega y MVP.**
Supuse unas 8 semanas. ¿Cuál es la fecha exacta, qué flujos debe mostrar la demostración y qué puede quedar especificado sin construir?

Respuesta:

---

## Notas de la reunión

Decisiones que cambian:

Cosas que se quitan:

Cosas que se agregan:

Próxima revisión:

---

## Anexo personal: pendientes que no dependen del profesor

No hace falta preguntarlos. Se corrigen después de la reunión, junto con lo que cambie.

- **SPEC:** faltan las observaciones del pedido, los datos de contacto del negocio y la revocación de la autorización (DEC-E36).
- **Historias:** HU-10 y HU-12 no reflejan las decisiones posteriores del catálogo y del pedido (DEC-E45 a DEC-E53).
- **ARQ-001:** corregir el tope bajo concurrencia, los permisos con initData, el canal en vivo del mapa, el modelo de datos, la detección de señal perdida y la trazabilidad, con las 7 SPEC adjuntas.
- **Evidencias:** declarar el asistente adicional. La validación que dice «Lo corregí a mano» (EPIC-001) no es exacta: la corrección la aplicó el asistente con mis decisiones. Los encabezados «Correcciones de la estudiante» de las historias tienen el mismo problema. El historial de las SPEC-002 a 007 dice «aprobada por la estudiante» en una nota escrita antes de la aprobación.
- **Ubicación:** probar con un bot mínimo y un celular real, decidir los minutos sin señal y avisar en el consentimiento que el mensaje queda también en el chat de Telegram.
- **Conservación de datos:** decidir el plazo al terminar la relación con el negocio (único vacío que sigue abierto en el contexto).
- **Repositorio:** casi todo el trabajo desde el 19 de noviembre está sin commit (historias, SPEC, ARQ, evidencias y avisos).
