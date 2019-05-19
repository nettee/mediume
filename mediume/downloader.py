import mimeparse
import requests


class Downloader:

    def __init__(self, proxies):
        self.proxies = proxies

    def download_page(self, url, file_path, on_progress):

        with requests.get(url, proxies=self.proxies, stream=True) as r:
            r.raise_for_status()

            mime_type = r.headers['Content-Type']
            main_type, sub_type, params = mimeparse.parse_mime_type(mime_type)
            charset = params.get('charset', 'utf-8')
            print('charset:', charset)

            if 'Content-Length' in r.headers:
                total = r.headers['Content-Length']
            else:
                total = None

            with file_path.open('w') as f:
                got = 0
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        got += len(chunk)
                        on_progress(got, total)
                        f.write(chunk.decode(charset))
                on_progress(got, total, done=True)
