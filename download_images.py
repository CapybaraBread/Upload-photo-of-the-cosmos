import requests
import os

def download_image(url, file_name, directory, params):
    save_path = os.path.join(directory, file_name)
    response = requests.get(url, params=params)
    os.makedirs(directory, exist_ok=True)
    with open(save_path, 'wb') as file:
        file.write(response.content)



