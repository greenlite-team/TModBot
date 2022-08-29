import disnake, env
from disnake.ext import commands
from colorama import Style, Fore, init
from datetime import datetime
from os import listdir

init()
intents = disnake.Intents.default()
if env.TEST:
    bot = commands.InteractionBot(test_guilds=[883778577609412660], intents=intents)
else:
    bot = commands.InteractionBot(intents=intents)

for cog in listdir('./cogs'):
    if cog.endswith('.py'):
        bot.load_extension(f'cogs.{cog[:-3]}')
        print(f'{Fore.GREEN}[{datetime.now()}] [LAUNCH] - Loaded cog {cog}{Style.RESET_ALL}')

@bot.event
async def on_ready():
    print(f'{Fore.LIGHTGREEN_EX}[{datetime.now()}] [LAUNCH] - Launched as "{bot.user}"{Style.RESET_ALL}')

@bot.slash_command(description="Check the bot's ping")
async def ping(inter):
    await inter.send(f"Pong! The ping is `{round(bot.latency*1000)}` ms")

@commands.is_owner()
@bot.slash_command(description="DEV: Reload cogs", guild_ids=[883778577609412660])
async def reload(inter):
    for cog in listdir('./cogs'):
                if cog.endswith('.py'):
                    bot.reload_extension(f'cogs.{cog[:-3]}')
                    print(f'{Fore.GREEN}[{datetime.now()}] [LAUNCH] - Reloaded cog "{cog}"{Style.RESET_ALL}') 
    await inter.send('All cogs reloaded!', ephemeral=True)

@reload.error
async def reload_error(inter,error):
    if isinstance(error, commands.NotOwner):
        await inter.send('You are not a developer of this bot', ephemeral=True)

bot.run(env.TOKEN)