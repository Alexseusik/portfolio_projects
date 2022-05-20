import time
from selenium import webdriver
from selenium.webdriver.common.by import By

urls = [url.strip() for url in open('result_email_urls.txt').readlines()]
browser = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/espeakersScrapping/chromedriver')

with open('email2.txt', 'a') as f:
    for x in range(len(urls)):
        start = time.time()
        browser.get(urls[x])
        browser.implicitly_wait(5)
        email = browser.find_element(by=By.XPATH, value="//span[@style='unicode-bidi: bidi-override; direction: rtl;']")
        finish = time.time()
        print(email.text[::-1])
        print(f'Time for this page: {finish-start}')
        print(f'{x}/3701' + '\n')
        f.write(email.text[::-1]+'\n')
    f.close()
