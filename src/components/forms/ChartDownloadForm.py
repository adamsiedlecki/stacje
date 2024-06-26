import datetime

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from components.DateTimeInput import DateTimeInput
from components.ImageWindow import ImageWindow
from utils.ContentDownloader import download_image
from utils.saver import save_image


class ChartDownloadForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        current_datetime = datetime.datetime.now()
        current_datetime.date()

        one_week_ago = current_datetime - datetime.timedelta(weeks=1)

        self.add_widget(Label(text="Pobierz wykres temperatury: "))
        self.add_widget(Label(text="id lokacji:"))
        self.id_lokacji = TextInput(input_filter='int')
        self.add_widget(self.id_lokacji)

        self.add_widget(Label(text="data od:"))
        self.dateStart = DateTimeInput(date=one_week_ago.date().__str__(), time=one_week_ago.strftime('%H:%M'))
        self.add_widget(self.dateStart)

        self.add_widget(Label(text="data do:"))
        self.dateEnd = DateTimeInput(date=current_datetime.date().__str__(), time=current_datetime.strftime('%H:%M'))
        self.add_widget(self.dateEnd)

        self.submit_button = Button(text="Pobierz wykres")
        self.submit_button.bind(on_press=self.submit)
        self.add_widget(self.submit_button)

        self.wynikLabel = Label()
        self.add_widget(self.wynikLabel)

    def submit(self, instance):
        self.wynikLabel.text = ""
        locationId = self.id_lokacji.text
        dateStart = self.dateStart.date_input.text
        timeStart = self.dateStart.time_input.text

        dateEnd = self.dateEnd.date_input.text
        timeEnd = self.dateEnd.time_input.text

        if locationId == "" :
            self.wynikLabel.text = "Podaj id lokacji"
            return

        if dateStart == "" or timeStart == "":
            self.wynikLabel.text = "Podaj datę oraz czas od"
            return

        if dateEnd == "" or timeEnd == "":
            self.wynikLabel.text = "Podaj datę oraz czas do"
            return

        image_downloaded = download_image(f'https://otm.asiedlecki.net/api/v1/image'
                                          f'?locationPlaceId={locationId}&start={dateStart}T{timeStart}&end={dateEnd}T{timeEnd}')
        if image_downloaded is None:
            popup = Popup(title='Serwer nie zwrocil obrazka :(', size_hint=(0.8, 0.2))
            popup.open()
        else:
            filename = f'wykres temperatury {locationId} {dateStart} {timeStart.replace(":", ".")} do {dateEnd} {timeEnd.replace(":", ".")}.png'
            save_image(image_downloaded, "wykresy", filename)
            image_window = ImageWindow(image_downloaded, filename)
            image_window.open()
