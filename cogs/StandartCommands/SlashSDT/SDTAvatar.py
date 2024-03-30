import disnake
from disnake.ext import commands
import datetime
import config

class Avatar(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="avatar", description="Shows the member's avatar")
    async def avatar(ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        embed = disnake.Embed(title=f"{member.name}'s Avatar", color=disnake.Color.dark_green(), timestamp=datetime.datetime.now())
        embed.set_footer(text="SALAT!", icon_url="https://cdn.discordapp.com/app-icons/1215958585314381824/b9d4ec6f686085758ad2e7fdc5503f0d.png?size=256")
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Avatar(bot))