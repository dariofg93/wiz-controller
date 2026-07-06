# 001 · Support tests

**Estado:** en curso

## Qué hace

Agrega tests unitarios para todos los módulos de `src/`. Para poder testear en aislamiento, introduce inyección de dependencias en las clases que hoy instancian sus dependencias directamente (`BulbService`, `PinFunction` y sus subclases). Al final el desarrollador puede ejecutar `python -m unittest` y obtener un resultado verde sin necesidad de hardware real (GPIO) ni luces en la red.

## Por qué

El proyecto ya tiene código funcionando pero no hay tests. Cualquier cambio requiere validación manual contra las luces reales, lo que frena el desarrollo. Sin redes de seguridad, refactorizar o agregar features es riesgoso. Esta feature sienta la base para poder iterar con confianza.

## Criterios de aceptación

- [ ] Todos los módulos de `src/` (excepto `__init__.py` y `src/prompt/init_wiz_controller.py` que depende de GPIO físico) tienen al menos un archivo de test en `tests/`.
- [ ] `python -m unittest` pasa sin errores en un entorno sin Raspberry Pi, sin luces WiZ en la red y sin archivo `.env`.
- [ ] Los tests usan `unittest.mock` para aislar dependencias externas (red, GPIO, sistema de archivos, variables de entorno).
- [ ] `BulbRepository` se puede testear contra una base SQLite en memoria (`:memory:`).
- [ ] `BulbService` acepta un `BulbRepository` por constructor (inyección de dependencias) para poder mockearlo en tests.
- [ ] `PinFunction` y sus subclases aceptan un `BulbService` por constructor en lugar de instanciarlo directamente.
- [ ] La cobertura de líneas es al menos 70 % medida con `coverage run -m unittest && coverage report`.

## Fuera de alcance

- Tests de integración contra luces reales o GPIO físico (se harían en una feature separada si se justifica).
- Tests E2E del CLI con Click CliRunner (se difiere a una feature posterior de mejora de tests).
- CI/CD pipeline (se abordará cuando el proyecto se despliegue de forma automatizada).
- Refactorización profunda de la arquitectura hexagonal (solo se tocan los mínimos acoplamientos para permitir tests unitarios).
