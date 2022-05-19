import time
from selenium import webdriver
from selenium.webdriver.common.by import By

profile_url = 'https://www.espeakers.com/s/nsas/profile/'
url = 'https://www.espeakers.com/s/nsas/search?available_on=&awards&budget=0%2C10&bureau_id=304&distance=100&fee=false&items_per_page=3701&language=en&location=&norecord=false&nt=0&page=0&presenter_type=&q=%5B%5D&require&review=false&sort=speakername&video=false&virtual=false'
driver = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/espeakersScrapping/chromedriver')
emails = []
try:
    driver.get(url=url)
    time.sleep(1)
    button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/div[2]/div/div/div/div[1]/div/form/div[1]/div[3]/div/button')
    button.click()
    time.sleep(5)
    profile_urls = [profile_url + el.get_attribute('id')[3:] for el in driver.find_elements(By.CSS_SELECTOR, '.speaker-tile')]
    with open('result_email_urls.txt', 'a') as f:
        for profile, i in zip(profile_urls, range(3701)):
            f.write(profile+'\n')
            print(f'{i} saved!')
        f.close()
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()



