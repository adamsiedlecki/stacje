import os

from kivy.core.image import Image


def save_image(image: Image, type: str, filename: str):
    chart_disk_path = os.path.join("downloads", type, filename)
    image.save(chart_disk_path)
    print("image saved: " + chart_disk_path)
    return chart_disk_path
