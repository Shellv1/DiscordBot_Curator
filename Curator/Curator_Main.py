# Discord Bot: Curator
# Ver 2.00.00

# TODO
# Create channels on command
#   Create private exhibit channel for artists

# Installations
    # pip install -U discord.py
    # pip install -U python-dotenv

# IMPORTS
import discord
import os
from Curator_Functions import *
from Curator_Commands import *
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create Connection
client = discord.Client(intents = discord.Intents(34379))

# FUNCTION:     on_message(1)
#   1:          [obj]       Discord Message
@client.event
async def on_message(message):

    # VALIDATE: Call
    if (
        (str(message.channel) not in ['wips', 'curator']) or
        (not message.content) or
        (message.author == client.user)
    ): return

    guild = message.channel.category.guild
    cmd = message.content.split()

    if (str(message.channel) == 'curator'):
        match cmd[0]:
            case 'create': await CreateChannels(cmd, guild)
            case 'remove': await RemoveChannels(cmd, guild)
            case 'pop': await Pop(guild.categories[:1])
            case _: return

    else: await UploadWIP(message, guild, message.content.splitlines()[1])
        
# Start
client.run(TOKEN)