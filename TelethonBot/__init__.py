# By < @Saygisizlar >
# // @SaygisizlarSahip //

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = 3926716 # int
API_HASH = '2d0c249f0efe0fe1ea2551703a2f774d' 
BOT_TOKEN = "1725823055:AAGKZJFOdnrtEGlhR9aRA3CZONmiSZ-Ulyg"

BotzHub = TelegramClient('BotzHub', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 
