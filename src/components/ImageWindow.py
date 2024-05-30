import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image


class ImageWindow(Popup):
    def __init__(self, image: CoreImage, title:str, **kwargs):
        """
        Inicjalizuje Popup, którego treścią będzie obrazek.
        :param image: obrazek
        :param title: tytuł
        :param kwargs: dodatkowe parametry
        """
        super(ImageWindow, self).__init__(**kwargs)
        self.title = title
        self.size_hint = (0.9, 0.6)
        content = BoxLayout(orientation='vertical')
        self.content = content
        content.add_widget(Image(texture=image.texture))