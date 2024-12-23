import discord
from discord.ext import commands

with open("token.txt", "r") as file:
    TOKEN = file.read()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

info_msg = "Hello!"

@bot.event
async def on_ready():
    print(f"{bot.user} has been summoned :)")

@bot.command()
async def info(ctx):
    await ctx.channel.purge(limit=2)
    await ctx.send(info_msg)

bot.run(TOKEN)

