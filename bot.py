import discord
import time
from discord.ext import commands
import os
from dotenv import load_dotenv

"""Main bot class"""
class TicketBot(commands.Bot):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)


# Initialization
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = TicketBot(command_prefix='=', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0} ms'.format(round(bot.latency, 3) * 1000))

if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))
