from selenium import webdriver
from bs4 import BeautifulSoup

# tag = input('search tags: ')
# url = f'https://www.instagram.com/explore/tags/{tag}'
url = 'https://www.instagram.com/i_am_young22/'  # 주소 정도는 상관없지 않나요?
# url = 'https://www.instagram.com/coco20002/'
# 샐레니움이 응답받기까지를 기다리게 해줄수 있음

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)  # 이거는 위에는 다르게 객체임

# 셀레니움 최근에 바뀜

driver.implicitly_wait(3)   # 3초 기다렸다가 url 가져오겠다
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')
# img_list = soup.find_all('div',class_='KL4Bh')
# print(img_list)


one_photos =  soup.select('div.KL4Bh > img')[0]['src']

print(one_photos)

# for img in one_photos:
#     src_img =