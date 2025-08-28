import discord
from discord.ext import commands
from logs_generator import registrar_uso_comando

import pyfiglet

class Fun_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Comando para Artes ASCII 
    @commands.command(name="ascii")
    async def transform_ascii(self, ctx, Font: str, *, text: str):  
        
        try:
            result = pyfiglet.figlet_format(text, font=Font.lower())

        except pyfiglet.FontNotFound:
            await ctx.reply(f"Fonte '{Font}' não existe! Usando padrão.")
            result = pyfiglet.figlet_format(text, font="standard")

        registrar_uso_comando(f"{ctx.author} usou comando !ascii. fonte: '{Font}', texto: '{text}'")

        # Envia o arquivo se o resultado for muito grande
        if len(result) > 1990:
            await ctx.reply(f"{ctx.author.mention} Resultado Grande Demais, Enviando o Arquivo...")
            with open("ascii.txt", "w", encoding="utf8") as f:
                f.write(result)
            await ctx.reply(file=discord.File("ascii.txt"))

        else:
            await ctx.reply(f"{ctx.author.mention}```\n{result}\n```")

    @commands.command(name="ascii-fonts")
    async def asscii_fonts(self, ctx):
        await ctx.reply(ctx.author.mention, embed=discord.Embed(
            title="Ascii Fonts 🧑‍🎨",
            description="- standard\n- slant\n- 3-d\n- 3x5\n- 5lineoblique\n- alphabet\n- banner3-D\n- doh\n- isometric1\n- letters\n- alligator\n- dotmatrix\n- bubble\n- bulbhead\n- digital  ",
            color=discord.Color.blue()
        ))

        registrar_uso_comando(f"{ctx.author} usou comando ascii-fontes")

async def setup(bot):
    await bot.add_cog(Fun_Commands(bot))