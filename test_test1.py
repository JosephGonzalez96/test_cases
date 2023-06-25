from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")

# browser = webdriver.Chrome()
browser = webdriver.Chrome(options=chrome_options)

# browser.get('https://www.youtube.com/')

# elem = browser.find_element(By.NAME, 'search_query')  # Find the search box
# elem.send_keys('por un segundo')
# elem.send_keys(Keys.ENTER)
# print("Test completed succesfully")


browser.get('https://linux.how2shout.com/how-to-install-and-use-chrome-headless-on-ubuntu/')

elem = browser.find_element(By.XPATH, '//*[@class="entry-title"]')  # Find the search box
text = elem.get_attribute('innerText')
print(text)
print("Test completed succesfully")
