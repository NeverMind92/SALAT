import disnake
import datetime
from disnake.ext import commands
from utils import database

class Checkwarns(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="checkwarn", description="Shows all your/someone else's warns")
    async def checkwarns(self, ctx, member: disnake.Member):
        num_warns = await database.get_warnings(member.id)
        embed = disnake.Embed(title="Your warns:", color=disnake.Color.dark_green(), timestamp=datetime.datetime.now())
        embed.add_field(name=f"{num_warns} Warns", value="Be careful!", inline=False)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Checkwarns(bot))