from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class DateTimeInput(BoxLayout):
    def __init__(self, date: str, time: str, include_time=True, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.date_input = TextInput(hint_text='YYYY-MM-DD', text=date, readonly=False)
        self.add_widget(self.date_input)
        if include_time:
            self.time_input = TextInput(hint_text='HH:MM', text=time, readonly=False)
            self.add_widget(self.time_input)
