# -*- coding:utf-8 -*-
from kafka import KafkaProducer
from kafka import KafkaConsumer
import requests
import json
import datetime
import time
from pymongo import MongoClient
from hdfs import InsecureClient
from kafka.structs import TopicPartition

# ./bin/kafka-topics.sh --create  --bootstrap-server localhost:9092 --partitions 6 --replication-factor 1 --topic multiconsumer


now = datetime.datetime.now()
date = datetime.datetime.today().strftime("%Y%m%d")
nowDate = now.strftime("%Y%m%d")
print(now.strftime('%Y%m%d'))

pago_obs_lst = ['DT_0042', 'DT_0041', 'IE_0060', 'IE_0062', 'IE_0061', 'TW_0089', 'TW_0079', 'TW_0080', 'TW_0081', 'TW_0092', 'TW_0090', 'TW_0062', 'TW_0069', 'TW_0075', 'TW_0091', 'TW_0093', 'TW_0094', 'KG_0021', 'KG_0024', 'KG_0025', 'KG_0028', 'KG_0101']
Ocean_buoy_wind_obs = ['TW_0089','TW_0091','KG_0025','TW_0069','KG_0024','TW_0094','TW_0079','TW_0081','TW_0093','TW_0090','TW_0080','KG_0101','TW_0092','KG_0021','KG_0028','TW_0075','TW_0062']
condolence = ['DT_0063','DT_0032','DT_0031','DT_0029','DT_0058','DT_0026','DT_0049','DT_0018','DT_0017','DT_0065','DT_0057','DT_0062','DT_0023','DT_0007','DT_0006','DT_0025','DT_0005','DT_0056','DT_0061',
            'DT_0010','DT_0051','DT_0022','DT_0012','DT_0008','DT_0067','DT_0037','DT_0016','DT_0092','DT_0003','DT_0044','DT_0043','DT_0027','DT_0013','DT_0020','DT_0068','DT_0001','DT_0052','DT_0024',
            'DT_0004','DT_0028','DT_0021','DT_0050','DT_0014','DT_0002','DT_0091','DT_0066','DT_0011','DT_0035']
Ocean_buoy = ['TW_0088', 'TW_0077', 'TW_0089', 'TW_0074', 'TW_0072', 'TW_0091', 'KG_0025', 'TW_0069', 'KG_0024',
             'TW_0085', 'TW_0094', 'TW_0087', 'TW_0086', 'TW_0079'
             ,'TW_0081', 'TW_0093', 'TW_0090', 'TW_0083', 'TW_0078', 'TW_0080', 'KG_0101', 'TW_0076', 'TW_0092', 'KG_0021',
             'KG_0028', 'TW_0075', 'TW_0082', 'TW_0084', 'TW_0070', 'TW_0062']

def marine_weather(obs_lst,kind_weather):
    url = 'http://www.khoa.go.kr/api/oceangrid/{0}/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode={1}&Date={2}&ResultType=json'
    # tmp = {now.strftime("%Y%m%d"): {}}
    # print(tmp)
    lst_data = []
    for obs_id in obs_lst:
        # lst_data = []
        pago_url = url.format(kind_weather, obs_id, now.strftime('%Y%m%d'))
        # print(pago_url)
        resp = requests.get(pago_url)

        json_data = resp.json()
        # print(json_data)
        # print(list(json_data['result'].keys()))
        if list(json_data['result'].keys())[0] == 'error':
            continue
        else:
            # print(json_data['result']['data'][-1])
            # print(json_data['result']['meta'])
            # lst_data.append(json_data['result']['data'][-1])
            # tmp[now.strftime("%Y%m%d")][obs_id] = lst_data
            tmp_ex = json_data['result']['data'][-1]
            tmp_ex['obs_code'] = obs_id
            lst_data.append(tmp_ex)

    tmp = lst_data
    return tmp


