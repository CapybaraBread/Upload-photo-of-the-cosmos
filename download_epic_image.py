import os
import requests
from download_images import download_image
from dotenv import load_dotenv
from urllib.parse import urlencode
from datetime import datetime


def download_epic_image(epic_api_key):
    
    base_url = "https://api.nasa.gov/EPIC/api/natural"
    archive_url = "https://api.nasa.gov/EPIC/archive/natural"
    params = {
        "api_key":epic_api_key,
    }
    response = requests.get(base_url, params=params) 
    response.raise_for_status()
    data = response.json()
    epic_urls = []
    for item in data:
        image_date = item['date']
        image_date_format = datetime.fromisoformat(image_date)
        image_date = datetime.date(image_date_format).strftime("%Y/%m/%d")   
        epic_url = f"{archive_url}/{image_date}/png/{item['image']}.png"
        epic_urls.append(epic_url)
    for idx, link in enumerate(epic_urls, start=1):
        download_image(link, f"NASA_EPIC_{idx}.png", "images", params)

if __name__ == '__main__':
    load_dotenv()
    epic_api_key=os.environ["EPIC_API_KEY"]
    try:
       download_epic_image()
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка при запросе к API NASA EPIC: {e}")
    except requests.exceptions.RequestException as a:
        print(f"Не удалось скачать картинку, ошибка:{a}")
    except (ValueError, requests.exceptions.JSONDecodeError) as e:
        print(f"Ошибка при обработке JSON ответа от NASA EPIC: {e}")
