import discord
from discord.ext import commands
from discord.utils import get


class Givemerole(commands.Cog):
    def __init__(self,test):
        self.bot=test
    @commands.command()
    async def role(self,ctx,role_name):
        member = ctx.message.author
        role = get(member.guild.roles, name=role_name)
        await member.add_roles(role)

def setup(client):
    client.add_cog(Givemerole(client))