from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['test']
score = db['score']

# 이름이 유재석인 doc 찾아서 midterm의 kor 점수를 100점으로 변경하자
# doc 하나만 변경

result01 = score.update_one({'name':'유재석'},{'$set':{'kor':100}})
print(result01.matched_count)   # 1  조건 하나찾고
print(result01.modified_count)  # 1  조건 하나 수정

result02 = score.update_many(
    {'eng':{'$lt':80}},
    {'$set':{'eng':0}}
)
print(result02.matched_count)   # 1  조건 하나찾고
print(result02.modified_count)  # 1  조건 하나 수정

# score.update_many(
#    {'name':"홍길동",'kor':90,'eng':80,'math':98,'test':"midterm"},
#    {'name':"이순신",'kor':100,'eng':100,'math':76,'test':"final"},
#    {'name':"김선달",'kor':80,'eng':55,'math':67,'test' :"midterm"},
#    {'name':"강호동",'kor':70,'eng':69,'math':89,'test':"midterm"},
#    {'name':"유재석",'kor':60,'eng':80,'math':78,'test':"final"},
#    {'name':"신동엽",'kor':100,'eng':69,'math':89,'test':"midterm"},
#    {'name':"조세호",'kor':75,'eng':100,'math':100,'test':"final"}
# )