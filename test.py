# bot.py
import os

import discord
from dotenv import load_dotenv
from sheet_connect import *

load_dotenv()
token = 'NjYxNjU1MDU5MDk1ODc5Njkz.XgulCw.ehY8jPLqbeJvTt86zzjtm0ghc0A'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    service = connect()
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

client.run(token)