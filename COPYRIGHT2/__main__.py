import asyncio
import importlib
from pyrogram import idle
from COPYRIGHT2 import COPYRIGHT2
from COPYRIGHT2.modules import ALL_MODULES

LOGGER_ID = -1001970031336

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("COPYRIGHT2.modules." + all_module)
    print("ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟ sᴛᴀʀᴛ")
    await idle()
    print("ʟᴏᴡᴅᴇ ᴄᴏᴅᴇʀ ᴋᴇ ʙᴀᴀʟ ᴄᴏᴅᴇʀ ʙɴᴇɢᴀ ᴀᴀ ɢʏᴀ ɴᴀ ᴇʀʀᴏʀ ᴊᴀᴏ ᴅɪᴅɪ sᴇ ᴊᴀᴋʀ ᴇʀʀᴏʀ sᴏʟᴠᴇ ᴋʀᴡᴀᴏ @qnxanjaliabout")
    await COPYRIGHT2.send_message(LOGGER_ID, "**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ ʏᴏᴜʀ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴇᴘʟᴏʏ \n ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ  [˹ 🫧⏤͟͟͞ـﮩ♡︎ ˹Ҩ፝֟፝ͷ ꫝɴᴊᴀʟɪ˼ [🇮🇳]](https://t.me/AnjaliOwnerBot)**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
    
