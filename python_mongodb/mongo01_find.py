from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost',27017)

db = client.test

# cursor = db.score.find()
# print(cursor)

score = db.score

cursor = score.find()
for doc in cursor:
    # print(doc)
    pprint(doc)   # pretty print


lee = score.find({'name':'이순신'})
pprint(lee)   # 하나만 나와도 커서객체로 나옴
for doc in lee:
    pprint(doc)

lee2 = score.find_one({'name':'이순신'})
print(lee2)

print('score collection 안에 있는 doc 총 개수 : ',score.count_documents({}))

# 국어점수가 60점 보다 큰 도큐먼트 전체 출력

# kor = score.find({'kor':{'$gt':80}},{'_id':False})
# print(kor)
# for doc in kor:
#     print(doc)
