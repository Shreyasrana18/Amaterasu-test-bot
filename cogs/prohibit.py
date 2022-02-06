import discord
from discord.ext import commands

class Prohibition(commands.Cog):
    def __init__(self,test):
        self.bot=test
    
    @commands.Cog.listener()
    async def on_message(self,message):
        msg=str(message.content).lower().find('matar')
        msg2=str(message.content).lower().find('nirbhay')
        if not msg or not msg2 == -1 :
            await message.delete()
            

def setup(client):
    client.add_cog(Prohibition(client))
