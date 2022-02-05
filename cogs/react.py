import discord
from discord.ext import commands


class Testing(commands.Cog):
    def __init__(self, test):
        self.bot = test

    @commands.command()
    async def react(self, ctx):
            emoji='\N{Thumbs up sign}'
            await ctx.message.add_reaction(emoji)

def setup(client):
    client.add_cog(Testing(client))