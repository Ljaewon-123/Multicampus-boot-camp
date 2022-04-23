# -*- coding:utf-8 -*-
import requests
import json
import datetime
import sys
from observatory import find_obs
sys.path.append(r'C\Work_space')
import pandas
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()
print(now.strftime('%Y%m%d'))

now_back = now -  relativedelta(months=1)
# print(now_back.strftime('%Y%m%d'))
now_front = now + relativedelta(months=3)

dt = pandas.date_range(start=now_back,end=now_front)
print(dt.strftime('%Y%m%d'))

obs_lst = find_obs('조위')

def marine_weather(obs_lst,kind_weather):

    url = 'http://www.khoa.go.kr/api/oceangrid/{0}/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode={1}&Date={2}&ResultType=json'
    # tmp = {now.strftime("%Y%m%d"):{}}
    lst_data = []
    # print(tmp)
    for obs_id in obs_lst:
        # lst_data = []
        for date in dt.strftime('%Y%m%d'):
            pago_url = url.format(kind_weather,obs_id,date)
            # print(pago_url)
            resp = requests.get(pago_url)

            json_data = resp.json()
            # print(json_data)
            # print(date)
            # print(list(json_data['result'].keys()))
            if list(json_data['result'].keys())[0] == 'error':
                continue
            else:
                # 내용 전부다 들어가야됨

                lst_data.append(json_data['result']['data'])

    tmp = lst_data

    print(tmp)

    return tmp

result = marine_weather(obs_lst,'tideObsPre')

with open('../data/jo_temp.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False)