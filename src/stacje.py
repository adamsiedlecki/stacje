from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from imageDownload import download_image

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 3
        self.window.rows = 3

        image_downloaded = download_image('https://otm.asiedlecki.net/img/logo500.png')
        self.window.add_widget(Image(texture=image_downloaded.texture))

        return self.window

if __name__ == "__main__":
    SayHello().run()