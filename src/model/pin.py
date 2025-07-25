from dataclasses import dataclass
from typing import List

from src.util.constants import LAMP_4_NAME, LAMP_5_NAME, LAMP_3_NAME, LAMP_1_NAME, LAMP_2_NAME
from src.model.pin_function.new_mode import NewMode
from src.model.pin_function.none import Nothing
from src.model.pin_function.one_config import OneConfig
from src.model.pin_function.pin_function import PinFunction
from src.model.pin_function.toggle import Toggle
from src.model.pin_function.bash import Bash

@dataclass
class Pin:
    pin: int
    bcm: int
    color_arduino: str
    color_protoboard: str
    fn: PinFunction

pin_configuration: List[Pin] = [
    # Odd
    Pin(pin=7, bcm=4, color_arduino='black', color_protoboard='black', fn=Toggle(LAMP_3_NAME)),      # 0
    Pin(pin=11, bcm=17, color_arduino='grey', color_protoboard='grey', fn=Toggle(LAMP_4_NAME)),     # 1
    Pin(pin=13, bcm=27, color_arduino='violet', color_protoboard='violet', fn=Toggle(LAMP_5_NAME)),  # 2
    Pin(pin=15, bcm=22, color_arduino='green', color_protoboard='green', fn=Nothing()),               # 3
    Pin(pin=29, bcm=5, color_arduino='brown', color_protoboard='brown', fn=Nothing()),                # 4
    Pin(pin=31, bcm=6, color_arduino='green', color_protoboard='brown', fn=Nothing()),                # 5
    Pin(pin=33, bcm=13, color_arduino='blue', color_protoboard='grey', fn=Bash(                       # 6
        "sudo /sbin/shutdown -h now"
    )),
    Pin(pin=35, bcm=19, color_arduino='white', color_protoboard='white', fn=Nothing()),               # 7: Modify button

    # Even
    Pin(pin=12, bcm=18, color_arduino='black', color_protoboard='violet', fn=Toggle(LAMP_1_NAME)),    # 8
    Pin(pin=16, bcm=23, color_arduino='blue', color_protoboard='blue', fn=Toggle(LAMP_2_NAME)),       # 9
    Pin(pin=18, bcm=24, color_arduino='orange', color_protoboard='orange', fn=Nothing()),             # 10
    Pin(pin=22, bcm=25, color_arduino='yellow', color_protoboard='yellow', fn=Nothing()),             # 11
    Pin(pin=32, bcm=12, color_arduino='red', color_protoboard='red', fn=Nothing()),                   # 12
    Pin(pin=36, bcm=16, color_arduino='orange', color_protoboard='red', fn=Nothing()),                # 13
    Pin(pin=40, bcm=21, color_arduino='yellow', color_protoboard='brown', fn=NewMode([                # 14
        OneConfig(LAMP_4_NAME, 30)
    ])),
]