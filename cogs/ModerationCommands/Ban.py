import disnake
from disnake.ext import commands
import datetime
import config

class Ban(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot
        
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(name="ban", description="bans a member who broke the rules")
    async def ban(self, ctx, member: disnake.Member, *, reason):
        embed=disnake.Embed(title=":white_check_mark: Ban",description=f"{member.mention} has been banned for **{reason}**", color=0x006400, timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)
        await ctx.guild.ban(member, reason=reason)



def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))



class Slash_ban(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: disnake.Member, *, reason):
        embed=disnake.Embed(title=":white_check_mark: Ban",description=f"{member.mention} has been banned for **{reason}**", color=0x006400, timestamp=datetime.datetime.now())
        embed.add_field(name="By Admin/moderator:", value=f"{ctx.author.mention}", inline=None)
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        await ctx.send(embed=embed)
        await ctx.guild.ban(member, reason=reason)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_ban(bot)) 