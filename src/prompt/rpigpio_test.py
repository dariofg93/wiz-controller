import RPi.GPIO as GPIO
import time

botones = {
    17: "Botón Rojo",
    1: "Botón Azul",
    3: "Botón Verde"
}

GPIO.setmode(GPIO.BCM)  # <-- esta línea es necesaria

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(17) == 0:
    print("presionado 17")

if GPIO.input(3) == 0:
    print("presionado 3")

if GPIO.input(1) == 0:
    print("presionado 1")

# for pin in botones:
#     GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# print("Esperando pulsación...")
# try:
#     while True:
#         for pin, nombre in botones.items():
#             if GPIO.input(pin) == GPIO.LOW:
#                 print(f"nombre: {nombre}")
#                 print(f"pin: {pin}")
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     GPIO.cleanup()
