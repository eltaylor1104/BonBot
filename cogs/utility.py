import asyncio

import discord
from discord.ext import commands
from dislash import *
from jishaku.codeblocks import Codeblock, codeblock_converter

test_ids = [804935799316676629] # Put your server ID in this array
class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # reply to message cmd
    @slash_commands.command(name="reply", description="makes me reply to an existing message using the ID", guild_ids=test_ids, 
    options=[Option("link", "A message link or id for me to reply to", Type.STRING, required=True), Option("message", "The content of the reply", Type.STRING, required=True)])
    async def replycmd(self, ctx, link, message):
        c = commands.MessageConverter() # create instance
        msglink = await c.convert(ctx, link) 
        await msglink.reply(f"{message}")
        await ctx.send("The message was sent!", ephemeral=True)

    #@commands.command()
    #async def replycmd(self, ctx, link: discord.Message, message):
        #await link.reply(f"{message}")
#TODO add permissions do only manage messages can use
    @slash_commands.command(name="rickroll", description="Countdown to a rickroll!", guild_ids=test_ids, options=[Option("time", "Amount of time until the rickroll!", Type.INTEGER, required=True)])
    async def countdown_to_rickroll(self, ctx, time:int):
        if time > 1000:
            await ctx.send("Nah. Too long.")
            return
        count = time
        one = await ctx.send(f"Rickrolling you in {count}")
        for i in range(time):
            count -= 1
            await asyncio.sleep(1)
            await one.edit(content=f"Rickrolling you in {count}")
        await one.edit(content="https://youtu.be/dQw4w9WgXcQ")

    @slash_commands.command(name="react", description="makes me react to an existing message using the ID or message link.", guild_ids=test_ids, 
    options=[Option("link", "A message link or id for me to reply to", Type.STRING, 
    required=True), Option("reaction", "The reaction to be added", Type.STRING, required=True)])
    async def addreaction(self, ctx, link, reaction):
        c = commands.MessageConverter() # create instance
        mseglink = await c.convert(ctx, link) 
        await mseglink.add_reaction(f"{reaction}")
        await ctx.send("The reaction was added!", ephemeral=True)

    @commands.command(name="update")
    @commands.is_owner()
    async def botupdate(self, ctx):
        updatecommand = self.bot.get_command("jsk git")
        await updatecommand(ctx, argument=Codeblock("https://github.com/eltaylor1104/slash", "pull"))
        await self.bot.unload_extension('mod')
        await self.bot.load_extension('mod')
        await self.bot.unload_extension('utility')
        await self.bot.load_extension('utility')

    @slash_commands.command(name="update", decription="owner only!", guild_ids=test_ids)
    @slash_commands.is_owner()
    async def botupdate(self, ctx):
        updatecmd = self.bot.get_command("jsk git")
        await updatecmd(ctx, argument=Codeblock("https://github.com/eltaylor1104/slash", "pull"))
        await self.bot.unload_extension('mod')
        await self.bot.load_extension('mod')
        await self.bot.unload_extension('utility')
        await self.bot.load_extension('utility')


def setup(bot):
    bot.add_cog(utility(bot))
