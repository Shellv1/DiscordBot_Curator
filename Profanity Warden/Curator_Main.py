# Discord Bot: Profanity Warden
# Ver 0.01.00

# Installations
    # pip install -U discord.py
    # pip install -U python-dotenv

# IMPORTS
import discord
import os
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
        (not message.content) or
        (message.content[:4] == "http") or
        (message.author == client.user)
    ): return

    # Variable Declarations
    guild = message.channel.category.guild
    penance = str(message.author.nick)[-2:]
    talisman = message.content[-2:]

    if (penance != ":3"):
        await message.channel.send(content="Oopsie! Lewks like yew fowgot to add a ':3' to youw name. Fix it now. :3")
        await message.delete()

    elif (talisman != ":3"):
        await message.channel.send(content="Oopsie! Lewks like yew fowgot to add a ':3' to youw message. Let me fix it fow yew :3\n" + message.author.nick + ' - "' + message.content + '" :3')
        await message.delete()
        
# Start
client.run(TOKEN)