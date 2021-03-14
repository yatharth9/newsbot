#import discord
import os
import feedparser

links = {"Wired"          : "https://www.wired.com/feed/category/gear/latest/rss",
         "Verge"      : "https://www.theverge.com/rss/index.xml",
         "Techmeme"       : "https://www.techmeme.com/feed.xml",
         "Techcrunch"     : "https://techcrunch.com/tag/rss/",
         "Pc world"       : "https://www.pcworld.com/index.rss",
         "Engadget"       : "https://www.engadget.com/rss.xml",
         "Digital Trends" : "https://www.digitaltrends.com/computing/feed/",
         "Cnet"           : "https://www.cnet.com/rss/news/"}

def list_sources():
    print("The Sources are ")
    for x in links:
        print(x)

link = links["Verge"]
print(link)
def parse_single(url):
    news = feedparser.parse(link)
    for i in range(len(news.entries)):
        print(f"Title: {news.entries[i].title}\n Link: {news.entries[i].link}")

parse_single(link)
"""
client = discord.Client()
bot_token = os.getenv("newsbot")

@client.event
async def startup():
    print(f"News bot online ")
"""