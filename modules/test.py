import disnake
from disnake.ext import commands

class TestCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="test", description="Ny test 315")
    async def test(self, inter: disnake.ApplicationCommandInteraction, number: int):
        await inter.response.send_message(
            f"Название сервера: {inter.guild.name}\nВсего участников: {inter.guild.member_count}\nДополнительная информация: {inter.guild.created_at} и {inter.guild.verification_level}"
            f"\n\nВаш тег: {inter.author}\nВаш ID: {inter.author.id}"
            f"\n\nЗадержка бота: {round(self.bot.latency * 1000)}мс"
            f"\n\n{number}*7 = **{number * 7}**"
        )

def setup(bot: commands.Bot):
    bot.add_cog(TestCommand(bot))