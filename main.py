from configuration import config
import discord
from discord.ext import commands

#Initialize bot with prefix '!'
bot = commands.Bot(command_prefix='!', help_command=None)

#Load extensions from cogs folder
bot.load_extension("cogs.testcog")
bot.load_extension("cogs.apicog")

#Run the bot using the token in config.json
bot.run(config["botToken"])