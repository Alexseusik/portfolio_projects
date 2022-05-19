driver =
url = 'https://www.espeakers.com/s/nsas/profile/'
profile_urls = [url + el.get_attribute('id')[3:] for el in driver.find_elements(By.CSS_SELECTOR, '.speaker-tile')]
names = [el.text for el in driver.find_elements(By.CSS_SELECTOR, '.speaker-name')]