import requests
from io import BytesIO
from kivy.core.image import Image


def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        return Image(img_data, ext="png")
    except Exception as e:
        print("Error while image download:", e)
        return None