from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.test
score = db.score

result01 = score.delete_one({'name':'유재석'})
print(result01)
print(result01.deleted_count)


# test field 가 없는 doc들 모두 삭제
result02 = score.delete_many({'test':{'$exists':False}})
print(result02)
print(result02.deleted_count)