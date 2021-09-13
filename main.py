from discord.ext import commands
import discord
import requests
from dotenv import load_dotenv
import os
from pycenter import center
import nitrologo

load_dotenv("data/token.env")
bot = commands.Bot(command_prefix='!', self_bot=True)
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
	nitrologo.nitrologo()
	print(center("Bot is Online"))
	print(center(f"{bot.user.name}#{bot.user.discriminator}"))

@bot.event
async def on_message(message):
      if message.content.startswith("discord.gift/"):
         codevariable = message.content.split("discord.gift/")[1]
         redeemheaders = {'Authorization': TOKEN, 'content-type': 'application/json', 'payment_source_id': 'null'}
         r = requests.post('https://ptb.discordapp.com/api/v6/entitlements/gift-codes/'+ codevariable + '/redeem', headers=redeemheaders)
         r = r.json()
         data = ""
         print(f"GIFT FOUND ! {codevariable}")
         data = open('data/discordgifts.txt').read()
         with open('data/discordgifts.txt', 'w') as f:
             f.write(data+f"discord.gg/{codevariable}\n")



bot.run(TOKEN, bot=False)