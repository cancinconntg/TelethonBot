from .. import BotzHub
import telebot
import asyncio
from telethon import TelegramClient, sync, events, utils, types, Button
from telethon.events import StopPropagation
from telethon.sync import TelegramClient

@BotzHub.on(events.NewMessage(incoming=True, pattern="/starrt"))
def basla(message):

entity= BotzHub.get_entity("@Saygisizlar")
users = BotzHub.get_participants(entity)
print(len(users[0].first_name))
     
for user in users:
     if user.username is not None:
          print(user.username)
          BotzHub.send_message(-1001472566181,f"@{user.username}")
