from turtle import color
import discord
from discord.ext import commands
from discord.utils import get


class Givemerole(commands.Cog):
    def __init__(self, test):
        self.bot = test

    @commands.command()
    async def role(self, ctx, role_name):
        member = ctx.message.author
        role = get(member.guild.roles, name=role_name)
        await member.add_roles(role)

    @commands.command()
    async def createrole(self, ctx, role_name):

        guild = ctx.guild
        await guild.create_role(name=role_name)

    @commands.command()
    async def removerole(self,ctx,role_name):
        member=ctx.message.author
        role=get(member.guild.roles,name=role_name)
        await member.remove_roles(role)
    @commands.command()
    async def deleterole(self,ctx,role_name=None):
        role= discord.utils.get(ctx.message.guild.roles, name=role_name)
        try:
            await role.delete()
            await ctx.send(f'`role deleted succesfully`')
        except:
            await ctx.send(f'role not found')
    

def setup(client):
    client.add_cog(Givemerole(client))
