from src.model.pin_function.pin_function import PinFunction


class Nothing(PinFunction):

    def __init__(self):
        super().__init__()

    def exec(self):
        pass