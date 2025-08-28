import discord
from discord.ext import commands
import asyncio

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

# Carrega os cogs
async def load_cogs():
    cogs = [
        "cogs.commands.general",
        "cogs.commands.apis_commands",
        "cogs.commands.fun_commands",
        "cogs.events.message_events"
    ]

    for cog in cogs:
        await bot.load_extension(cog)
        
# Fução principal para exucutar o Bot    
async def main():
    async with bot:
        await load_cogs()
        await bot.start(api_key)

if __name__ == "__main__":
    asyncio.run(main())