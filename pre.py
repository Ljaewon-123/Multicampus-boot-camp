import folium
import requests

url = 'http://apis.data.go.kr/1520635/OceanBiospeciesInfoService/getOceanBiospeciesResult?' \
      'serviceKey=SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D&' \
      'numOfRows=100000&pageNo=1'

# # # 해양수산부 조위 실측 실측치가 있다!
# url = 'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode=DT_0002&Date=20220412&ResultType=json'
# #
# # # http://www.khoa.go.kr/api/oceangrid/tideObsPre/search.do?ServiceKey=인증키&ObsCode=관측소 번호&Date=검색 기준 날짜&ResultType=json
# # # 예측
# url2 = 'http://www.khoa.go.kr/api/oceangrid/tideObsPre/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode=DT_0002&Date=20190412&ResultType=json'


print(url)
# print(url2)

resp = requests.get(url)
print(resp)