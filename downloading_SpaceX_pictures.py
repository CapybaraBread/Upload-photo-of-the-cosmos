import requests
from download_images import download_image
import argparse
import random


def download_spacex_foto():
    response = requests.get(
         "https://api.spacexdata.com/v5/launches/", params=None
    )
    response.raise_for_status()
    random_number = random.randint(1, 30)
    image_links = response.json()[random_number]["links"]["flickr"]["original"]
    for idx, image_url in enumerate(image_links, start=1):
        directory = args.directory
        try:
            download_image(
                image_url,
                f"spacex_image_{idx}.jpg",
                directory,
                params=None
            )
        except requests.exceptions.RequestException as a:
            print(f"Не удалось скачать картинку, ошибка:{a}")


if __name__ == '__main__':
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
    try:
        download_spacex_foto()
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.JSONDecodeError,
        ValueError,
        KeyError,
        IndexError
    ) as e:
        print(f"Ошибка при запросе к API SpaceX: {e}")
