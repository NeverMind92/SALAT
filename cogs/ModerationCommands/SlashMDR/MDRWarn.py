import disnake
import datetime
from disnake.ext import commands
from utils import database

class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
   
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(name="warn", description="Warns the member")
    async def warn(self, ctx, member: disnake.Member, *, reason):
        await database.add_user(member.id, ctx.guild.id)
        await database.add_warn(member.id, ctx.guild.id, reason)
        embed = disnake.Embed(title="Warn", description=f"Member {member.mention} warned", color=disnake.Color.dark_green(), timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)
 
def setup(bot: commands.Bot):
    bot.add_cog(Warn(bot))