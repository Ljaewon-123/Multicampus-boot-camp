import folium
import requests

url = 'http://apis.data.go.kr/1520635/OceanBiospeciesInfoService/getOceanBiospeciesResult?' \
      'serviceKey=SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D&' \
      'numOfRows=1000000000&pageNo=1'
print(url)

resp = requests.get(url)
print(resp)