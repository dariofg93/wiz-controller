from functools import wraps
from typing import Any, Callable, Coroutine, TypeVar

import click
import pywizlight
import asyncio

from src.repository.migrations import create_tables
from src.util.constants import DEFAULT_BRIGHTNESS, DEFAULT_COLOR_TEMP
from src.service.bulb import BulbService

del pywizlight.wizlight.__del__

T = TypeVar("T")

bulb_service = BulbService()

def coro(f: Callable[..., Coroutine[Any, Any, T]]) -> Callable[..., T]:
    """Allow to use async in click."""

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        """Async wrapper."""
        return asyncio.run(f(*args, **kwargs))

    return wrapper

@click.group()
@click.version_option()
def main() -> None:
    """Command-line tool to interact with the controller."""

@main.command("create_database")
@coro
async def create_database() -> None:
    """Create all tables."""
    create_tables()

@main.command("on")
@coro
@click.option(
    "--name",
    prompt="Put the bulb name",
    help="Turn on the specific bulb",
)
@click.option(
    "--color_temp",
    prompt="Kelvin for temperature.",
    help="Kelvin value (1000-8000) for turn on. Default 3000",
    default=DEFAULT_COLOR_TEMP,
    type=int,
)
@click.option(
    "--brightness",
    prompt="Set the brightness value 0-255",
    help="Brightness for turn on. Default 128",
    default=DEFAULT_BRIGHTNESS,
    type=int,
)
async def on(name: str, color_temp: int, brightness: int) -> None:
    """Turn on the specific bulb."""
    await bulb_service.turn_on(name, color_temp, brightness)

@main.command("off")
@coro
@click.option(
    "--name",
    prompt="Put the bulb name",
    help="Turn on the specific bulb",
)
async def off(name: str) -> None:
    """Turn off the specific bulb."""
    await bulb_service.turn_off(name)

@main.command("toggle")
@coro
@click.option(
    "--name",
    prompt="Put the bulb name",
    help="Toggle light of the specific bulb",
)
async def toggle(name: str) -> None:
    """Toggle light of the specific bulb."""
    await bulb_service.toggle_light(name)

@main.command("discovery")
@coro
@click.option(
    "--broadcast_space",
    prompt="Put the broadcast space",
    help="Set in database the discovered bulbs",
)
async def discovery(broadcast_space: str) -> None:
    """Set in database the discovered bulbs."""
    await bulb_service.discovery(broadcast_space)

if __name__ == "__main__":
    main()