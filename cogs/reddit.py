import asyncio
import random
from collections import deque
from random import choice, randint
from urllib.parse import quote_plus

import aiohttp
import discord
import dislash
import requests
from discord.ext import commands
from dislash import *

FIFTEEN_MINUTES = 900

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="s!")
slash = SlashClient(bot)
test_ids = [804935799316676629] # Put your server ID in this array


#CREDIT TO BobDotCom on GitHub and Discord for part of this code, primarily the reddit commands. THAT IS NOT MY CODE!

acceptableImageFormats = [".png",".jpg",".jpeg",".gif",".gifv","imgur.com"]
memeHistory = deque()
memeSubreddits = ["memes", "dankmemes", "me_irl"]
async def getSub(self, ctx, subreddit):
    if True:
      url = f"https://reddit.com/r/{subreddit}/random.json?limit=1"
      async with aiohttp.ClientSession() as session:
        async with session.get(f"https://reddit.com/r/{subreddit}/random.json?limit=1") as r:
          res = await r.json()
          s = ""
          subredditDict = dict(res[0]['data']['children'][0]['data'])
          if subredditDict['over_18'] and not ctx.channel.is_nsfw():
              embed = discord.Embed(title="Thats an NSFW subreddit!", description="To get an image from this subreddit, please use this command again in an NSFW channel", color=discord.Color.red())
              await ctx.send(embed=embed)
              return
          embed = discord.Embed(title = f"{subredditDict['title']}", description = f"{subredditDict['subreddit_name_prefixed']}", url =  f"https://reddit.com{subredditDict['permalink']}")
          
          if subredditDict['selftext'] != "":
              embed.add_field(name = "Post Content:", value = subredditDict['selftext'])
          if subredditDict['url'] != "":
              embed.set_image(url = subredditDict['url'])
          embed.set_footer(text=f"🔺 {subredditDict['ups']} | u/{subredditDict['author']}")
          if subredditDict['selftext'] != "&amp;#x200B;":
                await ctx.send(embed = embed)
          else:
                await ctx.send("Annoying error with reddit being stupid. Try again lmao", ephemeral=True)
    else:
      try: 
        return await ctx.send("_{}! ({})_".format(str(subredditDict['message']), str(subredditDict['error'])), ephemeral=True)
      except:
        return await ctx.send("Error", ephemeral=True)
async def getSubs(self, ctx, sub):
      """Get stuff from requested sub"""
      async with aiohttp.ClientSession() as session:
          async with session.get(f"https://www.reddit.com/r{sub}/hot.json?limit=450") as response:
              request = await response.json()
                  
      attempts = 1
      while attempts < 5:
          if 'error' in request:
              print("failed request {}".format(attempts))
              await asyncio.sleep(2)
              async with aiohttp.ClientSession() as session:
                  async with session.get(f"https://www.reddit.com/r/{sub}/hot.json?limit=450") as response:
                      request = await response.json()
              attempts += 1
          else:
              index = 0
              for index, val in enumerate(request['data']['children']):
                  if val['data']["over_18"] == True:
                      if not ctx.channel.is_nsfw():
                          return await ctx.send("Thats an nsfw reddit, nonono", ephemeral=True)
                  if 'url' in val['data']:
                      print(val['data'])
                      url = val['data']['url']
                      thetitle = val['data']['title']
                      thereddit = val['data']['subreddit_name_prefixed']
                      upvotes = val['data']['ups']
                      link = val['data']['permalink']
                      if val['data']['selftext'] != "":
                          selftext = val['data']['selftext']
                      urlLower = url.lower()
                      accepted = False
                      for j, v, in enumerate(acceptableImageFormats): #check if it's an acceptable image
                          if v in urlLower:
                              accepted = True
                      if accepted:
                          if url not in memeHistory:
                              memeHistory.append(url)  #add the url to the history, so it won't be posted again
                              if len(memeHistory) > 500: #limit size
                                  memeHistory.popleft() #remove the oldest

                              break #done with this loop, can send image
              subredditDict = dict(request['data']['children'][0]['data'])
              embed = discord.Embed(title=f"{thereddit}", description=f"{thetitle}", url=f"{link}", footer=f"🔺 {upvotes}")
              embed.set_image(url=memeHistory[len(memeHistory) - 1])
              await ctx.send(embed=embed, ephemeral=True) #send the last image
              return
      await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])), ephemeral=True)

