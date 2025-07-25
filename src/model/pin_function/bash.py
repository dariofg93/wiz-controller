from src.model.pin_function.pin_function import PinFunction
import os


class Bash(PinFunction):
    _instruction: str

    def __init__(self, instruction: str):
        super().__init__() 
        self._instruction = instruction

    async def exec(self):
        os.system(self._instruction)