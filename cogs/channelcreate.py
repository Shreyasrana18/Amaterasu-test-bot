from dis import disco
import discord
from discord.ext import commands

class Channel(commands.Cog) :
    def __init__(self,test):
        self.bot=test


    @commands.command()
    async def createchannel(self,ctx,channel_name) :
        guild=ctx.guild
        channel= await guild.create_text_channel(channel_name)
    @commands.command()
    async def deletechannel(self,ctx,channel_name) :
        guild=ctx.guild
        exist=discord.utils.get(guild.channels,name=channel_name)
        if exist is not None :
            await exist.delete()
        else :
            await ctx.message.channel.send(f'This channel does not exist')


def setup(client):
    client.add_cog(Channel(client))