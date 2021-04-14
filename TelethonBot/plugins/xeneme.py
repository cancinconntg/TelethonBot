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

client = BotzHub

assert BotzHub.start()

if not client.is_user_authorized():
     client.send_code_request(bot_token)

grup = await client.get_entity(Saygisizlar)
users = client.get_participants(grup)
print(len(users[0].first_name)) 

if not user.bot:
    if user.username != None:
        print(user.username)
        Mention.append(user.username)
     
for etiket in Mention:
    BotzHub.send_message(event.chat_id,f"@{etiket}")
    Mention.remove(etiket)
