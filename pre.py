import requests
import json
# from json_class import Traffic

# service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'
# # #
# # url = f'http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking?serviceKey={service_key}&searchYearCd=2019&siDo=11&guGun=620&type=json&numOfRows=9999&pageNo=1'
# # 음주  전부 한번에
# url = f'https://api.odcloud.kr/api/15094170/v1/uddi:9011cf90-a379-4eca-bb29-8dcf99c11f1d?page=1&perPage=9999&serviceKey={service_key}'
# print(url)
# #
#
# resp = requests.get(url)
#
# json_res = resp.json()
# print(json_res)


with open(f'namename.json', 'r', encoding='utf-8') as f:
    total_json = json.load(f)

print(total_json.keys())
# print(total_json['2020'])  # 각 sido 리스트의 키 번지수가 될수도?
print(total_json['2020'][0]['서울특별시'][0].keys())
# print(total_json['2020'][0]['서울특별시'][3].keys())

new_json = {}
json_DD = {}
for YY in total_json.keys():
    for SS in total_json[YY][0].keys():
        # print(SS)
        # new_json[YY] = SS
        for GG in total_json[YY][0][SS][0].keys():
            # print(GG)
            # new_json[YY] = {SS:GG}
            # new_json[SS] = GG
            for DD in total_json[YY][0][SS][0][GG]:
                # print(DD)
                # print(DD.keys())
                json_DD[GG] = DD
                print(json_DD)
                new_json[YY] = {SS:json_DD}
                # print(new_json)

# print(new_json)

# 값 하나당 row 하나


# {year:{sido:{gugun:{details:data},{details:data},{details:data},},{gugun:{details:data},{details:data},{details:data}},
#       {sido:{gugun:{details:data},{details:data},{details:data},},{gugun:{details:data},{details:data},{details:data}},{year{{{}}}}
#

#
# print(total_json['2017'][0]['서울특별시'])
#
# for plz in total_json['2018'][0]['서울특별시'][4]['관악구']:
#     print(plz)
#     res_json = json.dumps(plz, ensure_ascii=False)
#     with open(f'T_T.json', 'a', encoding='utf-8') as f:
#         f.write(res_json + '\n')



# 한줄씩 쓴다