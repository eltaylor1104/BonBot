from discord.ext import commands
from dislash import *
from dotenv import load_dotenv
import discord
import os
import dislash
load_dotenv()


bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array



DISCORDTOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready(): 
	print("Bot is online.")

@slash.command(
	guild_ids=test_ids,
	description="Builds a custom embed",
	options=[
		Option('title', 'Makes the title of the embed', Type.STRING),
		Option('description', 'Makes the description', Type.STRING),
		Option('color', 'The color of the embed', Type.STRING)

		# Note that all args are optional
		# because we didn't specify required=True in Options
	]
)
async def embed(inter, title=None, description=None, color=None):
	# Converting color
	if color is not None:
		try:
			color = await commands.ColorConverter().convert(inter, color)
		except:
			color = None
	if color is None:
		color = discord.Color.default()
	# Generating an embed
	emb = discord.Embed(color=color)
	if title is not None:
		emb.title = title
	if description is not None:
		emb.description = description
	# Sending the output
	await inter.create_response(embed=emb, hide_user_input=True)

@slash.command(name="ping", description="Shows my latency!", guild_ids=test_ids
)
async def ping(ctx): # Defines a new "context" (ctx) command called "ping."
	await ctx.send(f"Pong! ({bot.latency*1000}ms)")
@slash.command(
	guild_ids=test_ids,
	name="user-info",
	description="Shows user's profile",
	options=[
		Option("user", "Specify any user", Type.USER)])
async def user_info(ctx, user=None):
	# Default user is the command author
	user = user or ctx.author

	emb = discord.Embed(color=discord.Color.blurple())
	emb.title = str(user)
	emb.description = (
		f"**Created at:** `{user.created_at}`\n"
		f"**ID:** `{user.id}`"
	)
	emb.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=emb)
@slash.command(name="invite", 
guild_ids=test_ids, description="Sends my invite!")
async def invite(ctx):
	await ctx.send("https://discord.com/api/oauth2/authorize?client_id=871145925425397810&permissions=261455605623&scope=bot%20applications.commands", ephemeral=True)
@slash.command(name="ban", guild_ids=test_ids, description="Ban a user", options=[
	Option("user", "Specify a user to ban.", Type.USER, required=True),
	Option("reason", "specify a reason", Type.STRING, required=False)
	])
@slash_commands.has_guild_permissions(ban_members=True)
async def ban(ctx, user, reason = None):
	await user.ban(reason = reason)
	await ctx.create_response(f"{user} has been banned.", ephemeral=True)
@slash.command(name="kick", guild_ids=test_ids, description="Kick a user", options=[
	Option("user", "Specify a user to kick.", Type.USER, required=True),
	Option("reason", "specify a reason", Type.STRING, required=False)
	])
@slash_commands.has_guild_permissions(kick_members=True)
async def kick(ctx, user, reason = None):
	await user.kick(reason = reason)
	await ctx.create_response(f"{user} has been kicked.", ephemeral=True)

@slash.command(name="echo", guild_ids=test_ids, description="Post a message in another channel", options=[
	Option("channel", "select a channel for me to post a message in", Type.CHANNEL, required=True),
	Option("message", "Giv eme a message to relay in the channel", Type.STRING, required=True)])
@slash_commands.has_permissions(manage_messages=True)
async def echo (ctx, channel, message):
    await channel.send(f"{message}")
    await ctx.send(f"Message has been sent to {channel}", ephemeral=True)

bot.load_extension('cogs.Slash')
bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)