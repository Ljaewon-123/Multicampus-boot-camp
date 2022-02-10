# -*- coding:utf-8 -*-

import requests
import json

def getSiDo():
    # __ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'  # https://www.starbucks.co.kr 까지가 endpoing -> 기본 호스트주소?  root
    # 비동기로 해봄
    resp = requests.post(url)
    # print(resp)
    # print(resp.json())    #  json 객체로 만들어서 줌 requets 모듈기능
    sido_list = resp.json()['list']   # 괜히 한단계 더가지 말고 중간 확인할것
    # print(sido_list[3])

    sido_code = list(map(lambda x: x['sido_cd'],sido_list))
    sido_nm = list(map(lambda  x:x['sido_nm'],sido_list))
    # print(sido_code)
    # print(sido_nm)
    sido_dict = dict(zip(sido_code,sido_nm))
    # print(sido_dict)

    return sido_dict

def getGuGun(sido_code):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url,data = {'sido_cd':sido_code})
    gugun_list = resp.json()['list']
    # print(gugun_list)

    # print(list(map(lambda x:x['gugun_cd'],gugun_list)))
    # print(list(map(lambda x:x['gugun_nm'],gugun_list)))

    gugun_dict = dict(zip(list(map(lambda x:x['gugun_cd'],gugun_list)),
                          list(map(lambda x:x['gugun_nm'],gugun_list))))
    # print(gugun_dict)

    return gugun_dict

def getStore(sido_code = '',gugun_code = ''):
    # __ajaxCall( storeInterfaceUrl ,$search, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url,data={'ins_lat': '37.56682',
                                    'ins_lng': '126.97865',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date': '',
                                    })
    # print(resp.json())
    store_list = resp.json()['list']
    # s_name, tel , doro_address,lat, lot
    result_list = list()
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)

    # print(result_list)
    # {'store_list' : [{},{},{}]}
    result_dict = dict()
    result_dict['store_list'] = result_list
    # print(result_dict)
    # json 저장
    result_json = json.dumps(result_dict,ensure_ascii=False)
    with open('../visual/03_folium/starbucks01.py.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

    return result_json

# 제대로된 요청에 응답이 안오면 네트워크 확인할것
# ? 이후는 새로운 데이터라고 생각해서 다시 읽음

if __name__=='__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        print(getStore(sido_code='17',gugun_code=''))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 : ')
        print(getStore(sido_code='',gugun_code=gugun))