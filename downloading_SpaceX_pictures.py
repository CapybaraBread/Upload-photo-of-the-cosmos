import os
import requests
from download_images import download_image


def download_spacex_foto():
    params = {
         "id":"5eb87d47ffd86e000604b38a"
    }
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_image(image_url, "hubble.jpeg", "images", params )

    response = requests.get("https://api.spacexdata.com/v5/launches/", params=params) 
    response.raise_for_status()
    image_links = response.json()[19]["links"]["flickr"]["original"]

    for idx, image_url in enumerate(image_links, start=1):
            download_image(image_url, f"spacex_image_{idx}.jpg", "images", params)
if __name__ == '__main__':
    try:
        download_spacex_foto()
    except(requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError, ValueError, KeyError, IndexError) as e:
        print(f"Ошибка при запросе к API SpaceX: {e}")
    except requests.exceptions.RequestException as a:
        print(f"Не удалось скачать картинку, ошибка:{a}")
