import os
os.system('pip uninstall discord')
os.system('pip install discord.py==1.7.3')
import discord
from discord.ext import commands
import os
import base64
import sys
import asyncio
import colorama
from colorama import Fore, Back, Style

prefix = '.'
toxxable = ['fag', 'Fag', 'kys', 'Kys', 'kill yourself', 'Kill yourself', 'kill', 'Kill', 'doxbin', 'gore', 'nigger', 'Nigger', 'niggers', 'Niggers', 'faggot', 'Faggot', 'FAggoT' 'Doxbin', 'd01ksb1n', 'dox', 'doxxing', 'doxx', 'Doxx', 'Doxxing', 'token', 'tok3n', 'give me your token', 'jewcord', 'Jewcord', 'Hitler', 'Jews', 'jews', 'hitler', 'nazi', 'Nazi', 'Heil Hitler', '1488', 'Heil Hitler', 'heil', 'Heil', 'blacks', 'Nazi Germany', 'Taiwan' , 'raid', 'raiding', 'raiders', 'rayd', 'Im raiding', 'raided', 'cp', 'Gore', 'child porn', 'pedo', 'Pedo', 'pedophile', 'Pedophile', 'nuke', 'Nuke', 'Nuking', 'nuking', 'Im nuking', 'nuking servers', 'Nuking servers', 'Nuking Servers', 'white supremacy', 'White supremacy', 'nigga', 'Nigga']

token = input(f"{Fore.LIGHTYELLOW_EX}[+] Token : {Style.RESET_ALL}")

intents = discord.Intents().all()
client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)

class main:
  def clear():
    try:
      os.system('clear')
    except:
      os.system('cls')

@client.event
async def on_ready():
  main.clear()
  print(f"{Fore.GREEN}{client.user} online{Style.RESET_ALL}")
  print(f"{Fore.YELLOW}Prefix {Fore.LIGHTYELLOW_EX}{prefix}{Style.RESET_ALL}")
  try:
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("ཌⱤ₲ད \\ DM To Join // ཌⱤ₲ད"))
  except Exception as e:
    print(e)

@client.event
async def on_message(message):
  if message.content in toxxable:
    await asyncio.sleep(10)
    await message.delete()
    print(f"[+] Deleted a message: {message.content} (REASON: Toxxable)")
    await asyncio.sleep(3)
  if ".status" in message.content:
    try:
      command, status = message.content.split()
      await client.change_presence(status=discord.Status.dnd, activity=discord.Game(status))
      print("[+] Changed Status!")
    except Exception as e:
      print(f"[-] {e}")
  if ".spam" in message.content:
    try:
      command, amount, *msg = message.content.split()
      amount = int(amount)
      msg = ''.join(msg)

      for _ in range(amount):
        try:
          await message.channel.send(msg)
        except:
          pass
    except:
      pass
  if ".purge" in message.content:
    try:
      messages = await message.channel.history(limit=100).flatten()
      for msg in messages:
        if message.author == client.user:
          try:
            await msg.delete()
          except:
            pass
    except Exception as e:
      print(f"[-] {e}")
  else:
    pass

client.run(token, bot=False)
