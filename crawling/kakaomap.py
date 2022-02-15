# -*- coding:utf-8 -*-
# 해당 파이썬 코드 한글로 인코딩

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep


url = 'https://map.kakao.com/'

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.implicitly_wait(3)   # 3초 기다렸다가 url 가져오겠다
driver.get(url)

sleep(5)


# print(soup)

driver.find_element(By.CSS_SELECTOR,'.layer_body').click()

keyword = driver.find_element(By.CLASS_NAME,'query.tf_keyword')

keyword.send_keys('서울 애견미용실')

sleep(2)

later = driver.find_element(By.ID,'search.keyword.submit')
later.click()

sleep(2)

soup = BeautifulSoup(driver.page_source,'html.parser')
ul = soup.find_all('ul',class_= 'placelist')[0]

sleep(1)

li = ul.select('li')

for lis in li:
    if lis.find('a',class_='link_ad'):
        pass
    else:
        found = lis.find('a',class_='link_name')['title']
        found2 = lis.find('em',).text
        div = lis.select('div p')[0]['title']
        div1 = lis.select('div p')[1]['title']
        # span = lis.find('span',class_='subcategory.clickable').text
        span = lis.select('span')[3].text
        print(found)
        print(found2)
        print(div)
        print(div1)
        print(f'last {span}')



driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div[7]/div[5]/a').click()

sleep(1)


for i in range(1,6):
    num = f'info.search.page.no{i}'
    driver.find_element(By.ID,num).click()
    sleep(3)
    # driver.find_element(By.ID,f'info.search.page.no{i}').click()
sleep(5)



# sleep(3)
#
# soup = BeautifulSoup(driver.page_source,'html.parser')
# ul = soup.find_all('ul',class_= 'placelist')[0]
#
# sleep(1)
#
# li = ul.select('li')
#
# for lis in li:
#     if lis.find('a',class_='link_ad'):
#         pass
#     else:
#         found = lis.find('a',class_='link_name')['title']
#         found2 = lis.find('em',).text
#         div = lis.select('div p')[0]['title']
#         div1 = lis.select('div p')[1]['title']
#         # span = lis.find('span',class_='subcategory.clickable').text
#         span = lis.select('span')[3].text
#         print(found)
#         print(found2)
#         print(div)
#         print(div1)
#         print(f'last {span}')