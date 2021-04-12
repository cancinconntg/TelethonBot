from .. import BotzHub
import telebot
import asyncio
from telethon import TelegramClient, sync, events, utils, types, Button
from telethon.events import StopPropagation
from telethon.sync import TelegramClient

api_id = 3926716 # int
api_hash = '2d0c249f0efe0fe1ea2551703a2f774d'
bot_token = "1725823055:AAGKZJFOdnrtEGlhR9aRA3CZONmiSZ-Ulyg"
client = TelegramClient('bot_token', api_id, api_hash)

@bot.message_handler(commands=["basla"])
def basla(message):

assert client.start()

if not client.is_user_authorized():
     client.send_code_request(bot_token)

entity=client.get_entity("@Saygisizlar")
users = client.get_participants(entity)
print(len(users[0].first_name))
     
for user in users:
     if user.username is not None:
          print(user.username)
          client.send_message(message.chat.id,f"@{user.username}")
       
@bot.message_handler(commands=["dur"])
def dur(message):
      string = '<b>Durduruldu!</b>'
      bot.send_message(message.chat.id, string, parse_mode='html')
      handler_state(False)
