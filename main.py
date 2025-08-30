import discord
from discord.ext import commands
import asyncio
from cogs_loader import load_cogs

from dotenv import load_dotenv
import os

# Colorama (corzinha nas letras :) 
from colorama import init, Fore, Style
init()

# Carregar Key 
load_dotenv()
api_key = os.getenv("DISCORD_KEY") 

# Definir Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Cria o bot
bot = commands.Bot(command_prefix="!", intents=intents)     

# Informações para o terminal
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"🤖 {bot.user} está {Fore.GREEN}online!{Style.RESET_ALL}")
    print(f"📊 Conectado a {len(bot.guilds)} servidores")
    
# Fução principal para exucutar o Bot    
async def main():
    async with bot:
        await load_cogs(bot)
        await bot.start(api_key)

if __name__ == "__main__":
    asyncio.run(main())