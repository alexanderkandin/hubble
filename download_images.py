import requests
import os



def download_image(url, folder, name, payload=None):
    save_path = os.path.join(os.getcwd(), folder, name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url,params=payload) if payload else requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)