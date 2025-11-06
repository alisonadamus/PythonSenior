import requests
from bs4 import BeautifulSoup

url = "https://www.ukr.net/"

# Ідентифікуємося як звичайний користувач (щоб сайт не заблокував)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    news_blocks = soup.find_all("a")
    for news_block in news_blocks:
        print(news_block.text)

else:
    print("Не вдалося завантажити сторінку:", response.status_code)
