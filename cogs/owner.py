import os

import discord
import dislash
import DiscordUtils
import jishaku
from discord.ext import commands
from dislash import *
from jishaku.codeblocks import Codeblock, codeblock_converter

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array

class owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author == self.bot.owner:
            return
        await self.bot.process_commands(after)
'''
    @slash_commands.command(name='load', description="owner only", options=[Option("cog", "a cog to load", Type.STRING, required=True)], default_permissions=False)
    @slash_commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)
        else:
            await ctx.send(f'📥 **`{cog}`**', ephemeral=True)

    @slash_commands.command(name='unload', description="unload a cog", options=[Option("cog", "a cog to unload", Type.STRING, required=True)], default_permissions=False)
    @slash_commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)
        else:
            await ctx.send(f'📤 **`{cog}`**', ephemeral=True)

    @slash_commands.command(name='reload', description='reload a cog', options=[Option("cog", "a cog to unload", Type.STRING, required=True)], default_permissions=False)
    @slash_commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)
        else:
            await ctx.send(f'🔁 **`{cog}`**', ephemeral=True)

    @slash_commands.command(name='servers', description='view all servers that I am in', default_permissions=False)
    @slash_commands.is_owner()
    async def guilds(self, ctx):
        em1 = discord.Embed(title=  "Guilds [1 - 20]", color = ctx.author.color, description = "The first 20 guilds of BonBot")
        em2 = discord.Embed(title=  "Guilds [20 - 40]", color = ctx.author.color, description = "The next 20 guilds of BonBot")
        em3 = discord.Embed(title=  "Guilds [40 - 60]", color = ctx.author.color, description = "The last 20 guilds of BonBot")
        for i in range(0, len(self.bot.guilds)):
            guild = self.bot.guilds[i]
            if i < 20:
                em1.add_field(name = f"{guild.name}", value = f"```diff\n+ ID: {guild.id}\n+ Owner: {guild.owner}\n- Members: {guild.member_count}```")
            elif i > 20 and i < 40:
                em2.add_field(name = f"{guild.name}", value = f"```diff\n+ ID: {guild.id}\n+ Owner: {guild.owner}\n- Members: {guild.member_count}```")
            else:
                em3.add_field(name = f"{guild.name}", value = f"```diff\n+ ID: {guild.id}\n+ Owner: {guild.owner}\n- Members: {guild.member_count}```")
        paginator = DiscordUtils.Pagination.AutoEmbedPaginator(ctx)
        embeds = [em1, em2, em3]
        await paginator.run(embeds)
'''

def setup(bot):
    bot.add_cog(owner(bot))
