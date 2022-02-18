# -*- coding:utf-8 -*-
# 파일 공유시 한글파일 명 때문에 에러 발생 --> 임의로 영어로 바꿔줌
import requests
import pandas as pd
import numpy as np
import warnings
import json
import folium
from conversion import addr_to_lat_lon
warnings.filterwarnings('ignore')



    # my_loc.save('pratice.html')

# folium.Marker(
#     location=[37.5752205086784, 127.010502773568],
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="green"),
# ).add_to(my_loc)


# ajax로 folium 보내보기
# 다음에 해야할게 마커랑 장고찍기
# Marker : 병원(십자이미지) , 약국(알약이미지) , 공원(암거나 찾아바), 교육센터, 펫카페, 펫 유치원, 펫 호텔, ,펫 놀이터, 펫 미용실,
#         펫 용품점, 동반카페, 동반식당