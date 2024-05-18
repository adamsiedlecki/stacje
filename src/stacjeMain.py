import asyncio
import datetime
import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from components.forms.ChartDownloadForm import ChartDownloadForm
from utils.imageDownload import download_image
from utils.imageSaver import save_image


class StacjeMain(App):
    def build(self):
        self.title = "stacje pogodowe by Adam Siedlecki s25300"
        print("Running inside: " + os.getcwd())
        asyncio.run(self.download_and_set_app_icon())

        print("starting program...")
        self.window = GridLayout()
        self.window.cols = 3
        self.window.rows = 3

        asyncio.run(self.configure_window())

        return self.window

    async def configure_window(self):
        print("Window configuration...")
        self.window.add_widget(Label(text='Witaj w tej wspaniałej aplikacji!'))
        self.window.add_widget(ChartDownloadForm())

        self.user_input = TextInput(multiline=False)
        self.user_input.input_filter='int'
        self.window.add_widget(self.user_input)

        self.button = Button(text="Wprowadź dane", bold=True, background_color='#00FFCE')
        self.button.bind(on_press=self.button_callback)
        self.window.add_widget(self.button)

    def button_callback(self, instance):
        text = self.user_input.text
        print(text)

    async def download_and_set_app_icon(self):
        print("icon download start...")
        image_downloaded = download_image('https://otm.asiedlecki.net/img/logo500.png')
        chart_disk_path = save_image(image_downloaded, "tmp", "app-icon.png")
        self.icon = chart_disk_path
        print("icon set: " + self.icon)


if __name__ == "__main__":
    StacjeMain().run()