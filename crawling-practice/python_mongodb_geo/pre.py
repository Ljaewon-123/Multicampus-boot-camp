# -*- coding:utf-8 -*-

import json
from pymongo import MongoClient

with open('starbucks_all.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# print(json_data)


result_dict = json_data['list']
# print(result_dict)
client = MongoClient('localhost',27017)
db = client.pre


### res = starbucks01.insert_many(result_dict)  # insert_many([])

# all = starbucks01.find({})
# for data in all:
#     print(data)

geo_list = list()
for data in result_dict:
    geo_dict = dict()
    geo_dict['s_name'] = data['s_name']
    coordinates = [float(data['lot']), float(data['lat'])]

    geo_dict['location'] = {'type': 'Point', 'coordinates': coordinates}

    geo_list.append(geo_dict)

starbucks02 = db.starbucks02
# res = starbucks02.insert_many(geo_list)
# print(len(res.inserted_ids))