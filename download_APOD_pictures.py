import os
import requests
from download_images import download_image
from dotenv import load_dotenv
import argparse


def download_apod_images(epic_api_key):
    apod_url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': epic_api_key,
        'count': int(count)
    }
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for idx, image_json in enumerate(nasa_images, start=1):
        image_url = image_json.get("url") or image_json.get("hdurl")
        if image_url:
            directory = args.directory
            download_image(image_url, f"NASA_{idx}.jpg", directory, params)


if __name__ == '__main__':
    load_dotenv()
    paser_count = argparse.ArgumentParser(
        description="Сколько изображений вы хотите загрузить?"
    )
    paser_count.add_argument(
        '--count',
        type=int,
        default=31,
        help='Сколько изображений вы хотите загрузить?'
    )
    args = paser_count.parse_args()
    count = args.count
    parser = argparse.ArgumentParser(
                description="Скрипт для загрузки космических изображений"
                )
    parser.add_argument(
                '--directory',
                type=str,
                default='./images',
                help='Путь к папке для сохранения изображений'
    )
    args = parser.parse_args()
    epic_api_key = os.environ["EPIC_API_KEY"]
    try:
        download_apod_images(epic_api_key)
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.JSONDecodeError
    ) as e:
        print(f"Ошибка при запросе к API NASA EPIC: {e}")
    except requests.exceptions.RequestException as a:
        print(f"Не удалось скачать картинку, ошибка:{a}")
