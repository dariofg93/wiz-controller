# WIZ Controller
Este es un proyecto para controlar las luces Wiz de mi departamento.
A nivel general, la idea es gestionar el uso de las luces, automatizar horarios para que se prendan o apaguen y actualizar una base de datos local para descubrir las luces disponibles.

## Stack
- Lenguaje: Python 3.13.2 con Crontab de Linux
- Framework / runtime: Ninguno, no hay build, ni Framework
- Base de datos: SQLite
- Tests: Aun ninguno, proximamente con libreria de unittest.

## Comandos
- `[source .venv/bin/activate]` — Accede al environment que contiene las librerias de python del proyecto.
- `[python3 -m src.prompt.cli --help]` — Muestras los comandos disponibles
- `[python -m unittest]` — Ejecuta los test de la aplicacion.
- `[pylint .]` — Evalua Lint en la aplicacion Python
- `[ruff check .]` — Evalua estilo Python

## Estructura del proyecto
- `src/` — Codigo del proyecto.
- `data/` — Logs, base de datos y cualquier otro tipo de fichero referentes a datos generados en la aplicacion.
- `spec/` - Documentacion para Spec Driver Development: `constitution/` (mission, tech-stack, roadmap) y `features/NNN-nombre/` (spec, plan, task).
- `AGENTS.md` Este archivo: Guia operativa del proyecto.
- `.venv/` — Contiene las librerias descargadas para el proyecto.
- `.env.example` — Ejemplo de estructura para el archivo .env.

## Arquitectura

El proyecto tiene una arquitectura hexagonal modesta donde el núcleo (service) ignora si lo llaman desde la terminal o desde un botón físico, y la persistencia da igual que sea SQLite u otra cosa mientras cumpla el contrato del repositorio.

## Convenciones
- Utiliza las convenciones estandar para codigo Python
- Textos en ingles. Excepto todo lo que este contenido dentro de la carpeta `spec/` y en el file `AGENTS.md`.
- Los tests van a estar en una carpeta `tests/` y deben estar a la misma altura que el archivo a testear en `src/`. La forma mas facil de entenderlo es seguir la siguiente estructura de ejemplo.

mi_proyecto/
│
├── src/                    # Código fuente de tu proyecto
│   ├── __init__.py
│   └── matematica.py       # Código a probar
│
├── tests/                  # Carpeta contenedora de pruebas
│   ├── __init__.py
│   └── test_matematica.py  # Archivos de pruebas

- Los errores deben existir en la carpeta `src/errors/`

## No hagas
- No instalar dependencias sin avisar.
- No tocar `.env` sin avisar.
- No subir archivos `.env*` al repositorio.
- No utilizar antipatrones del lenguaje Python sin justificarlo.

## Flujo de trabajo
- Trabajamos con **Spec Driven Development**: La spec va antes que el codigo. Para una feature nueva, primero `spec.md` → `plan.md` → `tasks.md` en `spec/features/NNN-nombre/`, y solo entonces se implementa (ver "Documentacion").
- Antes de una tarea no trivial, propón un plan y espera mi OK.
- Una tarea a la vez; al terminar, dime qué cambiaste para que lo revise.
- Si no estás seguro al 80%, pregunta. No inventes.

## Documentación
La documentacion para hacer **Spec Driven Development(SSD)** vive en `spec/`. Empieza por `spec/README.md`, que explica la estructura y el flujo completo. En resumen.

- `spec/constitution/` - Las reglas estables del proyecto. **Lealas antes de tocar nada:**
  - `mission.md` - Que construimos y para quien.
  - `roadmap.md` - El orden de las features (hechas, siguientes, backlog).
  - `tech-stack.md` - Tecnologias, convenciones y limites duros.
- `spec/features/NNN-nombre` - Una carpeta por feature, cada una con `spec.md` (que hace + criterios de aceptacion), `plan.md` (como se implementa) y `tasks.md` (checklist).  

Como usarla:
1. **Antes de implementar**, lee la `constitution/` y la `spec.md` de la feature afectada para no contradecirlas.
2. **Para una feature nueva**, crea `spec/NNN-nombre/` (siguiente numero libre) y escribe `spec.md` → `plan.md` → `tasks.md` antes de escribir codigo.
3. **Al terminar**, marca las tareas `tasks.md` y mueve la feature a "Hecho" en `roadmap.md`.
4. La constitucion manda: Si una feature choca con `mission.md` o `tech-stack.md` (p. ej. pide un build o una dependencia), se replantea la feature, no la constitucion.