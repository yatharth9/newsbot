#import discord
import os
import feedparser
import re
import discord

commandslist = """```py

newsbot.single("Term"): Returns the news feed for the term
newsbot.sources() : Returns the sources currently being resolved```
"""

links = {"Wired"          : "https://www.wired.com/feed/category/gear/latest/rss",
         "Verge"          : "https://www.theverge.com/rss/index.xml",
         "Techmeme"       : "https://www.techmeme.com/feed.xml",
         "Techcrunch"     : "https://techcrunch.com/tag/rss/",
         "Pc world"       : "https://www.pcworld.com/index.rss",
         "Engadget"       : "https://www.engadget.com/rss.xml",
         "Digital Trends" : "https://www.digitaltrends.com/computing/feed/",
         "Cnet"           : "https://www.cnet.com/rss/news/"}

def list_sources():
    sources =[]
    for x in links:
        sources.append(x)

link = links["Verge"]
#print(link)
def parse_single(url):
    try:
        news = feedparser.parse(url)
        for i in range(len(news.entries)):
            print(f"Title: {news.entries[i].title}\n Link: {news.entries[i].link}")
    except:
        print(f"Error resolving feed: {url}")

#parse_single(link)

def search_term(message):
    try:
        match = re.fullmatch('newsbot.single\((["|\'])([^\)]+)(["|\'])\)', message)
        if match.group(1) != match.group(3):
            return False
        for check in re.finditer(match.group(1), match.group(2)):
            if match.group(2)[check.start()-1] != '\\':
                return False
        return match.group(2)
    except:
        return False

istr = 'newsbot.single("Hello")'

search_term(message=istr)
intents = discord.Intents.default()

client = discord.Client(intents=intents)
bot_token = os.getenv("newsbot")

@client.event
async def on_ready():
    print(f"News bot online ")
    await client.change_presence(status = discord.Status.online, activity = discord.Game('help(newsbot)'))

@client.event
async def on_message(message):
    if "help(newsbot)" == message.content.lower() or "newsbot.commands()" == message.content.lower():
        await message.channel.send(commandslist)
    
    elif "newsbot.close()" == message.content.lower:
        await client.close()
        print(f"Bot shutting down\n")

client.run(bot_token, reconnect=True)