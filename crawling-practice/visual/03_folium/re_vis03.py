# -*- coding:utf-8 -*-

import folium
import json


# 1.starbucks01.json 파일을 읽자
with open('starbucks01.py.json','r',encoding='utf-8') as f:
    starbucks_json = json.load(f)

# print(starbucks_json)
# 2. 지도 만들자
starbucks_map = folium.Map(location=[36.3659806300997, 127.436127730684],zoom_start=12)


# 3. starbucks.json 파일ㅇ르 읽어 드린 내용(1에서 실행한 결과) 를 가지고
# 반복해서 starbucks 매장의 marker를 만들어 지도에 추가하자
for starbucks in starbucks_json['store_list']:
    folium.Marker([starbucks['lat'],starbucks['lot']],popup=folium.Popup(starbucks['s_name'],max_width=100)).add_to(starbucks_map)

# 4. 지도 저장하자
starbucks_map.save('vis.html')
