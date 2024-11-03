import os
import requests


from download_images import download_image
from links_ext import get_links_ext
from dotenv import load_dotenv


def main():
    try:
        load_dotenv()
        api_key = os.getenv("NASA_API_KEY")
        if not api_key:
            raise ValueError("Переменная окружения 'NASA_API_KEY' не найдена.")
        payload = {
            "api_key": api_key,
        }
        response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payload)
        response.raise_for_status()
        epic_images = response.json()
        for count, image in enumerate(epic_images):
            date = str(image['date'].split(" ")[0]).replace('-', '/')
            image_id = image["image"]
            base_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png'
            download_image(base_url,"images",f'NASA_EPIC_{count}.png',payload)
    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}. Проверьте параметры запроса и доступность сервера.")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения. Проверьте подключение к интернету или доступность сервера.")


if __name__  == "__main__":
    main()