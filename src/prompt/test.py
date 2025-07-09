import lgpio
import time

# --- Configuración de los pines ---
# Define los pines a los que están conectados tus botones
PIN_BOTON_AC_2 = 2
PIN_BOTON_AC_3 = 3

# Inicializar lgpio
# g_handle es el identificador de la conexión con el demonio de lgpio.
# Por defecto, 0 (cero) se refiere a la Raspberry Pi local.
g_handle = lgpio.gpio_open()

try:
    print("Esperando inputs... presiona el botón en el Pin 2 o Pin 3.")

    # --- Configuración de los pines como entradas con pull-up ---
    # Se configuran los pines como ENTRADAS para leer su estado.
    lgpio.gpio_set_mode(g_handle, PIN_BOTON_AC_2, lgpio.GPIO_INPUT)
    lgpio.gpio_set_mode(g_handle, PIN_BOTON_AC_3, lgpio.GPIO_INPUT)

    # Se habilita la resistencia pull-up interna.
    # Esto significa que el pin estará en estado ALTO (HIGH/1) por defecto.
    # Cuando el botón se presiona (conectando el pin a GND/Tierra), el estado cambia a BAJO (LOW/0).
    lgpio.gpio_set_pull(g_handle, PIN_BOTON_AC_2, lgpio.GPIO_PUD_UP)
    lgpio.gpio_set_pull(g_handle, PIN_BOTON_AC_3, lgpio.GPIO_PUD_UP)

    # --- Bucle principal para monitoreo continuo ---
    while True:
        # Leer el estado actual de cada pin
        estado_pin_2 = lgpio.gpio_read(g_handle, PIN_BOTON_AC_2)
        estado_pin_3 = lgpio.gpio_read(g_handle, PIN_BOTON_AC_3)

        # --- Lógica para actuar cuando se presiona un botón ---
        # Si el estado es 0 (LOW), significa que el botón fue presionado.
        if estado_pin_2 == 0:
            print("¡Pin 2 presionado!")
            # Pausa para "antirrebote" (debouncing): evita múltiples detecciones por una sola pulsación.
            time.sleep(0.5) 
        
        if estado_pin_3 == 0:
            print("¡Pin 3 presionado!")
            # Pausa para "antirrebote" (debouncing).
            time.sleep(0.5)

        # Pequeña pausa para reducir el uso de CPU.
        # Permite que el sistema realice otras tareas y no sature el procesador.
        time.sleep(0.1)

except Exception as e:
    # Captura cualquier error inesperado y lo imprime.
    print(f"Ocurrió un error inesperado: {e}")
finally:
    # --- Liberación de recursos GPIO ---
    # Es VITAL cerrar la conexión con lgpio al finalizar el script.
    # Esto libera los pines para que otros programas o futuras ejecuciones puedan usarlos.
    if g_handle is not None:
        lgpio.gpio_close(g_handle)
    print("Script finalizado. Pines GPIO liberados correctamente.")