# bot.py
import os

import discord
from dotenv import load_dotenv
from sheet_connect import *
import re

load_dotenv()

client = discord.Client()
service = connect() # connect to google sheets
spreadsheet_id = '1SCdDXMjHbD0fg7OV_E7q4O6tT62NBoqNc4Wu7Pr-GGc'
print('connected to google api')

@client.event
async def on_ready():
		print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.channel.name == "returning-player-reg" or message.channel.name == "spam-bot":
			if not re.match('http(s?)://(osu|old).ppy.sh/(u|users)/[^\s]+$', message.content):
					if message.content.startswith("!iattend "):
						role = discord.utils.get(message.author.guild.roles, name=message.content[9:])
						if role:
							await message.author.add_roles(role)
						else:
							await message.channel.send("That school role doesn't exist! D:")
					else:
						return

			else:
				profile = message.content
				print("found profile link: " + profile)

				add_row_to_sheet(service, profile)
				await message.add_reaction('\N{THUMBS UP SIGN}')

				role = discord.utils.get(message.author.guild.roles, name='OCL W20 Player')
				await message.author.add_roles(role)


client.run(os.environ['BOT_TOKEN'])