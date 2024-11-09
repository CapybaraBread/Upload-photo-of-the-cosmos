import os
import requests
from download_images import download_image
from dotenv import load_dotenv
from urllib.parse import urlencode
from datetime import datetime
load_dotenv()

def get_epic_image_links():
    api_key=os.getenv("API_KEY")
    base_url = "https://api.nasa.gov/EPIC/api/natural"
    archive_url = "https://api.nasa.gov/EPIC/archive/natural"
    params = {
        "api_key":api_key,
    }
    try:
        response = requests.get(base_url, params=params) 
    except (requests.exceptions.RequestException,requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
        print(f"Ошибка при запросе к API NASA EPIC: {e}")
        return
    try:
        data = response.json()
    except (ValueError, requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
        print(f"Ошибка при обработке JSON ответа от NASA EPIC: {e}")
        return
    epic_urls = []
    for item in data:
        image_date = item['date']
        image_date_format = datetime.fromisoformat(image_date)
        image_date = datetime.date(image_date_format).strftime("%Y/%m/%d")   
        epic_url = f"{archive_url}/{image_date}/png/{item['image']}.png?api_key={api_key}"
        epic_urls.append(epic_url)
    for idx, link in enumerate(epic_urls, start=1):
        download_image(link, f"NASA_EPIC_{idx}.png", "images")

if __name__ == '__main__':
    get_epic_image_links()