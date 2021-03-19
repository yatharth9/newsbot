#import discord
import os
import feedparser
import re
import discord

commandslist = """```py

newsbot.single("Term"): Returns the news feed for the term
newsbot.sources() : Returns the sources currently being resolved```
"""

links = {"wired"          : "https://www.wired.com/feed/category/gear/latest/rss",
         "verge"          : "https://www.theverge.com/rss/index.xml",
         "techmeme"       : "https://www.techmeme.com/feed.xml",
         "techcrunch"     : "https://techcrunch.com/tag/rss/",
         "pc world"       : "https://www.pcworld.com/index.rss",
         "engadget"       : "https://www.engadget.com/rss.xml",
         "digital Trends" : "https://www.digitaltrends.com/computing/feed/",
         "cnet"           : "https://www.cnet.com/rss/news/"}

def list_sources():
    sources =[]
    for x in links:
        sources.append(x)
    return sources

key = links.keys()

#link = links["Verge"]
#print(link)
def parse_single(url):
    renders = []
    try:
        news = feedparser.parse(url)
        for i in range(len(news.entries)):
            #print(f"Title: {news.entries[i].title}\n Link: {news.entries[i].link}")
            renders.append(news.entries[i].title)
            renders.append(news.entries[i].link)
        return renders
    except:
        print(f"Error resolving feed: {url}")

#parse_single(link)

def search_term(message):
    #try:
        match = re.fullmatch('newsbot.single\((["|\'])([^\)]+)(["|\'])\)', message)
        if match.group(1) != match.group(3):
            return False
        for check in re.finditer(match.group(1), match.group(2)):
            if match.group(2)[check.start()-1] != '\\':
                return False
        return match.group(2)
    #except:
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
    
    elif "newsbot.close()" == message.content.lower() and str(message.author).lower() == "yatharth#3059":
        await client.change_presence(status = discord.Status.offline)
        await message.channel.send(f"Bot shutting down after request by {message.author}")
        await client.close()
        print(f"Bot shutting down\n")
    
    elif "newsbot.sources()" == message.content.lower():
        await message.channel.send(f"The sources are: ")
        source = list_sources()
        print(len(source))
        await message.channel.send(f"``` {source}```    ")
    
    else:
        term = search_term(message.content.lower())
        if term in key:
            render = parse_single(links[term])
            if render:
                no = len(render)
                actual_no = no/2
                await message.channel.send(f"{actual_no} news stories incoming")
                for y in render:
                    await message.channel.send(y)
                    print(y)
            else:
                await message.channel.send(f"Unable to fetch news from {term}")
                print("Unable to fetch news from {term}")
        else:
            print("Error in Term finding")
            await message.channel.send(f"Error in finding term from {message.content}")


client.run(bot_token, reconnect=True)
