# Discord Bot: Curator
# Ver 2.00.00

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
    # 1:        [obj]       Discord Message
@client.event
async def on_message(message):

    # Validate message
    if (
        (str(message.channel) not in ['wips', 'curator']) or
        (not message.content) or
        (message.author == client.user)
    ): return

    # Variable Declarations
    guild = message.channel.category.guild

    # Check if message is a command
    if (str(message.channel) == 'curator'):
        cmd = message.content.split()

        match cmd[0]:
            case 'create': await CreateChannels(cmd, guild)
            case 'remove': await RemoveChannels(cmd, guild)
            case 'help': await CuratorHelp(message.channel)
            case 'pop': await Pop(guild.categories[0].channels[:1] + guild.categories[1].channels)
            case 'ban': await BanUser()
            case _: await message.channel.send(content="```Unknown command. Type 'help' for list of commands.```")

        await message.delete()

    # Check if message is a content upload
    if (str(message.channel) == 'wips'):
        await UploadWIP(message, guild, message.content.splitlines()[1])
        
# Start
client.run(TOKEN)