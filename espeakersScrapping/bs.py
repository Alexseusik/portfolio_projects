import time
from selenium import webdriver
from selenium.webdriver.common.by import By


urls = [url.strip() for url in open('result_email_urls.txt').readlines()]
browser = webdriver.Chrome(executable_path='D:\portfolio_projects\espeakersScrapping\chromedriver_win32\chromedriver.exe')



with open('emails.txt', 'a') as f:
    for url in urls:
        browser.get(url)
        browser.implicitly_wait(5)
        email = browser.find_element(by=By.XPATH, value="//span[@style='unicode-bidi: bidi-override; direction: rtl;']")
        print(email.text[::-1])
        if urls.index(url) <= len(urls):
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[urls.index(url)+1])

    f.close()
