import requests
from bs4 import BeautifulSoup
import re

ids = list(range(1, 51))

urls = [f'https://russia.gorodrabot.ru/resumes?p={i}' for i in ids]

# result = []
#
# for i, url in zip(ids, urls):
#     page = requests.get(url).text
#     soup = BeautifulSoup(page, 'lxml')
#     links = soup.find_all('a', class_='snippet__title-link')
#     for link in links:
#         res = link['href']
#         print(res)
#         result.append(res)
#
# with open('links.txt', 'a') as f:
#     for res in result:
#         f.write(res+'\n')
#     f.close()




