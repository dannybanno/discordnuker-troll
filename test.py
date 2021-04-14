import discord
from discord.ext import commands
import os
import asyncio
import youtube_dl
from threading import Thread
from flask import Flask
import random
from discord.utils import get
import urllib.parse, urllib.request, re
from discord.ext import commands
from colorama import Fore, Back, Style



intents = discord.Intents(
    messages=True, guilds=True, reactions=True, members=True)

bot = commands.Bot(command_prefix='/', intents=intents)

player1 = ""
player2 = ""
turn = ""
gameover = True

board = []

app = Flask('')


@app.route('/')
def main():
    return "the bot is online yaaaaaaaaaaaaaaay"


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()


client = commands.Bot(command_prefix="/")

print(Fore.RED + '''
▓█████  ▄████▄   ██░ ██  ▒█████  
▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒
▒███   ▒▓█    ▄ ▒██▀▀██░▒██░  ██▒
▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░
░▒████▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░
░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░ 
 ░ ░  ░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░           
   ░   ░         ░  ░░ ░░ ░ ░ ▒  
   ░  ░░ ░       ░  ░  ░    ░ ░  
       ░ 
https://github.com/dannybanno                        
''')

TOKEN=input(Fore.MAGENTA + "Enter The Token Of Your Bot : ")

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.command()
async def clear100(ctx, amount=100):
    await ctx.send("the last 100 messages have been deleted")
    await ctx.channel.purge(limit=amount)

client.remove_command('help')

@client.command()
async def embed(ctx, *, message):
    for i in range(60):
        emb = discord.Embed(tile="embed", description=f"{message}", color=0x00A2FF)
        msg = await ctx.channel.send(embed=emb)
        print("SPAMMED EMBED")

@client.command(aliases=['make_role'])
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

@client.event
async def on_message(message):
    if message.content == "/vc":
        while True:
            channel = await message.guild.create_voice_channel('get-nuked-hahahaha')
            channel = await message.guild.create_voice_channel('FDFaSADwF_DADKAWDwdadwDaWdDFrgrGRyrTuy%^&8%5')
            channel = await message.guild.create_voice_channel('DADW_Dw-do0wDPkwadWDDS_DWDWwFWRfsFfwdsdFWWDssdw')
            channel = await message.guild.create_voice_channel('dsddADssDsddssdasadRTYUTYYTyttrtr87I(&U^YTY66yyrer')
            channel = await message.guild.create_voice_channel('FDfdgfgdsdfefeSFEFESFfESfesFeFGtUyjy_=-')


@client.command()
async def removechannel(ctx, channel: discord.TextChannel):
    await channel.delete(reason=None)
    print("Successfully deleted the channel!")



@client.event
async def on_ready():
    client.loop.create_task(playingLoop(client))
    # name=f"{len(client.guilds)} servers!"


async def playingLoop(client):  # danny this just refreshes the bot every 15 seconds
    while True:
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(client.guilds)} servers!"))
        await asyncio.sleep(15)



keep_alive()

client.run(TOKEN)