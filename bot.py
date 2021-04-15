from discord_webhook import DiscordWebhook, DiscordEmbed
from configparser import ConfigParser
from discord.ext import commands
from discord.utils import get
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import discord as d
import asyncio
from termcolor import colored
from colorama import Fore, init
import random
import os


app = Flask('')

TOKEN = input("Enter Your Token: ")


@app.route('/')
def main():
    return "the bot is online yaaaaaaaaaaaaaaay"


intents = discord.Intents(
    messages=True, guilds=True, reactions=True, members=True)


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()


client = commands.Bot(command_prefix="/", intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")


print(Fore.MAGENTA + '''



███╗   ██╗██╗   ██╗██╗  ██╗███████╗
████╗  ██║██║   ██║██║ ██╔╝██╔════╝
██╔██╗ ██║██║   ██║█████╔╝ █████╗  
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  
██║ ╚████║╚██████╔╝██║  ██╗███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                 
''')

print('''
[1] - Creates 500 voice channels 

[2] - 
''')





@client.event
async def on_message(message):
    if message.content == "1":
        while True:
            channel = await message.guild.create_voice_channel(random.randint(1, 999999))
            channel = await message.guild.create_voice_channel(random.randint(1, 999999))
            channel = await message.guild.create_voice_channel(random.randint(1, 999999))
            channel = await message.guild.create_voice_channel('dsddADssDsddssdasadRTYUTYYTyttrtr87I(&U^YTY66yyrer')
            channel = await message.guild.create_voice_channel('FDfdgfgdsdfefeSFEFESFfESfesFeFGtUyjy_=-')





@client.event
async def on_ready():
    client.loop.create_task(playingLoop(client))
    # name=f"{len(client.guilds)} servers!"


async def playingLoop(client):
    while True:
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(client.guilds)} servers!"))
        await asyncio.sleep(15)

keep_alive()

client.run(TOKEN)
