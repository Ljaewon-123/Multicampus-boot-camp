# -*- coding:utf-8 -*-
# kafka
from platform import python_branch
from kafka import KafkaProducer, KafkaConsumer
from kafka.structs import TopicPartition
from pendulum import yesterday

#airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import requests, json, datetime, time, copy

from hdfs import InsecureClient


# ./bin/kafka-topics.sh --create  --bootstrap-server localhost:9092 --partitions 6 --replication-factor 1 --topic multiconsumer

# dag
dag = DAG(
    dag_id = 'test',
    schedule_interval=None,
    start_date = yesterday('Asia/Seoul'),
)

now = datetime.datetime.now()
date = datetime.datetime.today().strftime("%Y%m%d")
nowDate = now.strftime("%Y%m%d")
print(now.strftime('%Y%m%d'))


# declare functions 

def marine_weather(obs_lst,kind_weather):
    now = datetime.datetime.now()
    date = datetime.datetime.today().strftime("%Y%m%d")
    nowDate = now.strftime("%Y%m%d")
    print(now.strftime('%Y%m%d'))

    # declare obs_list
    pago_obs_lst = ['DT_0042', 'DT_0041', 'IE_0060', 'IE_0062', 'IE_0061', 'TW_0089', 'TW_0079', 'TW_0080', 'TW_0081', 'TW_0092', 'TW_0090', 'TW_0062', 'TW_0069', 'TW_0075', 'TW_0091', 'TW_0093', 'TW_0094', 'KG_0021', 'KG_0024', 'KG_0025', 'KG_0028', 'KG_0101']
    Ocean_buoy_wind_obs = ['TW_0089','TW_0091','KG_0025','TW_0069','KG_0024','TW_0094','TW_0079','TW_0081','TW_0093','TW_0090','TW_0080','KG_0101','TW_0092','KG_0021','KG_0028','TW_0075','TW_0062']
    condolence = ['DT_0063','DT_0032','DT_0031','DT_0029','DT_0058','DT_0026','DT_0049','DT_0018','DT_0017','DT_0065','DT_0057','DT_0062','DT_0023','DT_0007','DT_0006','DT_0025','DT_0005','DT_0056','DT_0061',
                'DT_0010','DT_0051','DT_0022','DT_0012','DT_0008','DT_0067','DT_0037','DT_0016','DT_0092','DT_0003','DT_0044','DT_0043','DT_0027','DT_0013','DT_0020','DT_0068','DT_0001','DT_0052','DT_0024',
                'DT_0004','DT_0028','DT_0021','DT_0050','DT_0014','DT_0002','DT_0091','DT_0066','DT_0011','DT_0035']
    Ocean_buoy = ['TW_0088', 'TW_0077', 'TW_0089', 'TW_0074', 'TW_0072', 'TW_0091', 'KG_0025', 'TW_0069', 'KG_0024',
                'TW_0085', 'TW_0094', 'TW_0087', 'TW_0086', 'TW_0079'
                ,'TW_0081', 'TW_0093', 'TW_0090', 'TW_0083', 'TW_0078', 'TW_0080', 'KG_0101', 'TW_0076', 'TW_0092', 'KG_0021',
                'KG_0028', 'TW_0075', 'TW_0082', 'TW_0084', 'TW_0070', 'TW_0062']

    url = 'http://www.khoa.go.kr/api/oceangrid/{0}/search.do?ServiceKey=CndQ9ayWwjk5aH/aT22Bzw==&ObsCode={1}&Date={2}&ResultType=json'
    lst_data = []
    for obs_id in obs_lst:
        pago_url = url.format(kind_weather, obs_id, now.strftime('%Y%m%d'))
        resp = requests.get(pago_url)

        json_data = resp.json()
        if list(json_data['result'].keys())[0] == 'error':
            continue
        else:
            tmp_ex = json_data['result']['data'][-1]
            tmp_ex['obs_code'] = obs_id
            lst_data.append(tmp_ex)

    tmp = lst_data

    pago_data = marine_weather(pago_obs_lst,'obsWaveHight') # 관측소에 맞는 기상정보 뽑음
    Ocean_buoy_wind_data = marine_weather(Ocean_buoy_wind_obs,'tidalBuWind')

    data1 = pago_data
    data2 = Ocean_buoy_wind_data

    # declare producer
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))


    producer.send('multiconsumer', key=b'pago', value=data1, partition=0)  # key = bytes string
    producer.send('multiconsumer', key=b'tidalBuWind', value=data2, partition=1)
    producer.flush()
    # return tmp


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
            data = temp_data["result"]["data"][cnt - 1]
            
            data_dict = {}
            data_dict['record_time']=data['record_time']
            data_dict['water_temp']=data['water_temp']
            data_dict['obs_code'] = obs_code
            data_list.append(data_dict)

    # declare producer
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'))


    # jo_temp_list=data_list
    producer.send('multiconsumer', key=b'jo_temp_data', value=data_list, partition=2)
    producer.flush()
    producer.close()
    # return result

