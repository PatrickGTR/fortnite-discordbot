import discord
from discord.ext import commands as cmd
from discord.ext.commands import CommandNotFound

class Main(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @cmd.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("Made with ❤️ by PatrickGTR"))
        print('Logged on as', self.client.user)

    @cmd.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return

def setup(client):
    client.add_cog(Main(client))