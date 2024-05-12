import asyncio
import importlib

from pyrogram import idle

from ChatBot import LOGGER, ASUR
from ChatBot.modules import ALL_MODULES


async def anony_boot():
    try:
        await ASUR.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("ChatBot.modules." + all_module)

    LOGGER.info(f"♥︎ @{ASUR.username} STARTED.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("♥︎ BOT HAS BEEN STOPED...")
  
