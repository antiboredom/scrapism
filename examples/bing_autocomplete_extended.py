from bs4 import BeautifulSoup
import requests


def auto_complete(query):
    url = (
        "https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry="
        + query
        + "&cp=10&cvid=B8D86CB090A240A196E4867715E40B15"
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("li")
    for item in items:
        print(item.text)


base_query = "How can I "
for letter in "abcdefghijklmnopqrstuvwxyz":
    auto_complete(base_query + letter)
    for letter2 in "abcdefghijklmnopqrstuvwxyz":
        auto_complete(base_query + letter + letter2)
