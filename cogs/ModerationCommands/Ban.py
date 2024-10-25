import disnake
from datetime import datetime
from config import IconUrl
from disnake.ext import commands

class Msg_ban(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    #BAN
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: disnake.Member, *, reason):
        embed=disnake.Embed(title=":white_check_mark: Ban",description=f"{member.mention} has been banned for **{reason}**", color=0x006400, timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)
        await ctx.guild.ban(member, reason=reason)

    #UNBAN
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, member: disnake.Member, *, reason=None):
        embed=disnake.Embed(title=":white_check_mark: Unban",description=f"{member.mention} has been unbanned", color=disnake.Color.dark_green, timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)
        await ctx.guild.unban(member, reason=reason)

def setup(bot: commands.Bot):
    bot.add_cog(Msg_ban(bot)) 