from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.set_window_size(1200, 1200)
driver.get("https://foxnews.com")

# javascript to replace many elements with "lol"
script = """
let headlines = document.querySelectorAll("h1, h2, h3, h4, h5, nav a");
for (let h of headlines) {
  h.textContent = "Lol"
}
"""

# execute the script
driver.execute_script(script)

# save a screenshot
driver.save_screenshot("lol.png")