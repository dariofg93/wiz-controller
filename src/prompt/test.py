import lgpio
import time

PIN_BOTON_AC_2 = 2
PIN_BOTON_AC_3 = 3

# Abrir chip 0
h = lgpio.gpiochip_open(0)

# Reclamar los pines como entrada con pull-up
lgpio.gpio_claim_input(h, lgpio.SET_PULL_UP, PIN_BOTON_AC_2)
lgpio.gpio_claim_input(h, lgpio.SET_PULL_UP, PIN_BOTON_AC_3)

try:
    print("Esperando inputs... presiona el botón en el Pin 2 o Pin 3.")

    while True:
        estado_pin_2 = lgpio.gpio_read(h, PIN_BOTON_AC_2)
        estado_pin_3 = lgpio.gpio_read(h, PIN_BOTON_AC_3)

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
    lgpio.gpiochip_close(h)
    print("Script finalizado.")
