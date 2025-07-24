from typing import Any, Dict, List, Optional, Set

from src.util.constants import DEFAULT_BRIGHTNESS, DEFAULT_COLOR_TEMP
from src.util.utils import mapping
from src.model.bulb import BulbEntity
from src.repository.bulb import BulbRepository

from pywizlight import PilotBuilder, PilotParser, wizlight
from pywizlight.cli import discovery
from pywizlight.models import DiscoveredBulb


BulbResponse = Dict[str, Any]

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

    async def turn_off(self, name: str) -> None:
        bulb_entity: BulbEntity = self._bulb_repository.get(name)
        bulb = wizlight(bulb_entity.ip_address)
        await bulb.turn_off()

    async def toggle_light(self, name: str) -> None:
        bulb_entity: BulbEntity = self._bulb_repository.get(name)
        bulb = wizlight(bulb_entity.ip_address)
        bulb_state: Optional[PilotParser] = await bulb.updateState()
        bulb_result: BulbResponse = bulb_state.pilotResult

        if bulb_result['state']:
            await bulb.turn_off()
        else:
            await bulb.turn_on(
                PilotBuilder(
                    colortemp=DEFAULT_COLOR_TEMP,
                    brightness=DEFAULT_BRIGHTNESS
                )
            )

    async def discovery(self, broadcast_space: str) -> None:
        saved_bulbs: List[BulbEntity] = self._bulb_repository.retrieve()
        discovered_bulbs: List[DiscoveredBulb] = await discovery.find_wizlights(broadcast_address=broadcast_space)

        mac_addresses_discovered_set: Set[BulbEntity] = { discovered.mac_address for discovered in discovered_bulbs }
        mac_addresses_saved_bulbs_set: Set[str] = { bulb.mac_address for bulb in saved_bulbs }

        for mac_address, bulb_name in mapping.items():
            if self._is_in_set(mac_address, mac_addresses_discovered_set) and \
            not self._is_in_set(mac_address, mac_addresses_saved_bulbs_set):
            # Bulb is discovered, but is not saved
                self._insert_or_update_discovered_bulb(bulb_name, mac_address, discovered_bulbs)

            elif not self._is_in_set(mac_address, mac_addresses_discovered_set) and \
            self._is_in_set(mac_address, mac_addresses_saved_bulbs_set):
            # Bulb is saved, but is not discovered
                self._bulb_repository.delete(bulb_name)

            elif self._is_in_set(mac_address, mac_addresses_discovered_set) and \
            self._is_in_set(mac_address, mac_addresses_saved_bulbs_set):
            # Bulb is saved and discovered
                self._insert_or_update_discovered_bulb(bulb_name, mac_address, discovered_bulbs)

            # Bulb is not in discovered neither in database, then, do nothing

    def _insert_or_update_discovered_bulb(self, bulb_name: str, mac_address: str, discovered_bulbs: List[DiscoveredBulb]) -> None:
        discovered_bulb: DiscoveredBulb = self._get_discovered_bulb_by_mac_address(mac_address, discovered_bulbs)
        new_bulb_entity = BulbEntity(bulb_name, mac_address, discovered_bulb.ip_address, None)
        return self._bulb_repository.insert_or_update(new_bulb_entity)
    
    def _is_in_set(self, mac_address: str, bulbs: Set[str]) -> bool:
        return mac_address in bulbs
    
    def _get_discovered_bulb_by_mac_address(self, mac_address: str, bulbs: List[DiscoveredBulb]) -> DiscoveredBulb:
        return next(bulb for bulb in bulbs if bulb.mac_address == mac_address)