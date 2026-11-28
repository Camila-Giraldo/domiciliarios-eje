# Runtime de agentes (agentes-ia)

Runtime propio del kit SDD. Cada agente es una instrucción de sistema (`prompt.md`) más una configuración (`config.json`) que ejecutan dos scripts:

- `agente.py`: agentes de una sola llamada (Especificaciones, Arquitectura, historias de usuario). Guarda cada documento por estado y versión.
- `herramientas.py`: agentes con herramientas (S1–S3, B1–B4, R1–R2). Leen y escriben archivos del repositorio y ejecutan pruebas, cada uno con una política fija de rutas, comandos y tope de pasos.

Los dos usan cualquier proveedor compatible con la API de OpenAI (Gemini, Mistral, Groq u OpenRouter) con tu API key. No dependen de ningún asistente ni CLI externo.

Todo lo que cambia entre proyectos sale de `proyecto.json` (raíz del proyecto) y del archivo de contexto. `proyecto.py` los carga y reemplaza los marcadores de los prompts.

## Estructura

```text
agentes-ia/
├── agente.py          agentes de una llamada: preguntas, versiones, aprobación sin modelo
├── herramientas.py    bucle de herramientas de QA y construcción, con políticas por paso
├── proyecto.py        carga proyecto.json, reemplaza marcadores, busca skills, registra evidencias
├── requirements.txt
├── .env.example       copia como .env con tu API key (nunca se sube a git)
├── agentes/           un agente por carpeta: prompt.md + config.json (_plantilla para crear nuevos)
├── skills/
│   ├── nucleo/        procedimientos que sirven en cualquier proyecto
│   └── perfiles/      procedimientos de un stack: nestjs-prisma, telegram-grammy, react-web
└── salidas/           lo que producen los agentes (se crea al ejecutar)
```

## Configuración (una vez)

1. Crea una API key gratuita, por ejemplo en <https://aistudio.google.com/app/apikey> (Gemini). Los planes gratuitos pueden usar lo que envías: usa solo datos ficticios.
2. Copia `.env.example` como `.env` y pon tu llave: `GEMINI_API_KEY=...`.
3. Instala dependencias: `pip install -r agentes-ia/requirements.txt` (mejor dentro de un entorno virtual).
4. Verifica: `python agentes-ia/proyecto.py --validar` y `python agentes-ia/agente.py --listar`.

## Agentes

| Agente | Paso | Tipo | Qué entrega |
|---|---|---|---|
| `generador-hu-invest` | HU | una llamada | Historias de usuario autoevaluadas con INVEST |
| `user-story-reviewer` | RHU | una llamada | Historias corregidas y resumen de cambios |
| `specification-agent` | SPEC | una llamada, interactivo | SPEC de 17 secciones; modo «priorizar MVP» |
| `architecture-agent` | ARQ | una llamada, interactivo | ARQ con drivers, alternativas, matriz, ADR; modo «cortar MVP» |
| `qa-s1-revisor-spec` | S1 | herramientas | Informe de revisión con veredicto |
| `qa-s2-disenador-casos` | S2 | herramientas | Casos TC-*, trazabilidad y oráculos pendientes |
| `qa-s3-generador-pruebas` | S3 | herramientas | Pruebas rojas |
| `backend-servicios-api` | B1 | herramientas | Módulo de backend en verde |
| `backend-bot-telegram` | B2 | herramientas | Canal conversacional (cualquier bot de mensajería) |
| `frontend-interfaz-web` | B3 | herramientas | Interfaz gráfica (web, PWA o Mini App) |
| `ejecutor-corrector` | B4 | herramientas | Correcciones de producción y RUN |
| `qa-r1-humo` | R1 | herramientas | Reporte de humo |
| `qa-r2-triage` | R2 | herramientas | Informe de incidente |

Los nombres de carpeta se conservan del primer proyecto para que la evidencia de reutilización sea directa; los roles son genéricos.

## Uso

Especificaciones y Arquitectura (preguntas una a una en la terminal, resumen y aprobación `[S/n]`):

```text
python agentes-ia/agente.py specification-agent "Necesidad de una funcionalidad"
python agentes-ia/agente.py specification-agent "Respuestas o correcciones" --continuar SPEC-001
python agentes-ia/agente.py specification-agent "El equipo aprueba la SPEC-001" --continuar SPEC-001
python agentes-ia/agente.py architecture-agent "Propón la arquitectura" --aprobada SPEC-001 SPEC-002
python agentes-ia/agente.py specification-agent "priorizar MVP" --aprobada SPEC-001 --adjuntar docs/mvp.md
python agentes-ia/agente.py architecture-agent "cortar MVP" --adjuntar docs/mvp.md docs/arquitectura/propuesta-tecnologica.md
```

