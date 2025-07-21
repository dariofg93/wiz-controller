from src.model.pin_function.pin_function import PinFunction


class Dimmer(PinFunction):

    def __init__(self):
        super().__init__()

    def exec(self):
        """
        Mode to turn on dimmer control, if it is neccesary
        """
        pass