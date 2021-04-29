from .. import BotzHub
import asyncio
from telethon import TelegramClient, sync, events, utils, types, Button
from telethon.events import StopPropagation
from telethon.sync import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import UserStatusOnline
from telethon import functions, types
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

@BotzHub.on(events.NewMessage(incoming=True, pattern="/startt"))
async def tag(event):
    chat_id = message.chat.id
    BotzHub.send_message(chat_id, "/join {}".format(chat_id))


@BotzHub.on(events.NewMessage(incoming=True, pattern="/join"))
def join(message):
    print("group: " + message.text.replace("/join","").replace(" ","")) 
    user_id = str(message.from_user.id)
    id_file = open("id.txt","a+")
    id_list = id_file.readlines()
    estar = False
    print(user_id, id_list) 
    for i in id_list:
        if i.replace("\n","") == user_id:
            estar = True
    if not estar:
        id_file.write("{0}\n".format(user_id))
    id_file.close()

@BotzHub.on(events.NewMessage(incoming=True, pattern="/etiket"))
def all(message):
    ctext = message.text.replace("all ","")
    id_list = open("id.txt","r").readlines()
    for i in id_list:
        user_id = i.replace("\n","")
        #BotzHub.send_message(int(user_id), text)
        BotzHub.send_message(int(user_id), "@" +str(message.from_user.username) + " (*" + message.chat.title + "*): " + ctext + "\n" parse_mode = 'Markdown')

@BotzHub.on(events.NewMessage(incoming=True, pattern="/data"))
def data(message):
    print(message)

BotzHub.polling()
