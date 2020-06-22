import discord
import time

async def Ping(ctx, message):
    StartingTime = time.time()
    if type(message) == discord.Embed:
        EditThis = await ctx.send(embed=message)
    else:
        EditThis = await ctx.send(message)
    EndingTime = time.time()
    Timespan = str(round((EndingTime - StartingTime)*1000))
    return Timespan, EditThis