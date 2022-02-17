# -*- coding:utf-8 -*-
# 함수화가 편할듯
import json
import sys
# gu_set 은 구이름 ex) 마포구
# gu_list 는 전체 구이름
# 구입력, 카카오의 구 리스트, 카카오의 bowwow dict

sys.stdin = open('inputs.txt','r',encoding='utf-8')
def make_gu_json(gu_name, gu_list, bowwow_dict):
    name_json = {}
    list_json = []
    for num in range(len(gu_list)):

        if gu_name == gu_list[num]:
            # 구에 해당되는 모든 가게 정보를 가져온 것
            list_json.append(bowwow_dict[num])

        name_json[gu_name] = list_json

    print(name_json)
    return name_json

# 전역변수
final = dict()
cnt = 0
business = ''
file_name = input()
with open(f'{file_name}.json', 'w') as f:
    pass

while True :
    cnt += 1
    if cnt > 25:
        break
    # 함수화를 못해서 구분해놔야함
    # file_name_kakao = input('카카오 파일 이름 : ')
    # file_name_naver = input('네이버 파일 이름 : ')
    business = file_name
    # file_name = '반려견놀이터'
    gu_name = input()
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
    # print(gu_set_kakao)
    # print(gu_list)

    ## 네이버 버전
    gu_set_naver = set()
    gu_list_naver = []
    for lst in list_address_naver:
        gu = lst.split()[1]  # ~구 ~구 ~구 ~구
        gu_list_naver.append(gu)
        gu_set_naver.add(gu)  # 그냥 한바퀴 일단 돌아야함
        # print(gu)
    # print(gu_set_naver)
    # gu_name = '마포구'
    # gu_name = '구로구'


    kakao_gu = make_gu_json(gu_name, gu_list_kakao, bowwow_dict_kakao)
    naver_gu = make_gu_json(gu_name, gu_list_naver, bowwow_dict_naver)
    # print(kakao_gu)


    # 구에 해당되는 모든 가게 정보를 가져온 것 (딕셔너리 형태) kakao_gun
    list_kakao_name = list(map(lambda x: x['s_name'].replace(' ',''),kakao_gu[gu_name]))  # 결론엔 필요없음 제목 같은거 잡을려고 쓰는거
    list_naver_name = list(map(lambda x: x['s_name'].replace(' ',''),naver_gu[gu_name]))
    list_kakao = list(map(lambda x: x,naver_gu[gu_name]))
    list_naver = list(map(lambda x: x,naver_gu[gu_name]))
    # print(list_kakao)
    # print(list_naver_name)
    for kakao in range(len(list_kakao_name)-1,0,-1):
        for naver in range(len(list_naver_name)-1,0,-1):
            if list_naver_name[naver] == list_kakao_name[kakao]:
                # print(kakao_gu , naver_gu)
                kakao_gu[gu_name][kakao]['address'] = naver_gu[gu_name][naver]['address']
                del list_naver[naver], list_naver_name[naver]

    kakao_gu[gu_name] +=  list_naver  # 구 밑으로 합쳐짐
    final[gu_name] = []
    final[gu_name] += list_naver
    print(final)


    ## 지수
    ## inputs.txt 수정
    with open(f'inputs.txt', 'r', encoding='utf-8') as f:
        sentences = f.readlines()
    with open(f'inputs.txt', 'w', encoding='utf-8') as f:
        for sen in sentences:
            # 만약 한 줄이 내가 입력한 gu_name과 다르다면
            if sen.strip('\n') != gu_name:
                # 만약 한 줄이 내가 입력한 파일 명도 아니라면
                # if sen.strip('\n') != file_name:
                #     f.write(file_name+'\n')
                f.write(sen)

final_json = json.dumps(final,ensure_ascii=False)
with open(f'{business}.json', 'a', encoding='utf-8') as f:
    f.write(final_json)
print('마지막 모습', final_json)