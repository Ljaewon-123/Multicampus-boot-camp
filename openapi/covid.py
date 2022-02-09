from xml.etree import ElementTree
import requests
import re

service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'

url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
#  활용에서 endpoint 구분 확실히 할것
print(url)

resp = requests.get(url)
# print(resp.text)
tree = ElementTree.fromstring(resp.text)   # 이것도 parser tree 만드는거
# print(tree)
# 트리의 자식 자식
for items in tree[1][0]:
    # print(items[3].text)
    if items.find('gubun').text == '합계':
        stdDay = re.sub(r'(\D)+','',items.find('stdDay').text)  # 정규표현식
        # print(stdDay)
        stdDay = stdDay[2:4] + '/' + stdDay[4:6] + '/' + stdDay[6:8]
        print(stdDay)
        # items.find('incDec').text
        print(f'일일합계: {items[6].text} \n'
              f'국내발생: {items[8].text} \n'
              f'해외발생: {items[9].text} \n')
