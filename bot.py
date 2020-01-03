# bot.py
import os

import discord
from dotenv import load_dotenv
from sheet_connect import *
import re

load_dotenv()

client = discord.Client()
service = connect() # connect to google sheets
autoreg_sheet_id = '1SCdDXMjHbD0fg7OV_E7q4O6tT62NBoqNc4Wu7Pr-GGc'
returning_player_id = '14icD7xiHcSgMK41HqxioajDzNAEobhES_nHFHlkqlgw'
RETURNING_PLAYERS = print_sheet_contents(service, returning_player_id, "Form Responses 1")
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

			profile_id = profile[profile.rfind('/')+1:]
			l = len(profile_id)

			university = ""
			for entry in RETURNING_PLAYERS[1:]:
				if entry:
					user = entry[2]
					if (user[len(user)-l:] == profile_id):
						university = entry[1]
						break
			if (university):
				add_row_to_sheet(service, profile, university, autoreg_sheet_id)
				await message.add_reaction('\N{THUMBS UP SIGN}')

				role = discord.utils.get(message.author.guild.roles, name='OCL W20 Player')
				await message.author.add_roles(role)
			else:
					await message.channel.send("It looks like you aren't a returning player! Please register using the registration form, or make sure your profile link is correct.")


client.run(os.environ['BOT_TOKEN'])