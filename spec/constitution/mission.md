# Misión

## Qué construimos

Un controlador local para las luces inteligentes WiZ de un departamento. Recibe órdenes desde la terminal (CLI) y desde botones físicos conectados a GPIO, descubre las luces en la red WiFi y las sincroniza con una base de datos local.

1. **CLI** — Prender, apagar, togglear y descubrir luces por nombre.
2. **Interfaz física (GPIO)** — Botones con funciones asignables (toggle, temporizador, dimmer, apagado del sistema).
3. **Discovery automático** — Escanea la red WiFi, cruza MACs con un mapeo conocido y mantiene la DB actualizada.
4. **Automatización por Crontab** — Programar encendidos/apagados en horarios fijos sin depender de la nube.

## Para quién

- El autor del proyecto (uso personal en su departamento).
- Cualquier persona con un Raspberry Pi y luces WiZ que quiera control local sin apps ni nube.

## Principios

- **Simple por elección** — Sin frameworks web, sin ORM, sin build. Cada dependencia se justifica.
- **Local-first** — Todo corre en la Raspberry Pi, sin depender de internet ni de servicios externos. La nube WiZ es solo el medio de transporte, no un requisito de funcionamiento.
- **Orientado a hardware** — Los botones físicos son ciudadanos de primera clase, no un añadido.
- **Offline-capable** — La configuración y las automatizaciones deben funcionar aunque la red WiFi esté caída (excepto el control de las luces, que necesita la red local).
- **Iterativo y pragmático** — Se entrega rápido, se mejora después. Los tests y la documentación van después de validar que la feature funciona.

## Qué NO es

- Una app mobile o web. No hay interfaz gráfica ni REST API (salvo que la spec lo pida explícitamente).
- Un sistema comercial o multi-usuario. No hay autenticación, roles ni onboarding.
- Un hub universal para IoT. Solo soporta luces WiZ (protocolo pywizlight).
- Un proyecto con disponibilidad 24/7. Si la Pi se apaga, el control se pierde hasta que vuelva a encenderse.
