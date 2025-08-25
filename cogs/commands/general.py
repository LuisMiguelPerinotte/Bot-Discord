import discord
from discord.ext import commands
from logs_generator import registrar_uso_comando

class General(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

# Comando Info do Server
    @commands.command(name="info")
    async def server_info(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            title=f"📊 Informações de {guild.name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="👥 Membros", value=guild.member_count, inline=True)
        embed.add_field(name="📅 Criado em", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="👑 Dono", value=guild.owner.mention, inline=True)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await ctx.reply(embed=embed)
        
        registrar_uso_comando(f"{ctx.author} usou comando !info.")

# Comando Ping para ver a latencia do bot    
    @commands.command(name="ping")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title=" 🏓 Pong!",
            description=f"Latência: {latency}ms",
            color=discord.Color.green()
        )
        await ctx.reply(embed=embed)

        registrar_uso_comando(f"{ctx.author} usou comando !ping. ")
def setup(bot):
    bot.add_cog(General(bot))