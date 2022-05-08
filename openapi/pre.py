from xml.etree import ElementTree
import requests

service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'

url = f'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey={service_key}&searchYearCd=2020&siDo=42&guGun=780&type=xml&numOfRows=9999&pageNo=1'
print(url)

resp = requests.get(url)
tree = ElementTree.fromstring(resp.text)
print(tree)
