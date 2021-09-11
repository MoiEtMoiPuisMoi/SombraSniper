from discord.ext import commands
import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv("data/token.env")
bot = commands.Bot(command_prefix='!', self_bot=True)
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():

    print(pycenter.center(nitrologo))
    print(f'Bot is Online')
    print(f'{bot.user.name}#{bot.user.discriminator}')

@bot.event
async def on_message(message):
      if message.content.startswith("discord.gift/"):
         codevariable = message.content.split("discord.gift/")[1]
         redeemheaders = {'Authorization': TOKEN, 'content-type': 'application/json', 'payment_source_id': 'null'}
         r = requests.post('https://ptb.discordapp.com/api/v6/entitlements/gift-codes/'+ codevariable + '/redeem', headers=redeemheaders)
         r = r.json()
         print(f"GIFT FOUND ! {codevariable}")
         with open('data/discordgifts.txt') as f:
             f.write(f"discord.gg/{codevariable}\n")



bot.run(TOKEN, bot=False)