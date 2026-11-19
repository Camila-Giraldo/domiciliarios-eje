---
name: cliente-api-tipado
description: Perfil react-web. Reglas para generar un cliente tipado de la API en la carpeta de la interfaz y usarlo en todas las pantallas. Úsalo en B3 para evitar fetch suelto y mantener el contrato con el backend.
---
# Cliente API tipado

## Estructura

```text
apps/web/src/api/
├─ cliente.ts       instancia base (baseURL, cookies, errores)
├─ tipos.ts         tipos de DTO / OpenAPI
├─ <modulo>.ts      funciones de cada módulo de proyecto.json
└─ indice.ts        exporta todo
```

## Reglas

1. Todas las llamadas pasan por `src/api/`. **Nada de `fetch` suelto en pantallas o componentes.**
2. Los tipos salen del contrato de la API (OpenAPI o DTO). No los inventes.
3. Las cookies httpOnly las pone el backend: `credentials: 'include'` cuando aplique, sin manipularlas.
4. Errores tipados: `{ codigo, mensaje }`; la UI decide cómo mostrarlos con plantillas fijas.
5. No registres cuerpos de respuesta con datos sensibles en consola ni analítica.
6. No guardes datos sensibles en `localStorage`.
7. Un cambio de contrato se refleja primero en `tipos.ts`; si el backend no lo tiene, es una PREG.

## Ejemplo

```ts
export async function crearRecurso(entrada: EntradaRecurso): Promise<Recurso> {
  const r = await cliente.post('/recursos', entrada);
  return r.data as Recurso;
}
```

## Verificación

- `grep -R "fetch(" apps/web/src` no devuelve llamadas fuera de `src/api/`.
- Los tipos compilan.
- Ningún `console.log` imprime datos sensibles.
