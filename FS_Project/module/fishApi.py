import requests
import json
import xml
from kafka import KafkaProducer
from datetime import *
from dateutil.relativedelta import relativedelta
import xmltodict
from kafka import KafkaConsumer
from json import loads
from hdfs import InsecureClient




# 조위 실측 수온 각 관측소 별 최신 데이터 가져오기 api
def jo_temp():

    #producer = KafkaProducer(acks=0,
    #                         compression_type='gzip',
    #                         bootstrap_servers=['56.104.126:8992'],
    #                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


    api_url = 'http://www.khoa.go.kr/api/oceangrid/tideObsTemp/search.do'


    obs_codes=['DT_0063','DT_0031','DT_0029','DT_0026','DT_0018','DT_0017','DT_0062','DT_0023','DT_0007','DT_0006','DT_0025','DT_0005','DT_0061'
        ,'DT_0010','DT_0022','DT_0012','DT_0008','DT_0067','DT_0037','DT_0016','IE_0062','DT_0027','DT_0013','DT_0020','IE_0060','DT_0001'
        ,'DT_0004','DT_0028','DT_0021','DT_0014','DT_0002','DT_0091','DT_0011','DT_0035']

    service_key='RUGtj1GPESsGHsiqinO2BA=='
    date=datetime.today().strftime("%Y%m%d")
    result_type='json'
    #?ServiceKey=인증키&ObsCode=관측소 번호&Date=검색 기준 날짜&ResultType=json

    # 이 api의 총 데이터 갯수 구해서 마지막
    data_list=[]

    for obs_code in obs_codes:
        url = api_url + f'?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType={result_type}'
        temp_resp = requests.get(url)
        temp_data = temp_resp.json()
        cnt = len(temp_data["result"]["data"])
        # print(temp_data["result"]["data"][cnt-1])
        data = temp_data["result"]["data"][cnt - 1]
        data_dict = {}
        data_dict['obs_code'] = obs_code
        data_dict['record_time']=data['record_time']
        data_dict['water_temp']=data['water_temp']
        data_list.append(data_dict)

    result=data_list

    with open('../data/jo_temp.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)

    #print(data_list)

    #producer.send('Hello',key=?, value=data_dict)
    #producer.flush()


#해양 부이 수온 각 관측소 별 최신 데이터 가져오기 api
def bu_temp():
    #producer = KafkaProducer(acks=0,
    #                         compression_type='gzip',
    #                         bootstrap_servers=['localhost:9092'],
    #                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    api_url = 'http://www.khoa.go.kr/api/oceangrid/tidalBuTemp/search.do'

    obs_codes = ['TW_0088', 'TW_0077', 'TW_0089', 'TW_0074', 'TW_0072', 'TW_0091', 'KG_0025', 'TW_0069', 'KG_0024',
                 'TW_0085', 'TW_0094', 'TW_0087', 'TW_0086', 'TW_0079'
        , 'TW_0081', 'TW_0093', 'TW_0090', 'TW_0083', 'TW_0078', 'TW_0080', 'KG_0101', 'TW_0076', 'TW_0092', 'KG_0021',
                 'KG_0028', 'TW_0075', 'TW_0082', 'TW_0084', 'TW_0070', 'TW_0062']

    service_key = 'RUGtj1GPESsGHsiqinO2BA=='
    date = datetime.today().strftime("%Y%m%d")
    result_type = 'json'

    data_list=[]

    for obs_code in obs_codes:
        url = api_url + f'?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType={result_type}'
        temp_resp = requests.get(url)
        temp_data = temp_resp.json()
        cnt = len(temp_data["result"]["data"])
        data = temp_data["result"]["data"][cnt - 1]
        data_dict = {}
        data_dict['obs_code'] = obs_code
        data_dict['record_time']=data['record_time']
        data_dict['water_temp']=data['water_temp']
        data_list.append(data_dict)

    result=data_list

    with open('../data/bu_temp.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)

    # producer.send('test',key='?', value=data_dict)
    # producer.flush()


# 해무 api 오늘 기준 앞뒤 6달 해야하는데 1달만 일단 ..
def seafog():
    #producer = KafkaProducer(acks=0,
    #                         compression_type='gzip',
    #                         bootstrap_servers=['localhost:9092'],
    #                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    api_url = 'http://www.khoa.go.kr/api/oceangrid/seafog/search.do'
    obs_codes = ['SF_0001','SF_0002','SF_0003','SF_0004','SF_0005','SF_0006','SF_0007','SF_0008','SF_0009','SF_0010','SF_0011']

    service_key = 'RUGtj1GPESsGHsiqinO2BA=='
    result_type = 'json'

    today = datetime.today()
    #ago_6mon= (today - relativedelta(months=1))
    #after_6mon = (today + relativedelta(months=1))

    #dates_range = [(ago_6mon + timedelta(n)) for n in range(int((after_6mon - ago_6mon).days))]

    # 일주일 전 부터 이주 뒤
    dates_range = [(today + timedelta(n)) for n in range(-7,15)]

    per_hour_list=[]
    for i in dates_range:
        temp = [(i + timedelta(hours = j)).strftime("%Y%m%d%H") for j in range(-3,22)]
        per_hour_list.extend(temp)

    data_list=[]
    for obs_code in obs_codes:
        for date in per_hour_list:
            try:
                print(obs_code,date)
                url = api_url + f'?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType={result_type}'
                temp_resp = requests.get(url)
                temp_data = temp_resp.json()
                data = temp_data["result"]["data"][0]
                data_dict = {}
                data_dict['obs_code'] = obs_code
                data_dict['pre_time'] = data['pre_time']
                data_dict['seafog_master'] = data['seafog_master']
                data_list.append(data_dict)
            except:
                data_dict = {}
                data_dict['obs_code'] = obs_code
                data_dict['pre_time'] = datetime.strptime(date, '%Y%m%d%H').strftime("%Y-%m-%d %H:%M:%S")
                data_dict['seafog_master'] = '-'
                data_list.append(data_dict)



    result=data_list

    with open('../data/fog_temp.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)

    # producer.send('test',key='?', value=data_dict)
    # producer.flush()






def fish_spc():
    #producer = KafkaProducer(acks=0,
    #                         compression_type='gzip',
    #                         bootstrap_servers=['54.65.104.126:8992'],
    #                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    api_key = '8tUsV2I69mcbJU0vrzLkwwDjeUInZKMSlL3s64E%2B7rb5uv%2BTp7xSKOse8zFfECPaXSrMucFlmAoIYtDpHDCmNg%3D%3D'
    api_url ='http://apis.data.go.kr/1520635/OceanBiospeciesInfoService/getOceanBiospeciesResult?'
    url = api_url + f'ServiceKey={api_key}&pageNo=1&numOfRows=1'
    xml_string = requests.get(url).text
    # xmltodict.parse() 함수는 OrderedDict 으로 return
    dict = xmltodict.parse(xml_string)
    # JSON 형태로 변경하여 Dictionary로 변경
    item = json.loads(json.dumps(dict))
    cnt = int(item['response']['body']['totalCount'])
    print('total_count:' + str(cnt))


    items=list()

    url2 = api_url + f'ServiceKey={api_key}&pageNo=1&numOfRows=10000'
    xml_string2 = requests.get(url2).text
    dict2 = xmltodict.parse(xml_string2)
    item2 = json.loads(json.dumps(dict2))
    items.extend(item2['response']['body']['items']['item'])


    result=items

    with open('../data/fish_spc.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)











# 컨슈머
def consumer(key,location):
    client = InsecureClient('hdfs://54.65.104.126:9000/user/fish/data'+location, user='ubuntu')

    consumer = KafkaConsumer( 'test',
                              key='?',
                              bootstrap_servers=['54.65.104.126:8992'],
                              auto_offset_reset='latest',
                              enable_auto_commit=True,
                              group_id='?',
                              value_deserializer=lambda x: loads(x.decode('utf-8')),
                              consumer_timeout_ms=1000 )
    # consumer list를 가져온다


    for message in consumer:
        print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" % ( message.topic,
                                                                             message.partition,
                                                                             message.offset,
                                                                             message.key,
                                                                             message.value ))
        print('get consumer list')

    data = consumer.value

    with open((client+'.json'), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)




if __name__=='__main__':
    #fish_spc()
    #bu_temp()
    #jo_temp()
    seafog()





"""
[{"obs_code":"관측소코드","record_time": "2014-11-01 00:00","wave_height": "0.96”},
 {"obs_code":"관측소코드2","record_time": "2014-11-01 00:00","wave_height": "0.96”}]

"""
"""
수온
관측소 번호	관측소 명	위도	경도
DT_0063	가덕도	35.024	128.81
DT_0031	거문도	34.028	127.308
DT_0029	거제도	34.801	128.699
DT_0026	고흥발포	34.481	127.342
DT_0018	군산	35.975	126.563
DT_0017	대산	37.007	126.352
DT_0062	마산	35.197	128.576
DT_0023	모슬포	33.214	126.251
DT_0007	목포	34.779	126.375
DT_0006	묵호	37.55	129.116
DT_0025	보령	36.406	126.486
DT_0005	부산	35.096	129.035
DT_0061	삼천포	34.924	128.069
DT_0010	서귀포	33.24	126.561
DT_0022	성산포	33.474	126.927
DT_0012	속초	38.207	128.594
DT_0008	안산	37.192	126.647
DT_0067	안흥	36.674	126.129
DT_0037	어청도	36.117	125.984
DT_0016	여수	34.747	127.765
IE_0062	옹진소청초	37.423	124.738
DT_0027	완도	34.315	126.759
DT_0013	울릉도	37.491	130.913
DT_0020	울산	35.501	129.387
IE_0060	이어도	32.122	125.182
DT_0001	인천	37.451	126.592
DT_0004	제주	33.527	126.543
DT_0028	진도	34.377	126.308
DT_0021	추자도	33.961	126.3
DT_0014	통영	34.827	128.434
DT_0002	평택	36.966	126.822
DT_0091	포항	36.047	129.383
DT_0011	후포	36.677	129.453
DT_0035	흑산도	34.684	125.435
"""
"""
부이 수온
관측소 번호	관측소 명	위도	경도
TW_0088	감천항	35.052	129.003
TW_0077	경인항	37.523	126.592
TW_0089	경포대해수욕장	37.808	128.931
TW_0074	광양항	34.859	127.792
TW_0072	군산항	35.984	126.508
TW_0091	낙산해수욕장	38.122	128.65
KG_0025	남해동부	34.222	128.419
TW_0069	대천해수욕장	36.274	126.457
KG_0024	대한해협	34.919	129.121
TW_0085	마산항	35.103	128.631
TW_0094	망상해수욕장	37.593	129.09
TW_0087	부산항	35.091	129.085
TW_0086	부산항신항	35.043	128.761
TW_0079	상왕등도	35.652	126.194
TW_0081	생일도	34.258	126.96
TW_0093	속초해수욕장	38.198	128.631
TW_0090	송정해수욕장	35.164	129.219
TW_0083	여수항	34.794	127.808
TW_0078	완도항	34.325	126.763
TW_0080	우이도	34.543	125.802
KG_0101	울릉도북동	38.007	131.552
TW_0076	인천항	37.389	126.533
TW_0092	임랑해수욕장	35.302	129.292
KG_0021	제주남부	32.09	126.965
KG_0028	제주해협	33.7	126.59
TW_0075	중문해수욕장	33.234	126.409
TW_0082	태안항	37.006	126.27
TW_0084	통영항	34.773	128.46
TW_0070	평택당진항	37.136	126.54
TW_0062	해운대해수욕장	35.148	129.17
"""
"""
파고
관측소 번호	관측소 명	위도	경도
TW_0089	경포대해수욕장	37.808	128.931
DT_0042	교본초	34.704	128.306
TW_0091	낙산해수욕장	38.122	128.65
KG_0025	남해동부	34.222	128.419
TW_0069	대천해수욕장	36.274	126.457
KG_0024	대한해협	34.919	129.121
TW_0094	망상해수욕장	37.593	129.09
DT_0041	복사초	34.098	126.168
TW_0079	상왕등도	35.652	126.194
TW_0081	생일도	34.258	126.96
TW_0093	속초해수욕장	38.198	128.631
TW_0090	송정해수욕장	35.164	129.219
IE_0061	신안가거초	33.941	124.592
IE_0062	옹진소청초	37.423	124.738
TW_0080	우이도	34.543	125.802
KG_0101	울릉도북동	38.007	131.552
IE_0060	이어도	32.122	125.182
TW_0092	임랑해수욕장	35.302	129.292
KG_0021	제주남부	32.09	126.965
KG_0028	제주해협	33.7	126.59
TW_0075	중문해수욕장	33.234	126.409
TW_0062	해운대해수욕장	35.148
"""
"""
seafog
관측소 번호	관측소 명	위도	경도
SF_0001	부산항	35.091	129.099
SF_0002	부산신항	35.023	128.808
SF_0003	인천송도	37.379	126.616
SF_0004	평택풍도	37.113	126.393
SF_0005	군산	35.974	126.586
SF_0006	대산	36.977	126.304
SF_0007	목포	34.751	126.309
SF_0008	여수.광양항	34.754	127.752
SF_0009	해운대	35.159	129.16
SF_0010	울산	35.501	129.387
SF_0011	포항	36.051	129.378
"""