import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

email = 'alexgnibeda03@gmail.com'
password = 'tiA7YIoU'

driver = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/extractphonesandemailsfromGORODRABOT/chromedriver')
links = [link.strip() for link in open('links.txt').readlines()]
print(links)

try:
    driver.get('https://gorodrabot.ru/site/login')
    driver.find_element(by=By.NAME, value='email').send_keys(email)
    driver.find_element(by=By.NAME, value='password').send_keys(password)
    driver.find_element(by=By.CLASS_NAME, value='button').click()

    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    errors = driver.find_elements(by=By.CLASS_NAME, value="flash-error")
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")

    for link in links:
        driver.get(link)
        driver.find_element(by=By.CLASS_NAME, value='resume-view__action').click()
        email = driver.find_element(by=By.CLASS_NAME, value='contacts-info__content').text
        time.sleep(5)
        print(email)
except Exception as e:
    print(e)
finally:
    driver.close()
