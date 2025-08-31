import discord
from discord.ext import commands
from discord import app_commands

import requests
from logs_generator import registrar_uso_comando
from langdetect import detect
import os

class Other_Apis_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.key_weather = os.getenv("HGWEATHER_API_KEY")
        self.key_ia = os.getenv("OPENROUTER_API_KEY")

# Comando para ver o tempo da cidade escolhida (APENAS BRASIL)
    @app_commands.command(name="weather", description="Ver o tempo em outra cidade. (Apenas Brasil)")
    @app_commands.describe(city_name="A cidade para ver o tempo")
    async def weather(self, interaction: discord.Interaction, city_name: str):
        base_url = "https://api.hgbrasil.com/weather"
        url = f"{base_url}?key={self.key_weather}&city_name={city_name}"

        try:
            await interaction.response.defer()

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
                    
                    await interaction.followup.send(embed=discord.Embed(
                        description=f"Tempo em {cidade_retornada}🏙️:\n - Condição: {descricao}\n - Temperatura: {temperatura}°C\n - Umidade: {umidade}%\n - Vento: {velocidade_vento}",
                        color=discord.Color.blue()
                    ))
                    registrar_uso_comando(f"{interaction.user} uso o comando /weather no server: {interaction.guild.name}. city name: {city_name}")
                    
                else:
                    await interaction.followup.send(f"Erro Ao Buscar Dados. Tente Novamente Mais Tarde!")

        except requests.exceptions.RequestException as e:
            await interaction.followup.send(f"Erro de conexão: {e}")


# Comando para traduzir o texto enviado
    @app_commands.command(name="translator", description="Traduza o seu texto para a lingua de sua escolha")
    @app_commands.describe(language="Para qual lingua traduzir", text="O texto a ser traduzido")
    @app_commands.choices(language=[
        app_commands.Choice(name="Inglês", value="en"),
        app_commands.Choice(name="Espanhol", value="es"),
        app_commands.Choice(name="Português", value="pt"),
        app_commands.Choice(name="Francês", value="fr"),
        app_commands.Choice(name="Alemão", value="de"),
        app_commands.Choice(name="Italiano", value="it"),
        app_commands.Choice(name="Russo", value="ru"),
        app_commands.Choice(name="Chinês (Simplificado)", value="zh-CN"),
        app_commands.Choice(name="Japonês", value="ja"),
        app_commands.Choice(name="Coreano", value="ko"),
        app_commands.Choice(name="Árabe", value="ar"),
        app_commands.Choice(name="Hindi", value="hi"),
        app_commands.Choice(name="Bengali", value="bn"),
        app_commands.Choice(name="Urdu", value="ur"),
        app_commands.Choice(name="Turco", value="tr")
    ])
    async def translator(self, interaction: discord.Interaction, language: str, *, text: str):
        url = "https://api.mymemory.translated.net/get"
        idioma_origem = detect(text)

        params = {
            "q": text.lower(),
            "langpair": f"{idioma_origem}|{language}"
        }
        try:
            await interaction.response.defer()

            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                resposta = data["responseData"]["translatedText"]

                if resposta:
                    await interaction.followup.send( embed=discord.Embed(
                        description=f"Tradução: {resposta}",
                        color=discord.Color.blue()
                    ))

                    registrar_uso_comando(f"{interaction.user} usou o comando /translate no server {interaction.guild.name}. lingua: '{language}', texto: '{text}'")
            
                else: 
                    await interaction.followup.send("ERRO! Algo Inesperado Aconteceu ")

        except requests.exceptions.RequestException as e:
            await interaction.followup.send(f"Erro de conexão: {e}")
        

# Comando Busca no Wikipedia
    @app_commands.command(name="wikipedia", description="Faz uma breve pesquisa na wikipedia sobre o assunto de sua escolha")
    @app_commands.describe(text="Assunto para a pesquisa")
    async def wikipedia(self, interaction: discord.Interaction, *, text: str):
        url = "https://pt.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "format": "json",
            "titles": text
        }
        headers = {
            "User-Agent": "BotDiscord/1.0"
        }

        try:
            await interaction.response.defer()

            response = requests.get(url, params=params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                pages = data["query"]["pages"]
                page_id = next(iter(pages))
                resultado = pages[page_id]["extract"]

                if resultado:
                    await interaction.followup.send(embed=discord.Embed(
                        description=resultado,
                        color=discord.Color.blue()
                    ))
                    registrar_uso_comando(f"{interaction.user} usou o comando /wikipedia no server {interaction.guild.name}. Assunto: {text}")

                else:
                    await interaction.followup.send(f"Erro ao Buscar Dados. Tente Novamente mais tarde!")
            else:
                await interaction.followup.send(f"Erro na Requisição! Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            await interaction.followup.send(f"Erro de conexão: {e}")


async def setup(bot):
    await bot.add_cog(Other_Apis_Commands(bot))