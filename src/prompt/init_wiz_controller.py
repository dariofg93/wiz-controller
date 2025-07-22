from dataclasses import dataclass
from typing import List
import gpiod
import asyncio

from src.model.pin import pin_configuration


@dataclass
class PressedButtons:
    _is_modified: bool
    _indexes: List[int]

    def __init__(self):
        pass

MODIFIED_BUTTON_INDEX: int = 7
chip = gpiod.Chip('gpiochip0')
pins = [pin.bcm for pin in pin_configuration]

def request_lines(pins):
    lines = chip.get_lines(pins)
    lines.request(consumer='test', type=gpiod.LINE_REQ_DIR_IN, flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP)

    return lines

lines = request_lines(pins)

def _pressed_buttons():
    pressed: List[int] = lines.get_values()
    pressed_buttons: PressedButtons = PressedButtons()
    pressed_indexes: List[int] = []

    pressed_buttons._is_modified = pressed[MODIFIED_BUTTON_INDEX] == 0 

    for index, value in enumerate(pressed):
        if value == 0 and index != MODIFIED_BUTTON_INDEX:
            pressed_indexes.append(index)

    pressed_buttons._indexes = pressed_indexes
    
    return pressed_buttons

async def main():

    try:
        print("Esperando botones GPIOs...")
        while True:
            buttons = _pressed_buttons()

            for button_index in buttons._indexes:
                # Enviar por parametro de exec el buttons._is_modified
                pin_configuration[button_index].fn.exec()
        
    except KeyboardInterrupt:
        print("Salida con Ctrl+C")
    finally:
        lines.release()
        chip.close()

if __name__ == "__main__":
    asyncio.run(main())
