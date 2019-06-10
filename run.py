import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "/")

extensions = [
    #handler
    "main",
    #commands
    "commands.cmd_host",
    "commands.cmd_cogloadunload"
]

# development purposes, force kill
@client.command()
async def kill(ctx):
    await ctx.message.delete()
    await client.logout()

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as err:
            print(f"{extension} cannot be unloaded [ERR: {err}]")

    client.run(os.getenv("TOKEN"))


