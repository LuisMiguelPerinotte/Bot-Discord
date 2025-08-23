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
        self.key_ia = os.getenv("OPENROUTER_API_KEY")

# Comando para ver o tempo da cidade escolhida (APENAS BRASIL)
    @commands.command(name="weather")
    async def weather(self, ctx, *, city_name: str):
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
                    
                    await ctx.send(ctx.author.mention, embed=discord.Embed(
                        description=f"Tempo em {cidade_retornada}🏙️:\n - Condição: {descricao}\n - Temperatura: {temperatura}°C\n - Umidade: {umidade}%\n - Vento: {velocidade_vento}",
                        color=discord.Color.blue()
                    ))
                    
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
                    await ctx.send(ctx.author.mention, embed=discord.Embed(
                        description=f"Tradução: {resposta}",
                        color=discord.Color.blue()
                    ))
            
                else: 
                    await ctx.send("ERRO! Algo Inesperado Aconteceu ")

        except requests.exceptions.RequestException as e:
            await ctx.send(f"Erro de conexão: {e}")

# Respostas usando ia para o bot
    @commands.command(name="ia")
    async def chat_ia(self, ctx, *, text: str):
            try:
                await ctx.send(embed=discord.Embed(
                    description="Pensando...🤓☝️",
                    color=discord.Color.blue()
                ))
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"bearer {self.key_ia}",
                        "Content-Type": "application/json"
                    },
                    json=({
                        "model": "google/gemma-3n-e4b-it:free",
                        "messages": [
                            {
                                "role": "user",
                                "content": text
                            }
                        ]
                    })
                )
                if response.status_code == 200:
                    data = response.json()
                    resposta = data["choices"][0]["message"]["content"]

                    if resposta:
                        await ctx.send(ctx.author.mention, embed=discord.Embed(
                            description=f"Sua Resposta Gerada Por IA:\n\n{resposta}",
                            color=discord.Color.blue()
                        ))

                    else: 
                        await ctx.send("ERRO! Algo Inesperado Aconteceu ")
                else:
                    await ctx.send(f"Erro na requisição! Status code: {response.status_code}")

            except requests.exceptions.RequestException as e:
                await ctx.send(f"Erro de conexão: {e}")


def setup(bot):
    bot.add_cog(Apis_Commands(bot))