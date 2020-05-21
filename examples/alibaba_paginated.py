import time
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0",
}

def get_page(search, page):
    url = "https://www.alibaba.com//trade/search"
    params = {
        "fsb": "y",
        "IndexArea": "product_en",
        "CatId": "",
        "SearchText": search,
        "page": page,
    }

    r = requests.get(url, params=params, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    items = soup.select(".organic-list-offer-outter")

    for item in items:
        title = item.select_one("h4").text.strip()
        price_element = item.select_one(".gallery-offer-price")
        if price_element:
            price = price_element.text.strip()
        else:
            price = None

        print(title, price)


for i in range(1, 1000):
    get_page("riot gear", i)
    time.sleep(4)
