from src.model.pin_function.pin_function import PinFunction


class Toggle(PinFunction):
    _bulb_name: str

    def __init__(self, bulb_name: str):
        super().__init__() 
        self._bulb_name = bulb_name

    async def exec(self):
        await self._bulb_service.toggle_light(self._bulb_name)