import os
import discord
from dotenv import load_dotenv
from gpt import GptUtil

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

GPT_TOKEN = os.getenv('GPT_TOKEN')
gpt: GptUtil = GptUtil(GPT_TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # We don't want to react to our bot's own messages
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content == 'hey':
        await message.channel.send(gpt.ask_question('whats 2 + 2'))

client.run(DISCORD_TOKEN)