def jo_temp():

    api_url = 'http://www.khoa.go.kr/api/oceangrid/tideObsTemp/search.do'

    obs_codes=['DT_0063','DT_0031','DT_0029','DT_0026','DT_0018','DT_0017','DT_0062','DT_0023','DT_0007','DT_0006','DT_0025','DT_0005','DT_0061'
        ,'DT_0010','DT_0022','DT_0012','DT_0008','DT_0067','DT_0037','DT_0016','IE_0062','DT_0027','DT_0013','DT_0020','IE_0060','DT_0001'
        ,'DT_0004','DT_0028','DT_0021','DT_0014','DT_0002','DT_0091','DT_0011','DT_0035']

    service_key='RUGtj1GPESsGHsiqinO2BA=='
    # date=datetime.today().strftime("%Y%m%d")
    result_type='json'
    #?ServiceKey=인증키&ObsCode=관측소 번호&Date=검색 기준 날짜&ResultType=json

    # 이 api의 총 데이터 갯수 구해서 마지막
    data_list=[]

    for obs_code in obs_codes:
        url = api_url + f'?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType={result_type}'
        temp_resp = requests.get(url)
        temp_data = temp_resp.json()
        if list(temp_data['result'].keys())[0] == 'error':  # 해당함수 에러 키 처리 안되있어서 추가
            continue
        else:
            cnt = len(temp_data["result"]["data"])
            # print(temp_data["result"]["data"][cnt-1])
            data = temp_data["result"]["data"][cnt - 1]
            data_dict = {}
            # data_dict['obs_code'] = obs_code
            data_dict['record_time']=data['record_time']
            data_dict['water_temp']=data['water_temp']
            data_dict['obs_code'] = obs_code
            data_list.append(data_dict)

    result=data_list
    return result

def bu_temp():


    api_url = 'http://www.khoa.go.kr/api/oceangrid/tidalBuTemp/search.do'

    obs_codes = ['TW_0088', 'TW_0077', 'TW_0089', 'TW_0074', 'TW_0072', 'TW_0091', 'KG_0025', 'TW_0069', 'KG_0024',
                 'TW_0085', 'TW_0094', 'TW_0087', 'TW_0086', 'TW_0079'
        , 'TW_0081', 'TW_0093', 'TW_0090', 'TW_0083', 'TW_0078', 'TW_0080', 'KG_0101', 'TW_0076', 'TW_0092', 'KG_0021',
                 'KG_0028', 'TW_0075', 'TW_0082', 'TW_0084', 'TW_0070', 'TW_0062']

    service_key = 'RUGtj1GPESsGHsiqinO2BA=='
    # date = datetime.today().strftime("%Y%m%d")
    result_type = 'json'

    data_list=[]

    for obs_code in obs_codes:
        url = api_url + f'?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType={result_type}'
        temp_resp = requests.get(url)
        temp_data = temp_resp.json()
        cnt = len(temp_data["result"]["data"])
        if list(temp_data['result'].keys())[0] == 'error': # 해당함수 에러 키 처리 안되있어서 추가
            continue
        else:
            data = temp_data["result"]["data"][cnt - 1]
            data_dict = {}
            # data_dict['obs_code'] = obs_code
            data_dict['record_time']=data['record_time']
            data_dict['water_temp']=data['water_temp']
            data_dict['obs_code'] = obs_code
            data_list.append(data_dict)

    result=data_list
    return result

