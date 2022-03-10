from pymongo import MongoClient

'''
score collections에
    name:'한지민',kor:100,eng:30,math:50
    name: '송강',kor:50,eng:100,math:70
입력
'''

client = MongoClient('localhost',27017)
db = client.pre
score = db.score

# result01 = score.insert_many(
#     [
#         { 'name':'한지민','kor':100,'eng':30,'math':50},
#         {'name': '송강','kor':50,'eng':100,'math':70}
#     ]
# )
#
# print(result01)
# print(result01.inserted_ids)

# result02 = score.insert_one({'name':'신민아','kor':50,'eng':70,'math':100})
# print(result02)
# print(result02.inserted_id)
#
# result01 = score.update_one({'name':'유재석'},{'$set':{'midterm.kor':100}})
# print(result01.matched_count)
# print(result01.modified_count)
#
# result02 = score.update_many(
#     {'eng':{'$lt':80}},
#     {'$set':{'eng':0}}
# )
#
# print(result02.matched_count)   # 1  조건 하나찾고
# print(result02.modified_count)  # 1  조건 하나 수정

# result01 = score.delete_one({'name':'유재석'})
# print(result01)
# print(result01.deleted_count)
#
# result02 = score.delete_many({'test':{'$exists':False}})
# print(result02)
# print(result02.deleted_count)



aggr = score.aggregate(
    [
        {'$match':{'kor':{'$gt':50}}},
        {'$group':{'_id':'kor','sum':{'$sum':'$kor'}}}
    ]
)

print(aggr)
print(list(aggr))