import gpiod
import time

# Abrir chip0 (pinctrl-rp1)
chip = gpiod.Chip('gpiochip0')

# Pines a usar
pins = [4, 5]  # cambiá por los que quieras

# Pedir como entrada con pull-up
lines = chip.get_lines(pins)
lines.request(consumer='test', type=gpiod.LINE_REQ_DIR_IN, flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP)

try:
    print("Esperando botones en GPIO 4 o GPIO 5...")
    while True:
        values = lines.get_values()
        if values[0] == 0:
            print("¡Botón en GPIO 4 presionado!")
            time.sleep(0.5)
        if values[1] == 0:
            print("¡Botón en GPIO 5 presionado!")
            time.sleep(0.5)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Salida con Ctrl+C")
finally:
    lines.release()
    chip.close()
