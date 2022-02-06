import discord
from discord.ext import commands

class Channel(commands.Cog) :
    def __init__(self,test):
        self.bot=test


    @commands.command()
    async def createchannel(self,ctx,channel_name,channel_type) :
        guild=ctx.guild
        if channel_type == 'voice' :
            channel= await guild.create_voice_channel(channel_name)
        elif channel_type =='text' :
            channel= await guild.create_text_channel(channel_name)
        else :
             await ctx.messsage.channel.send(f'Wrong command')

    @commands.command()
    async def deletechannel(self,ctx,channel_name) :
        guild=ctx.guild
        exist=discord.utils.get(guild.channels,name=channel_name)
        if exist is not None :
            await exist.delete()
        else :
            await ctx.message.channel.send(f'This channel does not exist')
        
    @commands.command()
    async def renamechannel(self,ctx,channel_name,new_name):
        guild=ctx.guild
        rename=discord.utils.get(guild.channels,name=channel_name)
        if rename is not None :
            await rename.edit(name=new_name)
        else :
            await ctx.message.channel.send(f'the channel u wanted to rename does not exist')


def setup(client):
    client.add_cog(Channel(client))