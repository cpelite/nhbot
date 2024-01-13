import discord
from discord.ext import commands

class comms(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name= "cogstatus", description= "Zeigt ob die Cogs einsatzbereit sind.")
    async def cogstatus(self, ctx: discord.ApplicationContext):
        await ctx.respond("Cogs einsatzbereit!")

    @commands.slash_command(name= "botinfo", description= "Zeigt Infos über den Bot.")
    async def botinfo(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(
            title = "Botinfo",
            description = "Informationen über den Bot.",
        )

        embed.add_field(name="Bot-Version", value="v0.1-dev")
        embed.add_field(name="Python-Version", value="3.11.7", inline=True)
        embed.add_field(name="Entwickler", value="SvH", inline=True)
        embed.add_field(name="Verwendete Library", value="Pycord", inline=True)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(comms(bot))