import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Made with ❤️ by PatrickGTR"))
    print('Logged on as', client.user)


@client.command()
async def host(ctx, code, mode):

    embed = discord.Embed(
        title = f"{mode.upper()} Arena",
        colour = discord.Colour.orange()
    )

    rules = \
    """
    **YOU MAY** fight your drop, if someone is contesting you, you can fight them
    **DO NOT** fight after clearing out and leaving your drop
    **DO NOT** fight until the 2nd zone has fully closed
    **DO NOT** grief, this means stealing any item at all
    **DO NOT** play like a bot, we want you to practice like this is WCn
    Game will start in **3 minutes** from this post
    """

    host = ctx.message.author # person who wrote the command

    embed.add_field(name="**Host**", value=host)
    embed.add_field(name="**Custom Key**", value=code, inline=False)
    embed.add_field(name="**Rules**", value=rules, inline=False)

    channel = ctx.message.channel # retrieve the channel
    await ctx.message.delete()
    await channel.send(embed=embed) # send the message

@client.command()
async def kill(ctx):
    await ctx.message.delete()
    await client.logout()

client.run(os.getenv("TOKEN"))