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
    sido_url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp_gugun = requests.post(sido_url)
    # print(resp_gugun)
    resp_gu = resp_gugun.json()
    resp_gu['list'] = getSiDo()
    # print(resp_gu['list'])
    resp_last = resp_gu['list']
    # print(resp_last['01'])
    print(type(resp_last.keys()))
    if resp_last.keys() == sido_code:
        print(resp_last[sido_code])

if __name__=='__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        pass
    else:
        getGuGun(sido)