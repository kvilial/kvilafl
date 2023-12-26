import discord
from discord.ext import commands

TOKEN = 'MTE4ODA5NTIwNjUyOTE5MjAxNw.GurDF1.6WR0KYMSdc3PttmSO4RtGh1gNosdxB-rz2Zr7E'

intents = discord.Intents.default()  # Используем стандартные намерения
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run(TOKEN)
