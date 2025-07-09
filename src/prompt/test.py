import lgpio
import signal

class GpioWrapper:
    def __init__(self):
        # Abre el chip GPIO 0 (el default en Raspberry Pi)
        self.h = lgpio.gpiochip_open(0)

    def set_pull_up_down(self, pin, pud):
        # Configura pull-up o pull-down
        # En lgpio, pud es: LGPIO_PULL_UP, LGPIO_PULL_DOWN, o LGPIO_PULL_NONE
        lgpio.gpio_set_pull_up_down(self.h, pin, pud)

    def callback(self, pin, edge, func):
        # edge puede ser: LGPIO_BOTH_EDGES, LGPIO_RISING_EDGE, LGPIO_FALLING_EDGE
        return lgpio.callback(self.h, pin, edge, func)

    def close(self):
        lgpio.gpiochip_close(self.h)

# Constantes de lgpio
PUD_UP = lgpio.LGPIO_PULL_UP
FALLING_EDGE = lgpio.LGPIO_FALLING_EDGE

button_pins = [2, 3]

# Creamos la instancia
gpio = GpioWrapper()

# Configuramos los pines con pull-up
for pin in button_pins:
    gpio.set_pull_up_down(pin, PUD_UP)

# Callback para flanco de bajada
def button_callback(pin, level, tick):
    print(f"Botón en pin {pin} presionado (level={level}, tick={tick})")

# Registramos callback para cada pin
for pin in button_pins:
    gpio.callback(pin, FALLING_EDGE, button_callback)

print("Esperando que se presionen botones. Ctrl+C para salir.")

try:
    signal.pause()
except KeyboardInterrupt:
    print("\nSaliendo...")
finally:
    gpio.close()
