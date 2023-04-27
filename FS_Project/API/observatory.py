# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd

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
    # print(lst_type)
    return lst_type

def full_obs():
    url = 'http://www.khoa.go.kr/api/oceangrid/ObsServiceObj/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ResultType=json'

    # print(url)
    # print(url2)

    resp = requests.get(url)
    # print(resp)
    json_data = resp.json()
    # print(json_data['result']['data'])

    json_data = resp.json()
    # print(json_data)
    # a = {}
    # a['obs_lst'] = json_data['result']['data']

    # res_json = json.dumps(a, ensure_ascii=False)

    # with open('full_obs.json', 'w', encoding='utf-8') as f:
    #     f.write(res_json)
    # print(json_data['result']['data'])
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    for i in json_data['result']['data']:
        print(i)
        lst1.append(i['obs_post_id'])
        lst2.append(i['data_type'])
        lst3.append(i['obs_lat'])
        lst4.append(i['obs_lon'])
        lst5.append(i['obs_post_name'])
        lst6.append(i['obs_object'])

    colname_lst = ['obs_code','data_type','obs_lat','obs_lon','obs_post_name','obs_object']
    df = pd.DataFrame(zip(lst1,lst2,lst3,lst4,lst5,lst6),columns=colname_lst)
    df.to_csv('full_obs.csv', encoding='utf-8', index=False)
    return json_data['result']['data']


# print(full_obs())
full_obs()
# find_obs('파고')
# find_obs('풍향')

