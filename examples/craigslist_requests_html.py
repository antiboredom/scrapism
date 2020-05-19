from requests_html import HTMLSession

s = HTMLSession()

r = s.get("https://newyork.craigslist.org/d/security/search/sec")

html = r.html.html
print(html)

titles = r.html.find(".result-title")

for item in titles:
    print(item.text)
    print(item.attrs["href"])
