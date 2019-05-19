from pathlib import Path

import yaml

from humanize import naturalsize

from mediume.downloader import Downloader

network_setting = Path('.') / 'settings' / 'network.yaml'

url = 'https://onezero.medium.com/why-airpods-and-earbuds-like-them-are-especially-bad-for-your-hearing-20f32b6e02e2'
file_path = Path('.') / 'page.html'


if __name__ == '__main__':


    with network_setting.open('r') as f:
        yaml_object = yaml.load(f, Loader=yaml.FullLoader)

    proxies = yaml_object['proxies']
    print('proxies:', proxies)

    def on_progress(got, total=None, done=False):
        if done:
            print('(Downloading ... {} got.)'.format(naturalsize(got)))
            return
        if total is None:
            text = '(Downloading ... {}'.format(naturalsize(got))
        else:
            text = '(Downloading ... {}/{}'.format(naturalsize(got), naturalsize(total))
        print(text, end='\r')

    downloader = Downloader(proxies=proxies)
    downloader.download_page(url, file_path, on_progress=on_progress)