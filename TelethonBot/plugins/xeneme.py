from .. import BotzHub
import asyncio
from telethon import TelegramClient, sync, events, utils, types, Button
from telethon.events import StopPropagation
from telethon.sync import TelegramClient

TOKEN = "1725823055:AAGKZJFOdnrtEGlhR9aRA3CZONmiSZ-Ulyg" 

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['basla'])
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

client = BotzHub

assert BotzHub.start()

if not client.is_user_authorized():
     client.send_code_request(bot_token)

entity=client.get_entity("@Saygisizlar")
users = client.get_participants(entity)
print(len(users[0].first_name)) 

for user in users:
    if user.username is not None:
        print(user.username)
        BotzHub.send_message(-1001472566181,f"@{user.username}")
        
