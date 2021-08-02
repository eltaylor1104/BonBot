from discord.ext import commands
from dislash import *
from dotenv import load_dotenv
import discord
import os
import dislash
import jishaku
load_dotenv()


bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array



DISCORDTOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready(): 
	print("Bot is online.")

@bot.command()
async def ping(self, ctx): # Defines a new "context" (ctx) command called "ping."
	await ctx.send(f"Pong! 🏓 ({bot.latency*1000}ms)")

@bot.command(name="update")
@commands.is_owner()
async def update(ctx):
	updater = bot.get_command("jsk git")
	await updater(ctx, argument=Codeblock("https://github.com/eltaylor1104/slash", "pull"))
	await bot.unload_extension('mod')
	await bot.load_extension('mod')
	await bot.unload_extension('utility')
	await bot.load_extension('utility')

bot.load_extension('cogs.utility')
bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)