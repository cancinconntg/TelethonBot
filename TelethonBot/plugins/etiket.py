from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from userbot.events import register
from userbot import bot
from asyncio import sleep
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/etiket ?(\w*)"))
async def deneme(event: NewMessage.Event):
    reason = ""
    text: str = event.message.text.split()
    try:
        reason = " ".join(text[2:])
    except:
        pass
    _id: str = text[1]
    if _id.startswith("@"):
        _id = _id.replace("@", "")
    async for user in event.client.iter_participants(_id):
        if not user.bot:
        	print(user.username)
        
        await bot.send_message(event.chat_id, f"@{user.username} {reason}")
        await sleep(0.5)
