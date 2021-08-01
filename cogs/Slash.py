test_ids = [804935799316676629] # Put your server ID in this array
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # Example of a slash command in a cog
    @slash_commands.command(description="Says Hello")
    async def hello(self, ctx):
        await ctx.send("Hello from cog!")

    @slash_commands.command(name="rickroll", description="Countdown to a rickroll!", guild_ids=test_ids, options=[Option("time", "Amount of time until the rickroll!", Type.INTEGER)])
    async def countdown_to_rickroll(ctx, time:int):
        await ctx.message.delete()
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
    bot.add_cog(Slash(bot))