import datetime
import json
import re
import sys
import requests
from bs4 import BeautifulSoup
import os
import shutil

full_data = []

url_index = BeautifulSoup(requests.get('https://coinmarketcap.com/nft/upcoming/').text, 'lxml')\
    .find_all('li', class_='page')[-1].text

indexes = [int(x) for x in range(1, int(url_index)+1)]  # From 1 page to last

urls = [f'https://coinmarketcap.com/nft/upcoming/?page={i}' for i in indexes]

# creating dirs
if os.path.isfile('json_data.json') is False:
    for i in indexes:
        try:
            os.mkdir(f'page{i}')
        except OSError:
            pass

# SAVING PAGES TO HAVE BETTER ACCESS AND DO NOT OVER LOAD SITE
for url, i in zip(urls, indexes):
    page = requests.get(url).text
    if os.path.isdir(f'page{i}'):
        with open(f'page{i}/page{i}.html', 'a') as f:
            f.write(page)
            f.close()

dir_list = []
for dr in sorted(os.listdir()):
    dr_name = re.search('page\d+', dr)
    if dr_name is not None:
        dir_list.append(dr_name.group(0))
    else:
        continue
# To receive only names of dirs without other files

if os.path.isfile('json_data.json'):
    print('File exists!')
    sys.exit()

for dr, i in zip(dir_list, indexes):
    with open(f'page{i}/page{i}.html') as html_file:
        print(f'<---- File page{i}.html opened successfully! ---->')
        rows = BeautifulSoup(html_file, 'lxml').find_all('tr')[1:]  # First element is names for columns so we avoid it
        for row in rows:
            # Extracting name and description
            title = row.find('div', class_='sc-15yqupo-0').find_all('p')
            NAME = title[0].find('span').string
            DESCRIPTION = title[1].string
            ECOSYSTEM = row.find('span', class_='lsid7u-0').text
            print(f'<---- NAME, DESCRIPTION, ECOSYSTEM derrived successfully! ---->')
            # Extracting socials
            socials = row.find('div', class_='sc-15yqupo-1').find_all('p')
            DISCORD = socials[0].find('a').get('href')
            TWITTER = socials[1].find('a').get('href')
            WEBSITE = socials[2].find('a').get('href')
            print(f'<---- SOCIALS derrived successfully! ---->')
            # START DATE
            start_date_raw = row.find('div', class_='sc-15yqupo-2').find_all('p')[1].text
            START_DATE = datetime.datetime.strptime(start_date_raw, '%m/%d/%Y, %H:%M:%S %p')
            print(f'<---- START_DATE derrived successfully! ---->')
            # SALE INFO
            sales = row.find('div', class_='sc-1ay2tc4-0').find_all('span')
            if len(sales) == 2:
                PRE_SALE = re.search('(?<=Pre-sale: )(.+)|(?<=Sale: )(.+)', sales[0].text).group(0)
                SALE = re.search('(?<=Pre-sale: )(.+)|(?<=Sale: )(.+)', sales[1].text).group(0)
            else:
                PRE_SALE = None
                SALE = re.search('(?<=Pre-sale: )(.+)|(?<=Sale: )(.+)', sales[0].text).group(0)
            print(f'<---- SALE PRICE derrived successfully! ---->')
            data_dict = {
                'NAME' : NAME,
                'DESCRIPTION' : DESCRIPTION,
                'ECOSYSTEM' : ECOSYSTEM,
                'DISCORD' : DISCORD,
                'TWITTER' : TWITTER,
                'WEBSITE' : WEBSITE,
                'START_DATE' : str(START_DATE),
                'PRE_SALE' : PRE_SALE,
                'SALE' : SALE
            }
            full_data.append(data_dict)
            print(f'{NAME} info is added to file \n\n\n')

json_full_data = json.dumps(full_data, indent=2)

for dr in dir_list:
    shutil.rmtree(dr)
# Deleting unusful files containing pages of our site

with open('json_data.json', 'w+') as f:
    f.write(json_full_data)
    f.close()
