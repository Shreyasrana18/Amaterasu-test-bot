

from http import client
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('TOKEN')

prefix = '!'
client=commands.Bot(command_prefix=prefix)

cogs=['cogs.react','cogs.git','cogs.greetings','cogs.steal','cogs.role','cogs.prohibit','cogs.channelcreate']

for cog in cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    print('we have logged in', format(client))




client.run(token)
