import discord
from discord.ext import commands

import pyfiglet

class Fun_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Comando para Artes ASCII 
    @commands.command(name="ascii")
    async def transform_ascii(self, ctx, Font: str = "standard", *, Text: str):  
        
        try:
            result = pyfiglet.figlet_format(Text, font=Font)
        except:
            await ctx.send(f"Fonte '{Font}' não existe! Usando padrão.")
            result = pyfiglet.figlet_format(Text, font="standard")

        # Envia o arquivo se o resultado for muito grande
        if len(result) > 1990:
            await ctx.send("Resultado Grande Demais, Enviando o Arquivo...")
            with open("ascii.txt", "w", encoding="utf8") as f:
                f.write(result)
            await ctx.send(file=discord.File("ascii.txt"))

        else:
            await ctx.send(f"```\n{result}\n```")

async def setup(bot):
    await bot.add_cog(Fun_Commands(bot))