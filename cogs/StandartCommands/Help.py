import disnake
from disnake.ext import commands
import datetime
import config

class Help(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.slash_command()
    async def help(self, ctx):
        embed = disnake.Embed(title="Help", description="all commands in Salat", color=0x006400, timestamp=datetime.datetime.now())
        embed.add_field(name=":page_facing_up: Info", value="".join(config.standart_commands), inline=False)
        embed.add_field(name=":hammer: Moderation", value="", inline=False)
        embed.add_field(name=":toolbox: Tools", value="", inline=False)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
