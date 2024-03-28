import disnake
from disnake.ext import commands
import datetime

class Avatar(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="avatar", description="shows the user's avatar")
    async def avatar(self, ctx, user: disnake.User = None):
        user = user or ctx.user
        embed=disnake.Embed(title="Avatar", color=disnake.Color.dark_green)
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Avatar(bot))


class Slash_avatar(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, user: disnake.User = None):
        user = user or ctx.user
        embed=disnake.Embed(title="Avatar", color=disnake.Color.dark_green)
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Slash_avatar(bot))