# -*- coding:utf-8 -*-
import requests
import json
# import sys
# from observatory import find_obs
# sys.path.append(r'C\Work_space')
#
# find_obs('파고')
import datetime

print(datetime.datetime.now())
now = datetime.datetime.now()

print(now.strftime('%Y-%m-%d %H:%M'))
print(now.strftime('%Y%m%d'))


# CndQ9ayWwjk5aH/aT22Bzw==
# url = 'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode=DT_0002&Date=20220415&ResultType=json'
#
# print(url)
# # print(url2)
#
# resp = requests.get(url)
# # print(resp)
#
# json_data = resp.json()
# print(json_data)
#
# print(json_data['result'])

print('asdf',)
'''
VM에서 추가
from pyspark.sql import SparkSession
# spark = SparkSession.builder.master("yarn").appName("파일명").getOrCreate() // 하둡을 안써서 스파크 셰션을 사용못함  

저장 해줄 json 변수하나에 담고 ex) data = json_data['result']

변수명.write.format('mongo').option('database','test').option('collection','test').mode('overwrite').save()


{“관측소1”:[{"record_time": "2014-11-01 00:00",
"wave_height": "0.96"}],“관측소2”: {“record_time": "2014-11-01 00:05",
"wave_height": "0.96”}}

최종 
{'2020-04-17':{관측소_코드:[{아무튼값임}],관측소_코드2:[{아무튼값음2,3,4,5,}]}}
이후 추가로 값이 들어가게 하는거는 카프카에서 처리??

'''

