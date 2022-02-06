from email import message
import discord
from discord.ext import commands


class Greets(commands.Cog):
    def __init__(self, test):
        self.bot = test

    @commands.command()
    async def greet(self, ctx):
        await ctx.message.channel.send(f'Aur bhai kaise ho')


def setup(client):
    client.add_cog(Greets(client))
