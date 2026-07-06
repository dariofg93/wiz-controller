# 001 · Support tests — Tareas

_Checklist accionable derivada del `plan.md`. Tareas pequeñas y concretas; marca `[x]` al completarlas._

## Refactorización para testabilidad

- [ ] Refactorizar `src/util/constants.py`: diferir `load_dotenv()` a una función explícita `load_config()` para evitar side effects al importar.
- [ ] Refactorizar `src/util/logger.py`: mover la configuración de handlers a `setup_logger()`; mantener funciones `info()`, `debug()` etc. como wrappers seguros de importar.
- [ ] Refactorizar `src/service/bulb.py`: agregar parámetro `repository: BulbRepository | None = None` al constructor de `BulbService`.
- [ ] Refactorizar `src/model/pin_function/pin_function.py`: agregar parámetro `bulb_service: BulbService | None = None` al constructor de `PinFunction`.
- [ ] Verificar que la app existente (`cli.py`, `init_wiz_controller.py`) sigue funcionando tras las refactorizaciones.

## Tests — Modelos

- [ ] Crear `tests/model/test_bulb.py`: testear creación de `BulbEntity` con valores válidos.
- [ ] Crear `tests/model/test_pin.py`: testear creación de `Pin`, integridad de `pin_configuration`.
- [ ] Crear `tests/model/pin_function/__init__.py`.
- [ ] Crear `tests/model/pin_function/test_toggle.py`: testear `Toggle.exec()` con `BulbService` mockeado.
- [ ] Crear `tests/model/pin_function/test_bash.py`: testear `Bash.exec()` con `os.system` mockeado.
- [ ] Crear `tests/model/pin_function/test_none.py`: testear que `Nothing.exec()` es no-op.
- [ ] Crear `tests/model/pin_function/test_one_config.py`: testear creación y exec (hoy no-op).
- [ ] Crear `tests/model/pin_function/test_new_mode.py`: testear creación con lista de sub-funciones.
- [ ] Crear `tests/model/pin_function/test_dimmer.py`: testear creación (hoy no-op).
- [ ] Crear `tests/model/pin_function/test_automation.py`: testear creación (hoy no-op).

## Tests — Utilidades

- [ ] Crear `tests/util/test_constants.py`: testear valores por defecto con `os.getenv` mockeado.
- [ ] Crear `tests/util/test_utils.py`: testear `mapping` y resolución MAC-nombre.
- [ ] Crear `tests/util/test_logger.py`: testear que las funciones `info()`, `debug()` etc. existen y llaman al logger subyacente.

## Tests — Repositorio

- [ ] Crear `tests/repository/test_bulb.py`: testear CRUD de `BulbRepository` contra SQLite `:memory:`.
- [ ] Crear `tests/repository/test_migrations.py`: testear `create_tables()` contra SQLite `:memory:`.

## Tests — Servicios

- [ ] Crear `tests/service/test_bulb.py`: testear `turn_on`, `turn_off`, `toggle_light`, `discovery` con `BulbRepository` mockeado y `pywizlight` mockeado.

## Tests — Prompt

- [ ] Crear `tests/prompt/test_cli.py`: testear el decorador `coro` con funciones síncronas y asíncronas.
- [ ] Crear `tests/prompt/test_shut_down.py`: testear `main()` con `os.system` mockeado.

## Validación y cierre

- [ ] Ejecutar `python -m unittest` y verificar que todos los tests pasan.
- [ ] Ejecutar `coverage run -m unittest && coverage report` y verificar cobertura >= 70 %.
- [ ] Validar contra los criterios de aceptación de `spec.md`.
- [ ] Mover la feature a "Hecho" en `../../constitution/roadmap.md`.
