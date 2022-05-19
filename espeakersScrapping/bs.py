import time
from selenium import webdriver
from selenium.webdriver.common.by import By


urls = [url.strip() for url in open('result_email_urls.txt').readlines()]
browser = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/espeakersScrapping/chromedriver')

with open('emails.txt', 'a') as f:
    for x in range(len(urls)):
        browser.get(urls[x])
        time.sleep(1)
        check_len = browser.find_element(by=By.XPATH,
                    value='//*[@id="profileLeftSidebar"]/div[4]')\
                    .find_elements(by=By.TAG_NAME, value = 'div')
        if len(check_len) <= 8:
            email = browser.find_element(by=By.CSS_SELECTOR, value= '#profileLeftSidebar > div:nth-child(4) > div:nth-child(1) > span')
            print(email.text[::-1])
            f.write(email.text[::-1]+'\n')
        else:
            email = browser.find_element(by=By.CSS_SELECTOR, value= '#profileLeftSidebar > div:nth-child(4) > div:nth-child(2) > span')
            print(email.text[::-1])
            f.write(email.text[::-1]+'\n')
        if x < len(urls):
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[x+1])

