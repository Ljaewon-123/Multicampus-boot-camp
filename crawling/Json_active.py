# -*- coding:utf-8 -*-

import json
import requests


with open('서울 반려견놀이터_kakao.json', 'r',encoding='utf-8') as f:
    bowwow_json = json.load(f)

api_list = [ x for x in bowwow_json['서울 반려견놀이터'][1].items()]

print(bowwow_json)
print(api_list)


# 목표는 원하는 데이터 가져와야 하고
# 키값을 넣으면 알맞은 value값만 뱉어내는???
#