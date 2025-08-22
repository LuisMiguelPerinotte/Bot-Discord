import discord
from discord.ext import commands
import asyncio

from dotenv import load_dotenv
import os

# Carregar Key 
load_dotenv()
api_key = os.getenv("Discord_API_Key") 

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
    sincs = await bot.tree.sync()
    print(f"{bot.user} está online!")
    print(f"{len(sincs)} comandos sincronizados!")
    print(f"Conectado a {len(bot.guilds)} servidores")

# Carrega os cogs
async def load_cogs():
    await bot.load_extension("cogs.commands.general")
    await bot.load_extension("cogs.commands.apis_commands")
    await bot.load_extension("cogs.commands.fun_commands")

    await bot.load_extension("cogs.events.message_events")

# Função slash teste
@bot.tree.command()
async def diga_ola(interact:discord.Interaction):
    await interact.response.send_message(f"Olá, {interact.user.mention}!")

# Fução principal para exucutar o Bot    
async def main():
    async with bot:
        await load_cogs()
        await bot.start(api_key)

if __name__ == "__main__":
    asyncio.run(main())
