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

def find_obs(obs_type):
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
    tmp = {now.strftime("%Y%m%d"): {}}
    # print(tmp)
    for obs_id in obs_lst:
        lst_data = []
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
            lst_data.append(json_data['result']['data'][-1])
            tmp[now.strftime("%Y%m%d")][obs_id] = lst_data
    return tmp

obs_lst = find_obs('파고')  # 매개변수 해당하는 관측소들 뽑음
obs_lst2 = find_obs('풍향')
input_data1 = marine_weather(obs_lst,'obsWaveHight') # 관측소에 맞는 기상정보 뽑음
input_data2 = marine_weather(obs_lst2,'tidalBuWind')

# 프로듀서 만듬  ,서버의 승인 기다리지 않고 버퍼에 추가 , 압축타입, 서버
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
