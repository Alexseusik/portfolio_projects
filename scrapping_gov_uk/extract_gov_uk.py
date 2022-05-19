from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

browser = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/selenium_practice/chromedriver')

url = 'https://www.flhsmv.gov/motor-vehicles-tags-titles/dealers-installers-manufacturers-distributors-importers/mv-rv-mh-dealer-broker-licenses/list-licensed-dealers/licensed-franchise-and-service-facility-dealers/'


try:
    browser.get(url=url)
    time.sleep(5)
    browser.refresh()
    browser.get_screenshot_as_file('first.png')
except Exception as e:
    print(e)
finally:
    browser.close()
    browser.quit()

