from datetime import datetime

import requests
from io import BytesIO
from kivy.core.image import Image


def download_image(url):
    try:
        download_start = datetime.now()
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        download_end = datetime.now()
        print(f"image downloaded, took {(download_end - download_start).total_seconds()} seconds")
        return Image(img_data, ext="png")
    except Exception as e:
        print("Error while image download:", e)
        return None


def download_pdf(url):
    try:
        download_start = datetime.now()
        response = requests.get(url)
        response.raise_for_status()
        pdf_data = BytesIO(response.content)
        download_end = datetime.now()
        print(f"pdf downloaded, took {(download_end - download_start).total_seconds()} seconds")
        return pdf_data
    except Exception as e:
        print("Error while image download:", e)
        return None


def download_text(url):
    try:
        download_start = datetime.now()
        response = requests.get(url)
        response.raise_for_status()
        download_end = datetime.now()
        print(f"text downloaded, took {(download_end - download_start).total_seconds()} seconds")
        return response.text
    except Exception as e:
        print("Error while text download:", e)
        return None