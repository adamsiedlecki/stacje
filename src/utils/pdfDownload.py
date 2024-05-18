from datetime import datetime

import requests
from io import BytesIO
from kivy.core.image import Image


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