from pydoc import cli
import discord 
from discord.ext import commands

class Stealing(commands.Cog) :
    def __init__(self,test):
        self.bot=test


    @commands.command()
    async def steal(self,ctx):
        if not ctx.bot and ctx.reaction.message.content == "steal":
            await ctx.reaction.remove(ctx.bot)
        # await reaction.message.add_reaction(reaction.emoji)
            await ctx.reaction.message.add_reaction('🇸')
            await ctx.reaction.message.add_reaction('🇹')
            await ctx.reaction.message.add_reaction('🇪')
            await ctx.reaction.message.add_reaction('🇦')
            await ctx.reaction.message.add_reaction('🇱')

def setup(client):
    client.add_cog(Stealing(client))