from bs4 import BeautifulSoup
import requests

base_url = "https://newyork.craigslist.org"
r = requests.get(base_url)

soup = BeautifulSoup(r.text, "lxml")
job_cats = soup.select(".jobs .cats a")

for job in job_cats:
    url = job.get("href")
    name = job.text.strip()
    full_url = base_url + url
    r = requests.get(full_url)
    soup = BeautifulSoup(r.text, "lxml")
    total = soup.select_one(".totalcount").text.strip()
    print(name, total)

