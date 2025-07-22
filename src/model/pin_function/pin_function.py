from abc import ABC, abstractmethod

from src.service.bulb import BulbService


class PinFunction(ABC):
    """
    Principal service
    """
    _bulb_service: BulbService

    """
    Abstract class to declare contract definition of any pin function.
    """
    def __init__(self):
        self._bulb_service = BulbService()

    @abstractmethod
    async def exec(self):
        """
        Execute the pin wiz function.
        """
        pass
