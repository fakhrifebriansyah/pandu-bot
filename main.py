import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asyncio

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Success: BOT CONNECTED!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Pandu Bot || $help'))
    
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:3]} is loaded")

async def main():
    async with bot:
        await load()
        await bot.start("MTA1OTQyNjQ3MzUyNzc1MDY1Ng.GxiH4N.CYyDAiWTaLRB-Nd10EhyJToax-NtWUjjSZfHuA")
        
@bot.command()
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.")
    
@bot.command(aliases=['takon'])
async def magic_eightball(ctx, *, question):
    with open('takon.txt') as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        
    await ctx.send(response)

@bot.command(aliases=['list_film'])
async def list(ctx, *, question):
    with open('list_film.txt') as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        
    await ctx.send(response)
    
@bot.command(aliases=['quote'])
async def pandu_quote(ctx, *, question):
    with open('quote.txt') as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        
    await ctx.send(response)
    
@bot.command(aliases=['helps'])
async def tanyaDongNdu(ctx, *, question):
    with open('help.txt', 'r') as f:
        random_responses = f.read()
        
    await ctx.send(random_responses)

@bot.command(aliases=['avatars'])
async def ava(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.author
    embed = discord.Embed(title=member).set_image(url=member.avatar.url )
    await ctx.send(embed=embed)


asyncio.run(main())