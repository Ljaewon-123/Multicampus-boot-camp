from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = 'https://pixabay.com/images/search/'

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.implicitly_wait(3)   # 3초 기다렸다가 url 가져오겠다
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')

div = soup.find('div',class_='container--HcTw2')
# atag = div.select('a[class=link--h3bPw]')
# print(atag)
# print(div)
# img = div.select('img[src]')[0]['src']
# img = div.find('img')['src']
# print(img)
imgs = div.select('img[src]')

for img in range(len(imgs)):
    # print(img)
    src_img = div.select('img[src]')[img]['src']
    print(src_img)




