import discord
import os
import bot_commands.playingtime as pt
import bot_commands.API_KEYS as cfg
import urllib.request, json
import numpy as np

load_dotenv()
client = discord.Client()

prefix = '$'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(prefix):
        msg = message.content 
        msg = msg.replace(prefix, '')
        msg = msg.split()

        if msg[0] == 'playingtime':
           await pt.playingtime(message)
    
    return


        
# Generate new API Key
# api_key = 
#client.run(os.environ.get(api_key))