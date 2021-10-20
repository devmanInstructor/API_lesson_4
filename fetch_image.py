import requests
import os
from urllib.parse import urlparse
import urllib3
urllib3.disable_warnings()

def fetch_image(image_url, image_dir, image_name, payload = ''):
    filename = f'{image_dir}/{image_name}{get_file_ext_from_url(image_url)}'
    response = requests.get(image_url, verify=False, params=payload)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def get_file_ext_from_url(url):
    parsed_url_path = urlparse(url).path
    extension = os.path.splitext(parsed_url_path)[1]
    return extension
