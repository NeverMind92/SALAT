import disnake
from datetime import datetime
from config import IconUrl
from disnake.ext import commands

class Msg_avatar(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def avatar(ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        embed = disnake.Embed(title=f"{member.name}'s Avatar", color=disnake.Color.dark_green(), timestamp=datetime.now())
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Msg_avatar(bot))