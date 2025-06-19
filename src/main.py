# import subprocess

# cmd = ["wizlight", "on", "--ip", "192.168.0.97", "--k", "3000", "--brightness", "128"]
# subprocess.run(cmd)

from pywizlight import wizlight, PilotBuilder
import asyncio

async def main():
    bulb = wizlight("192.168.0.167")  # IP de la lámpara
    await bulb.turn_on(
        PilotBuilder(
            colortemp=3000,     # Temperatura de color
            brightness=128      # Brillo
        )
    )

asyncio.run(main())