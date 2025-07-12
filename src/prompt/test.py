import gpiod
import asyncio

from dataclasses import dataclass
from typing import List
from src.service.bulb import BulbService

@dataclass
class Pin:
    pin: int
    bcm: int
    color_arduino: str
    color_protoboard: str

pin_configuration: List[Pin] = [
    # Odd
    Pin(pin=7, bcm=4, color_arduino='black', color_protoboard='black'),
    Pin(pin=11, bcm=17, color_arduino='grey', color_protoboard='grey'),
    Pin(pin=13, bcm=27, color_arduino='violet', color_protoboard='violet'),
    Pin(pin=15, bcm=22, color_arduino='green', color_protoboard='green'),
    Pin(pin=29, bcm=5, color_arduino='brown', color_protoboard='brown'),
    Pin(pin=31, bcm=6, color_arduino='green', color_protoboard='brown'),
    Pin(pin=33, bcm=13, color_arduino='blue', color_protoboard='grey'),
    Pin(pin=35, bcm=19, color_arduino='white', color_protoboard='white'),

    # Even
    Pin(pin=12, bcm=18, color_arduino='black', color_protoboard='violet'),
    Pin(pin=16, bcm=23, color_arduino='blue', color_protoboard='blue'),
    Pin(pin=18, bcm=24, color_arduino='orange', color_protoboard='orange'),
    Pin(pin=22, bcm=25, color_arduino='yellow', color_protoboard='yellow'),
    Pin(pin=32, bcm=12, color_arduino='red', color_protoboard='red'),
    Pin(pin=36, bcm=16, color_arduino='orange', color_protoboard='red'),
    Pin(pin=40, bcm=21, color_arduino='yellow', color_protoboard='brown'),
]

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
                print("¡Botón en GPIO 4 presionado!")
                await bulb_service.toggle_light('hallway')
                await asyncio.sleep(0.5)
    except KeyboardInterrupt:
        print("Salida con Ctrl+C")
    finally:
        yellow_domain_lines.release()
        chip.close()

if __name__ == "__main__":
    asyncio.run(main())
