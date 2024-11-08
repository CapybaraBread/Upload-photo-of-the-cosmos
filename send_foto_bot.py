import telegram
import random
import os
import time
from dotenv import load_dotenv
import argparse
def send_random_image(TELEGRAM_BOT_TOKEN, IMAGES_FOLDER, TELEGRAM_CHANNEL_ID):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    

    images = [f for f in os.listdir(IMAGES_FOLDER) if os.path.isfile(os.path.join(IMAGES_FOLDER, f))]
    

    random_image = random.choice(images)
    image_path = os.path.join(IMAGES_FOLDER, random_image)
    

    with open(image_path, 'rb') as image_file:
        bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=image_file)
        print(f"Изображение '{random_image}' отправлено в канал.")

def main(directory):
    load_dotenv()
    TELEGRAM_BOT_TOKEN = os.environ("TELEGRAM_BOT_TOKEN")
    PUBLICATION_DELAY = int(os.getenv("PUBLICATION_DELAY", 14400))
    TELEGRAM_CHANNEL_ID = os.environ("TELEGRAM_CHANNEL_ID")

    while True:
        send_random_image(TELEGRAM_BOT_TOKEN, directory, TELEGRAM_CHANNEL_ID)
        time.sleep(PUBLICATION_DELAY)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скрипт для загрузки космических изображений")
    parser.add_argument('--directory', type=str, default='./images', help='Путь к папке для сохранения изображений')
    args = parser.parse_args()
    main(args.directory)