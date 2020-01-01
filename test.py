# bot.py
import os

import discord
from dotenv import load_dotenv
from sheet_connect import *
import re

load_dotenv()
token = 'NjYxNjU1MDU5MDk1ODc5Njkz.XgxDyw.-HUUpVLRS3ML_hlr53CQI0GDRWI'

client = discord.Client()
service = connect() # connect to google sheets
spreadsheet_id = '1SCdDXMjHbD0fg7OV_E7q4O6tT62NBoqNc4Wu7Pr-GGc'
print('connected to google api')

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