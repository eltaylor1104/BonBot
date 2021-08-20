import asyncio
import DiscordUtils

import discord
from discord.ext import commands
from dislash import *
from jishaku.codeblocks import Codeblock, codeblock_converter


bot = commands.Bot(command_prefix="b!")
inter = InteractionClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_commands.command(name="reply", description="makes me reply to an existing message using the ID or message link", 
    options=[Option("link", "A message link or id for me to reply to", Type.STRING, required=True), Option("message", "The content of the reply", Type.STRING, required=True)])
    @slash_commands.has_permissions(manage_messages=True)
    @slash_commands.guild_only()
    async def replycmd(self, ctx, link, message):
        c = commands.MessageConverter() # create instance
        msglink = await c.convert(ctx, link) 
        await msglink.reply(f"{message}")
        await ctx.send("The message was sent!", ephemeral=True)



    @slash_commands.command(name="react", description="makes me react to an existing message using the ID or message link.", 
    options=[Option("link", "A message link or id for me to reply to", Type.STRING, 
    required=True), Option("reaction", "The reaction to be added", Type.STRING, required=True)])
    @slash_commands.guild_only()
    @slash_commands.has_permissions(manage_messages=True)
    async def addreaction(self, ctx, link, reaction):
        c = commands.MessageConverter() # create instance
        mseglink = await c.convert(ctx, link) 
        await mseglink.add_reaction(f"{reaction}")
        await ctx.send("The reaction was added!", ephemeral=True)




    @slash_commands.command(name="invite", description="Sends my invite!")
    async def invite(self, ctx):
            servers = len(self.bot.guilds)
            members = 0
            for guild in self.bot.guilds:
                members += guild.member_count - 1
            embed = discord.Embed(title="Add me to your server!", description = "Click [here](https://discord.com/api/oauth2/authorize?client_id=871145925425397810&permissions=261455605623&scope=bot%20applications.commands) to invite me! 🔗", color=discord.Color.blurple())
            embed.set_footer(text=f"In {servers} servers and watching {members} members!", icon_url="https://cdn.discordapp.com/attachments/807323728379772991/875921381752180736/mikey-removebg-preview-3.png")
            await ctx.send(embed=embed, ephemeral=True)


    @slash_commands.command(name="echo", description="Post a message in another channel", options=[
        Option("channel", "select a channel for me to post a message in", Type.CHANNEL, required=True),
        Option("message", "Give me a message to relay in the channel", Type.STRING, required=True)])
    @slash_commands.has_permissions(manage_messages=True)
    @slash_commands.guild_only()
    async def echo (self, ctx, channel, message):
        try:
            await channel.send(f"{message}")
            await ctx.send(f"Message has been sent to {channel}", ephemeral=True)
        except discord.Forbidden:
            await ctx.send('I couldn\'t send the message. Please be sure I have access to the channel.', ephemeral=True)


    @slash_commands.command(name='bugreport', description='report a bug to my owner, make sure to include details!', options=[Option('bug', 'a bug to report to my developer, make sure to include details!', Type.STRING, required=True)])
    async def bugreport(self, ctx, bug):
        channel = self.bot.get_channel(872374545372299274)
        await channel.send(f'<@494010761782231042> {bug} - {ctx.author.name}#{ctx.author.discriminator}')
        await ctx.send("Your bug has been reported to my owner.", ephemeral=True)


    @slash_commands.command(name='servers', description='view all servers that I am in')
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

    @slash_commands.command(name="help", description="See what I can do!")
    async def help(self, ctx):
        embed = discord.Embed(title="About BonBot™️!", color=ctx.author.color, description="I am an epic bot created by **judger#6969**. All of my commands are seen and run via slash commands, you may view those by typing `/` in a chat that you have the `Use Slash Commands` permission. You may also see this message by using the command `b!help`.")
        embed.add_field("[View my source code](https://github.com/eltaylor1104/BonBot) | [Join my support server](https://discord.gg/zVkkfbB7EN)")
        embed.set_footer(text="created by judger#6969", icon_url="https://cdn.discordapp.com/attachments/878365588915912764/878366239918026812/mikey-removebg-preview-3.png")
        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(utility(bot))
