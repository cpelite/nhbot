import discord
import os 
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot(debug_guilds=[931187178980126780])

@bot.event 
async def on_ready():
    print(f"{bot.user} ist online und bereit!")

@bot.slash_command(name = "ready", description = "Zeigt an ob der Bot einsatzbereit ist.")
async def ready(ctx):
    await ctx.respond("Bot online, warte auf Befehle!")

bot.load_extension('cogs.comms')
bot.load_extension('cogs.gifs')
bot.run(os.getenv('TOKEN'))
