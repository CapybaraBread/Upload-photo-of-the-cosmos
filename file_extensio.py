import os
def get_file_extension(url):
    image_format_extractor = os.path.splitext(url)
    image_format = image_format_extractor[1]
    return image_format