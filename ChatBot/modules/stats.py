from pyrogram import filters, Client
from pyrogram.types import Message

from ChatBot import OWNER, ASUR
from ChatBot.database.chats import get_served_chats
from ChatBot.database.users import get_served_users


@ASUR.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""❖ ɪᴅ ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} ⏤͟͟͞͞★\n\n● ᴛᴏᴛᴀʟ ᴄʜᴀᴛs ➥ {chats}\n● ᴛᴏᴛᴀʟ ᴜsᴇʀs ➥ {users}""",
    )
    
  
  
