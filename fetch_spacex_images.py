import argparse
import requests
from download_images import download_image
from links_ext import get_links_ext
import sys

def main():
    try:
        parser = argparse.ArgumentParser(
                    description='Загружает фото с сайта Spacex. Укажите номер полета, если его не указать, то загрузятся фото с последнего полета',
                    )
        parser.add_argument("flight_id", nargs="?", help='Укажите номер полета.', default="latest")
        flight_id = parser.parse_args(sys.argv[1:]).flight_id
        if flight_id == "latest":
            response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
        else:
            response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
        response.raise_for_status()
        spacex_images = response.json()
        links = spacex_images['links']['flickr']['original']
        if not links:
            print("В последних полетах нет фото")
        else:
            for link_number, link in enumerate(links):
                download_image(link, 'images', f'space_{link_number}{get_links_ext(link)}')
    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}. Проверьте параметры запроса и доступность сервера.")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения. Проверьте подключение к интернету или доступность сервера.")


if __name__  == "__main__":
    main()