import datetime
from decouple import config

token = config('TOKEN')

import discord
import random

intents = discord.Intents.default()
intents.message_content = True
date = datetime.datetime.now()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # if message.content.startswith('$hello'):
    #     await message.channel.send('world!')
    if message.content.startswith('$definition'):
        await message.channel.send('definition')

client.run(token)
