import requests

class Downloader:

    def __init__(self, proxies):
        self.proxies = proxies

    def download_page(self, url, file_path):
        r = requests.get(url, proxies=self.proxies)
        print(r)

        with open(file_path, 'w') as f:
            print(r.text, file=f)
