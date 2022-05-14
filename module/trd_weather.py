# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
import time, copy

# 서해북부
dict1 = {'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[2]/button' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[1]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[2]'],
#서해중부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[3]/button' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[4]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[6]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[7]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[1]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[3]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[2]'],
# 서해남부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[4]/button' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[6]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[7]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[8]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[9]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[10]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[2]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[1]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[3]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[4]'],
# 남해서부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[4]/div/button[1]' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[4]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[1]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[2]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[3]'],
# 제주도
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[4]/div/button[2]' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[8]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[7]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[6]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[2]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[4]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[3]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[1]'],
# 남해동부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[5]/button[1]' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[6]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[7]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[4]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[1]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[3]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[2]'],
# 동해남부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[5]/button[2]' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[6]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[7]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[8]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[4]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[3]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[2]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[1]'],
# 동해중부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[6]/button' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[4]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[5]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[6]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[1]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[2]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[3]'],
# 동해북부
'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[7]/button' : ['/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[2]', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[1]']}


dict2 = {'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[1]' : '서해북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[2]' : '서해북부 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[4]' : '인천,경기 북부 앞바다' , '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[5]' : '인천,경기 남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[6]' : '충남 북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[7]' : '충남 남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[1]' : '서해중부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[3]' : '서해중부 안쪽 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[2]' : '서해중부 바깥 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[6]' : '전북 북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[7]' : '전북 남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[8]' : '전남 북부 서해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[9]' : '전남 중부 서해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[10]' : '전남 남부 서해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[2]' : '서해남부 북쪽안쪽먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[1]' : '서해남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[3]' : '서해남부 남쪽안쪽먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[5]' : '서해남부 남쪽바깥먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[4]' : '서해남부 북쪽바깥먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[4]' : '전남 서부 남해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[5]' : '전남 동부 남해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[1]' : '남해 서부 서쪽먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[2]' : '남해서부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[3]' : '남해서부 동쪽먼바다','/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[5]' : '제주도 북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[8]' : '제주도 동부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[7]' : '제주도 남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[6]' : '제주도 서부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[2]' : '제주도 남서쪽안쪽 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[4]' : '제주도 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[3]' : '제주도 남동쪽안쪽 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[1]' : '제주도 남쪽바깥면바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[6]' : '경남 서부 남해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[7]' : '거제시 동부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[5]' : '경남 중부 남해 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[4]' : '부산 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[1]' : '남해 동부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[3]' : '남해동부 안쪽먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[2]' : '남해동부 바깥먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[6]' : '경남 북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[7]' : '경남 남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[8]' : '울산 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[4]' : '동해남부 북쪽바깥먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[5]' : '동해남부 북쪽안쪽먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[3]' : '동해남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[2]' : '동해남부 남쪽안쪽먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[1]' : '동해남부 남쪽바깥먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[4]' : '강원 북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[5]' : '강원 중부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[6]' : '강원 남부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[1]' : '동해 중부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[2]' : '동해 중부 안쪽 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[3]' : '동해 중부 바깥 먼바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[2]' : '동해 북부 앞바다', '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[1]' : '동해 북부 먼바다'}
# def donghaebuk():
#     url = ""

final_dict = {}

# db = pymysql.connect(host='127.0.0.1',
#     port=3306,
#     user="root",
#     passwd="tlawjdgns1",
#     db='test')
# kkk = {'동해 북부 먼바다': {'5월08일': [['오전', '1m', '2m', '구름많음'], ['오후', '1m', '2m', '맑음']], '5월09일': [['오전', '1m', '2m', '맑음'], ['오후', '1m', '2m', '맑음']], '5월10일': [['오전', '1m', '2m', '맑음'], ['오후', '1m', '2m', '구름많음']], '5월11일': [['오전', '1m', '2m', '구름많음'], ['오후', '1m', '2m', '구름많음']]}}
# print(kkk[ehdgo])

for key in dict1.keys():
    for value in dict1[key]:
        url = "https://www.weather.go.kr/w/ocean/forecast/daily-forecast.do"

        # driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
        driver = webdriver.Edge(service=service)
        driver.implicitly_wait(3)
        driver.get(url)
        time.sleep(1)
        # print(f'key:  {key}')
        dongbukbu = driver.find_element(By.XPATH,key)
        dongbukbu.send_keys(Keys.ENTER)
        driver.implicitly_wait(1)
        time.sleep(1)

        dongbukbu_ap = driver.find_element(By.XPATH,value)
        dongbukbu_ap.send_keys(Keys.ENTER)
        driver.implicitly_wait(1)
        time.sleep(1)

        fst_table = driver.find_element(By.XPATH,'//*[@id="sea-today-short-term"]/div[2]/table/tbody')
        table_contents = list()
        cnt = len(fst_table.get_attribute("innerText").split('\n'))
        table_contents.append(fst_table.get_attribute("innerText").split('\n'))
        print(cnt)
        if cnt == 5:
            table_contents = table_contents[0]
            cnt = int((cnt-1)/2)
            result_dict = dict()
            day = table_contents[0].split('\t')[0].split(' ')[0].split('(')[0]

            result_dict[day] = list()
            weather = table_contents[0].split('\t')[0].split(' ')[-1]
            result_dict[day] = table_contents[0].split('\t')[1:]
            result_dict[day].append(weather)

            for k in range(1, cnt+1):
                weather = table_contents[2*k-1].split('\t')[0].split(' ')[1:]
                day = table_contents[2*k-1].split('\t')[0].split(' ')[0].split('(')[0]
                result_dict[day] = list()
                result_dict[day].append(table_contents[2*k-1].split('\t')[1:])
                result_dict[day].append(table_contents[2*k-1].split('\t')[1:])
                result_dict[day][0].append(weather[0])
                result_dict[day][1].append(weather[-1])

                
            test_dict = dict()
            test_dict[dict2[value]] = result_dict

            se_table = driver.find_element(By.XPATH,'//*[@id="sea-today-mid-term"]/div[2]/div/ul[2]')
            se_table = se_table.get_attribute("innerText").split('\n')[1:-12]

            cnt = len(se_table)
            result2_dict = dict()
            for i in range(1,int(cnt/6)):
                day = str(se_table[6*i].split('(')[0].split(". ")[0][1:])+'월'+str(se_table[6*i].split('(')[0].split(". ")[1])+'일'
                
                result2_dict[day] = list()
                temp_list = list()

                result2_dict[day].append([se_table[6*i+1],se_table[6*i+5].split(' ')[3],se_table[6*i+5].split(' ')[7],se_table[6*i+2]])
                result2_dict[day].append([se_table[6*i+3],se_table[6*i+5].split(' ')[11],se_table[6*i+5].split(' ')[-1],se_table[6*i+4]])
        
            test_dict = dict()
            kk = copy.deepcopy(result_dict)
            
            place = dict2[value]
            test_dict = dict()
            test2_dict = dict()
            test_dict['날씨전망'] = result_dict
            test2_dict['주간날씨'] = result2_dict

            print(test_dict)            
            print(test2_dict)

            final_lst = [test_dict, test2_dict]
            final_dict[place] = final_lst

            driver.close()

        else:
# /html/body/div[2]/section/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[6]/td[1]/span
# /html/body/div[2]/section/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[6]/td[1]/span
            table_contents = table_contents[0]
            print(table_contents)
            cnt = int((len(table_contents))/2)
            result_dict = {}
            lst = []
            pm = ''
            # ['6일(금)', '비\t오후\t서-북서\t3~7\t0.5~1', '', '7일(토)', '비  맑음\t오전\t북서-북\t4~8\t0.5~1', '오후\t북서-북\t4~8\t0.5~1', '', '8일(일)', '구름많음  구름많음\t오전\t북-북동\t3~7\t0.5~0.5', '오후\t북서-북\t2~5\t0.5~0.5', '', '9일(월)', '맑음  구름많음\t오전\t북동-동\t3~6\t0.5~0.5', '오후\t남서-서\t3~6\t0.5~0.5']
            # {'4일': [['오전', '남-남서', '7~12', '1~2.5', '맑음'], ['오후', '남-남서', '8~12', '1~2.5', '맑음']], '5일': [['오전', '남-남서', '7~11', '1~2.5', '맑음'], ['오후', '남동-남', '6~10', '1~2', '맑음']], '6일': [['오전', '남-남서', '5~9', '1~2', '비'], ['오후', '북서-북', '4~8', '0.5~1.5', '비']]}}
            for weather in table_contents:
                if weather in '':
                    continue
                # print(weather)
                if weather[0].isdigit():
                    weather_key = weather
                    # print(weather_key)
                else:
                    info = weather.split('\t')
                    if info[1] == '오전':
                        info_div = info[1:]
                        am = info[0].split()[0]
                        pm = info[0].split()[1]
                        info_div.append(am)
                        lst.append(info_div)
                    elif info[1] == '오후' or info[0] == '오후':
                        if pm == '':
                            result_dict[weather_key] = info
                        else:
                            info_div = info
                            info_div.append(pm)
                            lst.append(info_div)
                            # print('----------------------------------------------------------')
                            result_dict[weather_key] = lst
                            lst = []
            # print(result_dict)
            # for k in range(0, cnt):
            #     dhwjs = table_contents[2*k].split('\t')[1:]
            #     print(dhwjs,'dhwjs')
            #     # print(table_contents[2*k].split('\t')[0].split(' '))
            #     dhwjs.append(table_contents[2*k].split('\t')[0].split(' ')[0])  # 마지막 1을 0으로 바꿈
            #     # ['오전', '남-남서', '7~12', '1~2.5', '맑음']
            #     dhgn = table_contents[2*k+1].split('\t')
            #     print(dhgn,'dhgn')
            #     dhgn.append(table_contents[2*k].split('\t')[0].split(' ')[-1])
            #     # ['오후', '남-남서', '8~12', '1~2.5', '맑음']
            #     day = table_contents[2*k].split('\t')[0].split(' ')[0].split('(')[0]
            #     # '4일'
            #     result_dict[day] = list()
            #     result_dict[day].append(dhwjs)
            #     result_dict[day].append(dhgn)

            # print(result_dict,'asdfaewfasdf')

            se_table = driver.find_element(By.XPATH,'//*[@id="sea-today-mid-term"]/div[2]/div/ul[2]')
            se_table = se_table.get_attribute("innerText").split('\n')[1:-12]

            cnt = len(se_table)
            result2_dict = dict()
            for i in range(1,int(cnt/6)):
                # '5월08일'
                day = str(se_table[6*i].split('(')[0].split(". ")[0][1:])+'월'+str(se_table[6*i].split('(')[0].split(". ")[1])+'일'
                result2_dict[day] = list()
                temp_list = list()

                result2_dict[day].append([se_table[6*i+1],se_table[6*i+5].split(' ')[3],se_table[6*i+5].split(' ')[7],se_table[6*i+2]])
                result2_dict[day].append([se_table[6*i+3],se_table[6*i+5].split(' ')[11],se_table[6*i+5].split(' ')[-1],se_table[6*i+4]])
    

            place = dict2[value]
            test_dict = dict()
            test2_dict = dict()
            test_dict['날씨전망'] = result_dict
            test2_dict['주간날씨'] = result2_dict

            print(test_dict)            
            print(test2_dict)
            final_lst = [test_dict,test2_dict]
            final_dict[place] = final_lst
            print(final_dict)
            # {'서해북부 먼바다': {'4일': [['오전', '남-남서', '7~12', '1~2.5', '맑음'], ['오후', '남-남서', '8~12', '1~2.5', '맑음']], '5일': [['오전', '남-남서', '7~11', '1~2.5', '맑음'], ['오후', '남동-남', '6~10', '1~2', '맑음']], '6일': [['오전', '남-남서', '5~9', '1~2', '비'], ['오후', '북서-북', '4~8', '0.5~1.5', '비']]}}
            # {'서해북부 먼바다': {'5월08일': [['오전', '0.5m', '1.5m', '구름많음'], ['오후', '0.5m', '1.5m', '맑음']], '5월09일': [['오전', '0.5m', '1.5m', '맑음'], ['오후', '0.5m', '1.5m', '맑음']], '5월10일': [['오전', '1m', '2m', '구름많음'], ['오후', '1m', '2m', '구름많음']], '5월11일': [['오전', '1m', '2m', '흐림'], ['오후', '1m', '2m', '흐림']]}}

            driver.close()


res_json = json.dumps(final_dict,ensure_ascii=False)

with open(f'../../Fishing/data/weather.json' ,'w',encoding='utf-8') as f:
    f.write(res_json)