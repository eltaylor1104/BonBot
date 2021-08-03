from discord.ext import commands


class owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'📥**`{cog}`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'📤**`{cog}`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'🔁**`{cog}`**')

    @slash_commands.command(name="update")
    @slash_commands.is_owner()
    async def update(self, ctx):
        updater = self.bot.get_command("jsk git")
        await updater(ctx, argument=Codeblock("https://github.com/eltaylor1104/slash", "pull"))
        self.bot.unload_extension('cogs.mod')
        self.bot.load_extension('cogs.mod')
        self.bot.unload_extension('cogs.utility')
        self.bot.load_extension('cogs.utility')
        self.bot.unload_extension('cogs.general')
        self.bot.load_extension('cogs.general')
        self.bot.unload_extension('cogs.owner')
        self.bot.load_extension('cogs.owner')



def setup(bot):
    bot.add_cog(owner(bot))