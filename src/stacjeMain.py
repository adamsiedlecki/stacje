import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from components.forms.ChartDownloadForm import ChartDownloadForm
from components.forms.FrostRaportDownloadForm import FrostReportDownloadForm
from components.forms.MapsForm import MapsForm
from components.forms.OtmScreenForm import OtmScreenForm


class StacjeMain(App):
    def build(self):
        """
        Buduje aplikację
        :return: okno aplikacji
        """
        self.title = "stacje pogodowe by Adam Siedlecki s25300"
        print("Running inside: " + os.getcwd())
        self.set_app_icon()

        print("starting program...")
        self.window = GridLayout()
        self.window.cols = 3
        self.window.rows = 3

        self.configure_window()

        return self.window

    def configure_window(self):
        """
        Konfiguruje okno aplikacji
        """
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

        otm_screen_label = Label()
        otm_screen_label.text_size = (300, None)
        otm_screen_label.halign = 'left'
        otm_screen_label.valign = 'middle'

        self.window.add_widget(OtmScreenForm(otm_screen_label))
        self.window.add_widget(otm_screen_label)

        self.window.add_widget(MapsForm())

    def set_app_icon(self):
        """
        Ustawia ikonę aplikacji. Wykorzystuje katalog static.
        W przypadku zbudowania do exe, wymaga dodania ścieżki _internal.
        """
        path = os.path.join("static", "app-icon.png")
        if os.path.exists(path):
            self.icon = path
        else:
            self.icon = os.path.join("_internal", "static", "app-icon.png")
            print("icon set")


if __name__ == "__main__":
    StacjeMain().run()