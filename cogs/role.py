import discord
from discord.ext import commands
from discord.utils import get


class Givemerole(commands.Cog):
    def __init__(self,test):
        self.bot=test
    @commands.command()
    async def role(self,ctx):
        member = ctx.message.author
        role = get(member.guild.roles, name="testrole")
        await member.add_roles(role)

def setup(client):
    client.add_cog(Givemerole(client))