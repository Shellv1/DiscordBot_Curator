# IMPORTS
import discord

# FUNCTION:     Pop(1)
#   1:          [obj]       Channels
async def Pop(channels):
    msg = []

    for channel in channels:
        msg = [message async for message in channel.history(limit=1)]
        await msg[0].delete()

# FUNCTION:     CreateChannels(1, 2)
#   1:          [str list]  Command
#   2:          [obj]       Guild
async def CreateChannels(cmd, guild):
    for i in range(2, len(cmd)):
        if (cmd[i] == '-v'): await CreateViewerChannel(cmd[1], guild)
        elif (cmd[i] == '-a'): await CreateArtistChannel(cmd[1], guild)

# FUNCTION:     CreateViewerChannel(1, 2)
#   1:          [obj]       User
#   2:          [obj]       Guild
async def CreateViewerChannel(user, guild):
    viewerChannelName = str('wips-' + CharToNum(user[0]) + IntToStr(len(guild.categories[1].channels) + 1))

    viewerChannel = await guild.categories[1].create_text_channel(viewerChannelName)

    projects = [message async for message in guild.categories[1].channels[0].history()]

    for project in reversed(projects):
        await viewerChannel.send(embeds=project.embeds)

    for member in guild.members:
        if (member.name == user[:-5] and member.discriminator == user[-4:]):
            await viewerChannel.set_permissions(
                member,
                view_channel=True,
                add_reactions=True,
                read_message_history=True
            )
            break

# FUNCTION:     CharToNum(1)
#   1:          [char]      ASCII Character
def CharToNum(x):
    y = ord(x.lower()) - 96
    return '0' + str(y) if (y < 10) else str(y)

# FUNCTION:     IntToStr(1)
#   1:          [int]       Integer Value
def IntToStr(i): return '0' + str(i) if (i < 10) else str(i)

# FUNCTION:     CreateArtistChannel(1, 2)
#   1:          [obj]       User
#   2:          [obj]       Guild
async def CreateArtistChannel(user, guild):
    artistChannelName = str(user[:-5] + '-exhibit')

    artistChannel = await guild.categories[2].create_text_channel(artistChannelName)

    for member in guild.members:
        if (member.name == user[:-5] and member.discriminator == user[-4:]):
            await artistChannel.set_permissions(
                member,
                view_channel=True,
                send_messages=True,
                send_messages_in_threads=True,
                create_public_threads=True,
                create_private_threads=True,
                embed_links=True,
                attach_files=True,
                add_reactions=True,
                use_external_emojis=True,
                use_external_stickers=True,
                manage_messages=True,
                read_message_history=True
            )
            break

# FUNCTION:     RemoveChannels(1, 2)
#   1:          [str list]  Command
#   2:          [obj]       Guild
async def RemoveChannels(cmd, guild):
    for i in range(2, len(cmd)):
        if (cmd[i] == '-v'): await RemoveUserChannel(cmd[1], guild.categories[1].channels)
        elif (cmd[i] == '-a'): await RemoveUserChannel(cmd[1], guild.categories[2].channels)

# FUNCTION:     CreateViewerChannel(1, 2)
#   1:          [obj]       User
#   2:          [obj]       Guild
async def RemoveUserChannel(user, category):
    for channel in category:
        if (len(channel.members) < 4):
            await channel.delete()
            continue
        for member in channel.members:
            if (
                (user[-5] == '#' and member.name == user[:-5] and member.discriminator == user[-4:]) or
                (member.name == user)
            ):
                await channel.delete()
                