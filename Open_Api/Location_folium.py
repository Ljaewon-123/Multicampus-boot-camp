# -*- coding:utf-8 -*-
# 파일 공유시 한글파일 명 때문에 에러 발생 --> 임의로 영어로 바꿔줌
import requests
import json
import folium
from conversion import addr_to_lat_lon

input_file = input('파일이름 입력 : ')
input_gu = input('구 입력: ')
# input_gu = '강남구'

def Location_Map(input_file,input_gu):

    with open(f'../Open_Api/json_total/{input_file}.json', 'r', encoding='utf-8') as f:
        total_json = json.load(f)

    center = addr_to_lat_lon(input_gu)
    center_loc = folium.Map(location=[center[0],center[1]],zoom_start=14)
    # print(total_json)
    gu_data = total_json[input_gu]
    print(gu_data)
    # local = []
    for gu in gu_data:
        gu_address = gu["address"]
        print(gu_address)
        # local.append(addr_to_lat_lon(gu_address))
        local = addr_to_lat_lon(gu_address)
        # folium.Marker([local[0],local[1]], popup=folium.Popup(gu['s_name'], max_width=100)).add_to(my_loc)
        folium.RegularPolygonMarker([local[0], local[1]], popup=folium.Popup(gu['s_name'], max_width=100)).add_to(center_loc)

    # print(local)
    # print(local[1][1])
    # local[i][0], local[i][1]

    # # local[0],local[1]
    # my_loc = folium.Map(location=[local[0],local[1]],zoom_start=18)
    # folium.Marker([local[0],local[1]],popup=folium.Popup('',max_width=100)).add_to(my_loc)
    #
    center_loc.save('pratice.html')

Location_Map()