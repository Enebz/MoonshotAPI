import discord
from discord.ext import commands as cmd
import asyncio
import yaml
import random

import cogs.voting

TOKEN = 'NzI0NjU4MDUwMDk4NjU5NDMw.XvDYxw.xCIy98zDs7xthKZhYHDSPLlQJdc'

bot = cmd.Bot(command_prefix='!', case_insensitive=True)

with open("config.yml", 'r') as stream:
    config = yaml.safe_load(stream)

@bot.event
async def on_ready():
    
    bot.add_cog(cogs.voting.Voting(bot))
    print("Loaded Cog: Voting")
    print("Active!")

bot.run(TOKEN)