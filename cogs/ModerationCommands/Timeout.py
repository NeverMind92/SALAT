import disnake
from disnake.ext import commands

class Msg_timeout(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
     
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def timeout(self, ctx, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        cool_time = disnake.utils.format_dt(time, style="T")
        embed = disnake.Embed(title=f"Timeout", description=f"{member.mention} **has been timed out until {cool_time}**", color=disnake.Color.dark_green, timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await member.timeout(reason=reason, until=time)
        await ctx.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def untimeout(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Untimeouted", description=f"{member.mention} **has been untimeouted**", color=disnake.Color.dark_green(), timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await member.timeout(reason=None, until=None)
        await ctx.send(embed=embed)

        
def setup(bot):
    bot.add_cog(Msg_timeout(bot))