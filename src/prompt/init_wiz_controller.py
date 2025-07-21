import gpiod
import asyncio

from dataclasses import dataclass
from typing import List
from src.service.bulb import BulbService


chip = gpiod.Chip('gpiochip0')

def request_lines(pins):
    lines = chip.get_lines(pins)
    lines.request(consumer='test', type=gpiod.LINE_REQ_DIR_IN, flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP)

    return lines

yellow_domain_pins = [pin.bcm for pin in pin_configuration if pin.color_protoboard in ('yellow', 'orange', 'red')]
brown_domain_pins = [pin.bcm for pin in pin_configuration if pin.color_protoboard in ('brown')]
violet_domain_pins = [pin.bcm for pin in pin_configuration if pin.color_protoboard in ('violet')]
blue_domain_pins = [pin.bcm for pin in pin_configuration if pin.color_protoboard in ('blue', 'green')]
monocromatic_domain_pins = [pin.bcm for pin in pin_configuration if pin.color_protoboard in ('white', 'grey', 'black')]

yellow_domain_lines = request_lines(yellow_domain_pins)
brown_domain_lines = request_lines(brown_domain_pins)
violet_domain_lines = request_lines(violet_domain_pins)
blue_domain_lines = request_lines(blue_domain_pins)
monocromatic_domain_lines = request_lines(monocromatic_domain_pins)

async def main():
    bulb_service = BulbService()

    try:
        print("Esperando botones GPIOs...")
        while True:
            values = yellow_domain_lines.get_values()
            if 0 in values:
                print("¡Botón GPIO YELLOW DOMAIN presionado!")
                await bulb_service.toggle_light('kitchen')
                await asyncio.sleep(0.5)
        
            values = brown_domain_lines.get_values()
            if 0 in values:
                print("¡Botón GPIO BROWN DOMAIN presionado!")
                await bulb_service.toggle_light('living')
                await asyncio.sleep(0.5)

            values = violet_domain_lines.get_values()
            if 0 in values:
                print("¡Botón GPIO VIOLET DOMAIN presionado!")
                await bulb_service.toggle_light('hallway')
                await asyncio.sleep(0.5)

            values = blue_domain_lines.get_values()
            if 0 in values:
                print("¡Botón GPIO BLUE DOMAIN presionado!")
                await bulb_service.toggle_light('room')
                await asyncio.sleep(0.5)

            values = monocromatic_domain_lines.get_values()
            if 0 in values:
                print("¡Botón GPIO MONOCROMATIC DOMAIN presionado!")
                await bulb_service.toggle_light('bathroom')
                await asyncio.sleep(0.5)
    except KeyboardInterrupt:
        print("Salida con Ctrl+C")
    finally:
        yellow_domain_lines.release()
        brown_domain_lines.release()
        violet_domain_lines.release()
        blue_domain_lines.release()
        monocromatic_domain_lines.release()
        chip.close()

if __name__ == "__main__":
    asyncio.run(main())
