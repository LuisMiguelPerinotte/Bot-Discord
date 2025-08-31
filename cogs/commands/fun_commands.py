import discord
from discord.ext import commands
from discord import app_commands
from logs_generator import registrar_uso_comando

import pyfiglet

class Fun_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando para Artes ASCII 
    @app_commands.command(name="ascii", description="Arte ASCII com o texto de sua escolha")
    @app_commands.describe(
        font="Fonte para que o texto vai ser transformado",
        text="Texto que vai ser transformado"
    )
    @app_commands.choices(font=[
        app_commands.Choice(name="standard", value="standard"),
        app_commands.Choice(name="slant", value="slant"),
        app_commands.Choice(name="3-d", value="3-d"),
        app_commands.Choice(name="3x5", value="3x5"),
        app_commands.Choice(name="5lineoblique", value="5lineoblique"),
        app_commands.Choice(name="alphabet", value="alphabet"),
        app_commands.Choice(name="3d_diagonal", value="3d_diagonal"),
        app_commands.Choice(name="doh", value="doh"),
        app_commands.Choice(name="isometric1", value="isometric1"),
        app_commands.Choice(name="letters", value="letters"),
        app_commands.Choice(name="alligator", value="alligator"),
        app_commands.Choice(name="dotmatrix", value="dotmatrix"),
        app_commands.Choice(name="bubble", value="bubble"),
        app_commands.Choice(name="bulbhead", value="bulbhead"),
        app_commands.Choice(name="digital", value="digital")
    ])
    async def transform_ascii(self, interaction: discord.Interaction, font: str, *, text: str):  
        try:
            await interaction.response.defer()

            result = pyfiglet.figlet_format(text, font=font.lower())

        except pyfiglet.FontNotFound:
            await interaction.followup.send(f"Fonte '{font}' não existe! Usando padrão.")
            result = pyfiglet.figlet_format(text, font="standard")

        registrar_uso_comando(f"{interaction.user} usou o comando /ascii no server {interaction.guild.name}. fonte: '{font}', texto: '{text}'")

        
        if len(result) > 1990:
            await interaction.followup.send(f"Resultado Grande Demais, Enviando o Arquivo...")
            with open("ascii.txt", "w", encoding="utf8") as f:
                f.write(result)
            await interaction.followup.send(file=discord.File("ascii.txt"))

        else:
            await interaction.followup.send(f"```\n{result}\n```")

async def setup(bot):
    await bot.add_cog(Fun_Commands(bot))