from src.model.pin_function.pin_function import PinFunction


class Nothing(PinFunction):

    def __init__(self):
        super().__init__()

    async def exec(self):
        pass