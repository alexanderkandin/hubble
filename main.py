import requests
import argparse
import sys
import os
import urllib.parse
from dotenv import load_dotenv


def download_image(url_user, folder, name):
    save_path = os.path.join(os.getcwd(), folder, name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url_user)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch():
    parser = argparse.ArgumentParser()
    parser.add_argument("flight_id", nargs="?", default="latest")
    id = parser.parse_args(sys.argv[1:]).flight_id
    if id == "latest":
        response = requests.get(f'https://api.spacexdata.com/v3/launches/{id}')
    else:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    launch_data = response.json()
    links = launch_data['links']['flickr']['original']
    count = 0
    for link in links:
        count += 1
        download_image(link, 'images', f'space_{count}{get_links_ext(link)}')


def get_links_NASA():
    load_dotenv()
    api_key = os.getenv("API_KEY")
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


def get_links_ext(url):
    decode_url = urllib.parse.unquote(
        url)
    url = urllib.parse.urlparse(decode_url).path
    _, ext = os.path.splitext(url)
    return ext


def get_links_EPIC():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    payload = {
        "api_key": api_key,
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payload)
    response.raise_for_status()
    launch_data = response.json()
    image_id = [item["image"] for item in launch_data]
    image_date = [item["date"] for item in launch_data]
    for i in range(0, len(image_date)):
        date = str(image_date[i].split(" ")[0]).replace('-', '/')
        id = image_id[i]
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{id}.png?api_key=gdPzfbvhAsScM7wQyZRkUkMllJEmTzaS5Br4uPii'
        download_image(url,"epic",f'NASA_{i}{get_links_ext(url)}')


def main():
    get_links_NASA()

if __name__ == "__main__":
    main()

# flight_id = '5eb87d47ffd86e000604b38a'
# "api_key": "gdPzfbvhAsScM7wQyZRkUkMllJEmTzaS5Br4uPii"

