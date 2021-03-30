# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("Grubumuz", url="https://t.me/Saygisizlar")],
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")

@BotzHub.on(events.NewMessage(incoming=True, pattern="/etiket"))
users = teleb.get_participants(1001472566181)
print(users[0].first_name)

for user in users:
    if user.username is not None:
        print(user.username)
        teleb.send_message(1001472566181, "@{}".format(user.username))
        time.sleep(2)
