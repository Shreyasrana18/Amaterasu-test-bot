
import discord
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, test):
        self.bot = test

    @commands.command()
    async def gitsearch(self, ctx):
        try:
            s = str(ctx.message.content).split('gitsearch ')[1]
            await ctx.message.channel.send(f'https://github.com/{s}')
        except:
            tag = (ctx.message.author.mention)
            await ctx.message.channel.send(f'Naam toh likh btc {tag}')
                

def setup(client):
    client.add_cog(Search(client))
