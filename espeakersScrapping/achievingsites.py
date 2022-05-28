import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

urls = [url.strip() for url in open('result_email_urls.txt').readlines()]
browser = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/espeakersScrapping/chromedriver')

with open('sites2.txt', 'a') as f:
    for x in range(len(urls)):
        start = time.time()
        browser.get(urls[x])
        browser.implicitly_wait(5)
        try:
            site = browser.find_element(by=By.CLASS_NAME, value='websiteLink')
            finish = time.time()
            print(site.text)
            print(f'Time for this page: {finish - start}')
            print(f'{x}/3700' + '\n')
            f.write(site.text + '\n')
        except NoSuchElementException:
            site = ''
            finish = time.time()
            print(site)
            print(f'Time for this page: {finish - start}')
            print(f'{x}/3700' + '\n')
            f.write(site + '\n')
        finally:
            browser.get(urls[x+1])
    f.close()

# browser.get('')
# browser.implicitly_wait(5)
# try:
#     site = browser.find_element(by=By.CLASS_NAME, value='websiteLink')
#     print(site.text)
# except NoSuchElementException:
#     site = ''
#     print(site)
# finally:
#     browser.close()
#     browser.quit()
