import requests
import json
#
# service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'
#
# # url = f'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey={service_key}&searchYearCd=2020&siDo=42&guGun=110&type=json&numOfRows=9999&pageNo=1'
# url = f'http://apis.data.go.kr/B552061/frequentzoneTmzon/getRestFrequentzoneTmzon?serviceKey={service_key}&searchYearCd=2017&siDo=11&guGun=680&type=json&numOfRows=9999&pageNo=1'
# print(url)


# resp = requests.get(url)
# # json
# json = resp.json()
# # print(json)




with open(f'fffffff.json', 'r', encoding='utf-8') as f:
    total_json = json.load(f)

print(total_json['2020'])