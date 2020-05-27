Title: Using Real Browsers
sortorder: 555

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/PIcfhlpq_xc" frameborder="0" allowfullscreen></iframe></div>

The technique shown in the previous chapter involved using `requests` to download HTML and `BeautifulSoup` to parse it. You'll find that that technique frequently fails, for one of two reasons:

1. Many websites load content using JavaScript ***after*** the initial HTML loads. `requests` can only load that initial HTML and isn't able to execute JavaScript.
2. The website you're trying to scrape might have some measures in place to block bots.

One method to (sometimes) get around these issues is to automate a real browser like Chrome or Firefox. This means that rather than just downloading the HTML content of a site, you actually open Chrome or Firefox on your computer and control it with a script. This tends to be a bit slower than downloading and parsing HTML, but gives you the ability to scrape otherwise-difficult sites, and allows you to do fun things like take screenshots and fill out forms.

The guide covers two browser automation libraries: [selenium](https://selenium-python.readthedocs.io/) and [puppeteer](https://pptr.dev).

## Selenium

Selenium is a library that allows you to control Chrome, Firefox and Safari from a variety of programming languages.

To install:

```bash
pip3 install selenium
```

You also need to install a "driver" for the browser you intend to automate. This is a kind of bridge application that allows selenium to communicate with a given browser.

For Chrome (on Mac):

```bash
brew cask install chromedriver
```

For Firefox:

```bash
brew install geckodriver
```

Scraping with selenium is very similar to BeautifulSoup. You create a `webdriver` object, visit a website, and then use css selectors to extract text and attributes from HTML elements. 

Note that the method to query by selector is `find_elements_by_css_selector` for multiple elements, and `find_element_by_css_selector` for just one element. To extract attributes like `href` or `src` use the `get_attribute` method.

Here's a simple example script that gets product names from Alibaba, searching fro the phrase "labor camp":


```python
# import the selenium
from selenium import webdriver

# open chrome
driver = webdriver.Chrome()

# visit alibaba
driver.get("https://www.alibaba.com/products/labor_camp.html?IndexArea=product_en&page=1")

# select h4 elements
items = driver.find_elements_by_css_selector("h4")

for i in items:
    print(i.text)

driver.close()
```

Please note that you must explicitly tell selenium to close the browser when you are done!

#### Headless Mode

Selenium can also operate in "headless" mode, which means that the browser will run without a graphic interface and never appear on your screen. I find that I prefer this mode once I've debugged my code and everything is working as intended. To use headless mode, you must instantiate your webdriver object with some additional parameters:

```bash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
```

#### Screenshots

Selenium allows you to change the window size of the browser and take screenshots:

```python
# take a square screenshot
driver.set_window_size(1000, 1000)
driver.save_screenshot("screenshot.png")
```

#### Forms

You can also fill out forms, which can allow you to log in to websites.

```python
# type "karl" into a "username" input
user = driver.find_element_by_css_selector(".username")
user.send_keys("karl")

# type "capit@l" into a password field
passw = driver.find_element_by_css_selector(".password")
passw.send_keys("capit@l")

# click on the submit button
submit = driver.find_element_by_css_selector(".submit")
submit.click()
```

#### JavaScript

Finally, selenium can execute JavaScript code.

```python
# javascript to replace all h2s with "lol"
script = """
let headlines = document.querySelectorAll("h1, h2, h3, h4, h5");
for (let h of headlines) {
  h.textContent = "Lol"
}
"""

# execute the script
driver.execute_script(script)

# save a screenshot
driver.save_screenshot("lol.png")
```

#### Selenium Examples

* [Alibaba Scraper](https://github.com/antiboredom/scrapism/blob/master/examples/alibaba_selenium.py): scrapes Alibaba for a search query, downloads product images, and saves product information into a json file called `product.json`
* [Fox News Lol](https://github.com/antiboredom/scrapism/blob/master/examples/foxlol.py): replaces headlines with "Lol" on foxnews.com and saves a screenshot
* [Breitbart Comments](https://github.com/antiboredom/scrapism/blob/master/examples/breitbart_comments.py): scrapes Breitbart for headlines and sorts them by total user comments


## Puppeteer {#puppeteer}

[Puppeteer](https://pptr.dev/) is a Node.js library written by Google for automating Chrome. There is also an (unofficial) Python version of it called [pyppeteer](https://github.com/pyppeteer/pyppeteer).

More to come!

## requests_html

[requests_html](https://requests-html.kennethreitz.org/) is a convenient library that combines `requests`, `pyquery` and `pyppeteer`. It provides less control than just using pyppeteer directly, but is extremely convenient for certain use cases.

More to come!
