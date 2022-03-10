# pip install pymongo
from pymongo import MongoClient

# client = MongoClient('localhost',27017)
client = MongoClient('mongodb://localhost:27017/')  # mongo 라고 쳤을때랑 똑같음

# db = client.test
db = client['test']

collection = db.score
# collection = db['score']

result = collection.find()
# print(result)
for res in result:
    print(res)