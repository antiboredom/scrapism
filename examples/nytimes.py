import requests
from bs4 import BeautifulSoup


r = requests.get("https://nytimes.com")

soup = BeautifulSoup(r.text, "html.parser")

titles = soup.select("h2")
for item in titles:
    # print(item)
    print(item.text)
