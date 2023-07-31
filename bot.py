import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

discordtoken = os.getenv("discordtoken")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


bot.command()
async def subtract(ctx, num1: int, num2: int):
    result = num1 - num2
    await ctx.send(f'The result of {num1} - {num2} is {result}')

bot.run(discordtoken)