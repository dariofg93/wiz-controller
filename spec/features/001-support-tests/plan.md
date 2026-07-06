# 001 · Support tests — Plan

_Cómo se implementa lo descrito en `spec.md`. Debe respetar la `constitution/`._

## Enfoque

Estrategia de dos fases: **primero caracterización** (testear lo que hay sin modificarlo) y **luego refactorización** (inyectar dependencias para aislar los tests). Se arranca por los módulos más puros (modelos, utilidades) y se avanza hacia los que tienen más acoplamiento (servicios, repositorios). En cada módulo se aplica el skill `/solid`: TDD donde sea práctico (Red-Green-Refactor) y SOLID (sobre todo DIP) al refactorizar.

Para los módulos con dependencias externas se usa `unittest.mock`; para el repositorio se usa una SQLite `:memory:`; para evitar los side effects de import-time se usa `patch` o se reestructuran los módulos para diferir los efectos laterales.

## Implementación

1. **Refactorizar `src/util/constants.py`** — Mover `load_dotenv()` a un bloque `if __name__ == "__main__"` o a un `configure()` explícito para que no se ejecute al importar. Alternativa: permitir que el test parchee `os.getenv` antes del import. Afecta: `constants.py`.

2. **Refactorizar `src/util/logger.py`** — Diferir la creación de los handlers a una llamada explícita `setup_logger()` para evitar I/O al importar. Mantener las funciones `info()`, `debug()` etc. como están. Afecta: `logger.py`.

3. **Refactorizar `src/service/bulb.py` — `BulbService`** — Agregar parámetro opcional `repository: BulbRepository | None = None` al constructor. Si no se pasa, crear el default (`BulbRepository()`). Esto permite inyección sin romper el código existente. Afecta: `service/bulb.py`.

4. **Refactorizar `src/model/pin_function/pin_function.py` — `PinFunction`** — Agregar parámetro opcional `bulb_service: BulbService | None = None` al constructor. Si no se pasa, crear el default (`BulbService()`). Esto rompe la creación directa y abre la puerta a mockeo. Afecta: `pin_function.py`.

5. **Agregar tests para `src/model/`** — `test_model_bulb.py`, `test_model_pin.py`, y tests para cada `PinFunction` en `tests/model/pin_function/`. Cubren: creación de entidades, configuración de pines, ejecución de cada estrategia (mocked). Afecta: `tests/model/`.

6. **Agregar tests para `src/util/`** — `test_utils.py`, `test_constants.py` (con parcheo de `os.getenv`). Afecta: `tests/util/`.

7. **Agregar tests para `src/repository/`** — `test_repository_bulb.py` usando `:memory:` SQLite. `test_migrations.py` similar. Afecta: `tests/repository/`.

8. **Agregar tests para `src/service/`** — `test_service_bulb.py` con `BulbRepository` mockeado. Afecta: `tests/service/`.

9. **Agregar tests para `src/prompt/`** — `test_cli.py` solo para `coro` decorator (test unitario puro). `test_shut_down.py` con `os.system` mockeado. `init_wiz_controller.py` queda fuera de alcance por dependencia de GPIO. Afecta: `tests/prompt/`.

10. **Medir cobertura** — Ejecutar `coverage run -m unittest && coverage report` para verificar el criterio de 70 %.

## Decisiones

- **Inyección opcional con default** — Se agrega como parámetro opcional (`= None`) en vez de refactorizar toda la cadena de llamadas. Esto mantiene compatibilidad con el código existente mientras permite tests aislados. Alternativa descartada: crear interfaces/Protocols (ISP puro) — es más correcto pero demasiado cambio para esta feature; se posterga a una futura limpieza arquitectónica si se justifica por la regla del tres (DRY).
- **`:memory:` SQLite para repositorio** — La stdlib soporta `:memory:` sin crear archivos temporales, lo que hace los tests rápidos y sin limpieza. Alternativa descartada: mockear `sqlite3.connect` — es más frágil y no prueba las queries reales.
- **Caracterización primero** — En vez de refactorizar todo antes de testear, se escriben tests que documentan el comportamiento actual. Luego se refactoriza con la red de seguridad puesta.
- **Sin Click CliRunner** — Los tests de Click requieren armar el grupo de comandos completo y mockear `BulbService`. Es posible pero añade complejidad; se difiere para mantener la feature acotada.
- **Fuera: `init_wiz_controller.py`** — Depende de `gpiod` (solo Linux) y hace side effects al importarse. Testearlo requeriría una refactorización mayor que no justifica el esfuerzo hoy.

## Riesgos

- **Los side effects de import-time (`load_dotenv`, `logger`, `gpiod`) rompen la importación de los tests** — Se mitiga parcheando (`patch`) las funciones problemáticas antes del import o moviendo los side effects a funciones explícitas de inicialización.
- **Los tests de `BulbService` quedan frágiles por el mockeo de `pywizlight`** — Se mitiga manteniendo los mocks lo más acotados posible (solo el método que se necesita) y validando que los mocks tengan la misma API que los reales mediante aserciones de `assert_called_with`.
- **Cobertura menor a 70 % por código no testeable** — Si algún módulo resiste el testeo, se documenta explícitamente y se ajusta la expectativa. La prioridad es tener tests útiles, no alcanzar un número arbitrario.
- **La refactorización de `constants.py` y `logger.py` puede romper el inicio de la aplicación** — Se mitiga asegurándose de que el `main()` de la app llame explícitamente a las funciones de inicialización antes de usar los módulos.
