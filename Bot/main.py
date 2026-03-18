import discord
from discord.ext import commands
from model import jajko_wentylator
import os, random
import requests
import PIL.Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def egg_fan(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./{file_name}')
            image = PIL.Image.open(f'./{file_name}')
            await ctx.send(jajko_wentylator(image, "labels.txt", "keras_model.h5"))

    else:
        await ctx.send("Nie załączyłeś żadnego pliku!")

bot.run(token tu !)





















































