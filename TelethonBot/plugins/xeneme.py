from .. import BotzHub
import telebot
import asyncio
from telethon import TelegramClient, sync, events, utils, types, Button
from telethon.events import StopPropagation
from telethon.sync import TelegramClient

@BotzHub.on(events.NewMessage(pattern='basla'))
async def handler(event):
    # Good
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id

    # BAD. Don't do this
    chat = event.chat
    sender = event.sender
    chat_id = event.chat.id
    sender_id = event.sender.id

    entity = BotzHub.get_entity(event.chat.id)
    for user in BotzHub.get_participants('entity')
    if not user.bot:
          if user.username != None:
        	  print(user.username)
        	  Mention.append(user.username)
     
for etiket in Mention:
    BotzHub.send_message(event.chat.id,f"@{etiket}")
    Mention.remove(etiket)4 
