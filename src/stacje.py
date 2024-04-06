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

        self.window.add_widget(Label(text='Witaj w tej wspaniałej aplikacji!'))
        self.window.add_widget(Label(text='Test'))

        self.user_input = TextInput(multiline=False)
        self.user_input.input_filter='int'
        self.window.add_widget(self.user_input)

        self.button = Button(text="Wprowadź dane")
        self.button.bind(on_press=self.button_callback)
        self.window.add_widget(self.button)

        return self.window

    def button_callback(self, instance):
        text = self.user_input.text
        print(text)


if __name__ == "__main__":
    SayHello().run()