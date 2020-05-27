import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import wget


def download_image(url):
    image_name = url.split("/")[-1]
    destination = "images/" + image_name
    if os.path.exists(destination):
        return True
    wget.download(url, destination)


def get_items(search, page):
    search = search.replace(" ", "_")
    url = "https://www.alibaba.com/products/{}.html?IndexArea=product_en&page={}".format(
        search, page
    )
    driver.get(url)

    # sleep for a second then scroll to the bottom of the page
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    items = driver.find_elements_by_css_selector(".J-offer-wrapper")
    output = []

    for i in items:
        try:
            price = i.find_element_by_css_selector(".gallery-offer-price").text
        except:
            price = None

        try:
            name = i.find_element_by_css_selector("h4").text
        except:
            name = None

        try:
            product_url = i.find_element_by_css_selector("h4 a").get_attribute("href")
        except:
            product_url = None

        try:
            product_image = i.find_element_by_css_selector(".seb-img-switcher__imgs").get_attribute("data-image")
            product_image = "http:" + product_image
        except:
            product_image = None

        if product_image:
            try:
                download_image(product_image)
            except Exception as e:
                print(e)

        output_item = {"name": name, "price": price, "url": product_url, "image": product_image}
        output.append(output_item)

    return output


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

page = 1
search = "riot gear"
all_items = []

while True:
    print("getting page", page)
    results = get_items(search, page)
    all_items += results

    if len(results) == 0:
        break

    page += 1

# save all the items to a json file
json.dump(all_items, open("product.json", "w"), indent=2)

driver.close()