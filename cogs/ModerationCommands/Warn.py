import disnake
import datetime
from disnake.ext import commands
from utils.database import UsersDataBase

class Msg_warn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def warn(ctx, member: disnake.Member):
        await self.db.warn_user(member.id, ctx.guild.id)
        embed = disnake.Embed(title="Warn", description=f"Member {member.mention} warned", color=disnake.Color.dark_green(), timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)
 
def setup(bot: commands.Bot):
    bot.add_cog(Msg_warn(bot))