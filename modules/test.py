import disnake
from disnake.ext import commands
from disnake.types.interactions import ApplicationCommandInteraction


class TestCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="test", description="Ny test 315")
    async def test(self, inter: disnake.ApplicationCommandInteraction, number: int = 10):
        await inter.response.send_message(
            f"Название сервера: {inter.guild.name}\nВсего участников: {inter.guild.member_count}\nДополнительная информация: {inter.guild.created_at} и {inter.guild.verification_level}"
            f"\n\nВаш тег: **{inter.author}**\nВаш ID: **{inter.author.id}**"
            f"\n\nЗадержка бота: **{round(self.bot.latency * 1000)}мс**"
            f"\n\n{number}*7 = **{number * 7}**"
        )

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Pong")

    @commands.slash_command()
    async def defer(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer
        await inter.response.sleep(10)
        await inter.edit_original_message(content="Wait... completed!")

def setup(bot: commands.Bot):
    bot.add_cog(TestCommand(bot))