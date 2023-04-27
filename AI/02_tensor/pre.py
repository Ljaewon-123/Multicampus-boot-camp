from pymongo import MongoClient
from pymongo.cursor import CursorType
# 잠깐 mongo db 연습함
host = 'localhost'
port = '27017'
client = MongoClient(host,int(port))
# print(mongo)
print(client.list_database_names())

db = client['mongodb_tu']
col = db['book']

print(db.list_collection_names())

print(col.find())

for i in col.find():
    print(i)