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
        }
        response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payload)
        response.raise_for_status()
        epic_images_data = response.json()
        image_id = [item["image"] for item in epic_images_data]
        image_date = [item["date"] for item in epic_images_data]
        for i in range(0, len(image_date)):
            date = str(image_date[i].split(" ")[0]).replace('-', '/')
            id = image_id[i]
            url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{id}.png?api_key=gdPzfbvhAsScM7wQyZRkUkMllJEmTzaS5Br4uPii'
            download_image(url,"images",f'NASA_EPIC_{i}{get_links_ext(url)}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP ошибка: {http_err}')


if __name__  == "__main__":
    main()