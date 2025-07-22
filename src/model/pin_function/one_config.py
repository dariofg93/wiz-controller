from src.constants import DEFAULT_BRIGHTNESS, DEFAULT_COLOR_TEMP
from src.model.pin_function.pin_function import PinFunction


class OneConfig(PinFunction):
    _name: str
    _brightness: int
    _color_temp: int

    def __init__(
        self, name: str,
        brightness: int = DEFAULT_BRIGHTNESS,
        color_temp: int = DEFAULT_COLOR_TEMP
    ):
        super().__init__()
        self._name = name
        self._brightness = brightness
        self._color_temp = color_temp

    async def exec(self):
        pass