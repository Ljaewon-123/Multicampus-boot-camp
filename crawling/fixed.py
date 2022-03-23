from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import json
import requests

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)
# lat_lon = ['35.566991800732', '128.159016359419'] # 합정군
# lat_lon = ['33.24838704093', '126.561417583056']   # 제주 서귀포
lat_lon = ['33.4867204359', '126.476394665083']
'''   제주 제주시
['33.514049417348', '126.53683656106']  # clear
['33.483780492776', '126.482451818498'] # clear
['33.490024243825', '126.488175533875'] # clear
['33.4867204359', '126.476394665083']  # clear
'''
url = f'https://www.google.co.kr/maps/search/어린이/@{lat_lon[0]},{lat_lon[1]},13.25z/'

driver.implicitly_wait(3)  # 3초 기다렸다가 url 가져오겠다
driver.get(url)

sleep(1)

exists_ele = driver.find_elements(By.CLASS_NAME,'MVVflb-haAclf.V0h1Ob-haAclf-d6wfac.MVVflb-haAclf-uxVfW-hSRGPd')

num_ele = len(exists_ele)
if num_ele >= 5:
# 스크롤 특정 엘리먼트로 이동  # 41
    for x in range(5,41,2):  # 스크롤만 해주면 되잖아 맨 아래로 내려가기만 하면 가능
        # if EE.is_displayed():
        element = driver.find_element(By.XPATH,f'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[{x}]/div/div[2]')

        driver.execute_script('arguments[0].scrollIntoView(true);', element)
else:
    for x in range(5,num_ele,2):
        element = driver.find_element(By.XPATH,
                                      f'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[{x}]/div/div[2]')
        driver.execute_script('arguments[0].scrollIntoView(true);', element)

# '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]'
# '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]'




# '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/div[2]'
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
    print(i.text.split('\n')[0])