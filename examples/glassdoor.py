from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=correct&sc.keyword=Correctional+Officer&locT=C&locId=1132348&jobType=")

print(r.text)
soup = BeautifulSoup(r.text)
jobs = soup.select(".jobContainer")

for item in jobs:
    print(item.text)

# from requests_html import HTMLSession
#
# s = HTMLSession()
#
# r = s.get("https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=correct&sc.keyword=Correctional+Officer&locT=C&locId=1132348&jobType=")
#
# jobs = r.html.find(".jobContainer")
#
# for item in jobs:
#     print(item.text)
