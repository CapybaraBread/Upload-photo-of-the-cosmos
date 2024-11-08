import requests
import os

def download_image(url, file_name, directory):
    save_path = os.path.join(directory, file_name)
    try:
        response = requests.get(url)

    except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
        print(f"Ошибка при загрузке изображения по URL {url}: {e}")
        return

    os.makedirs(directory, exist_ok=True)
    with open(save_path, 'wb') as file:
        file.write(response.content)



