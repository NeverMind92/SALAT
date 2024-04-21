import disnake
from datetime import datetime
from disnake.ext import commands
from utils.database import UsersDataBase
from config import IconUrl

class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = UsersDataBase()
   
    @commands.has_permissions(manage_nicknames=True)
    @commands.slash_command(name="warn", description="warns member")
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
 
def setup(bot: commands.Bot):
    bot.add_cog(Warn(bot))