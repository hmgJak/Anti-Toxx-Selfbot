import os
os.system('pip uninstall selfcord')
os.system('pip install selfcord.py')
import selfcord
from colorama import Fore, Back, Style

prefixes = ['.', '>']
toxxable = ['fag', 'Fag', 'kys', 'Kys', 'kill yourself', 'Kill yourself', 'kill', 'Kill', 'doxbin', 'gore', 'nigger', 'Nigger', 'niggers', 'Niggers', 'faggot', 'Faggot', 'FAggoT' 'Doxbin', 'd01ksb1n', 'dox', 'doxxing', 'doxx', 'Doxx', 'Doxxing', 'token', 'tok3n', 'give me your token', 'jewcord', 'Jewcord', 'Hitler', 'Jews', 'jews', 'hitler', 'nazi', 'Nazi', 'Heil Hitler', '1488', 'Heil Hitler', 'heil', 'Heil', 'blacks', 'Nazi Germany', 'Taiwan' , 'raid', 'raiding', 'raiders', 'rayd', 'Im raiding', 'raided', 'cp', 'Gore', 'child porn', 'pedo', 'Pedo', 'pedophile', 'Pedophile', 'nuke', 'Nuke', 'Nuking', 'nuking', 'Im nuking', 'nuking servers', 'Nuking servers', 'Nuking Servers', 'white supremacy', 'White supremacy', 'nigga', 'Nigga']

token = input(f"{Fore.LIGHTYELLOW_EX}[+] Token : {Style.RESET_ALL}")

bot = selfcord.Bot(prefixes=prefixes)

def clear():
  try:
    os.system('clear')
  except:
    os.system('cls')

@bot.on("ready")
async def ready(time):
  main.clear()
  print(f"{Fore.GREEN}{client.user} online{Style.RESET_ALL}")
  print(f"{Fore.YELLOW}Prefix {Fore.LIGHTYELLOW_EX}{prefix}{Style.RESET_ALL}")
  print(f"{Fore.YELLOW}Took {time} seconds to start")
  try:
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("ཌⱤ₲ད \\ DM To Join // ཌⱤ₲ད"))
  except Exception as e:
    print(e)




@client.on("message")
async def message_deleter(message):
  if any(message.content in word for word in toxxable):
    await message.channel.delayed_delete(message, 10)
    print(f"[+] Deleted a message: {message.content} (REASON: Toxxable)")
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
