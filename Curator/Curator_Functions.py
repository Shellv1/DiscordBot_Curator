# IMPORTS
import discord

# CLASS: Buttons
class ShelButton(discord.ui.View):

    ShelButtonResponse : bool = None

    @discord.ui.button(custom_id='yesButton', label='Yes', style=discord.ButtonStyle.primary)
    async def YesButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.ShelButtonResponse = True
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(custom_id='noButton', label='No', style=discord.ButtonStyle.secondary)
    async def NoButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.ShelButtonResponse = False
        await interaction.response.defer()
        self.stop()

# FUNCTION:     UploadWIP(1, 2, 3)
#   1:          [obj]       Message
#   2:          [obj]       Guild
#   3:          [str]       Project Name
async def UploadWIP(message, guild, projectName):

    # = = Create Project Embeds
        # Create embed information for single image as list of embeds
        # If original message has more than 1 attachment:
            # Append second attachment as embed

    embeds = [discord.Embed(color=0xE4F6F8, description=message.content, url='https://google.com/').set_image(url=message.attachments[0].url)]
    if (len(message.attachments) == 2):
        embeds.append(discord.Embed(url='https://google.com/').set_image(url=message.attachments[1].url))

    # = = Prompt to share to 'Shell Exhibit' category
        # Create a button
        # Send button in 'wips' channel
        # Await response

    view = ShelButton()

    botMsg = await message.channel.send(embed=discord.Embed(color=0xE4F6F8, description="Would you like to share to Shell Exhibit?"), view=view)

    await view.wait()

    # = = Update projects in 'Shell Exhibit' category
        # If button response is 'Yes'
            # For each channel in the 'Shell Exhibit' category
                # Update the project

        # Update the project in the 'wips-current' channel

    if (view.ShelButtonResponse):
        for channel in guild.categories[1].channels:
            await UpdateProject(projectName, channel, embeds)
    
    await UpdateProject(projectName, guild.categories[0].channels[0], embeds)

    # Delete Button Prompt
    await botMsg.delete()

# FUNCTION:     UpdateProject(1, 2, 3)
#   1:          [str]       Project Name
#   2:          [obj]       Channel
#   3:          [obj list]  Project Content
async def UpdateProject(projectName, channel, embeds):

    # Get message history in channel
    history = [message async for message in channel.history()]

    # = = Delete previous project if duplicate
        # For each project in history
            # If Project Name matches
                # Delete project in history

    for project in history:
        if (projectName == project.embeds[0].description.splitlines()[1]):
            await project.delete()

    # Send update project
    await channel.send(embeds=embeds)