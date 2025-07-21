from pathlib import Path

LIVING_NAME: str = 'living'
ROOM_NAME: str = 'room'
KITCHEN_NAME: str = 'kitchen'
BATHROOM_NAME: str = 'bathroom'
HALLWAY_NAME: str = 'hallway'
LAMP_NAME: str = 'lamp'

LIVING_MAC_ADDRESS: str = 'cc4085b67298'
ROOM_MAC_ADDRESS: str = 'cc4085b68992'
KITCHEN_MAC_ADDRESS: str = 'cc4085b68760'
BATHROOM_MAC_ADDRESS: str = 'cc4085b69718'
HALLWAY_MAC_ADDRESS: str = 'cc4085b68954'
LAMP_MAC_ADDRESS: str = 'cc4085b68c40'


DEFAULT_COLOR_TEMP: int = 3000
DEFAULT_BRIGHTNESS: int = 128

DATABASE_PATH: Path = Path(__file__).resolve().parent.parent / "data" / "wiz_controller.db"