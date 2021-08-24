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
bot.remove_command("help")
slash = SlashClient(bot)
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
        name = f'{servers} servers | b!help'
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

@slash.event
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
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{servers} servers | b!help'))
	await ctx.message.add_reaction('✅')


# Ping

@bot.command()
async def ping(ctx):
	await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')

@bot.command(name="help", description="See what I can do!")
async def help(ctx):
	embed = discord.Embed(title="About BonBot™️!", color=ctx.author.color, description="I am an epic bot created by **judger#6969**. All of my commands are seen and run via slash commands, you may view them by typing `/` in a chat that you have the `Use Slash Commands` permission in. You may also see this message by using the command `b!help`.\n**My Commands:**\n\n`/ban`: Bans the specified user\n`/bugreport`: Reports a bug to my owner\n`/decancer:` removes cancerous characters from a members nickname/username\n`/echo`: sends a message in a specified channel through me\n`/help`: Shows this message\n`/invite`: Shows my invite link\n`/kick`: Kicks a specified user\n`/meme`: Gets a meme from a random meme subreddit\n`/ping`: Shows my latency\n`/purge`: Deletes a specified amount of messsages\n`/reddit`: Get a random post from any specified subreddit\n`/react`: Makes me react to a specified message with a specified reaction. (Make sure I'm in the server that the emoji is from!)\n`/reply`: Makes me reply to a specified message\n`/rickroll`: Sends a countdown with the specified number of seconds, at the end a rickroll will be posted!")
	embed.add_field(name="About me!", value="[View my source code](https://github.com/eltaylor1104/BonBot) | [Join my support server](https://discord.gg/zVkkfbB7EN)")
	embed.set_image(url="https://cdn.discordapp.com/attachments/878365588915912764/878366239918026812/mikey-removebg-preview-3.png")
	embed.set_footer(text="Created by judger#6969", icon_url="https://cdn.discordapp.com/attachments/878365588915912764/878366239918026812/mikey-removebg-preview-3.png")
	await ctx.send(embed=embed)



bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)
