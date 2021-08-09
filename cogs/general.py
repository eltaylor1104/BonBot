import asyncio
import os

import discord
import dislash
import jishaku
from discord.ext import commands
from dislash import *
from dotenv import load_dotenv

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @slash_commands.command(name="rickroll", description="Countdown to a rickroll!", options=[Option("time", "Amount of time until the rickroll!", Type.INTEGER, required=True)])
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
        await ctx.send(embed=embed, ephemeral=True)









def setup(bot):
    bot.add_cog(general(bot))
