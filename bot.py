import os

import discord
import dislash
import jishaku
from discord.ext import commands
from dislash import *
from dotenv import load_dotenv
from jishaku.codeblocks import Codeblock, codeblock_converter
from discord import Intents

load_dotenv()



bot = commands.Bot(intents=discord.Intents.all(), command_prefix="b!")
inter = InteractionClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array





DISCORDTOKEN = os.getenv('TOKEN')


@bot.event
async def on_ready():
    print('BonBot is ready :D')

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{servers} servers, {members} members'
    ))



@bot.command(name="update", hidden=True)
@commands.is_owner()
async def update(ctx):
	updater = bot.get_command("jsk git")
	await updater(ctx, argument=Codeblock("https://github.com/eltaylor1104/bonbot", "pull"))
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			bot.unload_extension(f'cogs.{filename[:-3]}')
			bot.load_extension(f'cogs.{filename[:-3]}')

@inter.event
async def on_slash_command_error(ctx, error):
	await ctx.send(f'{error}', ephemeral=True)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command(name="status", hidden=True)
async def status(ctx):
	servers = len(bot.guilds)
	members = 0
	for guild in bot.guilds:
		members += guild.member_count - 1
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{servers} servers, {members} members'))
	await ctx.message.add_reaction('✅')


# Ping

@bot.command()
async def ping(ctx):
	await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')




bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)
