import lgpio
import time

PIN_BOTON_AC_4 = 4
PIN_BOTON_AC_18 = 18

# Abrir chip 0
h = lgpio.gpiochip_open(0)

# Reclamar los pines como entrada con pull-up
lgpio.gpio_claim_input(h, lgpio.SET_PULL_UP, PIN_BOTON_AC_4)
lgpio.gpio_claim_input(h, lgpio.SET_PULL_UP, PIN_BOTON_AC_18)

try:
    print("Esperando inputs... presiona el botón en el Pin 2 o Pin 3.")

    while True:
        estado_pin_2 = lgpio.gpio_read(h, PIN_BOTON_AC_4)
        estado_pin_3 = lgpio.gpio_read(h, PIN_BOTON_AC_18)

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
