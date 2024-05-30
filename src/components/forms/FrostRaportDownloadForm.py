import datetime

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from components.DateTimeInput import DateTimeInput
from utils.ContentDownloader import download_pdf
from utils.FileOpener import open_file
from utils.saver import save_pdf


class FrostReportDownloadForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        current_datetime = datetime.datetime.now()
        current_datetime.date()

        one_week_ago = current_datetime - datetime.timedelta(weeks=1)

        self.add_widget(Label(text="Pobierz raport przymrozkowy: "))
        self.add_widget(Label(text="id lokacji:"))
        self.id_lokacji = TextInput(input_filter='int')
        self.add_widget(self.id_lokacji)

        self.add_widget(Label(text="data od:"))
        self.dateStart = DateTimeInput(date=one_week_ago.date().__str__(),
                                       time="",
                                       include_time=False)
        self.add_widget(self.dateStart)

        self.add_widget(Label(text="data do:"))
        self.dateEnd = DateTimeInput(date=current_datetime.date().__str__(),
                                     time="",
                                     include_time=False)
        self.add_widget(self.dateEnd)

        self.submit_button = Button(text="Pobierz pdf")
        self.submit_button.bind(on_press=self.submit)
        self.add_widget(self.submit_button)

        self.wynikLabel = Label()
        self.add_widget(self.wynikLabel)

    def submit(self, instance):
        self.wynikLabel.text = ""
        locationId = self.id_lokacji.text
        dateStart = self.dateStart.date_input.text
        dateEnd = self.dateEnd.date_input.text

        if locationId == "" :
            self.wynikLabel.text = "Podaj id lokacji"
            return

        if dateStart == "":
            self.wynikLabel.text = "Podaj datę oraz czas od"
            return

        if dateEnd == "":
            self.wynikLabel.text = "Podaj datę oraz czas do"
            return

        pdf_bytes = download_pdf(f'https://otm.asiedlecki.net/api/v1/report/frost'
                                          f'?locationPlaceId={locationId}&start={dateStart}&end={dateEnd}')
        if pdf_bytes is None:
            popup = Popup(title='Serwer nie zwrocil pdf :(', size_hint=(0.8, 0.2))
            popup.open()
        else:
            filename = f'raport przymrozkowy {locationId} {dateStart} do {dateEnd}.pdf'
            disk_path = save_pdf(pdf_bytes, "pdf", filename)
            open_file(disk_path)

