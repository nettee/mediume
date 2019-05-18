import requests

class Downloader:

    def __init__(self, proxies):
        self.proxies = proxies

    def download_page(self, url, file_path):

        with requests.get(url, proxies=self.proxies, stream=True) as r:
            r.raise_for_status()
            with file_path.open('wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
