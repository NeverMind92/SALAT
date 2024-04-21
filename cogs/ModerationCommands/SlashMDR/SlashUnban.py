import disnake
from datetime import datetime
from config import IconUrl
from disnake.ext import commands

class Unban(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot
    
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(name="unban", description="Unban a member")
    async def unban(self, ctx, member: disnake.Member, *, reason):
        embed=disnake.Embed(title=":white_check_mark: Unban",description=f"{member.mention} has been unbanned", color=0x006400, timestamp=datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)
        await ctx.guild.unban(member, reason=reason)



def setup(bot: commands.Bot):
    bot.add_cog(Unban(bot))