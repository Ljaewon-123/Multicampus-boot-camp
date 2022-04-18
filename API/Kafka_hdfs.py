# -*- coding:utf-8 -*-
from kafka import KafkaProducer
from kafka import KafkaConsumer
import requests
import json
from pyspark.sql import SparkSession
import time
from pymongo import MongoClient
from hdfs import InsecureClient


# spark = SparkSession.builder.master("yarn").appName("kafka_spark").getOrCreate()

url = 'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode=DT_0002&Date=20220415&ResultType=json'

resp = requests.get(url)

json_data = resp.json()


input_data = json_data['result']['data']
# print(data)

producer = KafkaProducer(acks=0,compression_type='gzip',bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

start = time.time()

data = input_data
producer.send('hello',value=data)
producer.flush()

print('elapsed :',time.time() - start)

consumer = KafkaConsumer(
    'hello',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group', # --group my-group 와 같다
    value_deserializer= lambda x:json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000
)

client = InsecureClient('http://localhost:9870', user='jaewon')

lst = []
for message in consumer:
    records = message.value # only last value if you all data lst.append(message.value)
    print(records)

# records = my_data

# client.write('data/file.jsonl',data=json.dumps(records),encoding(utf-8)
with client.write('data/records2.jsonl',append=True  ,encoding='utf-8') as writer:
# with client.upload('data/records2.jsonl', encoding='utf-8') as writer:
    json.dump(records, writer)


print('The end')
