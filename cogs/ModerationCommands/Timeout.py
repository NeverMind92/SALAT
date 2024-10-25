import disnake
from datetime import datetime, timedelta
from disnake.ext import commands
from config import IconUrl

class Msg_timeout(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #TIMEOUT 
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def timeout(self, ctx, member: disnake.Member, time: str, reason: str):
        muted_role = disnake.utils.get(ctx.guild.roles, name='muted')
        if not muted_role:
            muted_role = await ctx.guild.create_role(name='muted', reason='Creatig the muted role')
        if muted_role and muted_role not in member.roles:
            await member.add_roles(muted_role)
        time = datetime.now() + timedelta(minutes=int(time))
        cool_time = disnake.utils.format_dt(time, style="T")
        embed = disnake.Embed(title="Timeout", description=f"{member.mention} **has been timed out until {cool_time}**", color=disnake.Color.dark_red, timestamp=datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await member.timeout(reason=reason, until=time)
        await ctx.send(embed=embed)

    #UNTIMEOUT 
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def untimeout(self, ctx, member: disnake.Member):
        embed = disnake.Embed(title="Untimeouted", description=f"{member.mention} **has been untimeouted**", color=disnake.Color.dark_red(), timestamp=datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await member.timeout(reason=None, until=None)
        await ctx.send(embed=embed)

        
def setup(bot):
    bot.add_cog(Msg_timeout(bot))