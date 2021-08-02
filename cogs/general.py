from discord.ext import commands
from dislash import *
from dotenv import load_dotenv
import discord
import os
import dislash
import jishaku

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

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









def setup(bot):
    bot.add_cog(general(bot)(bot))