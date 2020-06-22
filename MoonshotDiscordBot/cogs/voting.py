import discord
from discord.ext import commands
import asyncio
import yaml
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from collections import Counter


import urllib.request


from cogs.utils.embed import GenerateEmbed
from cogs.utils.config_utils import GetCommandConfig
from cogs.utils.misc import Random

class Voting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        with open("config.yml", 'r') as stream:
            self.conf = yaml.safe_load(stream)

    @commands.command(name="leaderboard")
    async def _leaderboard(self, ctx, length: int = 5):
        """ Checks leaderboard """

        await ctx.send("Scraping the moonshot website, please wait...")
        
        moonshot = 'https://app.moonshotpirates.com/bootcamps/previews/srZ7X8Z8oIVU0FsG/voting'

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get(moonshot)
        page = driver.page_source.encode("utf-8")
        soup = BeautifulSoup(page, 'html.parser')
        teams = soup.find_all("div", {'class': 'team-card-size'})

        teams_votes = {}

        for team in teams:
            # Get name
            name_div = team.find("div", {'class': 'break-words'})
            name_start, name_end = name_div.find_all("span")
            name = (name_start.text + name_end.text).replace("\xa0", " ")
            if name[-1] == " ":
                name = name[:-1]

            # Get votes
            votes_div = team.find("div", {'class': 'my-auto'})
            votes = votes_div.text

            teams_votes[name] = int(votes)

        

        if length > 10:
            length = 10
  
        c = Counter(teams_votes) 

        # Finding 3 highest values 
        high = c.most_common(length)

        embed = GenerateEmbed(ctx, "Leaderboard: Top " + str(length), "Beapirate voting leaderboards!", 0xC0D678)
        embed.set_thumbnail(url="https://i.imgur.com/fBXOfQ9.png")

        k = 0
        for team in high:
            k+=1
            embed.add_field(name=str(k) + ": " + team[0], value=str(team[1]) + " votes!", inline=False)

        await ctx.send(embed=embed)
        

    @commands.Cog.listener()
    async def on_message(self, msg):
        ctx = await self.bot.get_context(msg)