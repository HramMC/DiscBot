import disnake
from disnake.ext import commands
from disnake import TextInputStyle

class MyModal(disnake.ui.Modal, commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="Name",
                placeholder="Foo Tag",
                custom_id="название",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Description",
                placeholder="Lorem ipsum dolor sit amet.",
                custom_id="описание",
                style=TextInputStyle.paragraph,
            ),
        ]
        super().__init__(
            title="Create Tag",
            custom_id="create_tag",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Создание тега")
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await inter.response.send_message(embed=embed)

    @commands.slash_command()
    async def tags(self, inter: disnake.AppCmdInter):
        """Отправляет модальное окно для создания тега"""
        await inter.response.send_modal(modal=MyModal())

def setup(bot: commands.Bot):
    bot.add_cog(MyModal())