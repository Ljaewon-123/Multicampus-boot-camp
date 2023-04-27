# -*- coding:utf-8 -*-
# 함수화가 편할듯
import json
# gu_set 은 구이름 ex) 마포구
# gu_list 는 전체 구이름
def make_gu_json(gu_set,gu_list,bowwow_dict):
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
file_name = '반려견놀이터'
# file_name = '반려동물교육센터'

while True:
    gu_name = input('구 입력 : ')
    if gu_name == 'stop':
        break
    else:
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
            gu_set_kakao.add(gu)  # 그냥 한바퀴 일단 돌아야함 없어도됨
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


        kakao_gu = make_gu_json(gu_name,gu_list_kakao,bowwow_dict_kakao)
        naver_gu = make_gu_json(gu_name,gu_list_naver,bowwow_dict_naver)
        # print(kakao_gu)
        list_kakao_name = list(map(lambda x: x['s_name'].replace(' ',''),kakao_gu[gu_name]))  # 결론엔 필요없음 제목 같은거 잡을려고 쓰는거
        list_naver_name = list(map(lambda x: x['s_name'].replace(' ',''),naver_gu[gu_name]))
        list_kakao = list(map(lambda x: x,naver_gu[gu_name]))
        list_naver = list(map(lambda x: x,naver_gu[gu_name]))
        # print(list_kakao)
        # print(list_naver[1])
        # print(list_kakao_name)
        # print(list_naver_name)
        # list_kakao_name12 = list(map(lambda x: x['s_name'].replace(' ',''),kakao_gu[gu_name]))
        # print(list_kakao_name12)
        for kakao in range(len(list_kakao_name)-1,0,-1):
            for naver in range(len(list_naver_name)-1,0,-1):
                # print(naver)
                if list_kakao_name[naver] == list_kakao_name[kakao]:
                    # print(kakao_gu , naver_gu)
                    # print(kakao, naver)
                    kakao_gu[gu_name][kakao]['address'] = naver_gu[gu_name][naver]['address']
                    del list_naver[naver] , list_naver_name[naver]

        # print(list_naver)
        kakao_gu[gu_name] +=  list_naver  # 구 밑으로 합쳐짐
        print(kakao_gu)

        ## jisu
        # with open(f'{file_name}.json', 'a', encoding='utf-8') as f:
        #     f.write(str(kakao_gu))

