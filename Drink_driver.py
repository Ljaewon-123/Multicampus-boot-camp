import requests
import json

service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'


url = f'https://api.odcloud.kr/api/15094170/v1/uddi:9011cf90-a379-4eca-bb29-8dcf99c11f1d?page=1&perPage=9999&serviceKey={service_key}'
# print(url)
#

resp = requests.get(url)

json_res = resp.json()
# print(json_res)

# print(json_res['data'])
sido_list = ['서울','제주','부산']

# dic = {}

def plz_stop(sido1):
    lst = []
    dic = {}
    for sido in json_res['data']:  # 같은시가 끝날때 까지 같음 // 시 끼리 묶여있음

        if sido['시도'] == sido1:
            lst.append(sido)
        elif sido['시도'] != sido1 :
            dic[sido1] = lst

    print(dic)


for ss in sido_list:
    plz_stop(ss)



