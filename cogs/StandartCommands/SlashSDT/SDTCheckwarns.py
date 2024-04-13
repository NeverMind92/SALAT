import disnake
import datetime
from disnake.ext import commands
from utils.database import UsersDataBase

class Checkwarns(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.slash_command(name="checkwarn", description="Shows all your/someone else's warns")
    async def checkwarns(self, ctx, member: disnake.Member):
        num_warns = await self.db.get_warns(member.id, ctx.guild.id)
        embed = disnake.Embed(title=f"{member.mention} warns:", color=disnake.Color.dark_green(), timestamp=datetime.datetime.now())
        embed.add_field(name=f"Have {num_warns} warns!", value="Be careful!", inline=False)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Checkwarns(bot))