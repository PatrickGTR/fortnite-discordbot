import discord
from discord.ext import commands as cmd

from utils.utils import hostUsers

class HostCommand(cmd.Cog):

    def __init__(self, client):
        self.client = client

    @cmd.command()
    async def hostmsg(self, ctx, *, message=None) :

        roleid = [role.id for role in ctx.author.roles]

        if(not hostUsers(roleid)): # not an admin
            return

        await ctx.message.delete() # delete the command message.

        if(message == None) :
            await ctx.send(":exclamation: !hostmsg <message>")
            return # disallow the code from continuing below

        embed = discord.Embed(
            title = "Host Message",
            colour = discord.Colour.orange() # the embed colour
        )


        host = ctx.message.author # person who wrote the command
        embed.add_field(name="**Host**", value=host, inline=True)
        embed.add_field(name="**Message**", value=message, inline=True)
        await ctx.send(embed=embed) # send the message


    @cmd.command()
    async def host(self, ctx, code=None, mode=None) :

        roleid = [role.id for role in ctx.author.roles]

        if(not hostUsers(roleid)): # not an admin
            return

        await ctx.message.delete() # delete the command message.

        if(code == None):
            await ctx.send(":exclamation: !host <custom_key> <solo or duo>")
            return

        if(mode not in ["solo", "duo", "Solo", "Duo"]):
            await ctx.send(":exclamation: !host <custom_key> <solo or duo>")
            return # disallow the code from continuing below

        embed = discord.Embed(
            title = f"{mode.upper()} Arena",
            colour = discord.Colour.orange() # the embed colour
        )

        rules = \
        """
        **2ND ZONE** rule (when **second zone** has closed you may fight)
        YOU MAY fight your drop, if someone is contesting you, you can fight them
        **DO NOT** fight after clearing out and leaving your drop
        **DO NOT** fight until the **2nd zone** has fully closed
        **DO NOT** grief, this means stealing any item at all
        """

        host = ctx.message.author # person who wrote the command

        embed.add_field(name="**Host**", value=host)
        embed.add_field(name="**Custom Key**", value=code, inline=False)
        embed.add_field(name="**Rules**", value=rules, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/588083124731117577/588091727634497562/Boom_custom_photo.jpg")
        embed.set_footer(text="Please react below once you're ready!")

        msg = await ctx.send(embed=embed) # send the message
        await msg.add_reaction('👍') # attach reaction to message


def setup(client):
    client.add_cog(HostCommand(client))