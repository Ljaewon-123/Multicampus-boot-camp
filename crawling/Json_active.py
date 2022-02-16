# -*- coding:utf-8 -*-

import json
import requests

# with open('서울 반려견놀이터_kakao.json', 'r',encoding='utf-8') as f:
#     bowwow_json = json.load(f)
#
# api_list = [ x for x in bowwow_json['서울 반려견놀이터'][1].values()]
#
# print(bowwow_json)
# print(api_list[2])
# # print(type(api_list[2]))  # 문자임 str
# # print(api_list[2])
# input_name = input('파일 이름 : 서울 ')

with open(f'서울 반려견놀이터_kakao.json', 'r',encoding='utf-8') as f:
    bowwow_json = json.load(f)
with open(f'서울 반려견놀이터_naver.json','r',encoding='utf-8') as nf:
    json_naver = json.load(nf)

bowwow_dict = list(map(lambda x: x,bowwow_json['서울 반려견놀이터']))
list_address_kakao = list(map(lambda x: x['address'],bowwow_json['서울 반려견놀이터']))
list_address_naver = list(map(lambda x: x['address'],json_naver['서울 반려견놀이터']))

# print(bowwow_json)
# print(bowwow_json['서울 반려견놀이터'])
# print(bowwow_dict)
# print(bowwow_json['서울 반려견놀이터'][0])
# print(list_address_kakao)
# print(list_address_naver)
list_ad = set()
gu_list = []
for lst in list_address_kakao:
    gu = lst.split()[1]  # ~구 ~구 ~구 ~구
    gu_list.append(gu)
    list_ad.add(gu)  # 그냥 한바퀴 일단 돌아야함
    # print(gu)
print(list_ad)
print(gu_list)
name_json = {}
list_json = []



#### ---- for 문이 아니라 함수의 return 으로 해보기 
# for sets in list_ad:  ## 여기에 바로 json 으로 완성해야함 if 문에서 최종 완성
#     # print(sets)
#     for num in range(len(gu_list)):
#
#         # print(gu_list)
#         if sets == gu_list[num]:   # 구가 같은건 찾음 이제 어쩔거?  각 구가 몇번째에서 걸렸는지 번호를 알아야함 돌구있는 구가 몇번째인지 len()
#             list_json.append(bowwow_dict[num])
#             # print(list_json)
#         name_json[sets] = list_json  ## 이부분에서 캐치하고 지워줘야함
#
#     print(name_json)


    # 일단 카카오만 구로 분리

# 이거를 네이버랑 비교해야됨
# 과정 -------------=-=-=--==-=-=>>> 구 가 같은 거끼리 모여서 이름을 비교해서 이름까지 같으면 naver주소만 남음 일단은