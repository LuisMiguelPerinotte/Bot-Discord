import discord
from discord.ext import commands
from discord import app_commands
from logs_generator import registrar_uso_comando

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Lista todos os comandos disponíveis")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Comandos Disponíveis",
            color=discord.Color.blue()
        )
        for cog_name, cog in self.bot.cogs.items():
            comandos = []
            for command in cog.get_app_commands():
                comandos.append(f"`/{command.name}` — {command.description}")
            if comandos:
                embed.add_field(
                    name=f"{cog_name}",
                    value="\n".join(comandos),
                    inline=False
                )
        await interaction.response.send_message(embed=embed)
        registrar_uso_comando(f"{interaction.user} usou o comando /help no server {interaction.guild.name}. ")

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))