def bu_temp():
    api_url = 'http://www.khoa.go.kr/api/oceangrid/tidalBuTemp/search.do'

    obs_codes = ['TW_0088', 'TW_0077', 'TW_0089', 'TW_0074', 'TW_0072', 'TW_0091', 'KG_0025', 'TW_0069', 'KG_0024',
                 'TW_0085', 'TW_0094', 'TW_0087', 'TW_0086', 'TW_0079'
        , 'TW_0081', 'TW_0093', 'TW_0090', 'TW_0083', 'TW_0078', 'TW_0080', 'KG_0101', 'TW_0076', 'TW_0092', 'KG_0021',
                 'KG_0028', 'TW_0075', 'TW_0082', 'TW_0084', 'TW_0070', 'TW_0062']

    service_key = 'RUGtj1GPESsGHsiqinO2BA=='
    result_type = 'json'

    data_list=[]
    bu_temp_list = list()
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
            data_dict['record_time']=data['record_time']
            data_dict['water_temp']=data['water_temp']
            data_dict['obs_code'] = obs_code
            data_list.append(data_dict)

    bu_temp_list=data_list
    # declare producer
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    producer.send("multiconsumer", key=b'bu_temp_data', value=bu_temp_list, partition=3)
    producer.flush()
    producer.close()
    # return result

def jo_actual_condel():
    obs_post_id_list = ['DT_0063', 'DT_0032', 'DT_0031', 'DT_0029', 'DT_0058', 'DT_0026', 'DT_0049', 'DT_0018', 'DT_0017',
                  'DT_0065', 'DT_0057', 'DT_0062', 'DT_0023', 'DT_0007', 'DT_0006', 'DT_0025', 'DT_0005', 'DT_0056',
                  'DT_0061',
                  'DT_0010', 'DT_0051', 'DT_0022', 'DT_0012', 'DT_0008', 'DT_0067', 'DT_0037', 'DT_0016', 'DT_0092',
                  'DT_0003', 'DT_0044', 'DT_0043', 'DT_0027', 'DT_0013', 'DT_0020', 'DT_0068', 'DT_0001', 'DT_0052',
                  'DT_0024',
                  'DT_0004', 'DT_0028', 'DT_0021', 'DT_0050', 'DT_0014', 'DT_0002', 'DT_0091', 'DT_0066', 'DT_0011',
                  'DT_0035']
                  
    temp_dict = dict()
    jo_actual_condel_list = list()
    Key = 'PcaRy7HmUIAEp7FrsZX3hg=='
    for obs_post_id in obs_post_id_list:
        url = f'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey={Key}&ObsCode={obs_post_id}&Date={nowDate}&ResultType=json'
        resp = requests.get(url).json()

        try:
            temp_dict["obs_post_id"] = obs_post_id
            temp_dict['record_time'] = resp["result"]["data"][-1]["record_time"]
            temp_dict["tide_level"] = resp["result"]["data"][-1]["tide_level"]
            k = copy.deepcopy(temp_dict)
            jo_actual_condel_list.append(k)

        except:
            continue
            # declare producer
        producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        producer.send('multiconsumer', key=b'jo_actual_condel_data', value=jo_actual_condel_list, partition=4)
        producer.flush()
        producer.close()
    # return condolence_list

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
    temp_dict = dict()
    jo_actual_wind_list = list()
    Key = 'PcaRy7HmUIAEp7FrsZX3hg=='
    for obs_post_id in obs_post_id_list:
        url = f'http://www.khoa.go.kr/api/oceangrid/tideObsWind/search.do?ServiceKey={Key}&ObsCode={obs_post_id}&Date={nowDate}&ResultType=json'
        resp = requests.get(url).json()

        try:
            temp_dict['obs_post_id']=obs_post_id
            temp_dict['record_time'] = resp["result"]["data"][-1]["record_time"]
            temp_dict['wind_dir'] = resp["result"]["data"][-1]["wind_dir"]
            temp_dict['wind_speed'] = resp["result"]["data"][-1]["wind_speed"]
            k = copy.deepcopy(temp_dict)
            jo_actual_wind_list.append(k)

        except:
            continue
        
        # declare producer
    producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    producer.send('multiconsumer', key=b'jo_actual_wind_data', value=jo_actual_wind_list, partition=5)
    producer.flush()
    producer.close()
    # return wind_list


def assign():
    # declare consumer
    consumer1 = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,
    )

    consumer2 = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,
    )
    consumer3 = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,
    )
    consumer4 = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,
    )
    consumer5 = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',  # latest 가장 마지막 offset부터 // earliest 가장 처음 offset부터
        enable_auto_commit=True,
        group_id='ocean_weather',  # --group ocean_weather 와 같다
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,
    )
    consumer6 = KafkaConsumer(
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

    client = InsecureClient('http://localhost:9870', user='sim')

    con_lst = []

    con_lst.extend([consumer1,consumer2,consumer3,consumer4,consumer5,consumer6])

    for multi_consumer in con_lst:
        print('one partition')
        for message in multi_consumer:
            records = message.value  # only last value if you all data lst.append(message.value)
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



# marine_weather_task = PythonOperator(
#     task_id = 'marine_weather_task',
#     python_callable = marine_weather,
#     dag=dag
# )

jo_temp_task = PythonOperator(
    task_id = 'jo_temp_task',
    python_callable = jo_temp,
    dag=dag
)

bu_temp_task = PythonOperator(
    task_id = 'bu_temp_task',
    python_callable = bu_temp,
    dag=dag
)

jo_actual_condel_task = PythonOperator(
    task_id = 'jo_actual_condel_task',
    python_callable = jo_actual_condel,
    dag=dag
)

jo_actual_wind_task = PythonOperator(
    task_id = 'jo_actual_wind_task',
    python_callable = jo_actual_wind,
    dag=dag
)

assign_task = PythonOperator(
    task_id = 'assign_task',
    python_callable = assign,
    dag=dag
)
#marine_weather_task >>  jo_temp_task >> bu_temp_task >>  jo_actual_condel_task >>  jo_actual_wind_task
[jo_temp_task, bu_temp_task, jo_actual_condel_task, jo_actual_wind_task] >> assign_task
