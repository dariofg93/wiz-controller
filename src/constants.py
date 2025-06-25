from pathlib import Path


DEFAULT_COLOR_TEMP: int = 3000
DEFAULT_BRIGHTNESS: int = 128

DATABASE_PATH: Path = Path(__file__).resolve().parent / "data" / "wiz_controller.db"