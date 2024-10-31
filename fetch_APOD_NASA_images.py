import os
import requests


from download_images import download_image
from links_ext import get_links_ext
from dotenv import load_dotenv


def main():
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("Переменная окружения 'API_KEY' не найдена.")
        payload = {
            "api_key": api_key,
            'number_of_images': '5'
        }
        response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
        response.raise_for_status()
        apod_images_data = response.json()
        links = [item["url"] for item in apod_images_data]
        count = 0
        for link in links:
            count += 1
            download_image(link, 'images', f'NASA_APOD_{count}{get_links_ext(link)}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP ошибка: {http_err}')


if __name__  == "__main__":
    main()