from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.breitbart.com/")
articles = driver.find_elements_by_css_selector("article")

output = []

for a in articles:
    title = a.find_element_by_css_selector("h2").text
    comments = a.find_element_by_css_selector(".byC").text
    comments = comments.replace(",", "")
    comments = int(comments)
    output.append((comments, title))

# output = sorted(output, key=lambda item: item[0])

output.sort()

for o in output:
    print(o[0], o[1])

driver.close()