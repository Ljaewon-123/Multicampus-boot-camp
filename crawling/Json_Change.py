# -*- coding:utf-8 -*-
# 함수화가 편할듯
import json
# gu_set 은 구이름 ex) 마포구
# gu_list 는 전체 구이름
def change_gu_json(gu_set,gu_list,bowwow_dict):
    name_json = {}
    list_json = []
    for num in range(len(gu_list)):

        if gu_set == gu_list[num]:
            list_json.append(bowwow_dict[num])

        name_json[gu_set] = list_json

    print(name_json)
    return name_json
# 함수화를 못해서 구분해놔야함
# file_name_kakao = input('카카오 파일 이름 : ')
# file_name_naver = input('네이버 파일 이름 : ')
# file_name = input('파일 이름 입력: ')
file_name = '반려동물교육센터'
gu_name = input('구 입력 : ')
# 리턴 3개 적용 가능??
with open(f'서울 {file_name}_kakao.json', 'r',encoding='utf-8') as f:
    bowwow_json = json.load(f)
with open(f'서울 {file_name}_naver.json','r',encoding='utf-8') as nf:
    json_naver = json.load(nf)

bowwow_dict_kakao = list(map(lambda x: x,bowwow_json[f'서울 {file_name}']))
bowwow_dict_naver = list(map(lambda x: x,json_naver[f'서울 {file_name}']))
list_address_kakao = list(map(lambda x: x['address'],bowwow_json[f'서울 {file_name}']))
list_address_naver = list(map(lambda x: x['address'],json_naver[f'서울 {file_name}']))

# print(bowwow_json)
# print(bowwow_json['서울 반려견놀이터'])
# print(bowwow_dict)

## 카카오 버전
gu_set_kakao = set()
gu_list_kakao = []
for lst in list_address_kakao:
    gu = lst.split()[1]  # ~구 ~구 ~구 ~구
    gu_list_kakao.append(gu)
    gu_set_kakao.add(gu)  # 그냥 한바퀴 일단 돌아야함
    # print(gu)
print(gu_set_kakao)
# print(gu_list)

## 네이버 버전
gu_set_naver = set()
gu_list_naver = []
for lst in list_address_naver:
    gu = lst.split()[1]  # ~구 ~구 ~구 ~구
    gu_list_naver.append(gu)
    gu_set_naver.add(gu)  # 그냥 한바퀴 일단 돌아야함
    # print(gu)
print(gu_set_naver)
# gu_name = '마포구'
# gu_name = '구로구'


kakao_gu = change_gu_json(gu_name,gu_list_kakao,bowwow_dict_kakao)
naver_gu = change_gu_json(gu_name,gu_list_naver,bowwow_dict_naver)
# print(kakao_gu)
list_kakao_name = list(map(lambda x: x['s_name'],kakao_gu[gu_name]))  # 결론엔 필요없음 제목 같은거 잡을려고 쓰는거
list_naver_name = list(map(lambda x: x['s_name'],naver_gu[gu_name]))
list_kakao = list(map(lambda x: x,naver_gu[gu_name]))
list_naver = list(map(lambda x: x,naver_gu[gu_name]))
# print(list_kakao)
# print(list_naver_name)
for kakao in range(len(list_kakao_name)):
    for naver in range(len(list_naver_name)):
        if list_naver_name[naver] == list_kakao_name[kakao]:
            # print(kakao_gu , naver_gu)
            kakao_gu[gu_name][kakao]['address'] = naver_gu[gu_name][naver]['address']
            del list_naver[naver]
# print(list_naver)
kakao_gu[gu_name] +=  list_naver  # 구 밑으로 합쳐짐
print(kakao_gu)


# 일단 카카오만 구로 분리

# 이거를 네이버랑 비교해야됨
# 과정 -------------=-=-=--==-=-=>>> 구 가 같은 거끼리 모여서 이름을 비교해서 이름까지 같으면 naver주소만 남음 일단은
# 입력받아서 파일 이름까지 하고 해당 함수에 입력값 넣어주고 네이버 랑 비교해서 남김