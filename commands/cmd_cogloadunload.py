
import discord
from discord.ext import commands as cmd

from utils.utils import cmd_permission

class LoadUnloadCog(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @cmd.command()
    async def load(self, ctx, extension):
        try:
            self.client.load_extension(extension)
        except Exception as err:
            await ctx.send(f"{extension} cannot be loaded [ERR: {err}]")
            return
        await ctx.send(f"{extension} loaded.")

    @cmd.command()
    async def unload(self, ctx, extension):
        try:
            self.client.unload_extension(extension)
        except Exception as err:
            await ctx.send(f"{extension} cannot be unloaded [ERR: {err}]")
            return
        await ctx.send(f"{extension} unloaded.")

def setup(client):
    client.add_cog(LoadUnloadCog(client))