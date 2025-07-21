from dataclasses import dataclass
from typing import List

from src.constants import BATHROOM_NAME, HALLWAY_NAME, KITCHEN_NAME, LIVING_NAME, ROOM_NAME
from src.model.pin_function.new_mode import NewMode
from src.model.pin_function.one_config import OneConfig
from src.model.pin_function.pin_function import PinFunction
from src.model.pin_function.toggle import Toggle

@dataclass
class Pin:
    pin: int
    bcm: int
    color_arduino: str
    color_protoboard: str
    fn: PinFunction

pin_configuration: List[Pin] = [
    # Odd
    Pin(pin=7, bcm=4, color_arduino='black', color_protoboard='black', fn=Toggle(KITCHEN_NAME)),
    Pin(pin=11, bcm=17, color_arduino='grey', color_protoboard='grey', fn=Toggle(BATHROOM_NAME)),
    Pin(pin=13, bcm=27, color_arduino='violet', color_protoboard='violet', fn=Toggle(HALLWAY_NAME)),
    Pin(pin=15, bcm=22, color_arduino='green', color_protoboard='green'),
    Pin(pin=29, bcm=5, color_arduino='brown', color_protoboard='brown'),
    Pin(pin=31, bcm=6, color_arduino='green', color_protoboard='brown'),
    Pin(pin=33, bcm=13, color_arduino='blue', color_protoboard='grey'),
    Pin(pin=35, bcm=19, color_arduino='white', color_protoboard='white'),

    # Even
    Pin(pin=12, bcm=18, color_arduino='black', color_protoboard='violet', fn=Toggle(LIVING_NAME)),
    Pin(pin=16, bcm=23, color_arduino='blue', color_protoboard='blue', fn=Toggle(ROOM_NAME)),
    Pin(pin=18, bcm=24, color_arduino='orange', color_protoboard='orange'),
    Pin(pin=22, bcm=25, color_arduino='yellow', color_protoboard='yellow'),
    Pin(pin=32, bcm=12, color_arduino='red', color_protoboard='red'),
    Pin(pin=36, bcm=16, color_arduino='orange', color_protoboard='red'),
    Pin(pin=40, bcm=21, color_arduino='yellow', color_protoboard='brown', fn=NewMode([
        OneConfig(BATHROOM_NAME, 30)
    ])),
]