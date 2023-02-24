import discord
import logging
import os
from botconfigs.config import *
from discord.ext import commands

token = os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# discord logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log',
    encoding='utf-8',
    mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print(f'Awaiting commands...')

@client.event
async def on_message(message):

    # ignore bot messages including self
    if message.author == client.user or message.author.bot:
        return

    msg = message.content.lower()
    author = message.author
    author_id = message.author.id

    print(f'Message from {message.author}: {message.content}')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    await client.process_commands(message)

# display bot statistics
@client.command()
async def stats(ctx):

    # only allow commands in bot-commands channel
    if ctx.channel.name != 'bot-commands':
        return
    
    embed = discord.Embed(
        title='Pega Bot Statistics',
        description='\u1CBC\u1CBC',
        url=f'https://discord.com/users/{client.user.id}',
        color=0x34eb77)

    embed.set_author(
        name='Pega Bot',
        icon_url=client.user.avatar)

    print('Showing bot statistics...')
    for key, value in BOT_STATS.items():
        if key == 'Bot Developers':
            dev = await client.fetch_user(int(value['discordId']))
            value = f'<@{value["discordId"]}> {dev.name}#{dev.discriminator}'
        
        if key == 'Discord.py Version':
            value = f'{discord.version_info[0]}.{discord.version_info[1]}.{discord.version_info[2]}'
        
        embed.add_field(
            name=key,
            value=value
        )
    
    embed.set_footer(text=' ')

    await ctx.send(content=None, embed=embed)

@client.command()
async def test(ctx):
    print('fuck')
    
client.run(token)
