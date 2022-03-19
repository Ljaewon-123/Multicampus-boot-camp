# -*- coding:utf-8 -*-
from xml.etree import ElementTree
import requests
import json

SiDo = {'서울특별시':['11',{'강남구':'680','강동구':'740','강북구':'305','강서구':'500','관악구':'620','광진구':'215','구로구':'530','금천구':'545','노원구':'350','도봉구':'320','동대문구':'230','동작구':'590','마포구':'440',
                       '서대문구':'410','서초구':'650','성동구':'200','성북구':'290','송파구':'710','양천구':'470','영등포구':'560','용산구':'170','은평구':'380','종로구':'110','중구':'140','중랑구':'260'}],
        '부산광역시':['26',{'강서구':'440','금정구':'410','기장군':'710','남구':'290','동구':'170','동래구':'260','부산진구':'230','북구':'320','사상구':'530','사하구':'380','서구':'140','수영구':'500','연제구':'470','영도구':'200','중구':'110','해운대구':'350'}],
        '대구광역시':'27',
        '인천광역시':'28',
        '광주광역시':'29',
        '대전광역시':'30',
        '울산광역시':'31',
        '세종특별자치시':'36',
        '경기도':'41',
        '강원도':'42',
        '충청북도':'43',
        '충청남도':'44',
        '전라북도':'45',
        '전라남도':'46',
        '경상북도':'47',
        '경상남도':'48',
        '제주특별자치도':'50'}

# print(SiDo['서울특별시'])
# print(SiDo['서울특별시'][0])
# print(SiDo['서울특별시'][1]['강남구'])
# print(SiDo['서울특별시'][1].keys())

Year = ['2017','2018','2019','2020']
sido_list = ['서울특별시','부산광역시']

print(SiDo[sido_list[0]][1].values())

service_key='SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'
for year in Year:
        print(year)
        for sido in sido_list:
                print(sido)
                if sido == '서울특별시':  # 일단 서울만 보자
                        for gugun in SiDo[sido][1].keys():
                                print(gugun)
                # url = f'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey={service_key}&searchYearCd={year}&siDo={SiDo[sido_list[0]][0]}&guGun={SiDo[sido_list[0]][1]["강남구"]}&type=json&numOfRows=9999&pageNo=1'
                                url = f'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey={service_key}&searchYearCd={year}&siDo={SiDo[sido_list[0]][0]}&guGun={SiDo[sido_list[0]][1][gugun]}&type=json&numOfRows=9999&pageNo=1'
                                print(url)

                                # format123 = 'asdf{0},{1},{2}'
                                # ff123 = format123.format(123,421,56)
                                # print(ff123)

                                resp = requests.get(url)
                                # json
                                json = resp.json()
                                # print(json)
                                # xml
                                # tree = ElementTree.fromstring(resp.text)
                                # print(tree)
                                '''
                                5 : 지점명  spot_nm
                                6 : 발생건수  occrrnc_cnt
                                7 : 사상자수  caslt_cnt
                                8 : 사망자수  dth_dnv_cnt
                                9 : 중상자수  se_dnv_cnt
                                10 : 경상자수  sl_dnv_cnt
                                12 : 폴리곤  geom_json
                                13 : 경도   lo_crd
                                14 : 위도   la_crd
                                
                                '''
                                # print(json['items']['item'])
                                data = json['items']['item']
                                # print(data)
                                lst = []
                                total_occrrnc_cnt ,total_caslt_cnt, total_dth_dnv_cnt,total_se_dnv_cnt ,total_sl_dnv_cnt = 0,0,0,0,0

                                for item in data:
                                        print(item)
                                        tmp = {}
                                        for key in item.keys():
                                                if key == 'spot_nm':
                                                        tmp['상세주소'] = item[key]
                                                elif key == 'occrrnc_cnt':
                                                        tmp['발생건수'] = item[key]
                                                        total_occrrnc_cnt += item[key]
                                                elif key == 'caslt_cnt':
                                                        tmp['사상자수'] = item[key]
                                                        total_caslt_cnt += item[key]
                                                elif key == 'dth_dnv_cnt':
                                                        tmp['사망자수'] = item[key]
                                                        total_dth_dnv_cnt += item[key]
                                                elif key == 'se_dnv_cnt':
                                                        tmp['중상자수'] = item[key]
                                                        total_se_dnv_cnt = +item[key]
                                                elif key == 'sl_dnv_cnt':
                                                        tmp['경상자수'] = item[key]
                                                        total_sl_dnv_cnt = +item[key]
                                                elif key == 'geom_json':
                                                        tmp['폴리곤'] = item[key]
                                                elif key == 'lo_crd':
                                                        tmp['경도'] = item[key]
                                                elif key == 'la_crd':
                                                        tmp['위도'] = item[key]
                                        lst.append(tmp)

                                # 데이터 없으면 에러 발생
                                try:
                                        tmp['총합발생건수'] = total_occrrnc_cnt
                                        tmp['총합사상자수'] = total_caslt_cnt
                                        tmp['총합사망자수'] = total_dth_dnv_cnt
                                        tmp['총합중상자수'] = total_se_dnv_cnt
                                        tmp['총합경상자수'] = total_sl_dnv_cnt
                                        lst.append(tmp)
                                except NameError as e:
                                        print('데이터가 없음')

                                print(lst)
                                gu = {gugun:lst}
                                print(gu)
                        print(gu)


# a = {'s':['11',{'asdf':'123',"zxcv":'568'}]}
# print(a['s'][1].values())

# 유형== 파일이름?? 밑에 시도 밑에 년도 밑에 구별 데이터
# 파일 명을 유형별로?? 할꺼면 파일명을 리스트에 안넣어도됨
# class 에서 url 를 매개변수로 받는 형식 문제 : 파일 저장 으캄
# 매개변수로 url과 파일 명을 같이 받음


# xml
# print(tree[1][0].text)
# for item in tree[1][0]:  # response 는 안잡힘
#     print(f"지점명(상세주소): {item[5].text}\n발생건수: {item[6].text} 사상자수: {item[7].text} 사망자수: {item[8].text}"
#           f" 중상자수: {item[9].text} 경상자수: {item[10].text}\n폴리곤: {item[12].text} 경도: {item[13].text} 위도: {item[14].text}")
    # a = item.find('spot_nm').text
    # b = item.get('spot_nm')
    # print(a,b)
    # get 은 뭐야??

# 어떤 형식으로 저장??? 일단 json 이라고 하고 모든 사고다발지역의 url 과 시도 , 구 자동으로 전부~!! 해야함