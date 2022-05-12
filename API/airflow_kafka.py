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
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from pendulum import yesterday,tomorrow
from pyspark.sql import SparkSession
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from bs4 import BeautifulSoup
import time, copy

dag = DAG(
    dag_id = 'kafka',
    schedule_interval=None,
    start_date = yesterday('Asia/Seoul'),
)

def marine_weather(obs_lst,kind_weather):
    url = 'http://www.khoa.go.kr/api/oceangrid/{0}/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode={1}&Date={2}&ResultType=json'
    # tmp = {now.strftime("%Y%m%d"): {}}
    # print(tmp)
    lst_data = []
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
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
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
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
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
    data_list=[]

    for obs_code in obs_codes:
        url = api_url + f'?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType={result_type}'
        temp_resp = requests.get(url)
        temp_data = temp_resp.json()

        if list(temp_data['result'].keys())[0] == 'error': # 해당함수 에러 키 처리 안되있어서 추가
            continue
        else:
            cnt = len(temp_data["result"]["data"])
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
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
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
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
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



def producer_data():
    pago_obs_lst = ['DT_0042', 'DT_0041', 'IE_0060', 'IE_0062', 'IE_0061', 'TW_0089', 'TW_0079', 'TW_0080', 'TW_0081',
                    'TW_0092', 'TW_0090', 'TW_0062', 'TW_0069', 'TW_0075', 'TW_0091', 'TW_0093', 'TW_0094', 'KG_0021',
                    'KG_0024', 'KG_0025', 'KG_0028', 'KG_0101']
    Ocean_buoy_wind_obs = ['TW_0089', 'TW_0091', 'KG_0025', 'TW_0069', 'KG_0024', 'TW_0094', 'TW_0079', 'TW_0081',
                           'TW_0093', 'TW_0090', 'TW_0080', 'KG_0101', 'TW_0092', 'KG_0021', 'KG_0028', 'TW_0075',
                           'TW_0062']
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
    print(now.strftime('%Y%m%d'))

    pago_data = marine_weather(pago_obs_lst,'obsWaveHight') # 관측소에 맞는 기상정보 뽑음
    Ocean_buoy_wind_data = marine_weather(Ocean_buoy_wind_obs,'tidalBuWind')
    jo_temp_data = jo_temp()
    bu_temp_data = bu_temp()
    jo_actual_condel_data = jo_actual_condel()
    jo_actual_wind_data = jo_actual_wind()

    # declare producer
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))


    producer.send('multiconsumer', key=b'pago', value=pago_data, partition=0)  # key = bytes string
    producer.send('multiconsumer', key=b'tidalBuWind', value=Ocean_buoy_wind_data, partition=1)
    producer.send('multiconsumer', key=b'jo_temp_data', value=jo_temp_data, partition=2)
    producer.send('multiconsumer', key=b'bu_temp_data', value=bu_temp_data, partition=3)
    producer.send('multiconsumer', key=b'jo_actual_condel_data', value=jo_actual_condel_data, partition=4)
    producer.send('multiconsumer', key=b'jo_actual_wind_data', value=jo_actual_wind_data, partition=5)
    # producer.send('pago_kafka',{'pago':data})
    producer.flush()


