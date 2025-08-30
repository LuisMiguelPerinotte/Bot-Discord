async def load_cogs(bot):
    cogs = [
        "cogs.commands.general",
        "cogs.commands.apis_commands",
        "cogs.commands.fun_commands",
        "cogs.events.message_events",
        "cogs.commands.ia_commands"
    ]

    for cog in cogs:
        await bot.load_extension(cog)