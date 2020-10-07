import discord
from discord.ext import commands
import requests


def embedCreator(data):
    """
        Creates the embedded message for the covid-19 stats
    """
    state = data["state"]
    embedTitle = ":world_map: Covid Stats in " + state + " :world_map:"
    firstField = {
        "name": "Total " + state + " Cases",
        "value": "Total Cases: {:,}".format(data["cases"]),
        "inline": True
    }
    secondField = {
        "name": "Total " + state + " Deaths",
        "value": "Total Deaths: {:,}".format(data["deaths"]),
        "inline": True
    }
    thirdField = {
        "name": "Total " + state + " Tests",
        "value": "Total Tests: {:,}".format(data["tests"]),
        "inline": True
    }
    embed = discord.Embed(title=embedTitle, color=0x8D0000)
    embed.description = "Statistics for Covid-19 in " + state + "\n"
    embed.add_field(
        name=firstField["name"], value=firstField["value"], inline=firstField["inline"])
    embed.add_field(
        name=secondField["name"], value=secondField["value"], inline=secondField["inline"])
    embed.add_field(
        name=thirdField["name"], value=thirdField["value"], inline=thirdField["inline"])
    embed.set_footer(text="Data from corona.lmao.ninja")

    return embed


class CovidCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx):
        """
        Requests data from corona.lmao.ninja and parses it based on the users
        inputted state
        """
        r = requests.get("https://corona.lmao.ninja/v2/states")
        apidata = r.json()
        state = ctx.message.content[7:].title()
        returningData = {}
        for stateData in apidata:
            if stateData["state"] == state:
                returningData = stateData
        if returningData != {}:
            await ctx.send(embed=embedCreator(returningData))
            print(returningData)
        else:
            await ctx.send("State not found")


def setup(bot):
    bot.add_cog(CovidCog(bot))
