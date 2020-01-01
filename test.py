# bot.py
import os

import discord
from dotenv import load_dotenv
from sheet_connect import *
import re

load_dotenv()
service = connect()
print('connected to google api')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    profile = message.content
    if not re.match('http(s?)://(osu|old).ppy.sh/(u|users)/[^\s]+$', profile):
        return

    print("found profile link: " + profile)

    add_row_to_sheet(service, profile)
    await message.add_reaction('\N{THUMBS UP SIGN}')


client.run(os.environ['BOT_TOKEN'])