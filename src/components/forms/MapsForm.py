import datetime
import json
import webbrowser

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from utils.ContentDownloader import download_text


class MapsForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text="Mapa temperatur"))
        self.add_widget(Label(text="id lokacji:"))
        self.id_lokacji = TextInput(input_filter='int')
        self.add_widget(self.id_lokacji)

        self.submit_button = Button(text="Pokaż")
        self.submit_button.bind(on_press=self.submit)
        self.add_widget(self.submit_button)

        self.wynikLabel = Label()
        self.add_widget(self.wynikLabel)

    def submit(self, instance):
        self.wynikLabel.text = ""
        locationId = self.id_lokacji.text

        if locationId == "":
            self.wynikLabel.text = "Podaj id lokacji"
            return

        url = f'https://otm.asiedlecki.net/map/temperature/{locationId}'
        try:
            webbrowser.open(url)
            print(f'URL {url} was opened')
        except Exception as e:
            print(f'Exception while opening url: {e}')

