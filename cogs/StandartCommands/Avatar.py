import disnake
from disnake.ext import commands
import datetime

class Avatar(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(self, ctx, user: disnake.User = None):
        user = user or ctx.user
        embed=disnake.Embed(title="Avatar", color=disnake.Color.dark_green)
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)

    @commands.slash_command()
    async def avatar(self, ctx, user: disnake.User = None):
        user = user or ctx.user
        embed=disnake.Embed(title="Avatar", color=disnake.Color.dark_green)
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Avatar(bot))