import disnake
from disnake.ext import commands
from datetime import datetime
from utils.database import UsersDataBase
from config import IconUrl

class Remwarn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.has_permissions(manage_nicknames=True)
    @commands.slash_command()
    async def remwarn(self, ctx, member: disnake.Member):
        if member is None:
            member = ctx.author
        await self.db.remove_warn(member.id, ctx.guild.id)
        embed = disnake.Embed(title="Remove warn", description=f"1 warn successfully deleted from {member.mention}", color=disnake.Color.dark_green(),timestamp=datetime.now())
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Remwarn(bot))