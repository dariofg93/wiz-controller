from typing import List, Set
from datetime import datetime

from src.constants import DEFAULT_BRIGHTNESS, DEFAULT_COLOR_TEMP
from src.utils import mapping
from src.model.bulb import BulbEntity
from src.repository.bulb import BulbRepository

from pywizlight import PilotBuilder, wizlight
from pywizlight.cli import discovery
from pywizlight.models import DiscoveredBulb


class BulbService:

    _bulb_repository: BulbRepository

    def __init__(self):
        self._bulb_repository = BulbRepository()

    async def turn_on(self, name: str, color_temp: int, brightness: int) -> None:
        bulb_entity: BulbEntity = self._bulb_repository.get(name)
        bulb = wizlight(bulb_entity.ip_address)
        await bulb.turn_on(
            PilotBuilder(
                colortemp=color_temp,
                brightness=brightness
            )
        )
        bulb_entity.is_on = True
        self._bulb_repository.insert_or_update(bulb_entity)

    async def turn_off(self, name: str) -> None:
        bulb_entity: BulbEntity = self._bulb_repository.get(name)
        bulb = wizlight(bulb_entity.ip_address)
        await bulb.turn_off()
        bulb_entity.is_on = False
        self._bulb_repository.insert_or_update(bulb_entity)

    async def toggle_light(self, name: str) -> None:
        bulb_entity: BulbEntity = self._bulb_repository.get(name)
        bulb = wizlight(bulb_entity.ip_address)
        if bulb_entity.is_on:
            await bulb.turn_off()
        else:
            await bulb.turn_on(
                PilotBuilder(
                    colortemp=DEFAULT_COLOR_TEMP,
                    brightness=DEFAULT_BRIGHTNESS
                )
            )
        bulb_entity.is_on = not bulb_entity.is_on
        self._bulb_repository.insert_or_update(bulb_entity)

    async def update_all(self, broadcast_space: str, restart_bulbs: bool = False) -> None:
        saved_bulbs: List[BulbEntity] = self._bulb_repository.retrieve()
        discovered_bulbs: List[DiscoveredBulb] = await discovery.find_wizlights(broadcast_address=broadcast_space)

        mac_addresses_discovered_set: Set[BulbEntity] = { discovered.mac_address for discovered in discovered_bulbs }
        mac_addresses_saved_bulbs_set: Set[str] = { bulb.mac_address for bulb in saved_bulbs }
        mac_addresses: Set[str] = set(mapping.keys())

        for mac_address in mac_addresses:
            bulb_name = mapping.get(mac_address)

            if self._is_in_set(mac_address, mac_addresses_discovered_set) and \
            not self._is_in_set(mac_address, mac_addresses_saved_bulbs_set):
            # Bulb is discovered, but is not saved
                now = datetime.now().isoformat()
                discovered_bulb: DiscoveredBulb = self._get_bulb_by_mac_address(mac_address, discovered_bulbs)
                await self._insert_or_update_bulb(BulbEntity(bulb_name, None, mac_address, discovered_bulb.ip_address, now), True)

            elif not self._is_in_set(mac_address, mac_addresses_discovered_set) and \
            self._is_in_set(mac_address, mac_addresses_saved_bulbs_set):
            # Bulb is saved, but is not discovered
                self._bulb_repository.delete(bulb_name)

            elif self._is_in_set(mac_address, mac_addresses_discovered_set) and self._is_in_set(mac_address, mac_addresses_saved_bulbs_set):
            # Bulb is saved and discovered
                stored_bulb: BulbEntity = self._bulb_repository.get(bulb_name)
                await self._insert_or_update_bulb(stored_bulb, restart_bulbs)

            # Bulb is not in discovered neither in database, then, do nothing

    async def _insert_or_update_bulb(self, bulb_entity: BulbEntity, restart: bool = False) -> None:
        if restart:
            bulb_entity.is_on = False
            bulb = wizlight(bulb_entity.ip_address)
            await bulb.turn_off()

        self._bulb_repository.insert_or_update(bulb_entity)
    
    def _is_in_set(self, mac_address: str, bulbs: Set[str]) -> bool:
        return mac_address in bulbs
    
    def _get_bulb_by_mac_address(self, mac_address: str, bulbs: List[DiscoveredBulb]) -> DiscoveredBulb:
        return next(bulb for bulb in bulbs if bulb.mac_address == mac_address)