def jo_actual_condel():
    obs_post_id_list = ['DT_0063', 'DT_0032', 'DT_0031', 'DT_0029', 'DT_0058', 'DT_0026', 'DT_0049', 'DT_0018', 'DT_0017',
                  'DT_0065', 'DT_0057', 'DT_0062', 'DT_0023', 'DT_0007', 'DT_0006', 'DT_0025', 'DT_0005', 'DT_0056',
                  'DT_0061',
                  'DT_0010', 'DT_0051', 'DT_0022', 'DT_0012', 'DT_0008', 'DT_0067', 'DT_0037', 'DT_0016', 'DT_0092',
                  'DT_0003', 'DT_0044', 'DT_0043', 'DT_0027', 'DT_0013', 'DT_0020', 'DT_0068', 'DT_0001', 'DT_0052',
                  'DT_0024',
                  'DT_0004', 'DT_0028', 'DT_0021', 'DT_0050', 'DT_0014', 'DT_0002', 'DT_0091', 'DT_0066', 'DT_0011',
                  'DT_0035']

    condolence_list = list()
    Key = 'PcaRy7HmUIAEp7FrsZX3hg=='
    for k in range(0, len(obs_post_id_list)):
        url = f'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey={Key}&ObsCode={obs_post_id_list[k]}&Date={nowDate}&ResultType=json'
        resp = requests.get(url).json()

        try:
            temp_dict = dict()
            # print(resp)
            # temp_dict['obs_post_id']=obs_post_id_list[k]
            temp_dict['record_time'] = resp["result"]["data"][-1]["record_time"]
            temp_dict['wind_dir'] = resp["result"]["data"][-1]["tide_level"]
            temp_dict['obs_code'] = obs_post_id_list[k]
            condolence_list.append(temp_dict)

        except:
            # print('error')
            continue
    return condolence_list

def jo_actual_wind():
    obs_post_id_list = ['DT_0063', 'DT_0032', 'DT_0031', 'DT_0029', 'DT_0058', 'DT_0026', 'DT_0049', 'DT_0018',
                        'DT_0017',
                        'DT_0065', 'DT_0057', 'DT_0062', 'DT_0023', 'DT_0007', 'DT_0006', 'DT_0025', 'DT_0005',
                        'DT_0056',
                        'DT_0061',
                        'DT_0010', 'DT_0051', 'DT_0022', 'DT_0012', 'DT_0008', 'DT_0067', 'DT_0037', 'DT_0016',
                        'DT_0092',
                        'DT_0003', 'DT_0044', 'DT_0043', 'DT_0027', 'DT_0013', 'DT_0020', 'DT_0068', 'DT_0001',
                        'DT_0052',
                        'DT_0024',
                        'DT_0004', 'DT_0028', 'DT_0021', 'DT_0050', 'DT_0014', 'DT_0002', 'DT_0091', 'DT_0066',
                        'DT_0011',
                        'DT_0035']

    wind_list = list()
    Key = 'PcaRy7HmUIAEp7FrsZX3hg=='
    for k in range(0, len(obs_post_id_list)):
        url = f'http://www.khoa.go.kr/api/oceangrid/tideObsWind/search.do?ServiceKey={Key}&ObsCode={obs_post_id_list[k]}&Date={nowDate}&ResultType=json'
        resp = requests.get(url).json()

        try:
            temp_dict = dict()
            # temp_dict['obs_post_id']=obs_post_id_list[k]
            temp_dict['record_time'] = resp["result"]["data"][-1]["record_time"]
            temp_dict['wind_dir'] = resp["result"]["data"][-1]["wind_dir"]
            temp_dict['wind_speed'] = resp["result"]["data"][-1]["wind_speed"]
            temp_dict['obs_code'] = obs_post_id_list[k]
            wind_list.append(temp_dict)

        except:
            # print('error')
            continue
    return wind_list

start = time.time()

pago_data = marine_weather(pago_obs_lst,'obsWaveHight') # 관측소에 맞는 기상정보 뽑음
Ocean_buoy_wind_data = marine_weather(Ocean_buoy_wind_obs,'tidalBuWind')
jo_temp_data = jo_temp()
bu_temp_data = bu_temp()
jo_actual_condel_data=jo_actual_condel()
jo_actual_wind_data = jo_actual_wind()

print('elapsed :', time.time() - start)

print('confirm')

producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['54.65.104.126:8992'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

start = time.time()

data1 = pago_data
data2 = Ocean_buoy_wind_data
data3 = jo_temp_data
data4 = bu_temp_data
data5 = jo_actual_condel_data
data6 = jo_actual_wind_data
producer.send('multiconsumer', key=b'pago', value=data1,partition=0)  # key = bytes string
producer.send('multiconsumer', key=b'tidalBuWind', value=data2,partition=1)
producer.send('multiconsumer', key=b'jo_temp_data', value=data3,partition=2)
producer.send('multiconsumer', key=b'bu_temp_data', value=data4,partition=3)
producer.send('multiconsumer', key=b'jo_actual_condel_data', value=data5,partition=4)
producer.send('multiconsumer', key=b'jo_actual_wind_data', value=data6,partition=5)
# producer.send('pago_kafka',{'pago':data})
producer.flush()

print('elapsed :', time.time() - start)

# auto_offset_reset='latest' 이기때문에 처음돌때는 커밋이 안되서 안나옴 offset:1 부터 출력가능

consumer1 = KafkaConsumer(
#    'multiconsumer',
    bootstrap_servers=['54.65.104.126:8992'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='ocean_weather',  # --group ocean_weather 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000,

)

consumer2 = KafkaConsumer(
#    'multiconsumer',
    bootstrap_servers=['54.65.104.126:8992'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='ocean_weather',  # --group ocean_weather 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000,

)
consumer3 = KafkaConsumer(
#    'multiconsumer',
    bootstrap_servers=['54.65.104.126:8992'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='ocean_weather',  # --group ocean_weather 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000,

)
consumer4 = KafkaConsumer(
#    'multiconsumer',
    bootstrap_servers=['54.65.104.126:8992'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='ocean_weather',  # --group ocean_weather 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000,

)
consumer5 = KafkaConsumer(
#    'multiconsumer',
    bootstrap_servers=['54.65.104.126:8992'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='ocean_weather',  # --group ocean_weather 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000,

)
consumer6 = KafkaConsumer(
#    'multiconsumer',
    bootstrap_servers=['54.65.104.126:8992'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='ocean_weather',  # --group ocean_weather 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000,

)



consumer1.assign([TopicPartition('multiconsumer',0)])
consumer2.assign([TopicPartition('multiconsumer',1)])
consumer3.assign([TopicPartition('multiconsumer',2)])
consumer4.assign([TopicPartition('multiconsumer',3)])
consumer5.assign([TopicPartition('multiconsumer',4)])
consumer6.assign([TopicPartition('multiconsumer',5)])
#print(consumer1.assignment())
#print(consumer1)

client = InsecureClient('http://localhost:9870', user='ubuntu')

con_lst = []

con_lst.extend([consumer1,consumer2,consumer3,consumer4,consumer5,consumer6])

for multi_consumer in con_lst:
    print('one partition')
    for message in multi_consumer:
        records = message.value  # only last value if you all data lst.append(message.value)
        #    print(records)
        #    consumer.commit()
        print("topic %s:partition %d:offset %d: key=%s value=%s" % (message.topic, message.partition,
                                                                    message.offset, message.key,
                                                                    message.value))
        if message.key == b'pago':
            with client.write('data/pago.jsonl', overwrite=True, encoding='utf-8') as writer:
                json.dump(records, writer)
        elif message.key == b'tidalBuWind':
            with client.write('data/tidalBuWind.jsonl', overwrite=True, encoding='utf-8') as writer:
                json.dump(records, writer)
        elif message.key == b'jo_temp_data':
            with client.write('data/jo_temp_data.jsonl', overwrite=True, encoding='utf-8') as writer:
                json.dump(records, writer)
        elif message.key == b'bu_temp_data':
            with client.write('data/bu_temp_data.jsonl', overwrite=True, encoding='utf-8') as writer:
                json.dump(records, writer)
        elif message.key == b'jo_actual_condel_data':
            with client.write('data/jo_actual_condel_data.jsonl', overwrite=True, encoding='utf-8') as writer:
                json.dump(records, writer)
        elif message.key == b'jo_actual_wind_data':
            with client.write('data/jo_actual_wind_data.jsonl', overwrite=True, encoding='utf-8') as writer:
                json.dump(records, writer)



consumer1.commit()
consumer2.commit()
consumer3.commit()
consumer4.commit()
consumer5.commit()
consumer6.commit()


print('The end')
