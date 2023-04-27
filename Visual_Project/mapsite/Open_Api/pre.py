# -*- coding:utf-8 -*-
# 파일 공유시 한글파일 명 때문에 에러 발생 --> 임의로 영어로 바꿔줌
import requests
import pandas as pd
import numpy as np
import warnings
import json
import folium
from conversion import addr_to_lat_lon
warnings.filterwarnings('ignore')

file_name = 'cafe.json'
gu_name = '강남구'
input_file = 'hospital.csv'

with open(f"../data/pet_{file_name}", 'r', encoding="utf-8") as f:
    dict_info = json.load(f)
final_dict = dict()
final_dict['info'] = dict_info[gu_name]
print(dict_info)
print(final_dict)

input_gu = '강남구'

# hospital_data = pd.read_csv(f'../data/pet_{input_file}', encoding='cp949')
# # print(hospital_data)
# hospital_data = hospital_data[['상세영업상태명', '소재지전화', '소재지전체주소', '도로명전체주소', '사업장명', '좌표정보(x)', '좌표정보(y)']]
# hospital_data = hospital_data.loc[hospital_data['상세영업상태명'] == '정상']
#
# hospital_data = hospital_data.fillna(0)
# hospital_data = hospital_data[hospital_data['소재지전체주소'].str.contains(f'서울특별시 {input_gu}', na=False)]
#
# # print(hospital_data)
# hospital_local = hospital_data.loc[:, '도로명전체주소']
# print(hospital_local.values)
# csv_list = []
# info = {}
# for i in hospital_local:
#     # print(i)  # 주소
#     doro_add = hospital_data[hospital_data.도로명전체주소 == i]
#     hosp_name = doro_add['사업장명'].values
#     # print(hosp_name[0])
#     tmp = {}
#     tmp["s_name"] = hosp_name[0]
#     tmp["address"] = i
#     csv_list.append(tmp)
# print(csv_list)
# info['info'] = csv_list
# print(info)

input_file = 'city_park.csv'

city_park = pd.read_csv(f'../data/pet_{input_file}', encoding='cp949')
print(city_park)
city_park = city_park[['공원명', '전화번호', '소재지지번주소', '공원구분', '위도', '경도', '공원면적']]
city_park = city_park.fillna(0)
city_park = city_park[city_park['소재지지번주소'].str.contains(f'서울특별시 {input_gu}', na=False)]
# print(city_park)

# 공원면적하고 공원명이 돌면서 위도랑 경도 빼기

park_name = city_park['공원명']
csv_list = []
info = {}
for i in park_name:
    print(i)

    park_etc = city_park[city_park.공원명 == i]
    park_address = park_etc.소재지지번주소.values
    print(park_address)
    park_etc = city_park[city_park.공원명 == i]
    park_width = park_etc.공원면적.values
    print(park_width)
    tmp = {}
    tmp['s_name'] = i
    tmp['width'] = park_width[0]
    tmp['address'] = park_address[0]
    csv_list.append(tmp)

info['info'] = csv_list
print(info)


