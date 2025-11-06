import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/?"

# Ідентифікуємося як звичайний користувач (щоб сайт не заблокував)
headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/91.0.4472.124'
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())

    main_div = soup.find("div", id="tab_newreleases_content")
    cards = main_div.find_all("a", class_="tab_item")
    for card in cards:
        name = card.find("div", class_="tab_item_name")
        tags = card.find("div", class_="tab_item_top_tags")
        price = card.find("div", class_="discount_final_price")

        print(name.text.upper())
        print(tags.text)
        print(price.text)
        print()

else:
    print("Не вдалося завантажити сторінку:", response.status_code)
