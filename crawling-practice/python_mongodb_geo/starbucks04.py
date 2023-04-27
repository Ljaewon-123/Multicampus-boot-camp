# -*- coding:utf-8 -*-
import json
from pymongo import MongoClient

with open('starbucks_all.json', 'r', encoding='utf-8') as f:
    json_data = f.readline()

# print(json_data)
result_dict = json.loads(json_data)


geo_list = list()
for data in result_dict['list']:
    geo_dict = dict()
    geo_dict['s_name'] = data['s_name']
    coordinates = [float(data['lot']),float(data['lat'])]

    geo_dict['location'] = {'type':'Point','coordinates':coordinates}

    geo_list.append(geo_dict)

# print(geo_list)
client = MongoClient('localhost', 27017)
db = client.test
starbucks02 = db.starbucks02

# res = starbucks02.insert_many(geo_list)
# print(len(res.inserted_ids))