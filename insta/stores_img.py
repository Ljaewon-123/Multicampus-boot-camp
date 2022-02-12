from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep

# 어째선지 똑같은 동작도 while문이 먹지 않음 버튼과 각 이미지별 로딩차이 같음

def scroll(SCROLL_PAUSE_SEC):
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
        sleep(SCROLL_PAUSE_SEC)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_page_height == last_page_height:
            break
        last_page_height = new_page_height

## https://storiesdown.com/users/i_am_young22
url = 'https://storiesdown.com/users/i_am_young22'

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.implicitly_wait(3)   # 3초 기다렸다가 url 가져오겠다
driver.get(url)
# scroll()
sleep(5)

driver.find_element(By.CLASS_NAME,'tab-title.posts.mb-3').click()

# scroll(1)
sleep(5)

# more_btn = driver.find_element(By.CLASS_NAME,'load-more-btn')
# # 이게 왜안되지??
# while True:
#     if more_btn:
#         more_btn.click()
#         sleep(5)
#         sleep(5)
#     else:
#         break

driver.find_element(By.CLASS_NAME,'load-more-btn').click()

sleep(5)
sleep(5)

driver.find_element(By.CLASS_NAME,'load-more-btn').click()

# scroll()
sleep(5)
sleep(5)

driver.find_element(By.CLASS_NAME,'load-more-btn').click()

sleep(5)
sleep(5)

driver.find_element(By.CLASS_NAME,'load-more-btn').click()

sleep(5)
sleep(5)

driver.find_element(By.CLASS_NAME,'load-more-btn').click()

sleep(5)
sleep(5)

# driver.find_element(By.CLASS_NAME,'load-more-btn').click()

sleep(5)
sleep(5)

driver.execute_script('window.scrollTo(0,0)')
sleep(5)

for i in range(50):
    driver.execute_script("window.scrollTo(0, window.scrollY + 100);")
    sleep(1)

soup = BeautifulSoup(driver.page_source,'html.parser')

# imgs = soup.select('div.lazyload-wrapper > img')['src']
# print(imgs)
imgs = soup.select('div.lazyload-wrapper > img')
path = '../crawling_down_img/insta_img'

for img in range(len(imgs)):
    src_img = soup.select('div.lazyload-wrapper > img')[img]['src']
    with open(path + f'\im_young_22{img}.jpg', 'wb') as f:
        download_file = requests.get(src_img, )
        f.write(download_file.content)
    # print(src_img)


