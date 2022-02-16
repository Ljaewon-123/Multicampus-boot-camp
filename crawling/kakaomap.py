# -*- coding:utf-8 -*-
# 해당 파이썬 코드 한글로 인코딩

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
from time import sleep


url = 'https://map.kakao.com/'

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.implicitly_wait(3)   # 3초 기다렸다가 url 가져오겠다
driver.get(url)

sleep(5)
input_data = input('검색값 입력: ')
# print(soup)

driver.find_element(By.CSS_SELECTOR,'.layer_body').click()  # 그림 클릭해서 없앰

keyword = driver.find_element(By.CLASS_NAME,'query.tf_keyword')

keyword.send_keys(input_data)

sleep(2)

later = driver.find_element(By.ID,'search.keyword.submit')
later.click()

sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# the = soup.find('a',class_='more')
hidden = soup.find('a',class_='more HIDDEN')
# 더보기 버튼 클릭
# more = driver.find_element(By.ID,'#info.search.place.more')
# more.click()

# 애초에 목록이 부족하면 더보기 버튼이 숨겨진 상태라 그것을 따로 구분지어서 작동하도록함
# business 를 빼자고 합의함
lst = []
if hidden:
    num = f'info.search.page.no{1}'

    sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    ul = soup.find_all('ul', class_='placelist')[0]

    sleep(1)

    li = ul.select('li')

    for lis in li:
        if lis.find('a', class_='link_ad'):  # 중간 광고 스킵
            pass
        else:
            title = lis.find('a', class_='link_name')['title']  # 이름
            star = lis.find('em', ).text  # 별점
            div = lis.select('div p')[0]['title']  # 도로명주소
            # div1 = lis.select('div p')[1]['title']   # 지번주소,다그런것은 아닌데 갑자기 에러날때가 있음 아마 지번주소가 없어서 그럴듯, 근데 전화번호 추가해야함
            # span = lis.select('span')[3].text  # 상세 업종명

            tmp = {}
            tmp['s_name'] = title
            tmp['star'] = star
            tmp['address'] = div
            # tmp['business'] = span
            lst.append(tmp)

            # print(title)
            # print(star)
            # print(div)
            # # print(div1)
            # print(f'last {span}')

else:
    # more = driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div[7]/div[5]/a')
    # more.click()
    more = driver.find_element(By.ID,'info.search.place.more')
    more.click()
    sleep(1)

    while True:
        try:
            for i in range(1,6):
                num = f'info.search.page.no{i}'
                driver.find_element(By.ID,num).click()
                sleep(3)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                ul = soup.find_all('ul', class_='placelist')[0]

                sleep(1)

                li = ul.select('li')

                for lis in li:
                    if lis.find('a', class_='link_ad'):   # 중간 광고 스킵
                        pass
                    else:
                        title = lis.find('a', class_='link_name')['title']   # 이름
                        star = lis.find('em', ).text                       # 별점
                        div = lis.select('div p')[0]['title']                # 도로명주소
                        # div1 = lis.select('div p')[1]['title']   # 지번주소,다그런것은 아닌데 갑자기 에러날때가 있음 아마 지번주소가 없어서 그럴듯, 근데 전화번호 추가해야함
                        # span = lis.select('span')[3].text                    # 상세 업종명

                        tmp = {}
                        tmp['s_name'] = title
                        tmp['star'] = star
                        tmp['address'] = div
                        # tmp['business'] = span
                        lst.append(tmp)

                        # print(title)
                        # print(star)
                        # print(div)
                        # # print(div1)
                        # print(f'last {span}')
        except :
            break
        # next_page = driver.find_element(By.CLASS_NAME,'next')   # 이건 왜안됨??
        next_page = driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div[7]/div[6]/div/button[2]')
        if next_page:
            next_page.click()
        else:
            break

sleep(5)
res = {}
res[input_data] = lst

res_json = json.dumps(res,ensure_ascii=False)
print(res)

with open(f'{input_data}_kakao.json','w',encoding='utf-8') as f:
    f.write(res_json)
