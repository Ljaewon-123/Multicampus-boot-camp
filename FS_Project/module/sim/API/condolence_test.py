# bs4
from bs4 import BeautifulSoup
import requests

# kafka
from kafka import KafkaProducer, KafkaConsumer

# hdfs
from hdfs import InsecureClient

#json
from json import loads, dumps, dump
import json
import time

from datetime import *

producer = KafkaProducer(acks=0,compression_type='gzip',bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8'))


consumer = KafkaConsumer(
    'condolence_kafka',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
    enable_auto_commit=True,
    group_id='G_test',  # --group my-group 와 같다
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=1000
)

client = InsecureClient('http://localhost:9870', user='sim')


# declare
Key = 'PcaRy7HmUIAEp7FrsZX3hg=='


#[DT_0063,DT_0032,DT_0031,DT_0029,DT_0058,DT_0026,DT_0049,DT_0018,DT_0017,DT_0065,DT_0057,DT_0062,DT_0023,DT_0007,DT_0006,DT_0025,DT_0005,DT_0056,DT_0061,
# DT_0010,DT_0051,DT_0022,DT_0012,DT_0008,DT_0067,DT_0037,DT_0016,DT_0092,DT_0003,DT_0044,DT_0043,DT_0027,DT_0013,DT_0020,DT_0068,DT_0001,DT_0052,DT_0024,
# DT_0004,DT_0028,DT_0021,DT_0050,DT_0014,DT_0002,DT_0091,DT_0066,DT_0011,DT_0035]
with open('/Users/sim/Coding/kafka_test/obs_post_id.txt', 'r') as f:
    kk = f.readline()

obs_post_id_list = ["DT_0063","DT_0032","DT_0031","DT_0029","DT_0058","DT_0026","DT_0049","DT_0018","DT_0017","DT_0065","DT_0057","DT_0062","DT_0023","DT_0007","DT_0006","DT_0025","DT_0005"\
    ,"DT_0056","DT_0061","DT_0010","DT_0051","DT_0022","DT_0012","DT_0008","DT_0067","DT_0037","DT_0016","DT_0092","DT_0003","DT_0044","DT_0043","DT_0027","DT_0013","DT_0020","DT_0068","DT_0001"\
        ,"DT_0052", "DT_0024", "DT_0004","DT_0028","DT_0021","DT_0050","DT_0014","DT_0002","DT_0091","DT_0066","DT_0011","DT_0035"]



now = datetime.now()
nowDate = now.strftime("%Y%m%d")

temp_dict = dict()
condolence_list = list()

for k in range(0, len(obs_post_id_list)):
    url = f'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey={Key}&ObsCode={obs_post_id_list[k]}&Date={nowDate}&ResultType=json'
    resp = requests.get(url).json()

    try:
        # print(resp)
        temp_dict['obs_post_id']=obs_post_id_list[k]
        temp_dict['record_time'] = resp["result"]["data"][-1]["record_time"]
        temp_dict['wind_dir'] = resp["result"]["data"][-1]["tide_level"]
        condolence_list.append(temp_dict)

    except:
        print('error')
        continue


producer.send('condolence_kafka', key=b'wind', value=condolence_list)  # key = bytes string
producer.flush()

for message in consumer:
    records = message.value  # only last value if you all data lst.append(message.value)

consumer.commit()


# 78 바꿔야함..
with client.write('data/condolence.jsonl', overwrite=True, encoding='utf-8') as writer:
    json.dump(records, writer)