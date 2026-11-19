---
name: plantilla-humo
description: Perfil react-web. Estructura de un recorrido de humo con Playwright, con datos sintéticos, selectores data-testid y evidencia. Úsalo en R1 y en las pruebas E2E de S3.
---
# Plantilla Playwright — humo

## Estructura

```text
<rutas.e2e de proyecto.json>/
├─ humo-<camino>.spec.ts      un archivo por camino feliz del MVP
└─ fixtures/
   └─ datos-sinteticos.ts     datos ficticios y lista de valores sensibles sintéticos
```

## Recorrido mínimo (forma; los pasos salen del MVP)

```ts
test('humo: <rol> completa <flujo principal>', async ({ page }) => {
  await page.goto(process.env.URL_PRUEBA!);
  await page.getByTestId('btn-ingresar').click();

  await page.getByTestId('campo-<dato>').fill(DATOS.<dato>);
  await page.getByTestId('btn-confirmar').click();

  await expect(page.getByTestId('estado-<entidad>')).toHaveText('<estado esperado del TC>');
  await page.screenshot({ path: `qa/humo/evidencia/${Date.now()}-<camino>.png` });
});
```

## Reglas

1. Solo datos sintéticos del entorno de prueba.
2. Selectores por `data-testid` acordados en el TC; no por texto visible.
3. No accedas a la base de datos de producción.
4. Si un paso falla, captura pantalla y log, y continúa con el siguiente camino.
5. Verifica que una operación irreversible no se pueda repetir.
6. Verifica que ningún texto visible ni log contenga los valores sensibles sintéticos.
7. Verifica que un rol no autorizado no ve ni opera datos ajenos.
8. No modifiques las pruebas para que pasen: si el selector no existe, es un defecto o una PREG.

## Evidencia

- Captura por camino.
- Log o respuesta HTTP cuando falle.
- Enmascara datos personales antes de guardar la evidencia.
