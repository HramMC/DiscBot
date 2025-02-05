import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

bot = commands.InteractionBot()

@bot.event
async def on_ready():
    print("Bot enabled")

bot.load_extensions("modules")
load_dotenv('secrets.env')
bot.run(os.environ["BOT_TOKEN"])