from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import json
import requests
from selenium.webdriver import ActionChains




service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

# 일단 서울 강남 만 따짐
with open(f'../Data_Processing/namename3.json', 'r', encoding='utf-8') as f:
    total_json = json.load(f)

# print(total_json['2020'][0]['서울특별시'][0]['강남구'])
lst = ['카페', '술집', '어린이']
for cafe in lst:
    for i in total_json['2020'][0]['서울특별시'][0]['강남구']:  # 여기와 키워드 사이에 연도 ,sido,gugun 구분지어서 돌리는거,만들어진 파일,시도코드?
        lat_lon =[i['위도'],i['경도']]
        print(lat_lon)

        url = f'https://www.google.co.kr/maps/search/{cafe}/@{lat_lon[0]},{lat_lon[1]},13.25z/'

        driver.implicitly_wait(3)  # 3초 기다렸다가 url 가져오겠다
        driver.get(url)

        sleep(1)


        # 스크롤 특정 엘리먼트로 이동
        for x in range(5,41,2):
            element = driver.find_element(By.XPATH,f'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[{x}]/div/div[2]')
            driver.execute_script('arguments[0].scrollIntoView(true);', element)

        sleep(5)
        # 'MVVflb-haAclf.V0h1Ob-haAclf-d6wfac.MVVflb-haAclf-uxVfW-hSRGPd'
        # 'V0h1Ob-haAclf.OPZbO-KE6vqe.o0s21d-HiaYvf'
        # 'siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ'
        # 'siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ'
        # div = soup.find_all('a',)

# /html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]  ## 1
# /html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/div[2]  ## 2
# /html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]  ## 3
# /html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[9]/div/div[2]  ## 4
# /html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[41]/div/div[2]  ## last
#         for i in range(3,42,2):

        # find_name = driver.find_element(By.XPATH,f'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[{41}]/div/div[2]')
        # find_name = driver.find_element(By.CLASS_NAME,'siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ')
        find_name = driver.find_elements(By.CLASS_NAME,'MVVflb-haAclf.V0h1Ob-haAclf-d6wfac.MVVflb-haAclf-uxVfW-hSRGPd')
        # print(find_name.text.strip())

        for i in find_name:
            print(i.text.split('\n')[0])  # 식당 이름 \n 별점 \n 상호명 \n 등등... 의 형태로 나와 split('\n') 에서 [0]번째로 가져옴

        # sleep(60)


''' 
json_file = 
{2020 : {[sido :{gugun:[keyword:[],keyword:[]]}}} ]}
1000~1100

'''

