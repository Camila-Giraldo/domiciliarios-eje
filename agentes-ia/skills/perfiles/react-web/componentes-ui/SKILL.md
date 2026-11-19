---
name: componentes-ui
description: Perfil react-web. Reglas de composición de pantallas con Tailwind + shadcn/ui, estados vacíos/carga/error, accesibilidad y data-testid. Úsalo en B3.
---
# Componentes shadcn/ui

## Composición

- Una pantalla = un componente de página en `src/pantallas/`.
- Los bloques reutilizables van en `src/componentes/`.
- Usa los componentes de shadcn/ui sin reescribir su comportamiento.
- No mezcles lógica de API en componentes de presentación: pásale datos y callbacks.

## Estados obligatorios

Cada pantalla que consume la API debe tener:

- **Carga**: skeleton o spinner accesible.
- **Vacío**: mensaje claro y acción siguiente.
- **Error**: mensaje con plantilla fija y opción de reintentar.
- **Éxito**: confirmación visible.

## Accesibilidad

- Navegación por teclado.
- `label` asociado a cada campo.
- Foco visible.
- `aria-live` para mensajes de estado.
- Contraste suficiente.

## data-testid

- Usa los acuerdos del TC/Playwright: `data-testid="btn-confirmar"`, `data-testid="lista-pendientes"`.
- No cambies un `data-testid` existente sin actualizar el TC (y eso lo decide QA).
- No uses el texto visible como selector si hay un `data-testid`.

## Datos sensibles

- Muestra a cada rol solo los datos que la SPEC le autoriza.
- No guardes ni registres datos sensibles en el navegador.
- Los mensajes de error no exponen datos sensibles.
