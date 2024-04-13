import disnake
from disnake.ext import commands
from config import token
from utils.database import UsersDataBase

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?',intents=intents, help_command=None, sync_commands_debug=True)
dbsetup = UsersDataBase()


bot.load_extensions('cogs/StandartCommands')
bot.load_extensions('cogs/ModerationCommands')
bot.load_extensions('cogs/StandartCommands/SlashSDT')
bot.load_extensions('cogs/ModerationCommands/SlashMDR')


@bot.event
async def on_command_error(inter: disnake.ApplicationCommandInteraction, error):
  if isinstance(error, commands.MissingPermissions):
    #Instead of commands.Missing Permissions you insert your error
    embed = disnake.Embed(
        title='Missing permissions!',
        description='You dont have any Admin/moderator permisssions!',
        color=disnake.Color.red)
    await inter.send(embed=embed, ephemeral=True)

@bot.event
async def on_slash_command_error(inter: disnake.ApplicationCommandInteraction, error):
  if isinstance(error, commands.MissingPermissions):
    #Instead of commands.Missing Permissions you insert your error
    embed = disnake.Embed(
        title='Missing permissions!',
        description='You dont have any Admin/moderator permisssions!',
        color=disnake.Color.red)
    await inter.send(embed=embed, ephemeral=True)


@bot.event
async def on_ready():
    print('Dumbass bot is ready!')
    await dbsetup.setup_database()

bot.run(f'{token}')
