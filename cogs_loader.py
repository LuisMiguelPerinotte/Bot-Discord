# Função para Carregar os cogs
async def load_cogs(bot):
    cogs = [
        "cogs.commands.general",
        "cogs.commands.apis_commands",
        "cogs.commands.fun_commands",
        "cogs.events.message_events",
        "cogs.commands.ia_commands",
        "cogs.commands.command_help"
    ]

    for cog in cogs:
        await bot.load_extension(cog)