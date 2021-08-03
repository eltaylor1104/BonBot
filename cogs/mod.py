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


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    @slash_commands.command(name="ban", guild_ids=test_ids, description="Ban a user", options=[
        Option("user", "Specify a user to ban.", Type.USER, required=True),
        Option("reason", "specify a reason", Type.STRING, required=False)
        ])
    @slash_commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, user, reason = None):
        await user.ban(reason = reason)
        await ctx.create_response(f"{user} has been banned.", ephemeral=True)


    @slash_commands.command(name="kick", guild_ids=test_ids, description="Kick a user", options=[
        Option("user", "Specify a user to kick.", Type.USER, required=True),
        Option("reason", "specify a reason", Type.STRING, required=False)
        ])
    @slash_commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, user, reason = None):
        await user.kick(reason = reason)
        await ctx.create_response(f"{user} has been kicked.", ephemeral=True)

    @slash_commands.command(name='purge', description='Delete a specified amount of messages with an optional user decorator.', guild_ids=test_ids, options=[
        Option("amount", "amount of messages to be purged", Type.INTEGER, required=True), Option("user", "an optional user to purge", Type.USER, required=False)
    ])
    async def purge(ctx, amount, user: discord.Member=None):
        await ctx.message.delete()
        msg = []
        try:
            amount = amount
        except:
            return await ctx.send("Please pass in an integer as an amount", ephemeral=True)
        if not user:
            await ctx.channel.purge(limit=limit)
            return await ctx.send(f"Purged {limit} messages", ephemeral=True, delete_after=3)
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == user:
                msg.append(m)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {limit} messages of {user.name}", ephemeral=True, delete_after=3)





def setup(bot):
    bot.add_cog(mod(bot))