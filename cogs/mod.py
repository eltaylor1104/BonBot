import os

import discord
import dislash
import jishaku
from discord.ext import commands
from dislash import *
from dotenv import load_dotenv

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
inter = InteractionClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_commands.command(name="ban", description="Ban a user", options=[
        Option("user", "Specify a user to ban.", Type.USER, required=True),
        Option("reason", "specify a reason", Type.STRING, required=False)
        ])
    @slash_commands.has_guild_permissions(ban_members=True)
    @slash_commands.guild_only()
    async def ban(self, ctx, user, reason = None):
        me = await self.bot.fetch_user('494010761782231042')
        if user == me:
            await ctx.send("You can't ban the owner of the bot, you moron! God damn it!")
            return
        else:
            await user.ban(reason = reason)
            await ctx.create_response(f"{user} has been banned.", ephemeral=True)


    @slash_commands.command(name="kick", description="Kick a user", options=[
        Option("user", "Specify a user to kick.", Type.USER, required=True),
        Option("reason", "specify a reason", Type.STRING, required=False)
        ])
    @slash_commands.has_guild_permissions(kick_members=True)
    @slash_commands.guild_only()
    async def kick(self, ctx, user, reason = None):
        me = await self.bot.fetch_user('494010761782231042')
        if user == me:
            await ctx.send("You can't kick the owner of the bot, you absolute moron! God damn it! Get a life!")
            return
        else:
            await user.kick(reason = reason)
            await ctx.create_response(f"{user} has been kicked.", ephemeral=True)

    @slash_commands.command(name="purge", description="Purge a given amount of messages", options=[Option("amount", "amount of messages to purge", Type.INTEGER, required=True)])
    @slash_commands.has_permissions(manage_messages=True)
    @slash_commands.guild_only()
    async def clean(self, ctx, amount):
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'Cleared {amount} messages.', ephemeral=True)

    @slash_commands.command(name='addrole', description='Add a role to a specified user', options=[Option("user", "a user to add a role to", Type.USER, required=True),
    Option("role", "a role to add", Type.ROLE, required=True)])
    @slash_commands.has_permissions(manage_roles=True)
    @slash_commands.guild_only()
    async def addrole(self, ctx, user, role):
        if role in user.roles:
            await ctx.send(f'{user} already has {role}.', ephemeral=True)
        else:
            await user.add_roles(role)
            await ctx.send(f'{role} was added to {user}.', ephemeral=True)

    @slash_commands.command(name='removerole', description='Remove a role from a specified user', options=[Option("user", "a user to remove a role from", Type.USER, required=True),
    Option("role", "a role to remove", Type.ROLE, required=True)])
    @slash_commands.has_permissions(manage_roles=True)
    @slash_commands.guild_only()
    async def removerole(self, ctx, user, role):
        if role not in user.roles:
            await ctx.send(f'{user} does not have {role}.', ephemeral=True)
        else:
            await user.remove_roles(role)
            await ctx.send(f'{role} was removed from {user}.', ephemeral=True)

    @commands.command(description='Decancer a member.')
    async def decancer(self, ctx, member : discord.Member):
        """"Decancer" a member, or strip all the non-ASCII characters from their name. Useful to make your chat look good."""
        if ctx.me.permissions_in(ctx.channel).manage_nicknames and ctx.author.permissions_in(ctx.channel).manage_nicknames:
            cancer = member.display_name
            decancer = unidecode.unidecode_expect_nonascii(cancer)
            # decancer = re.sub(r'\D\W', '', decancer)
            if len(decancer) > 32:
                decancer = decancer[0:32-3] + "..."
            try:
                await member.edit(nick=decancer)
                await ctx.send(f'Successfully decancered {cancer} to ​`{decancer}​`.')
            except discord.Forbidden:
                await ctx.send('I couldn\'t decancer this member. Please move my role higher.')
        else:
            cancer = member.display_name
            decancer = unidecode.unidecode_expect_nonascii(cancer)
            await ctx.send(f'The decancered version of {cancer} is ​`{decancer}​`.')








def setup(bot):
    bot.add_cog(mod(bot))
