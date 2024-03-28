import disnake
from disnake.ext import commands
import datetime
import config

class Msg_avatar(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: disnake.Member):
        embed=disnake.Embed(title="Avatar", color=disnake.Color.dark_green)
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Msg_avatar(bot))