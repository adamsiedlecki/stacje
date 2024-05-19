import datetime
import json

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from utils.ContentDownloader import download_text


class OtmScreenForm(BoxLayout):
    def __init__(self, result_label: Label, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.result_label = result_label

        current_datetime = datetime.datetime.now()
        current_datetime.date()

        one_week_ago = current_datetime - datetime.timedelta(weeks=1)

        self.add_widget(Label(text="Pobierz dane OTM-SCREEN: "))
        self.add_widget(Label(text="id lokacji:"))
        self.id_lokacji = TextInput(input_filter='int')
        self.add_widget(self.id_lokacji)

        self.submit_button = Button(text="Pobierz dane tekstowe")
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

        text = download_text(f'https://otm.asiedlecki.net/api/v1/otm-screen/{locationId}?client=stacjePython')
        text_json = json.loads(text)

        self.result_label.text = (f" {text_json['line1']} \n"
                                  f" {text_json['line2']} \n"
                                  f" {text_json['line3']} \n "
                                  f" {text_json['line4']} \n ")

