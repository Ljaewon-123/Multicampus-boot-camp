from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost',27017)
db = client.pre
score  = db.score

cursor = score.find()
for doc in cursor:
    # print(doc)
    pprint(doc)

lee = score.find({'name':'이순신'})
pprint(lee)   # 하나만 나와도 커서객체로 나옴
for doc in lee:
    pprint(doc)

print('score clooection 안에 있는 doc 총 개수: ',score.count_documents({}))

# 국어점수가 60점 보다 큰 도큐먼트 전체 출력
#
# gt = score.find({'kor':{'$gt':60}},{'_id':0})
# for i in gt:
#     print(i)