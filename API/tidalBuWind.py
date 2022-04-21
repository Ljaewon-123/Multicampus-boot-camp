# -*- coding:utf-8 -*-
import requests
import json
import datetime
import sys
from observatory import find_obs
sys.path.append(r'C\Work_space')

now = datetime.datetime.now()
print(now.strftime('%Y%m%d'))

obs_lst = find_obs('풍향')

url = 'http://www.khoa.go.kr/api/oceangrid/{0}/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode={1}&Date={2}&ResultType=json'
tmp = {now.strftime("%Y%m%d"):{}}
# print(tmp)
for obs_id in obs_lst:
    lst_data = []
    pago_url = url.format('tidalBuWind',obs_id,now.strftime('%Y%m%d'))
    # print(pago_url)
    resp = requests.get(pago_url)

    json_data = resp.json()
    # print(json_data)
    # print(list(json_data['result'].keys()))
    if list(json_data['result'].keys())[0] == 'error':
        continue
    else:
        # print(json_data['result']['data'][-1])
        # print(json_data['result']['meta'])
        lst_data.append(json_data['result']['data'][-1])
        tmp[now.strftime("%Y%m%d")][obs_id] = lst_data
print(tmp)
# print(tmp['20220416']['TW_0079'])