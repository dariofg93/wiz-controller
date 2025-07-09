try:
    from rpi_lgpio import Gpio
except ImportError:
    from src.mock.mock_gpio import Gpio

import signal

button_pins = [2, 3]

# Creamos una instancia del controlador
gpio = Gpio()

# Configuramos los pines como entrada con pull-up
for pin in button_pins:
    gpio.set_mode(pin, Gpio.INPUT)
    gpio.set_pull_up_down(pin, Gpio.PUD_UP)

# Callback que se llama cuando se detecta un flanco de bajada
def button_callback(pin, level, tick):
    print(f"Botón en pin {pin} presionado (level={level}, tick={tick})")

# Registramos el callback para cada pin
for pin in button_pins:
    gpio.callback(pin, Gpio.FALLING_EDGE, button_callback)

print("Esperando que se presionen botones. Presioná Ctrl+C para salir.")

try:
    signal.pause()
except KeyboardInterrupt:
    print("\nSaliendo...")
finally:
    gpio.close()
