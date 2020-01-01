# bot.py
import os

import discord
from dotenv import load_dotenv
from sheet_connect import *

load_dotenv()
token = 'NjYxNjU1MDU5MDk1ODc5Njkz.XgxDyw.-HUUpVLRS3ML_hlr53CQI0GDRWI'

client = discord.Client()
service = connect() # connect to google sheets
spreadsheet_id = '1qQGHKvpmQ7KXiQE5zmOckpn-XzfSO5AFSAd8MI_0trg'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print_sheet_contents(service)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # only respond if in spam-bots
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('https://osu.ppy.sh/u'):
        register(message)

# take a message and send it to sheet
def register(message):
    body = {
        'values': [[str(message.content)]]
    }
    print (str(message.content))
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='Sheet1!A1',
        valueInputOption="RAW", body=body).execute()

client.run(token)