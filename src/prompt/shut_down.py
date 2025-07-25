import asyncio
from src.model.pin_function.bash import Bash

async def main():
    instruction = Bash("sudo shutdown -h now")
    await instruction.exec()
    await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())