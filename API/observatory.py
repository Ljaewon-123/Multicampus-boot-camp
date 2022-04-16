# -*- coding:utf-8 -*-
import requests
import json

# CndQ9ayWwjk5aH/aT22Bzw==

def find_obs(obs_type):

    url = 'http://www.khoa.go.kr/api/oceangrid/ObsServiceObj/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ResultType=json'

    # print(url)
    # print(url2)

    resp = requests.get(url)
    # print(resp)

    json_data = resp.json()
    # print(json_data)

    # print(json_data['result']['data'])
    lst_type = []
    for obs in json_data['result']['data']:
        # print(obs['obs_object'].split(','))
        obs_lst = obs['obs_object'].split(',')
        for lst in obs_lst:
            if lst == obs_type:  # 관측소가 2개만 있는게 아니라 더있음 그래서 여기까지만 찾고 관측소는 따로 만지는걸로
                # print(obs)
                lst_type.append(obs['obs_post_id'])

    # print(lst_type)

    return lst_type

# find_obs('파고')