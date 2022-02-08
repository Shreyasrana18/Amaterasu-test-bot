import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


class TopAnime(commands.Cog):
    def __init__(self,test):
        self.bot=test


    @commands.command()
    async def topanime(self,ctx):
        url = 'https://myanimelist.net/'
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        link_tags=soup('li',class_="ranking-unit")
        # print(tags)
        count=0
        rank=0
        for link_tag in link_tags:
            if count<5:
                rank=rank+1
                a=link_tag.find('a',class_='title')
                anime_name=a.get_text()
                anime_link=a.get('href')
                count=count+1
                # print(n)
                await ctx.send(f'```{rank}.Anime name: {anime_name}```'+anime_link)

def setup(client):
    client.add_cog(TopAnime(client))