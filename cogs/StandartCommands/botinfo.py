import disnake
import hyperlink
from config import version, IconUrl, ThumbnailIcon
from datetime import datetime
from disnake.ext import commands

class MSGBotInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        embed = disnake.Embed(title="Salat", description="Salat - a small open-source discord bot, prefix: ``/``", color=disnake.Color.dark_green(), timestamp=datetime.now())
        embed.add_field(name="Build:", value=f"{version}", inline=True)
        embed.add_field(name="Links:", value="[github](https://github.com/NeverMind92/bot-SALAT) [discord](https://discord.gg/QQ5sPRx7Qk)", inline=True)
        embed.set_thumbnail(url=f"{ThumbnailIcon}")
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(MSGBotInfo(bot))

