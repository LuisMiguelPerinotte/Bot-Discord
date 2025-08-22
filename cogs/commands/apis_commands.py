import discord
from discord.ext import commands
import requests

import os
from dotenv import load_dotenv
load_dotenv()

class Apis_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.key_weather = os.getenv("HGWEATHER_API_KEY")

# Comando para ver o tempo da cidade escolhida (APENAS BRASIL)
    @commands.command(name="weather")
    async def weather(self, ctx, *, city_name):
        base_url = "https://api.hgbrasil.com/weather"
        url = f"{base_url}?key={self.key_weather}&city_name={city_name}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                dados = response.json()
                resultados = dados.get("results", {})

                if resultados:
                    cidade_retornada = resultados.get("city")
                    temperatura = resultados.get('temp')
                    descricao = resultados.get('description')
                    umidade = resultados.get('humidity')
                    velocidade_vento = resultados.get('wind_speedy')
                    
                    await ctx.send(f"Tempo em {cidade_retornada}🏙️:\n - Condição: {descricao}\n - Temperatura: {temperatura}°C\n - Umidade: {umidade}%\n - Vento: {velocidade_vento}")
                
                else:
                    await ctx.send(f"Erro Ao Buscar Dados. Tente Novamente Mais Tarde!")

        except requests.exceptions.RequestException as e:
            await ctx.send(f"Erro de conexão: {e}")

# Comando para traduzir o texto enviado
    @commands.command(name="translate")
    async def translator(self, ctx, language: str, *, text: str):
        url = "https://api.mymemory.translated.net/get"
        params = {
            "q": text,
            "langpair": f"pt|{language}"
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                resposta = data["responseData"]["translatedText"]

                if resposta:
                    await ctx.send(f"Tradução: {resposta}")
            
                else: 
                    await ctx.send("ERRO! Algo Inesperado Aconteceu ")

        except requests.exceptions.RequestException as e:
            await ctx.send(f"Erro de conexão: {e}")

async def setup(bot):
    await bot.add_cog(Apis_Commands(bot))