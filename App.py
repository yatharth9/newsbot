import discord
import os

links = ["https://www.wired.com/feed/category/gear/latest/rss",
         "https://www.theverge.com/rss/index.xml",
         "https://www.techmeme.com/feed.xml",
         "https://techcrunch.com/tag/rss/",
         "https://www.pcworld.com/index.rss",
         "https://www.engadget.com/rss.xml",
         "https://www.digitaltrends.com/computing/feed/",
         "https://www.cnet.com/rss/news/"]

client = discord.Client()
bot_token = os.getenv("newsbot")

@client.event
async def startup():
    print(f"News bot online ")

