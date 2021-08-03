from discord.ext import commands
from dislash import *
from dotenv import load_dotenv
import discord
import os
import dislash
import jishaku
from jishaku.codeblocks import Codeblock, codeblock_converter
load_dotenv()


bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array



DISCORDTOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready(): 
	print("Bot is online.")



@bot.command(name="update", hidden=True)
@commands.is_owner()
async def update(ctx):
	updater = bot.get_command("jsk git")
	await updater(ctx, argument=Codeblock("https://github.com/eltaylor1104/slash", "pull"))
	bot.unload_extension('cogs.mod')
	bot.load_extension('cogs.mod')
	bot.unload_extension('cogs.utility')
	bot.load_extension('cogs.utility')
	bot.unload_extension('cogs.general')
	bot.load_extension('cogs.general')
	bot.unload_extension('cogs.owner')
	bot.load_extension('cogs.owner')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)