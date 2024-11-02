import os
import requests


from download_images import download_image
from links_ext import get_links_ext
from dotenv import load_dotenv


def main():
    try:
        load_dotenv()
        api_key = os.getenv("NASA_API_KEY")
        number_of_images = '5'
        if not api_key:
            raise ValueError("Переменная окружения 'NASA_API_KEY' не найдена.")
        payload = {
            "api_key": api_key,
            'count': number_of_images
        }
        response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
        response.raise_for_status()
        apod_images = response.json()
        links = [link["url"] for link in apod_images]
        for link_number, link in enumerate(links):
            download_image(link, 'images', f'NASA_APOD_{link_number}{get_links_ext(link)}')
    except requests.exceptions.HTTPError as http_err:
        print(f'Вы ввели неверный токен: {http_err}')


if __name__  == "__main__":
    main()