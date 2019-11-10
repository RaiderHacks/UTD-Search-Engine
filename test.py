from selenium import webdriver

browser = webdriver.Firefox()

print(type(browser))

browser.get('https://inventwithpython.com')

linkElem = browser.find_element_by_link_text('Read Online for Free')

print(type(linkElem))

linkElem.click()
