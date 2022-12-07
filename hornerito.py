# requirements decouple, discord, bs4, requests, selenium, #pymongo
# Dependencies imports
from decouple import config
import discord
from discord.ext import commands
# Local scripts
import wikiscraper
import youtubescraper
token = config('TOKEN')


wiki_web = wikiscraper.WikiWeb()
yt_web = youtubescraper.YoutubeWeb()

no_result_message = '''Lo siento, no puedo encontrar lo que estas buscando :('''

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def wiki(ctx, message: str):
    key_words, search_words = wiki_web.key_words_search_words(message)
    result = wiki_web.search(key_words)
    await ctx.send(result.text)
@bot.command()
async def yt(ctx, message: str):
    key_words, search_words = yt_web.key_words_search_words(message)
    results = yt_web.get_video_results(key_words)
    await ctx.send("Estos son algunos resultados encontrados relacionado a tu busqueda: \n"+results[0]+' \n'+results[1]+'\n'+results[2])

bot.run(token)
