import discord
from discord.ext import commands
from discord import app_commands
from logs_generator import registrar_uso_comando

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Comando Info do Server
    @app_commands.command(name="info", description="Exibe as informações do Server")
    async def server_info(self,interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title=f"📊 Informações de {guild.name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="👥 Membros", value=guild.member_count, inline=True)
        embed.add_field(name="📅 Criado em", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="👑 Dono", value=guild.owner.mention, inline=True)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await interaction.response.send_message(embed=embed)
        
        registrar_uso_comando(f"{interaction.user} usou o comando /info no server {interaction.guild.name}.")

# Comando Ping para ver a latencia do bot    
    @app_commands.command(name="ping", description="Exibe a latencia do Bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title=" 🏓 Pong!",
            description=f"Latência: {latency}ms",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

        registrar_uso_comando(f"{interaction.user} usou o comando /ping no server {interaction.guild.name}. ")


async def setup(bot):
    await bot.add_cog(General(bot))