import os
from io import BytesIO

from kivy.core.image import Image


def save_image(image: Image, type: str, filename: str):
    dirs_path = os.path.join("downloads", type)
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)

    disk_path = os.path.join("downloads", type, filename)
    image.save(disk_path)
    print("image saved: " + disk_path)
    return disk_path


def save_pdf(pdf_bytes: BytesIO, type: str, filename: str):
    dirs_path = os.path.join("downloads", type)
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)

    disk_path = os.path.join("downloads", type, filename)
    with open(disk_path, "wb") as binary_file:
        binary_file.write(pdf_bytes.read())
    print("pdf saved: " + disk_path)
    return disk_path
