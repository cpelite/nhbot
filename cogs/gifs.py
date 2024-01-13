import discord
from discord.ext import commands

class gifs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="isee", description="I see what you did there.")
    async def isee(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(
            title = "I see what you did there!",
        )

        embed.set_image(url="https://media1.tenor.com/images/d75387d37800addae30a6f33c196a036/tenor.gif?itemid=11363998")

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(gifs(bot))