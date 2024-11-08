# Скачивание космических изображений и бот для Telegram

Этот проект включает несколько Python-скриптов для загрузки изображений, связанных с космосом, из различных API (NASA APOD, NASA EPIC, SpaceX), а также бот для отправки случайных изображений в канал Telegram. В данном руководстве вы найдете информацию о каждом из скриптов.

## Содержание

- [Скрипты](#скрипты)
  - [download_APOD_pictures.py](#download_apod_picturespy)
  - [download_epic_image.py](#download_epic_imagepy)
  - [download_images.py](#download_imagespy)
  - [downloading_SpaceX_pictures.py](#downloading_spacex_picturespy)
  - [file_extensio.py](#file_extensiopy)
  - [send_foto_bot.py](#send_foto_botpy)
- [Установка и запуск](#установка-и-запуск)
- [Переменные окружения](#переменные-окружения)
- [Требования](#требования)

## Скрипты

### download_APOD_pictures.py

Этот скрипт загружает случайные изображения с сайта NASA APOD (Astronomy Picture of the Day).

#### Описание:
- Скрипт использует NASA API для запроса случайных изображений (по умолчанию 31 изображение).
- Для каждого изображения вызывается функция `download_image` из файла `download_images.py`, которая сохраняет его на диск.

#### Использование:
Запуск скрипта начнет загрузку изображений и сохранит их в папку "images":
```bash
python download_APOD_pictures.py
```

### download_epic_image.py

Скрипт загружает изображения с EPIC (Earth Polychromatic Imaging Camera), который делает снимки Земли.

#### Описание:
- Использует API EPIC от NASA для получения ссылок на изображения.
- Загружает изображения в формате PNG и сохраняет их на локальный диск с помощью функции `download_image`.

#### Использование:
```bash
python download_epic_image.py
```

### download_images.py

Вспомогательный скрипт, который содержит функцию `download_image` для загрузки изображений по URL.

#### Функции:
- `download_image(url, file_name, directory)`: загружает изображение по указанному URL и сохраняет его в указанную директорию.

### downloading_SpaceX_pictures.py

Скрипт для загрузки изображений последнего запуска SpaceX.

#### Описание:
- Получает URL изображения с последнего запуска SpaceX с помощью API SpaceX.
- Скачивает изображения с Flickr и сохраняет их на локальный диск.

#### Использование:
```bash
python downloading_SpaceX_pictures.py
```

### file_extensio.py

Скрипт для получения расширения файла по URL.

#### Описание:
- Функция `get_file_extension(url)` возвращает расширение файла, используя стандартные функции библиотеки `os`.

### send_foto_bot.py

Скрипт для отправки случайных изображений из локальной папки в Telegram-канал через бота.

#### Описание:
- Использует библиотеку `python-telegram-bot` для отправки изображений.
- Выбирает случайное изображение из папки и отправляет его в указанный канал.
- Работает в цикле с задержкой, задаваемой переменной окружения.

#### Использование:
```bash
python send_foto_bot.py
```

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone <URL репозитория>
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Настройте переменные окружения (см. ниже).

4. Запустите любой из скриптов, например:
   ```bash
   python download_APOD_pictures.py
   ```

## Переменные окружения

Для работы некоторых скриптов требуются переменные окружения, которые можно определить в файле `.env`:
- `TELEGRAM_BOT_TOKEN`: токен вашего Telegram-бота.
- `TELEGRAM_CHANNEL_ID`: ID канала Telegram, куда будут отправляться изображения.
- `PUBLICATION_DELAY`: задержка между публикациями (в секундах).

## Требования

- Python 3.x
- Библиотеки:
  - `requests`
  - `python-telegram-bot`
  - `python-dotenv`

---
