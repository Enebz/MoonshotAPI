import discord
from discord.ext import commands

import random

Colors = {
    "red": 0xff0000,
    "blue": 0x00ff00,
    "green": 0x0000ff
}

def GenerateEmbed(ctx, Title = None, Description = None, Color = None):
    if Color == "RANDOM":
        Color = random.randint(0, 0xffffff)
    elif Color in Colors:
        Color = Colors[Color]
    embed = discord.Embed(title=Title, description = Description, color = Color)
    return embed


