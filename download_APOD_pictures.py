from urllib.parse import urlencode
import os
import requests
from download_images import download_image
from dotenv import load_dotenv



def fetch_apod_images(apod_tocen):
    apod_url = "https://api.nasa.gov/planetary/apod?"
    count = 31 
    params = {
        'api_key': apod_tocen,
        'count': count
    }
    
    try:
        respons = requests.get(apod_url, params=params)
    except (requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
        print(f"Ошибка при запросе к API NASA EPIC: {e}")
        return
    
    try:
        nasa_images_json = respons.json()
    except (requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError):
        return
    
    for idx, image_json in enumerate(nasa_images_json, start=1):
        image_url = image_json.get("url") or image_json.get("hdurl")
        if image_url:
            download_image(image_url, f"NASA_{idx}.jpg","images")
if __name__ == '__main__':
    load_dotenv()
    apod_tocen=os.getenv("apod_tocen")
    fetch_apod_images(apod_tocen)