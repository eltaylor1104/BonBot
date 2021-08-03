import os
import discord
import dislash
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
    


    @slash_commands.command(name='load', guild_ids=test_ids, description="owner only", options=[Option("cog", "a cog to load", Type.STRING, required=True)])
    @slash_commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)
        else:
            await ctx.send(f'📥**`{cog}`**', ephemeral=True)

    @slash_commands.command(name='unload', guild_ids=test_ids, description="unload a cog", options=[Option("cog", "a cog to unload", Type.STRING, required=True)])
    @slash_commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)
        else:
            await ctx.send(f'📤**`{cog}`**', ephemeral=True)

    @slash_commands.command(name='reload', guild_ids=test_ids, description='reload a cog', options=[Option("cog", "a cog to unload", Type.STRING, required=True)])
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
            await ctx.send(f'🔁**`{cog}`**', ephemeral=True)

        @slash_commands.command(
        name='activity', description="owner ONLY", options=[Option("activity", "an activity to set", Type.STRING, required=True)], guild_ids=test_ids)
        @slash_commands.is_owner()
        async def change_activity(self, ctx, *activity):
            """Set Bot activity.
            Available activities:
            \u1160playing, streaming, listening, watching.
            Example activities:
            \u1160playing [game],
            \u1160streaming [linkToStream] [game],
            \u1160listening [music],
            \u1160watching [movie]"""

            await self.set_activity(text=' '.join(activity))


def setup(bot):
    bot.add_cog(owner(bot))
