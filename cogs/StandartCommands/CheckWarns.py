import disnake
from datetime import datetime
from disnake.ext import commands
from utils.database import UsersDataBase
from config import IconUrl

class Msg_checkwarns(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.command()
    async def checkwarns(self, ctx, member: disnake.Member):
        num_warns = await self.db.get_warns(member.id, ctx.guild.id)
        embed = disnake.Embed(title=f"{member.mention} warns:", color=disnake.Color.dark_green(), timestamp=datetime.now())
        embed.add_field(name=f"Have {num_warns} warns!", value="Be careful!", inline=False)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Msg_checkwarns(bot))