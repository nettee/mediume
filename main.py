from pathlib import Path

import yaml

from mediume.downloader import Downloader


if __name__ == '__main__':

    network_setting = Path('.') / 'settings' / 'network.yaml'
    with network_setting.open('r') as f:
        yaml_object = yaml.load(f, Loader=yaml.FullLoader)

    proxies = yaml_object['proxies']
    print(proxies)

    url = 'https://onezero.medium.com/why-airpods-and-earbuds-like-them-are-especially-bad-for-your-hearing-20f32b6e02e2'
    file_path = 'page.html'

    downloader = Downloader(proxies=proxies)
    downloader.download_page(url, file_path)