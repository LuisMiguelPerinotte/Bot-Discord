import discord
from discord.ext import commands
import asyncio

from dotenv import load_dotenv
import os

# Carregar Key 
load_dotenv()
api_key = os.getenv("key") 


# Definir Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Cria o bot
bot = commands.Bot(command_prefix="!", intents=intents)     

async def on_ready():
    print(f"{bot.user} está online!")
    print(f"Conectado a {len(bot.guilds)} servidores")

# Carrega os cogs
async def load_cogs():
    await bot.load_extension("cogs.commands.general")
    await bot.load_extension("cogs.events.message_events")

# Fução principal para exucutar o Bot    
async def main():
    async with bot:
        await load_cogs()
        await bot.start(api_key)

if __name__ == "__main__":
    asyncio.run(main())
