import disnake
from datetime import timedelta, datetime
from disnake.ext import commands
from config import IconUrl

class Timeout(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.slash_command(name="timeout", description="Gives a timeout to the member")
    async def timeout(self, ctx, member: disnake.Member, time: int, reason: str):
        muted_role = disnake.utils.get(ctx.guild.roles, name='muted')
        if not muted_role:
            muted_role = await ctx.guild.create_role(name='muted', reason='Creating the muted role')
        if muted_role not in member.roles:
            await member.add_roles(muted_role)
        time = datetime.now() + timedelta(minutes=int(time))
        # Set end_time as member's timeout until the end_time
        await member.edit(timeout=time)
        cool_time = disnake.utils.format_dt(time, style="f")
        embed = disnake.Embed(title="Timeout", description=f"{member.mention} has been timed out until {cool_time}", color=disnake.Color.dark_green(), timestamp=datetime.now())
        embed.add_field(name="By Admin/moderator:", value=ctx.author.mention, inline=None)
        embed.set_footer(text="SALAT!", icon_url=IconUrl)
        await ctx.send(embed=embed, ephemeral=True)

    @commands.has_permissions(manage_messages=True)
    @commands.slash_command(name="untimeout", description="Untimeout a member")
    async def untimeout(self, ctx, member: disnake.Member):
        muted_role = disnake.utils.get(ctx.guild.roles, name='muted')
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
        # Set member's timeout to None to remove the timeout
        await member.edit(timeout=None)
        embed = disnake.Embed(title="Untimeouted", description=f"{member.mention} has been untimeouted", color=disnake.Color.dark_green(), timestamp=datetime.now())
        embed.add_field(name="By Admin/moderator:", value=ctx.author.mention, inline=None)
        embed.set_footer(text="SALAT!", icon_url=IconUrl)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Timeout(bot))