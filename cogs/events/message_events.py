import discord
from discord.ext import commands

class Message_events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        content = message.content.lower()
        if "pinto" in content:
            await message.add_reaction("🍆")
        
async def setup(bot):
    await bot.add_cog(Message_events(bot))