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
        if "sage" in content:
            await message.add_reaction("😶‍🌫️")

async def setup(bot):
    await bot.add_cog(Message_events(bot))