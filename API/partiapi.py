# -*- coding:utf-8 -*-
from kafka import KafkaProducer
from kafka import KafkaConsumer
import requests
import json
import datetime
from pyspark.sql import SparkSession
import time
from pymongo import MongoClient
from hdfs import InsecureClient


## Pago PAGO PAgo pago

def find_obs(obs_type):  # 속도를 조금이라도 높이기 위해 잠금
    url = 'http://www.khoa.go.kr/api/oceangrid/ObsServiceObj/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ResultType=json'

    # print(url)
    # print(url2)

    resp = requests.get(url)
    # print(resp)

    json_data = resp.json()
    # print(json_data)

    # print(json_data['result']['data'])
    lst_type = []
    for obs in json_data['result']['data']:
        # print(obs['obs_object'].split(','))
        obs_lst = obs['obs_object'].split(',')
        for lst in obs_lst:
            if lst == obs_type:  # 관측소가 2개만 있는게 아니라 더있음 그래서 여기까지만 찾고 관측소는 따로 만지는걸로
                # print(obs)
                lst_type.append(obs['obs_post_id'])

    # print(lst_type)

    return lst_type


now = datetime.datetime.now()
print(now.strftime('%Y%m%d'))




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
            tmp_ex['obs'] = obs_id
            lst_data.append(tmp_ex)

    tmp = lst_data
    return tmp

# obs_lst = find_obs('파고')  # 매개변수 해당하는 관측소들 뽑음
# obs_lst2 = find_obs('풍향')
pago_obs_lst = ['DT_0042', 'DT_0041', 'IE_0060', 'IE_0062', 'IE_0061', 'TW_0089', 'TW_0079', 'TW_0080', 'TW_0081', 'TW_0092', 'TW_0090', 'TW_0062', 'TW_0069', 'TW_0075', 'TW_0091', 'TW_0093', 'TW_0094', 'KG_0021', 'KG_0024', 'KG_0025', 'KG_0028', 'KG_0101']
wind_obs_lst = ['DT_0063', 'DT_0031', 'DT_0029', 'DT_0058', 'DT_0026', 'DT_0049', 'DT_0018', 'DT_0017', 'DT_0065', 'DT_0057', 'DT_0062', 'DT_0023', 'DT_0007', 'DT_0006', 'DT_0025', 'DT_0005', 'DT_0056', 'DT_0061', 'DT_0010', 'DT_0051', 'DT_0022', 'DT_0012', 'DT_0008', 'DT_0067', 'DT_0037', 'DT_0016', 'DT_0092', 'DT_0003', 'DT_0043', 'DT_0027', 'DT_0013', 'DT_0020', 'DT_0068', 'DT_0001', 'DT_0052', 'DT_0024', 'DT_0004', 'DT_0028', 'DT_0021', 'DT_0050', 'DT_0014', 'DT_0002', 'DT_0091', 'DT_0066', 'DT_0011', 'DT_0035', 'DT_0042', 'DT_0041', 'IE_0060', 'IE_0062', 'IE_0061', 'TW_0089', 'TW_0079', 'TW_0080', 'TW_0081', 'TW_0092', 'TW_0090', 'TW_0062', 'TW_0069', 'TW_0075', 'TW_0091', 'TW_0093', 'TW_0094', 'KG_0021', 'KG_0024', 'KG_0025', 'KG_0028', 'KG_0101']

input_data1 = marine_weather(pago_obs_lst,'obsWaveHight') # 관측소에 맞는 기상정보 뽑음
input_data2 = marine_weather(wind_obs_lst,'tidalBuWind')

# 프로듀서 만듬  ,서버의 승인 기다리지 않고 버퍼에 추가 , 압축타입, 서버
'''
acks=0 : 프로듀서는 서버로부터 어떠한 ack도 기다리지 않습니다. 이 경우 서버가 데이터를 받았는지 보장하지 않고,
 클라이언트는 전송 실패에 대한 결과를 알지 못하기 때문에 재요청 설정도 적용되지 않습니다. 메시지가 손실될 수 있지만,
 서버로부터 ack에 대한 응답을 기다리지 않기 때문에 매우 빠르게 메시지를 보낼 수 있어 높은 처리량을 얻을 수 있습니다.
'''
producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

start = time.time()

data = input_data1
data2 = input_data2
producer.send('partiAPI', key=b'pago', value=data,partition=0)  # key = bytes string
producer.send('partiAPI', key=b'tidalBuWind', value=data2,partition=1)
# producer.send('pago_kafka',{'pago':data})
producer.flush()

print('elapsed :', time.time() - start)

consumer = KafkaConsumer(
    'partiAPI',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='parti_test',  # --group my-group 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000
)

client = InsecureClient('http://localhost:9870', user='jaewon')

lst = []
for message in consumer:
    records = message.value  # only last value if you all data lst.append(message.value)
    #    print(records)
    #    consumer.commit()
    print("topic %s:partition %d:offset %d: key=%s value=%s" % (message.topic, message.partition,
                                                                message.offset, message.key,
                                                                message.value))
    if message.key == b'pago':
        with client.write('data/pago_test.jsonl', overwrite=True, encoding='utf-8') as writer:
            json.dump(records, writer)
    elif message.key == b'tidalBuWind':
        with client.write('data/tidalBuWind_test.jsonl', overwrite=True, encoding='utf-8') as writer:
            json.dump(records, writer)


consumer.commit()



print('The end')

''' spark function 
pago_json = spark.read.json('/pago_test.json')

from pyspark.sql.functions import explode

pago01 = pago_json.select("20220420.*")
pago_ie_0060 = pago01.select("IE_0060")
pago_ie_0060_ele = pago_ie_0060.select(pago_ie_0060["IE_0060"].getItem(0).alias('ie_0060'))

pago_ie_0060_ele.select("ie_0060.*").show()
'''
