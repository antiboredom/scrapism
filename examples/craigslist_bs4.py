from bs4 import BeautifulSoup
import requests

r = requests.get("https://newyork.craigslist.org/d/security/search/sec")
# print(r.text)

soup = BeautifulSoup(r.text, "lxml")
titles = soup.select(".result-title")

for item in titles:
    # print(item)
    print(item.text)
    print(item.get("href"))
