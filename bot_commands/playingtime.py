import discord
from dotenv import load_dotenv
import os
import bot_commands.playingtime as pt
import bot_commands.API_KEYS as cfg
import urllib.request, json
import numpy as np

def playingtime(message):
    players = ['JokerJim','SireBadbeat','Leon_command']

    games = [252950]

    i = 0
    string = ''
    string += f'{games}: \n'
    for player in players:
        Web = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={cfg.API_KEY[player]}&steamid={cfg.PlayerIDs[player]}&format=json'

        with urllib.request.urlopen(Web) as url:
            data = json.loads(url.read().decode())

        for each in data['response']['games']:
            if each['appid'] in games:
                try:
                    playtime_2w = each['playtime_2weeks']/60
                except Exception:
                    playtime_2w = 0
                playtime_forever = each['playtime_forever']/60

        string += f'{players[i]} has a total playing time of {int(playtime_forever)} hours and {int((playtime_forever*60) %60)} minutes (last 2 weeks: {int(playtime_2w)}:{int(playtime_2w*60 %60):02d}) \n'
        i += 1
    return message.channel.send(string)
    
    
        
    

    