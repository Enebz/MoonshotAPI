import random
import discord

def Random(ctx, n1, n2, exceptions: dict = {1}, arg = None):
    try:
        if arg:
            DiscordMember = discord.utils.get(ctx.guild.members, name=arg)
            if DiscordMember.id in exceptions:
                return exceptions[DiscordMember.id]
        else:
            if ctx.author.id in exceptions:
                return exceptions[ctx.author.id]
    except:
        pass

    return random.randint(n1, n2)