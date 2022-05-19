import time
from selenium import webdriver
from fake_useragent import UserAgent
from fake_useragent import FakeUserAgentError

fakeua = None
try:
    fakeua = UserAgent()
except FakeUserAgentError:
    pass

ua = fakeua if (fakeua is not None) else 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) ' \
                                       'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                       'Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua}")
browser = webdriver.Chrome(executable_path='/Users/alexseyhnibida/Desktop/work/selenium_practice/chromedriver',
                           options = options)

try:
    browser.get(url='https://rezka.ag/')
    time.sleep(2)
except Exception as e:
    print(e)
finally:
    browser.close()
    browser.quit()
