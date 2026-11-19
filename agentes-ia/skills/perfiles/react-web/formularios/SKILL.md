---
name: formularios
description: Perfil react-web. Patrón de formularios con React Hook Form + Zod, con los mismos límites del backend y mensajes sin datos sensibles. Úsalo en B3.
---
# Formularios RHF + Zod

## Reglas

1. El esquema Zod vive junto al formulario y replica **los mismos límites del backend**: longitudes, formatos, cantidades y fechas que diga la SPEC.
2. No inventes validaciones que el backend no tenga; si el backend no las tiene, es una PREG.
3. Los mensajes de error son plantillas fijas y no exponen datos sensibles.
4. No registres el valor de los campos en consola ni analítica.
5. No guardes datos sensibles en `localStorage`.
6. El botón de envío se deshabilita mientras se envía y muestra el error del servidor.

## Ejemplo

```ts
// Los límites salen de la SPEC y del DTO del backend; estos son de ejemplo.
const esquema = z.object({
  nombre: z.string().min(1, 'Este campo es obligatorio.').max(80),
  cantidad: z.coerce.number().int().positive('Debe ser mayor que cero.'),
});

const { register, handleSubmit, formState: { errors } } = useForm({
  resolver: zodResolver(esquema),
});
```

## Verificación

- Los límites coinciden con la SPEC y con el DTO del backend.
- Los mensajes no contienen datos sensibles.
- El formulario es usable con teclado y lector de pantalla.
- El error del servidor se muestra sin volcar el cuerpo completo.