- «El equipo aprueba la X» no usa el modelo: congela la última Candidata tal cual. Se niega si quedan preguntas pendientes.
- Una respuesta cortada se guarda como `_INCOMPLETA` y nunca se reutiliza; una versión aprobada nunca se duplica.
- `--epica EPIC-001` adjunta todas las SPEC aprobadas de una épica.

Agentes con herramientas (normalmente los lanza el runner, `qa/scripts/runner.py`):

```text
python agentes-ia/herramientas.py --paso S1 --modulo pedidos
python agentes-ia/agente.py qa-s2-disenador-casos "Diseña los casos" --modulo pedidos
```

## Marcadores de los prompts

`{{NOMBRE_PROYECTO}}`, `{{IDIOMA}}`, `{{CONTEXTO_PROYECTO}}`, `{{ARCHIVO_CONTEXTO}}`, `{{STACK}}`, `{{DOCUMENTO_STACK}}`, `{{CANALES}}`, `{{RUTAS}}`, `{{COMANDOS}}`, `{{MODULOS}}`, `{{DATOS_SENSIBLES}}`, `{{REGLAS_CRITICAS}}`, `{{EVIDENCIAS}}`, `{{CARPETA_SPECS}}`, `{{CARPETA_ARQ}}` y `{{SKILLS}}`. Si un prompt trae un marcador desconocido, el script se detiene en lugar de enviar un prompt roto.

## Skills

Cada agente pide sus skills en `config.json` (`"skills": [...]`) y el runtime los inserta en el prompt. Se buscan en este orden:

1. `skills-proyecto/<skill>/SKILL.md` del proyecto (dominio propio; tiene prioridad).
2. `skills/perfiles/<perfil>/<skill>/SKILL.md` de los perfiles activos en `proyecto.json`.
3. `skills/nucleo/<skill>/SKILL.md`.

Un perfil aporta los skills de stack con nombres fijos (`modulo-estandar`, `plantilla-pruebas`, `canal-conversacional`, `cliente-api-tipado`, `componentes-ui`, `formularios`, `plantilla-humo`). Para otro stack, crea `skills/perfiles/<tu-stack>/` con esos nombres y actívalo en `proyecto.json`. Si falta un skill, el agente recibe el aviso y debe preguntar, no inventarlo.

## Evidencias

Cada ejecución agrega una fila a `docs/evidencias-ia.md` (agente, modelo, tarea, contexto, resultado). La columna «Validación de la persona» empieza en `pendiente` y la llena una persona. Ver el skill `registro-de-evidencias-ia`.

## Cambiar de proveedor o de modelo

En el `config.json` del agente: `proveedor` (`gemini`, `mistral`, `groq`, `openrouter`), `modelo` y `modelos_respaldo` (se prueban en orden ante errores 429 y 5xx). `python agentes-ia/agente.py --modelos gemini` lista los modelos de un proveedor. En el pipeline, `MODELO_S1`, `MODELO_B1`… en `.env` sobrescriben el modelo de un paso.

## Respaldo entre proveedores

Si el proveedor principal se queda sin cupo (429) o saturado (5xx) en todos sus modelos, el runtime puede pasar a otro proveedor. Está **apagado por defecto** para que todas las salidas de un proyecto usen el mismo modelo.

- Interruptor del proyecto, en `proyecto.json`: `"ia": {"respaldo_entre_proveedores": true}`.
- Orden de intentos, en el `config.json` de cada agente: `"proveedores_respaldo": [{"proveedor": "openrouter", "modelos": ["openrouter/free"]}]`.
- Necesita la llave de ese proveedor en `.env`; si falta, se omite con un aviso.
- El archivo guardado y la evidencia registran el proveedor que de verdad respondió, por ejemplo `openrouter/free (openrouter)`, para que la validación humana lo tenga en cuenta.
- Groq rechaza solicitudes de más de 8.000 tokens: no sirve como respaldo de los agentes con contexto largo.

## Crear un agente nuevo

1. Copia `agentes/_plantilla/` con el nombre del agente.
2. Escribe `prompt.md` con los marcadores y `config.json` con su modelo y skills.
3. Si debe leer y escribir archivos, agrégale una política en `POLITICAS` de `herramientas.py`.
4. Pruébalo con casos variados y revisa la evidencia que deja.
