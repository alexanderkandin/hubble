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
            'count': '5'
        }
        response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
        response.raise_for_status()
        launch_data = response.json()
        links = [item["url"] for item in launch_data]
        count = 0
        for link in links:
            count += 1
            download_image(link, 'images_NASA', f'NASA_{count}{get_links_ext(link)}')
    except requests.exceptions.RequestException as err:
        print(f'Ошибка при выполнении запроса: {err}')


if __name__  == "__main__":
    main()