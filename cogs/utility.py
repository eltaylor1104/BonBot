import asyncio

import discord
from discord.ext import commands
from dislash import *
from jishaku.codeblocks import Codeblock, codeblock_converter

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # reply to message cmd
    @slash_commands.command(name="reply", description="makes me reply to an existing message using the ID", 
    options=[Option("link", "A message link or id for me to reply to", Type.STRING, required=True), Option("message", "The content of the reply", Type.STRING, required=True)])
    async def replycmd(self, ctx, link, message):
        c = commands.MessageConverter() # create instance
        msglink = await c.convert(ctx, link) 
        await msglink.reply(f"{message}")
        await ctx.send("The message was sent!", ephemeral=True)



    @slash_commands.command(name="react", description="makes me react to an existing message using the ID or message link.", 
    options=[Option("link", "A message link or id for me to reply to", Type.STRING, 
    required=True), Option("reaction", "The reaction to be added", Type.STRING, required=True)])
    async def addreaction(self, ctx, link, reaction):
        c = commands.MessageConverter() # create instance
        mseglink = await c.convert(ctx, link) 
        await mseglink.add_reaction(f"{reaction}")
        await ctx.send("The reaction was added!", ephemeral=True)


    @slash_commands.command(
	guild_ids=test_ids,
	description="Builds a custom embed",
	options=[
		Option('title', 'Makes the title of the embed', Type.STRING),
		Option('description', 'Makes the description', Type.STRING),
		Option('color', 'The color of the embed', Type.STRING)

		# Note that all args are optional
		# because we didn't specify required=True in Options
	])
    @slash_commands.has_permissions(manage_messages=True)
    async def embed(self, inter, title=None, description=None, color=None):
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


    @slash_commands.command(name="ping", description="Shows my latency!")
    async def ping(self, ctx):
        if round(self.bot.latency*1000) <= 50:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pong! The ping is **{round(self.bot.latency*1000)}** milliseconds!", color=0x44ff44)
        elif round(self.bot.latency*1000) <= 100:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pong! The ping is **{round(self.bot.latency*1000)}** milliseconds!", color=0xffd000)
        elif round(self.bot.latency*1000) <= 200:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pong! The ping is **{round(self.bot.latency*1000)}** milliseconds!", color=0xff6600)
        else:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pong! The ping is **{round(self.bot.latency*1000)}** milliseconds!", color=0x990000)
        await ctx.send(embed=embed)

    @slash_commands.command(name="invite", description="Sends my invite!")
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=871145925425397810&permissions=261455605623&scope=bot%20applications.commands", ephemeral=True)


    @slash.command(name="echo", description="Post a message in another channel", options=[
        Option("channel", "select a channel for me to post a message in", Type.CHANNEL, required=True),
        Option("message", "Giv eme a message to relay in the channel", Type.STRING, required=True)])
    @slash_commands.has_permissions(manage_messages=True)
    async def echo (self, ctx, channel, message):
        await channel.send(f"{message}")
        await ctx.send(f"Message has been sent to {channel}", ephemeral=True)






def setup(bot):
    bot.add_cog(utility(bot))
