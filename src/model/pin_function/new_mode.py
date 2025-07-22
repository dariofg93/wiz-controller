from typing import List
from src.model.pin_function.pin_function import PinFunction


class NewMode(PinFunction):
    _configurations: List[PinFunction]

    def __init__(self, configurations):
        super().__init__()
        self._configurations = configurations

    async def exec(self):
        pass