from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox()

browser.get('https://www.youtube.com/')

elem = browser.find_element(By.NAME, 'search_query')  # Find the search box
elem.send_keys('por un segundo')
elem.send_keys(Keys.ENTER)
print("Test completed succesfully")