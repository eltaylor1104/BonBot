from jishaku.features.baseclass import Feature
import discord
import os
import dislash
import jishaku
from discord.ext import commands
from dislash import *
from jishaku.codeblocks import Codeblock, codeblock_converter

class CustomDebugCog(*OPTIONAL_FEATURES, *STANDARD_FEATURES):
    @Feature.Command(parent="jsk", name="git")
    async def jsk_git(self, ctx: commands.Context):
        await ctx.send("pull")

    @slash_commands.command(name="update")
    @slash_commands.is_owner()
    async def update(ctx):
        await jishaku_git(ctx, argument=Codeblock("https://github.com/eltaylor1104/slash", "pull"))
        self.bot.unload_extension('cogs.mod')
        self.bot.load_extension('cogs.mod')
        self.bot.unload_extension('cogs.utility')
        self.bot.load_extension('cogs.utility')
        self.bot.unload_extension('cogs.general')
        self.bot.load_extension('cogs.general')
        self.bot.unload_extension('cogs.owner')
        self.bot.load_extension('cogs.owner')

def setup(bot: commands.Bot):
    bot.add_cog(CustomDebugCog(bot=bot))