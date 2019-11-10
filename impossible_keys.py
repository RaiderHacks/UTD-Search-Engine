from selenium import webdriver

from selenium.webdriver.common.keys import keys

browser = webdriver.Firefox()

browser.get('https://nostarch.com')

htmlElem = browser.find_element_by_tag_name('html')

htmlElem.send_keys(Keys.END)

htmlElem.send_keys(Keys.HOME)
