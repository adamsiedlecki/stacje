from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from imageDownload import download_image
from kivy.graphics.texture import Texture
import asyncio
import datetime


class SayHello(App):
    def build(self):
        self.title = "stacje pogodowe by Adam Siedlecki s25300"
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
        self.window.add_widget(Label(text='Test'))

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
        downloadStart = datetime.datetime.now()
        image_downloaded = download_image('https://otm.asiedlecki.net/img/logo500.png')
        downloadEnd = datetime.datetime.now()
        print(f"icon downloaded, took {(downloadEnd-downloadStart).total_seconds()} seconds")
        icon_disk_path = 'downloads/downloads-icon.png'
        image_downloaded.save(icon_disk_path)
        self.icon = icon_disk_path
        print("icon set")


if __name__ == "__main__":
    SayHello().run()