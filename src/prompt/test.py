import lgpio
import time

PIN_BOTON_AC_2 = 2
PIN_BOTON_AC_3 = 3

# `chip` es 0 por defecto en Raspberry Pi
CHIP = 0

try:
    print("Esperando inputs... presiona el botón en el Pin 2 o Pin 3.")

    # Configurar pines
    lgpio.set_mode(CHIP, PIN_BOTON_AC_2, lgpio.INPUT)
    lgpio.set_mode(CHIP, PIN_BOTON_AC_3, lgpio.INPUT)

    # Activar pull-up interno
    lgpio.set_pull_up_down(CHIP, PIN_BOTON_AC_2, lgpio.PUD_UP)
    lgpio.set_pull_up_down(CHIP, PIN_BOTON_AC_3, lgpio.PUD_UP)

    while True:
        estado_pin_2 = lgpio.read(CHIP, PIN_BOTON_AC_2)
        estado_pin_3 = lgpio.read(CHIP, PIN_BOTON_AC_3)

        if estado_pin_2 == 0:
            print("¡Pin 2 presionado!")
            time.sleep(0.5)

        if estado_pin_3 == 0:
            print("¡Pin 3 presionado!")
            time.sleep(0.5)

        time.sleep(0.1)

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    print("Script finalizado.")
