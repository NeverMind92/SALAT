import disnake
from disnake.ext import commands
import datetime

from utils.database import UsersDataBase


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.slash_command(name="Warn", description="warns a member")
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, member: disnake.Member = None, *, reason):
        await self.db.create_table()
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(title="Warn", description=f"{member.mention} got warned", timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", 
        icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await self.db.update_warns(member, warns = 1)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Warn(bot))