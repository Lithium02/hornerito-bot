# requirements decouple, discord, bs4, requests, selenium, #google-search-results(serp_api)
# Dependencies imports
from decouple import config
import discord
# Local scripts
import wikiscraper
import youtubescraper

token = config('TOKEN')

wiki_web = wikiscraper.WikiWeb()
yt_web = youtubescraper.YoutubeWeb()

no_result_message = '''Sorry, we can\'t find what you are searching for.'''

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    message_content = message.content.lower()  
    
    # if message.content.startswith('$hello'):
    #     await message.channel.send('world!')
    if message.content.startswith('$definition'):
        await message.channel.send('definition')
        
    if f'$wiki' in message_content:
        key_words, search_words = wiki_web.key_words_search_words(message_content)
        result = wiki_web.search(key_words)
        await message.channel.send(result.text)
    if f'$tutorial' in message_content:
        key_words, search_words = yt_web.key_words_search_words(message_content)
        results = yt_web.get_video_results(key_words)
        
        await message.channel.send(results[0]+' \n'+results[1]+'\n'+results[2])

client.run(token)
