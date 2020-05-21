"""
Retrieves all job headlines from a section in craigslist
"""

from bs4 import BeautifulSoup
import requests
import time


def get_page(url, start):
    params = {"s": start}
    r = requests.get(url, params=params)

    soup = BeautifulSoup(r.text, "lxml")
    titles = soup.select(".result-title")

    output = []
    for item in titles:
        output.append(item.text.strip())

    # or
    # output = [i.text.strip() for i in titles]

    return output


url = "https://newyork.craigslist.org/search/csr"
start = 0

while True:
    results = get_page(url, start)

    if len(results) == 0:
        break

    for r in results:
        print(r)

    start += 120

    time.sleep(1)
