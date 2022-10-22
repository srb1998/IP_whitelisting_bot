from email import message
from tkinter import HIDDEN
import discord
import os
import requests
import json
import re
import asyncio
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# Validating IPv4 Address
regex = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@bot.event
async def on_message(message):
  id=message.author.id
  if message.content.startswith("!url"):
    return await message.author.send("http://52.59.195.10:3000/rpc/v0/apikey/"+str(id))


@bot.tree.command(name="add-ip")
@app_commands.describe(ip='Enter Ip Addres')
async def addip(interaction: discord.Interaction, ip: str):
  if (re.search(regex, ip)):
    await interaction.response.send_message(
      f"Added `{ip}` Please wait upto 5 mins for changes to take effect",
      ephemeral=True)
  else:
    await interaction.response.send_message("Invalid ip address",
                                            ephemeral=True)


@bot.tree.command(name="update-ip")
@app_commands.describe(ip='Enter Ip Addres')
async def updateip(interaction: discord.Interaction, ip: str):
  await interaction.response.send_message(f"Your ip address `{ip}` is updated",
                                          ephemeral=True)


@bot.tree.command(name="list-ip")
async def listip(interaction: discord.Interaction):
  await interaction.response.send_message("This is your Ip", ephemeral=True)


bot.run(os.getenv("TOKEN"))
