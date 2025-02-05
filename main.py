import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

bot = commands.Bot("!", test_guilds=[1336046980908191805])

@bot.event
async def on_ready():
    print("Bot enabled")

bot.load_extensions("modules")
load_dotenv('secrets.env')
bot.run(os.environ["BOT_TOKEN"])