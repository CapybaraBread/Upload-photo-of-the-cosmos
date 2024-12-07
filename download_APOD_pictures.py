from urllib.parse import urlencode
import os
import requests
from download_images import download_image
from dotenv import load_dotenv



def download_apod_images(apod_token):
    apod_url = "https://api.nasa.gov/planetary/apod"
    count = 31 
    params = {
        'api_key': apod_token,
        'count': count
    }
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    nasa_images_json = response.json()
    for idx, image_json in enumerate(nasa_images_json, start=1):
        image_url = image_json.get("url") or image_json.get("hdurl")
        if image_url:
            download_image(image_url, f"NASA_{idx}.jpg","images", params)
if __name__ == '__main__':
    load_dotenv()
    apod_token=os.environ["APOD_TOKEN"]
    try:
        download_apod_images(apod_token)
    except(requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
        print(f"Ошибка при запросе к API NASA EPIC: {e}")
    except requests.exceptions.RequestException as a:
        print(f"Не удалось скачать картинку, ошибка:{a}")
