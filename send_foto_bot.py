import telegram
import random
import os
import time
from dotenv import load_dotenv
import argparse



def send_random_image(token, folder, channel_id):
    bot = telegram.Bot(token=token)
    

    images = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    

    random_image = random.choice(images)
    image_path = os.path.join(folder, random_image)
    

    with open(image_path, 'rb') as image_file:
        bot.send_photo(chat_id=channel_id, photo=image_file)
        print(f"Изображение '{random_image}' отправлено в канал.")

def main():
    load_dotenv()
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    publication_delay= int(os.getenv("PUBLICATION_DELAY", 14400))
    telegram_channel_id = os.environ["TELEGRAM_CHANNEL_ID"]
    parser = argparse.ArgumentParser(description="Скрипт для загрузки космических изображений")
    parser.add_argument('--directory', type=str, default='./images', help='Путь к папке для сохранения изображений')
    args = parser.parse_args()
    directory = args.directory
    while True:
        send_random_image(telegram_bot_token, directory, telegram_channel_id)
        time.sleep(publication_delay)

        
if __name__ == "__main__":
    main()
    