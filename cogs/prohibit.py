import discord
from discord.ext import commands

class Prohibition(commands.Cog):
    def __init__(self,test):
        self.bot=test
    
    @commands.Cog.listener()
    async def on_message(self,message):
        curseWords = ['matar','levelled']
        msg = message.content.lower()
        for word in curseWords:
            if word in msg:
                await message.delete()
                break
    
        

        
    

def setup(client):
    client.add_cog(Prohibition(client))