# auto_offset_reset='latest' 이기때문에 처음돌때는 커밋이 안되서 안나옴 offset:1 부터 출력가능
def consumer_data():

    consumer1 = KafkaConsumer(
    #    'multiconsumer',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,

    )

    consumer2 = KafkaConsumer(
    #    'multiconsumer',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,

    )
    consumer3 = KafkaConsumer(
    #    'multiconsumer',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,

    )
    consumer4 = KafkaConsumer(
    #    'multiconsumer',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,

    )
    consumer5 = KafkaConsumer(
    #    'multiconsumer',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,

    )
    consumer6 = KafkaConsumer(
    #    'multiconsumer',
        bootstrap_servers=['localhost:9092'],
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

    client = InsecureClient('http://localhost:9870', user='jaewon')

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

def insert_mysql():
    spark = SparkSession.builder.master("yarn").appName("air_kafka").getOrCreate()  # ubuntu안에 있는 파일이름이 air_kafka임

    user = "root"
    password = "1234"
    url = "jdbc:mysql://localhost:3306/fish"  # ip포트번호 aws에 맞게 조정/데이터 베이스 이름
    driver = "com.mysql.cj.jdbc.Driver"

    pago_file = spark.read.format('json').load('/user/jaewon/data/pago.jsonl')

    tidalBuWind_file = spark.read.format('json').load('/user/jaewon/data/tidalBuWind.jsonl')

    jo_temp_data_file = spark.read.format('json').load('/user/jaewon/data/jo_temp_data.jsonl')

    bu_temp_data_file = spark.read.format('json').load('/user/jaewon/data/bu_temp_data.jsonl')

    jo_actual_condel_data_file = spark.read.format('json').load('/user/jaewon/data/jo_actual_condel_data.jsonl')

    jo_actual_wind_data_file = spark.read.format('json').load('/user/jaewon/data/jo_actual_wind_data.jsonl')

    obs_list_file = spark.read.format('csv').option('header', 'true').load('/user/jaewon/data/full_obs.csv')

    pago_file.write.option('truncate', True).jdbc(url, 'pago', 'overwrite',
                                                  properties={'driver': driver, 'user': user, 'password': password})
    tidalBuWind_file.write.option('truncate', True).jdbc(url, 'tidalBuWind', 'overwrite',
                                                         properties={'driver': driver, 'user': user,
                                                                     'password': password})
    jo_temp_data_file.write.option('truncate', True).jdbc(url, 'jo_temp_data', 'overwrite',
                                                          properties={'driver': driver, 'user': user,
                                                                      'password': password})
    bu_temp_data_file.write.option('truncate', True).jdbc(url, 'bu_temp_data', 'overwrite',
                                                          properties={'driver': driver, 'user': user,
                                                                      'password': password})
    jo_actual_condel_data_file.write.option('truncate', True).jdbc(url, 'jo_actual_condel_data', 'overwrite',
                                                                   properties={'driver': driver, 'user': user,
                                                                               'password': password})
    jo_actual_wind_data_file.write.option('truncate', True).jdbc(url, 'jo_actual_wind_data', 'overwrite',
                                                                 properties={'driver': driver, 'user': user,
                                                                             'password': password})
    obs_list_file.write.option('truncate', True).jdbc(url, 'obs_list', 'overwrite',
                                                      properties={'driver': driver, 'user': user, 'password': password})


def crawling():
    # 서해북부
    dict1 = {'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[2]/button': [
        '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[1]',
        '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[2]'],
        # 서해중부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[3]/button': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[4]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[6]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[7]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[1]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[3]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[2]'],
             # 서해남부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[4]/button': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[6]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[7]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[8]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[9]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[10]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[2]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[1]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[3]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[4]'],
             # 남해서부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[4]/div/button[1]': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[4]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[1]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[2]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[3]'],
             # 제주도
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[4]/div/button[2]': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[8]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[7]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[6]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[2]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[4]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[3]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[1]'],
             # 남해동부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[5]/button[1]': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[6]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[7]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[4]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[1]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[3]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[2]'],
             # 동해남부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[5]/button[2]': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[6]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[7]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[8]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[4]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[3]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[2]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[1]'],
             # 동해중부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[6]/button': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[4]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[5]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[6]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[1]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[2]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[3]'],
             # 동해북부
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[1]/div/div[7]/button': [
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[2]',
                 '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[1]']}

    dict2 = {'/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[1]': '서해북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[2]/div/button[2]': '서해북부 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[4]': '인천,경기 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[5]': '인천,경기 남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[6]': '충남 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[7]': '충남 남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[1]': '서해중부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[3]': '서해중부 안쪽 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[3]/div/button[2]': '서해중부 바깥 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[6]': '전북 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[7]': '전북 남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[8]': '전남 북부 서해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[9]': '전남 중부 서해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[10]': '전남 남부 서해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[2]': '서해남부 북쪽안쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[1]': '서해남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[3]': '서해남부 남쪽안쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[5]': '서해남부 남쪽바깥먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[4]/div/button[4]': '서해남부 북쪽바깥먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[4]': '전남 서부 남해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[5]': '전남 동부 남해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[1]': '남해 서부 서쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[2]': '남해서부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[5]/div/button[3]': '남해서부 동쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[5]': '제주도 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[8]': '제주도 동부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[7]': '제주도 남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[6]': '제주도 서부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[2]': '제주도 남서쪽안쪽 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[4]': '제주도 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[3]': '제주도 남동쪽안쪽 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[6]/div/button[1]': '제주도 남쪽바깥면바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[6]': '경남 서부 남해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[7]': '거제시 동부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[5]': '경남 중부 남해 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[4]': '부산 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[1]': '남해 동부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[3]': '남해동부 안쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[7]/div/button[2]': '남해동부 바깥먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[6]': '경남 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[7]': '경남 남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[8]': '울산 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[4]': '동해남부 북쪽바깥먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[5]': '동해남부 북쪽안쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[3]': '동해남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[2]': '동해남부 남쪽안쪽먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[8]/div/button[1]': '동해남부 남쪽바깥먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[4]': '강원 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[5]': '강원 중부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[6]': '강원 남부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[1]': '동해 중부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[2]': '동해 중부 안쪽 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[9]/div/button[3]': '동해 중부 바깥 먼바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[2]': '동해 북부 앞바다',
             '/html/body/div[2]/section/div/div[2]/div[4]/div/div[2]/div[10]/div/button[1]': '동해 북부 먼바다'}
    # def donghaebuk():
    #     url = ""

    final_dict = {}

    # db = pymysql.connect(host='127.0.0.1',
    #     port=3306,
    #     user="root",
    #     passwd="tlawjdgns1",
    #     db='test')
    # kkk = {'동해 북부 먼바다': {'5월08일': [['오전', '1m', '2m', '구름많음'], ['오후', '1m', '2m', '맑음']], '5월09일': [['오전', '1m', '2m', '맑음'], ['오후', '1m', '2m', '맑음']], '5월10일': [['오전', '1m', '2m', '맑음'], ['오후', '1m', '2m', '구름많음']], '5월11일': [['오전', '1m', '2m', '구름많음'], ['오후', '1m', '2m', '구름많음']]}}
    # print(kkk[ehdgo])

    for key in dict1.keys():
        for value in dict1[key]:
            url = "https://www.weather.go.kr/w/ocean/forecast/daily-forecast.do"

            # driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
            service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
            driver = webdriver.Edge(service=service)
            driver.implicitly_wait(3)
            driver.get(url)
            time.sleep(1)
            # print(f'key:  {key}')
            dongbukbu = driver.find_element(By.XPATH, key)
            dongbukbu.send_keys(Keys.ENTER)
            driver.implicitly_wait(1)
            time.sleep(1)

            dongbukbu_ap = driver.find_element(By.XPATH, value)
            dongbukbu_ap.send_keys(Keys.ENTER)
            driver.implicitly_wait(1)
            time.sleep(1)

            fst_table = driver.find_element(By.XPATH, '//*[@id="sea-today-short-term"]/div[2]/table/tbody')
            table_contents = list()
            cnt = len(fst_table.get_attribute("innerText").split('\n'))
            table_contents.append(fst_table.get_attribute("innerText").split('\n'))
            print(cnt)
            if cnt == 5:
                table_contents = table_contents[0]
                cnt = int((cnt - 1) / 2)
                result_dict = dict()
                day = table_contents[0].split('\t')[0].split(' ')[0].split('(')[0]

                result_dict[day] = list()
                weather = table_contents[0].split('\t')[0].split(' ')[-1]
                result_dict[day] = table_contents[0].split('\t')[1:]
                result_dict[day].append(weather)

                for k in range(1, cnt + 1):
                    weather = table_contents[2 * k - 1].split('\t')[0].split(' ')[1:]
                    day = table_contents[2 * k - 1].split('\t')[0].split(' ')[0].split('(')[0]
                    result_dict[day] = list()
                    result_dict[day].append(table_contents[2 * k - 1].split('\t')[1:])
                    result_dict[day].append(table_contents[2 * k - 1].split('\t')[1:])
                    result_dict[day][0].append(weather[0])
                    result_dict[day][1].append(weather[-1])

                test_dict = dict()
                test_dict[dict2[value]] = result_dict

                se_table = driver.find_element(By.XPATH, '//*[@id="sea-today-mid-term"]/div[2]/div/ul[2]')
                se_table = se_table.get_attribute("innerText").split('\n')[1:-12]

                cnt = len(se_table)
                result2_dict = dict()
                for i in range(1, int(cnt / 6)):
                    day = str(se_table[6 * i].split('(')[0].split(". ")[0][1:]) + '월' + str(
                        se_table[6 * i].split('(')[0].split(". ")[1]) + '일'

                    result2_dict[day] = list()
                    temp_list = list()

                    result2_dict[day].append(
                        [se_table[6 * i + 1], se_table[6 * i + 5].split(' ')[3], se_table[6 * i + 5].split(' ')[7],
                         se_table[6 * i + 2]])
                    result2_dict[day].append(
                        [se_table[6 * i + 3], se_table[6 * i + 5].split(' ')[11], se_table[6 * i + 5].split(' ')[-1],
                         se_table[6 * i + 4]])

                test_dict = dict()
                kk = copy.deepcopy(result_dict)

                place = dict2[value]
                test_dict = dict()
                test2_dict = dict()
                test_dict['날씨전망'] = result_dict
                test2_dict['주간날씨'] = result2_dict

                # print(test_dict)
                # print(test2_dict)

                final_lst = [test_dict, test2_dict]
                final_dict[place] = final_lst

                driver.close()

            else:
                # /html/body/div[2]/section/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[6]/td[1]/span
                # /html/body/div[2]/section/div/div[2]/div[4]/div/div[3]/div[2]/table/tbody/tr[6]/td[1]/span
                table_contents = table_contents[0]
                # print(table_contents)
                cnt = int((len(table_contents)) / 2)
                result_dict = {}
                lst = []
                pm = ''
                # ['6일(금)', '비\t오후\t서-북서\t3~7\t0.5~1', '', '7일(토)', '비  맑음\t오전\t북서-북\t4~8\t0.5~1', '오후\t북서-북\t4~8\t0.5~1', '', '8일(일)', '구름많음  구름많음\t오전\t북-북동\t3~7\t0.5~0.5', '오후\t북서-북\t2~5\t0.5~0.5', '', '9일(월)', '맑음  구름많음\t오전\t북동-동\t3~6\t0.5~0.5', '오후\t남서-서\t3~6\t0.5~0.5']
                # {'4일': [['오전', '남-남서', '7~12', '1~2.5', '맑음'], ['오후', '남-남서', '8~12', '1~2.5', '맑음']], '5일': [['오전', '남-남서', '7~11', '1~2.5', '맑음'], ['오후', '남동-남', '6~10', '1~2', '맑음']], '6일': [['오전', '남-남서', '5~9', '1~2', '비'], ['오후', '북서-북', '4~8', '0.5~1.5', '비']]}}
                for weather in table_contents:
                    if weather in '':
                        continue
                    # print(weather)
                    if weather[0].isdigit():
                        weather_key = weather
                        # print(weather_key)
                    else:
                        info = weather.split('\t')
                        if info[1] == '오전':
                            info_div = info[1:]
                            am = info[0].split()[0]
                            pm = info[0].split()[1]
                            info_div.append(am)
                            lst.append(info_div)
                        elif info[1] == '오후' or info[0] == '오후':
                            if pm == '':
                                result_dict[weather_key] = info
                            else:
                                info_div = info
                                info_div.append(pm)
                                lst.append(info_div)
                                # print('----------------------------------------------------------')
                                result_dict[weather_key] = lst
                                lst = []
                # print(result_dict)
                # for k in range(0, cnt):
                #     dhwjs = table_contents[2*k].split('\t')[1:]
                #     print(dhwjs,'dhwjs')
                #     # print(table_contents[2*k].split('\t')[0].split(' '))
                #     dhwjs.append(table_contents[2*k].split('\t')[0].split(' ')[0])  # 마지막 1을 0으로 바꿈
                #     # ['오전', '남-남서', '7~12', '1~2.5', '맑음']
                #     dhgn = table_contents[2*k+1].split('\t')
                #     print(dhgn,'dhgn')
                #     dhgn.append(table_contents[2*k].split('\t')[0].split(' ')[-1])
                #     # ['오후', '남-남서', '8~12', '1~2.5', '맑음']
                #     day = table_contents[2*k].split('\t')[0].split(' ')[0].split('(')[0]
                #     # '4일'
                #     result_dict[day] = list()
                #     result_dict[day].append(dhwjs)
                #     result_dict[day].append(dhgn)

                # print(result_dict,'asdfaewfasdf')

                se_table = driver.find_element(By.XPATH, '//*[@id="sea-today-mid-term"]/div[2]/div/ul[2]')
                se_table = se_table.get_attribute("innerText").split('\n')[1:-12]

                cnt = len(se_table)
                result2_dict = dict()
                for i in range(1, int(cnt / 6)):
                    # '5월08일'
                    day = str(se_table[6 * i].split('(')[0].split(". ")[0][1:]) + '월' + str(
                        se_table[6 * i].split('(')[0].split(". ")[1]) + '일'
                    result2_dict[day] = list()
                    temp_list = list()

                    result2_dict[day].append(
                        [se_table[6 * i + 1], se_table[6 * i + 5].split(' ')[3], se_table[6 * i + 5].split(' ')[7],
                         se_table[6 * i + 2]])
                    result2_dict[day].append(
                        [se_table[6 * i + 3], se_table[6 * i + 5].split(' ')[11], se_table[6 * i + 5].split(' ')[-1],
                         se_table[6 * i + 4]])

                place = dict2[value]
                test_dict = dict()
                test2_dict = dict()
                test_dict['날씨전망'] = result_dict
                test2_dict['주간날씨'] = result2_dict

                # print(test_dict)
                # print(test2_dict)
                final_lst = [test_dict, test2_dict]
                final_dict[place] = final_lst
                # print(final_dict)
                # {'서해북부 먼바다': {'4일': [['오전', '남-남서', '7~12', '1~2.5', '맑음'], ['오후', '남-남서', '8~12', '1~2.5', '맑음']], '5일': [['오전', '남-남서', '7~11', '1~2.5', '맑음'], ['오후', '남동-남', '6~10', '1~2', '맑음']], '6일': [['오전', '남-남서', '5~9', '1~2', '비'], ['오후', '북서-북', '4~8', '0.5~1.5', '비']]}}
                # {'서해북부 먼바다': {'5월08일': [['오전', '0.5m', '1.5m', '구름많음'], ['오후', '0.5m', '1.5m', '맑음']], '5월09일': [['오전', '0.5m', '1.5m', '맑음'], ['오후', '0.5m', '1.5m', '맑음']], '5월10일': [['오전', '1m', '2m', '구름많음'], ['오후', '1m', '2m', '구름많음']], '5월11일': [['오전', '1m', '2m', '흐림'], ['오후', '1m', '2m', '흐림']]}}

                driver.close()

    res_json = json.dumps(final_dict, ensure_ascii=False)

    with open(f'weather.json', 'w', encoding='utf-8') as f:
        f.write(res_json)


# marine_weather_task = PythonOperator(
#     task_id = 'marine_weather_task',
#     python_callable = marine_weather,
#     dag=dag
# )

producer_data_task = PythonOperator(
    task_id = 'producer_data_task',
    python_callable = producer_data,
    dag=dag
)


consumer_data_tsak = PythonOperator(
    task_id = 'consumer_data_task',
    python_callable = consumer_data,
    dag=dag
)

insert_mysql_task = PythonOperator(
    task_id = 'insert_mysql_task',
    python_callable = insert_mysql,
    dag=dag
)

crawling_task = PythonOperator(
    task_id = 'crawling_task',
    python_callable = crawling,
    dag=dag

)

#marine_weather_task >>  jo_temp_task >> bu_temp_task >>  jo_actual_condel_task >>  jo_actual_wind_task
#[jo_temp_task, bu_temp_task, jo_actual_condel_task, jo_actual_wind_task] >> assign_task
producer_data_task >> consumer_data_tsak >> insert_mysql_task >> crawling_task
