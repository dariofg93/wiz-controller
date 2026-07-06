# Tech stack y convenciones

_Cómo está construido el proyecto y las reglas que todo el código debe respetar. Es la referencia técnica que ningún plan de feature debería contradecir._

## Tecnologías

- **Lenguaje:** Python 3.13.2 estricto.
- **Framework / runtime:** Ninguno. CLI con Click 8 + asyncio de la stdlib. Botones GPIO con libgpiod y RPi.GPIO.
- **Base de datos:** SQLite mediante `sqlite3` de la stdlib. Sin ORM.
- **Tests:** `unittest` de la stdlib. Los archivos van en `tests/` paralelo a `src/`.
- **Despliegue:** Manual sobre Raspberry Pi (Raspbian). El código se copia o se hace pull desde el repo. Las automatizaciones se registran en Crontab del sistema.

## Archivos / módulos clave

- `src/prompt/cli.py` — CLI con Click: comandos `on`, `off`, `toggle`, `discovery`, `create_database`.
- `src/prompt/init_wiz_controller.py` — Loop principal de botones GPIO en la Raspberry Pi.
- `src/service/bulb.py` — Lógica de negocio: encender/apagar/togglear luces y sincronizar descubrimiento.
- `src/repository/bulb.py` — CRUD de bombillas contra SQLite.
- `src/model/bulb.py` — Entidad `BulbEntity` (name, mac_address, ip_address, updated_at).
- `src/model/pin.py` — Configuración de pines GPIO con su función asignada.
- `src/model/pin_function/` — Jerarquía de estrategias: `Toggle`, `OneConfig`, `NewMode`, `Bash`, `Dimmer`, `Automation`, `Nothing`.
- `src/util/constants.py` — Variables de entorno y constantes globales.
- `src/util/utils.py` — Mapeo MAC → nombre de bombilla.
- `data/wiz_controller.db` — Base de datos SQLite local.

## Comandos

- `source .venv/bin/activate` — Activa el entorno virtual.
- `python3 -m src.prompt.cli --help` — Muestra los comandos disponibles del CLI.
- `python -m unittest` — Ejecuta los tests.
- `pylint .` — Evalúa lint en la aplicación.
- `ruff check .` — Evalúa estilo Python.

## Modelo de datos / dominio

- **`BulletEntity`** (`src/model/bulb.py`) — `name` (PK, str), `mac_address` (str, única), `ip_address` (str), `updated_at` (datetime). Se sincroniza con el discovery WiFi.
- **`Pin`** (`src/model/pin.py`) — `pin` (int, numbering física), `bcm` (int, numbering BCM), `color_arduino` / `color_protoboard` (str, identificación física), `fn` (PinFunction, estrategia ejecutable). Configuración estática en `pin_configuration`.
- **Mapeo MAC → nombre** (`src/util/utils.py`) — Diccionario fijo alimentado desde `.env`. Las MACs no se descubren solas; se conocen de antemano y se cruzan contra el barrido WiFi.

## Convenciones

- Estilo estándar Python: `snake_case` para variables, funciones y módulos; `PascalCase` para clases.
- Tests en `tests/` paralelo a `src/` (ej. `src/repository/bulb.py` → `tests/repository/test_bulb.py`).
- Los errores personalizados van en `src/errors/`.
- Texto del código en inglés. Documentación (`spec/`, `AGENTS.md`) en español.
- Sin type ignore ni `Any` sin justificación; se prefiere tipado estricto.
- Sin dependencias nuevas sin avisar y justificar en una discusión antes de agregarlas.

## Estilo visual

_No aplica — el proyecto no tiene interfaz gráfica. Solo CLI y botones físicos._

## Límites duros

- No agregar dependencias sin avisar y discutir primero.
- No subir archivos `.env*` al repositorio.
- No utilizar antipatrones del lenguaje Python sin justificarlo por escrito en la spec o el plan de la feature.
- No tocar `.env` sin avisar al usuario.
- No modificar `spec/constitution/` a la ligera; cambiar la constitución requiere replantear las features afectadas.
