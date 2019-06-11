
import discord
from discord.ext import commands as cmd

from utils.utils import hostUsers

class LoadUnloadCog(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @cmd.command()
    async def load(self, ctx, module):
        roleid = [role.id for role in ctx.author.roles]

        if(not hostUsers(roleid)): # not an admin
            return

        try:
            self.client.load_extension(module)
        except Exception as err:
            await ctx.send(f"{module} cannot be loaded [ERR: {err}]")
            return
        await ctx.send(f"{module} loaded.")

    @cmd.command()
    async def unload(self, ctx, module):
        roleid = [role.id for role in ctx.author.roles]

        if(not hostUsers(roleid)): # not an admin
            return

        try:
            self.client.unload_extension(module)
        except Exception as err:
            await ctx.send(f"{module} cannot be unloaded [ERR: {err}]")
            return
        await ctx.send(f"{module} unloaded.")

def setup(client):
    client.add_cog(LoadUnloadCog(client))