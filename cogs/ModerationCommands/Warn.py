import disnake
from datetime import datetime
from disnake.ext import commands
from utils.database import UsersDataBase
from config import IconUrl

class Msg_warn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()

    #WARN
    @commands.has_permissions(manage_nicknames=True)
    @commands.command()
    async def warn(self, ctx, member: disnake.Member):
        warned_role = disnake.utils.get(ctx.guild.roles, name='warned')
        if not warned_role:
            warned_role = await ctx.guild.create_role(name='warned', reason='Creatig the warned role')
        if warned_role and warned_role not in member.roles:
            await member.add_roles(warned_role) 
        await self.db.warn_user(member.id, ctx.guild.id)
        embed = disnake.Embed(title="Warn", description=f"Member {member.mention} warned", color=disnake.Color.dark_red(), timestamp=datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)

    #RMWARN
    @commands.has_permissions(manage_nicknames=True)
    @commands.command()
    async def rmwarn(self, ctx, member: disnake.Member):
        if member is None:
            member = ctx.author
        await self.db.remove_warn(member.id, ctx.guild.id)
        embed = disnake.Embed(title="Remove warn", description=f"1 warn successfully deleted from {member.mention}", color=disnake.Color.dark_green(),timestamp=datetime.now())
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)
 
def setup(bot: commands.Bot):
    bot.add_cog(Msg_warn(bot))