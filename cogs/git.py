


import discord
from discord.ext import commands
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl
import asyncio


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

    @commands.command()
    async def gitinfo(self,ctx,user_name):  
        cx = ssl.create_default_context()
        cx.check_hostname = False
        cx.verify_mode = ssl.CERT_NONE

        url = f'https://github-readme-streak-stats.herokuapp.com/?user={user_name}&theme=radical'
        # await asyncio.sleep(8)
        # makes the whole discord bot sleep for 8 sec so use delete after instead of that
        # await msg2.delete()
        try :
            msg2= await ctx.send("Collecting data....")
            status_code = urllib.request.urlopen(url).getcode()

            response = urllib.request.urlopen(url,context=cx).read()
            

            soup=BeautifulSoup(response,'html.parser')

            tags=soup('g',transform="translate(1,48)")

            total_contribuition=tags[0].get_text()

            tag2=soup('g',transform="translate(166,48)")
            current_streak=tag2[0].get_text()

            tag3=soup('g',transform="translate(331,48)")
            longest_streak=tag3[0].get_text()

            # await asyncio.sleep(6)
            await msg2.delete()
            await ctx.message.channel.send(f'```Total contributions: {total_contribuition.strip()}```'+f'```\nCurrent Streak: {current_streak.strip()} ```'+f'```\nLongest Streak: {longest_streak.strip()}```')
        except :
            await ctx.message.channel.send('```either site is down or u are down```')

                        
def setup(client):
    client.add_cog(Search(client))
