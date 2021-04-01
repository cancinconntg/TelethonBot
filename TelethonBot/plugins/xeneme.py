from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from userbot.events import register
from userbot import bot
from asyncio import sleep


@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def deneme(event: NewMessage.Event):
    Mention = []
    reason = ""
    text: str = event.message.text.split()
    try:
        reason = " ".join(text[2:])
    except:
        pass
    _id: str = text[1]
    if _id.startswith("@"):
        _id = _id.replace("@", "")
    async for user in event.client.iter_participants(-1001326131404):
        if not user.bot:
          if user.username != None:
        	  print(user.username)
        	  Mention.append(user.username)
        	
    for etiket in Mention:
      await bot.send_message(-1001326131404, f"@{etiket} {reason}")
      Mention.remove(etiket)
      await sleep(0.5)
            
Komut = CmdHelp('Saygısızlar Mention')
Komut.add_info('Bu plugin @cancinconn tarafından yazılmıştır.')
Komut.add()

