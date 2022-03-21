import requests
import json
# from json_class import Traffic

service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'
# #
url = f'http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking?serviceKey={service_key}&searchYearCd=2019&siDo=11&guGun=620&type=json&numOfRows=9999&pageNo=1'
print(url)
#

resp = requests.get(url)

json_res = resp.json()
print(json_res)

print(json_res['resultMsg'])  # NODATA_ERROR


x = {'123':'asdf','5687':'zxcv'}




# with open(f'namename.json', 'r', encoding='utf-8') as f:
#     total_json = json.load(f)
# # 경기도
# print(total_json['2020'])


# for i in total_json['2017'][0]['서울특별시']:


