from xml.etree import ElementTree
import requests
import re

service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'

url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
print(url)

resp = requests.get(url)
tree = ElementTree.fromstring(resp.text)   # 이것도 parser tree 만드는거
print(tree)

for items in tree[1][0]:
    # print(items[3].text)
    if items[3].text == '대전':
        str_it = items[0].text
        print(f'{str_it[2:4] + "/" + str_it[5:7] + "/" + str_it[8:10]}\n'
              f'일일합계 {items[6].text}\n'
              f'국내합계 {items[7].text}\n'
              f'해외합계 {items[8].text}\n')