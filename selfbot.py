import os

os.system('pip uninstall selfcord')
os.system('pip install selfcord.py')
import selfcord
from colorama import Back, Fore, Style

prefixes = ['.', '>']

toxxable = [
    "fag",
    "kys",
    "kill",
    "dox",
    "doxbin",
    "gore",
    "nigger",
    "faggot",
    "doxxing",
    "d01ksb1n",
    "token",
    "tok3n",
    "jewcord",
    "hitler",
    "jews",
    "nazi",
    "heil",
    "1488",
    "blacks",
    "taiwan",
    "raid",
    "raiding",
    "rayd",
    "cp",
    "child porn",
    "pedo",
    "pedophile",
    "nuke",
    "nuking",
    "white supremacy",
    "nigga"
]
token = input(f"{Fore.LIGHTYELLOW_EX}[+] Token : {Style.RESET_ALL}")

bot = selfcord.Bot(prefixes=prefixes)

def clear():
    try:
        os.system('clear')
    except:
        os.system('cls')

@bot.on("ready")
async def ready(time):
    clear()
    print(f"{Fore.GREEN}{bot.user} online{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Prefix {Fore.LIGHTYELLOW_EX}{prefixes}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Took {time} seconds to start")
    try:
        await bot.change_presence(
            status="dnd",
            afk=False,
            activity=selfcord.Activity.Game(
                name="ཌⱤ₲ད \\ DM To Join // ཌⱤ₲ད",
                details="DM to Join!",
                state="vibing",
                buttons={
                    "Server": "https://discord.gg/9KtaxZKewk", # Change this to your liking
                    "Wrapper": "https://pypi.org/project/selfcord.py/", # Also change this to your liking
                },
                application_id="1100082565811015720",
                key="neovim",
            ),
        )
    except Exception as e:
        print(e)



@bot.cmd(description="Purges your messages", aliases=['wipe'])
async def purge(ctx, amount: int):
    await ctx.purge(amount) # Purges amount of messages you supply

@bot.cmd(description="Spams messages")
async def spam(ctx, amount: int, *, message: str):
    await ctx.spam(amount, message)


@bot.on("message")
async def message_deleter(message):
    if message.author == bot.user:
        if any(word in message.content.lower() for word in toxxable):
            await message.channel.delayed_delete(message, 10)
            print(f"[+] Deleted a message: {message.content} (REASON: Toxxable)")


bot.run(token)
