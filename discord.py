TOKEN = "OTk4OTg2OTA0NTE3MjE4MzU0.GHVwi3.AbfNh2-mGMTgs3XlUNsAW-HtJ7vP-7L0ux171E" 
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
   
    # copy what user says
    if message.content.startswith("$say"):
        await message.channel.send(message.content[5:])
        await message.delete()

    
    # russian roulette game
    if message.content.startswith("$russian roulette"):
        russian_roulette = random.randint(1, 6)
        await message.channel.send(russian_roulette)
        if russian_roulette == 1:
           await message.channel.send("you died")
    
    # censor
    language_warnings = 0
    censor_list = ["nigger", "cunny", "NIGGER"]
    for censored_word in censor_list:
        if message.content.__contains__(censored_word):
            message.author.id
            await message.delete()
            await message.channel.send("you cannot say that word !! (you now have {} warnings)".format(language_warnings))

client.run("OTk4OTg2OTA0NTE3MjE4MzU0.GHVwi3.AbfNh2-mGMTgs3XlUNsAW-HtJ7vP-7L0ux171E" )
