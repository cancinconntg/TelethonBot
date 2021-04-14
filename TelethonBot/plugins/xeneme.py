from .. import BotzHub
import telebot
import asyncio
from telethon import TelegramClient, sync, events, utils, types, Button
from telethon.events import StopPropagation
from telethon.sync import TelegramClient

@BotzHub.on(events.NewMessage(incoming=True, pattern="/starrt"))
def basla(message):
    entity=BotzHub.get_entity(chat_id)
    for user in BotzHub.get_participants(entity)
    if not user.bot:
          if user.username != None:
        	  print(user.username)
        	  Mention.append(user.username)
     
for etiket in Mention:
    BotzHub.send_message(chat_id,f"@{etiket}")
    Mention.remove(etiket)4 
