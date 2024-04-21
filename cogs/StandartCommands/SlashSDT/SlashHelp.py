import disnake
from datetime import datetime
from config import IconUrl, moderation_commands, tools_commands, info_commands
from disnake.ext import commands

class Help(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="help", description="shows all available commands")
    async def help(self, ctx):
        embed = disnake.Embed(title="Help", description="All commands in Salat", color=0x006400, timestamp=datetime.now())
        embed.add_field(name=":page_facing_up: Info", value="".join(info_commands), inline=False)
        embed.add_field(name=":hammer: Moderation", value="".join(moderation_commands), inline=False)
        embed.add_field(name=":toolbox: Tools", value="".join(tools_commands), inline=False)
        embed.set_footer(text="SALAT!", icon_url=f"{IconUrl}")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))