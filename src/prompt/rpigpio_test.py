import RPi.GPIO as GPIO
import signal

from src.service.bulb import BulbService

GPIO.setmode(GPIO.BCM)

button_pins = [2, 3]

bulb_service = BulbService()

for pin in button_pins:
    # Configuramos cada pin como entrada con pull-up interno
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callback que se llama cuando se detecta un flanco de bajada (botón presionado)
def button_callback(channel):
    bulb_service.toggle_light('living')
    print(f"Botón en pin {channel} presionado")

# Configuramos detección de eventos
for pin in button_pins:
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

print("Esperando que se presionen botones. Presioná Ctrl+C para salir.")

try:
    signal.pause()  # Suspende el proceso hasta que ocurra una señal
except KeyboardInterrupt:
    print("\nSaliendo...")
finally:
    GPIO.cleanup()
