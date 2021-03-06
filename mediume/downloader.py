import mimeparse
import requests
import yaml


class Downloader:

    def __init__(self):
        with open('settings/network.yaml', 'r') as f:
            yaml_object = yaml.load(f, Loader=yaml.FullLoader)
        self.proxies = yaml_object['proxies']

    def download_page(self, url):

        with requests.get(url, proxies=self.proxies, stream=True) as r:
            r.raise_for_status()

            mime_type = r.headers['Content-Type']
            main_type, sub_type, params = mimeparse.parse_mime_type(mime_type)
            charset = params.get('charset', 'utf-8')
            print('charset:', charset)

            data = ''
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    data += chunk.decode(charset)
            return data
