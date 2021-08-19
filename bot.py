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
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{servers} servers, {members} members'))
	await ctx.message.add_reaction('✅')


@bot.event
async def on_member_join(member):
	try:
		print(f'+[NEW_MEMBER]    {member} has joined the server: {member.guild.name}')
		
		channel = None
		if fetch_join_log_channel(int(member.guild.id)) is not None:
			channel = bot.get_channel(fetch_join_log_channel(int(member.guild.id))["channel_id"])

		if channel is not None:
			embed = discord.Embed(
					title = 'Member joined the server',
					description=f'Member **{member.name}** joined the server!',
					colour=0x008000
				)
			members = await member.guild.fetch_members().flatten()

			bot_count = 0
			for people in members:
				if people.bot is True:
					bot_count += 1

			embed.set_thumbnail(url=member.avatar_url)
			embed.add_field(name='Number of members', value=len(members) - bot_count)
			embed.add_field(name='Number of bots', value=bot_count)
			embed.set_footer(text=f'id: {member.id}')
			await channel.send(embed=embed)
		else:
			pass
	except Exception as e:
		raise Exception

@bot.event
async def on_member_remove(member):
	try:
		print(f'+[REMOVE_MEMBER]   {member} has left the server: {member.guild.name}')

		delete_warns(member.guild.id, member.id)

		channel = None
		if fetch_leave_log_channel(int(member.guild.id)):
			channel = bot.get_channel(fetch_leave_log_channel(int(member.guild.id))["channel_id"])


		if channel is not None:
			embed = discord.Embed(
				title = 'Member left the server',
				description=f'Member **{member.name}** has left the server!',
				colour=0xFF0000
			)
			try:
				members = await member.guild.fetch_members().flatten()

				bot_count = 0
				for people in members:
					if people.bot is True:
						bot_count += 1

				embed.set_thumbnail(url=member.avatar_url)
				embed.add_field(name='Number of members', value=len(members) - bot_count)
				embed.add_field(name='Number of bots', value=bot_count)
				embed.set_footer(text=f'id: {member.id}')
				await channel.send(embed=embed)
			except:
				pass
		else:
			pass
	except Exception as e:
		raise Exception

@bot.event
async def on_guild_channel_delete(channel):

	join_channel = None
	if fetch_join_log_channel(int(channel.guild.id)) is not None:
		join_channel = fetch_join_log_channel(int(channel.guild.id))["channel_id"]

		if channel.id == join_channel:
			delete_join_log_channel(int(channel.guild.id))

	leave_channel = None
	if fetch_leave_log_channel(int(channel.guild.id)) is not None:
		leave_channel = fetch_leave_log_channel(int(channel.guild.id))["channel_id"]

		if channel.id == leave_channel:
			delete_leave_log_channel(int(channel.guild.id))

	log_channel = None
	if fetch_mod_log_channel(int(channel.guild.id)) is not None:
		mod_channel = fetch_mod_log_channel(int(channel.guild.id))["channel_id"]

		if channel.id == mod_channel:
			delete_mod_log_channel(int(channel.guild.id))



@bot.event
async def on_guild_join(guild):

	insert_prefix(guild.id, "b!")


@bot.event
async def on_guild_remove(guild):

	clear_server_data(guild.id)

@bot.event
async def on_bulk_message_delete(messages):


	message_channel = fetch_message_edit_log_channel(int(messages[0].guild.id))
	if message_channel is not None:

		message_channel = fetch_message_edit_log_channel(int(messages[0].guild.id))["channel_id"]
		message_channel = bot.get_channel(message_channel)

		embed = discord.Embed(
				title='Bulk message delete',
				description=f'{len(messages)} messages deleted in {messages[0].channel.mention}',
				color=0xff0000
		)

		if message_channel.id != messages[0].channel.id:
			await message_channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
	
	message_channel = fetch_message_edit_log_channel(int(message.guild.id))
	if message_channel is not None:

		message_channel = fetch_message_edit_log_channel(int(message.guild.id))["channel_id"]
		message_channel = bot.get_channel(message_channel)

		embed = discord.Embed(
				title='Message deleted',
				description=f'Message deleted in {message.channel.mention}\nContents:\n```\n{message.content}\n```\n'
							f'Author of the message:\n{message.author.mention}',
				color=0xff0000
		)

		if message_channel.id != message.channel.id:
			await message_channel.send(embed=embed)

@bot.event
async def on_message_edit(before, after):

	if not after.author.bot:
		if before.content != after.content:

			message_channel = fetch_message_edit_log_channel(int(before.guild.id))
			if message_channel is not None:

				message_channel = fetch_message_edit_log_channel(int(before.guild.id))["channel_id"]
				message_channel = bot.get_channel(message_channel)

				embed = discord.Embed(
						title='Message edited',
						description=f'Message edited in {before.channel.mention}\nbefore:\n```\n{before.content}\n```\n\nAfter:\n```\n{after.content}\n```\n'
									f'Author of the message:\n{after.author.mention}\n'
									f'[jump](https://discordapp.com/channels/{after.guild.id}/{after.channel.id}/{after.id}) to the message',
						color=0xff0000
				)

				if message_channel.id != before.channel.id:
					await message_channel.send(embed=embed)


# Ping

@bot.command()
async def ping(ctx):
	await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')




bot.load_extension('jishaku')
bot.run(DISCORDTOKEN)
