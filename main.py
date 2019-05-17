import requests

proxies = {
    "http": "http://127.0.0.1:8118",
    "https": "http://127.0.0.1:8118",
}


url = 'https://onezero.medium.com/why-airpods-and-earbuds-like-them-are-especially-bad-for-your-hearing-20f32b6e02e2'

r = requests.get(url, proxies=proxies)
print(r)

with open('page.html', 'w') as f:
    print(r.text, file=f)
