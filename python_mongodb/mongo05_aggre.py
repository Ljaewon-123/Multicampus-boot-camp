from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.test
score = db.score

aggr = score.aggregate(
    [
        {'$match':{'kor':{'$gt':50}}},
        {'$group':{'_id':'kor','sum':{'$sum':'$kor'}}}
    ]
)
print(aggr)
print(list(aggr))