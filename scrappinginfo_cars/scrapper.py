import requests
from bs4 import BeautifulSoup


url = 'https://turo.com/us/en/search?country=US&defaultZoomLevel=11&delivery=false&deliveryLocationType=city&endDate=08%2F15%2F2022&endTime=10%3A00&isMapSearch=false&itemsPerPage=200&latitude=37.3382082&location=San%20Chos%C4%97%2C%20CA%2C%20USA&locationType=CITY&longitude=-121.88632860000001&placeId=ChIJ9T_5iuTKj4ARe3GfygqMnbk&region=CA&sortType=RELEVANCE&startDate=08%2F01%2F2022&startTime=10%3A00&useDefaultMaximumDistance=true'

page = requests.get(url)

print(page.text)