import asyncio
import datetime
import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from components.forms.ChartDownloadForm import ChartDownloadForm
from components.forms.FrostRaportDownloadForm import FrostReportDownloadForm
from utils.imageDownload import download_image
from utils.saver import save_image


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
        textLabel = Label(text='Aplikacja do poprawnego działania '
                   'wymaga połączenia z: '
                               '\n    internetem '
                               '\n    serwerem otm.asiedlecki.net')
        textLabel.text_size = (300, None)
        textLabel.halign = 'left'
        textLabel.valign = 'middle'

        self.window.add_widget(textLabel)
        self.window.add_widget(ChartDownloadForm())
        self.window.add_widget(FrostReportDownloadForm())
        self.window.add_widget(Label(text="aaa"))

    async def download_and_set_app_icon(self):
        print("icon download start...")
        image_downloaded = download_image('https://otm.asiedlecki.net/img/logo500.png')
        chart_disk_path = save_image(image_downloaded, "tmp", "app-icon.png")
        self.icon = chart_disk_path
        print("icon set: " + self.icon)


if __name__ == "__main__":
    StacjeMain().run()