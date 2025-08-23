import discord
from discord.ext import commands

class Message_events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

# Evento reação em mensagens especificas 
    @commands.Cog.listener()
    async def on_message_reaction(self, message):
        if message.author.bot:
            return
        
        content = message.content.lower()
        if "pinto" in content:
            await message.add_reaction("🍆")

# Evento Boas-vindas
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel("https://discord.com/channels/1006871049251594340/1407833723763822672")

        if channel:
            embed = discord.Embed(
                title="Bem Vindo(a) 🎉",
                description=f"Olá {member.mention}, seja bem-vindo(a) ao servidor!",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar.url)  
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Message_events(bot))