import disnake
from disnake.ext import commands
from config import token

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?',intents=intents, sync_commands_debug=True)


bot.load_extensions('cogs/StandartCommands')
bot.load_extensions('cogs/ModerationCommands')


@bot.event
async def on_ready():
    print('Dumbass bot is ready!')

bot.run(f'{token}')