class Reddit(commands.Cog):
  def __init__(self, client):
    self.client = client


  @slash_commands.command(name="reddit", description="get a random post from any subreddit", options=[Option("subreddit", "A subreddit to get a post from", Type.STRING, required=True)])
  @slash_commands.guild_only()
  async def reddit(self, ctx, subreddit):
    if True:
      url = f"https://reddit.com/r/{subreddit}/random.json?limit=1"
      async with aiohttp.ClientSession() as session:
        async with session.get(f"https://reddit.com/r/{subreddit}/random.json?limit=1") as r:
          res = await r.json()
          s = ""
          subredditDict = dict(res[0]['data']['children'][0]['data'])
          if subredditDict['over_18'] and not ctx.channel.is_nsfw():
              embed = discord.Embed(title="Thats an NSFW subreddit!", description="To get an image from this subreddit, please use this command again in an NSFW channel", color=discord.Color.red())
              await ctx.send(embed=embed)
              return
          embed = discord.Embed(title = f"{subredditDict['title']}", description = f"{subredditDict['subreddit_name_prefixed']}", url =  f"https://reddit.com{subredditDict['permalink']}")
          
          if subredditDict['selftext'] != "":
              embed.add_field(name = "Post Content:", value = subredditDict['selftext'])
          if subredditDict['url'] != "":
              embed.set_image(url = subredditDict['url'])
          embed.set_footer(text=f"🔺 {subredditDict['ups']} | u/{subredditDict['author']}")
          if subredditDict['selftext'] != "&amp;#x200B;":
                await ctx.send(embed = embed)
          else:
                await ctx.send("Annoying error with reddit being stupid. Try again lmao", ephemeral=True)
    else:
      try: 
        return await ctx.send("_{}! ({})_".format(str(subredditDict['message']), str(subredditDict['error'])))
      except:
        return await ctx.send("Error", ephemeral=True)



  @slash_commands.command(description="Get a meme from a random meme subreddit")
  @slash_commands.guild_only()
  async def meme(self, ctx):
    """Memes from various subreddits"""
    if True:
        await getSub(self, ctx, choice(memeSubreddits))
    else:
        async with aiohttp.ClientSession() as session:
          async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=450".format(random.choice(memeSubreddits))) as response:
              request = await response.json()

        attempts = 1
        while attempts < 5:
          if 'error' in request:
              print("failed request {}".format(attempts))
              await asyncio.sleep(2)
              async with aiohttp.ClientSession() as session:
                  async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=450".format(random.choice(memeSubreddits))) as response:
                      request = await response.json()
              attempts += 1
          else:
              index = 0

              for index, val in enumerate(request['data']['children']):
                  if 'url' in val['data']:
                      url = val['data']['url']
                      urlLower = url.lower()
                      accepted = False
                      for j, v, in enumerate(acceptableImageFormats): 
                          if v in urlLower:
                              accepted = True
                      if accepted:
                          if url not in memeHistory:
                              memeHistory.append(url)  
                              if len(memeHistory) > 500: 
                                  memeHistory.popleft() 

                              break 
              embed = discord.Embed(title=f"Meme",color=ctx.author.color)
              embed.set_image(url=memeHistory[len(memeHistory) - 1])
              await ctx.send(embed=embed, ephemeral=True)
              return
        await ctx.send(url="_{}! ({})_".format(str(request['message']), str(request['error'])), ephemeral=True)
        

    

                 
def setup(client):
  client.add_cog(Reddit(client))
