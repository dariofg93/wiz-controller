import RPi.GPIO as GPIO
import time

botones = {
    17: "Botón Rojo",
    1: "Botón Azul",
    3: "Botón Verde"
}

GPIO.setmode(GPIO.BCM)  # <-- esta línea es necesaria

for pin in botones:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Esperando pulsación...")
try:
    while True:
        for pin, nombre in botones.items():
            print(f"nombre: {nombre}")
            print(f"pin: {pin}")
            if GPIO.input(pin) == GPIO.LOW:
                print(f"nombre: {nombre}")
                print(f"pin: {pin}")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
