#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 18155804
API_HASH = "e076156e161d0443b49382adb99595af"
BOT_TOKEN = "5962175498:AAFT8_f7rKAA1_T8VDG4qdkezvp-6iMWKTg"
SESSION = "BQAbYFG2F2AL-sFesfQurpDin_-6ni9BdlqqQcRVGRu1qeTZr0Pa7Oz6-_2ioGf_VCIapeOzc8BtU_PV5l0iWoQezzfWG52JOTyDxvhzYr74ArPQYzogcH416YFDDfw-qpEFVtokGZ8pLPVZ6EXsMvNhK4jsYRynqpMOE9B1PzlgEbvDwFESqG0FSV7MgF5TpruYfCHrTl1wkUT8bEDT8LqfPBpYoGfKSXlqL-YPkR3YmiUn4LZq1MLTKC37BFmV6R7yPl1nOrK0ibO_N0ylSmd4fNhHvdYyEaqQYmrmjg9394AoTMetF-DRznjZWVMmcQMxXVdutpIUPdWIG3FPOv_kbXwuvgA"
FORCESUB = "mabar_mobile_legends_bang_bang"
AUTH = "1316840924"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
