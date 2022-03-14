# MongoDB

pip install pymongo

- NOSQL (Not Only Sql)

  >기존의 관계형 DBMS가 갖고있는 특성 뿐만 아니라 다른 특성들을 부가적으로 지원한다는 것
  >
  >**스키마 없이 동작**하며, 구조에 대한 정의를 변경할 필요 없이 데이터베이스 레코드에 자유롭게 필드를 추가할 수 있다.

몽고db 스키마 고정X



mongodb 기본 function 테스트
 function test(){
... print('test')
... }



function test2(n){
... return n + 10;
... }



## CRUD

시작 use db

```javascript
db.jstest.insertOne({name:'test',age:100,class:"de"})
db.jstest.insertOne({name:,'mongo',class:'db'})
db.jstest.find()
```

위의경우 jstest라는 collection을 스스로만듬



데이터베이스라는 개념안에 collection 이라는 개념아래 document가있음
rdb로 따지면 table임

document = bson(bins json)형태로 저장 
필드 중복불가  json 으로 따지면 키 == 필드 



_id == pk ,기본키

```javascript
db.multi.insert({name:'hong-gd',class:'de',midterm:{kor:100,eng:60,math:80}})


var lee = {name:'lee-ss',midterm:{kor:70,eng:100},final:{kor:100,math:20,sci:50},class:'de'}
db.multi.insertOne(lee)
{
   "acknowledged" : true,
   "insertedId" : ObjectId("622947082cbe6f260e471a01")
}

하나 더 insert해보자

 db.multi.insertMany([{name:'kim-sd',class:'ds',kor:100,eng:40,math:400},{name:'kang-hd', class:'ds', kor:88, eng:50, math:70}])
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("622947cb2cbe6f260e471a02"),
                ObjectId("622947cb2cbe6f260e471a03")
        ]
}


```



var cursor = db.multi.find()  //가져온값 저장 

cursor
{ "_id" : ObjectId("622946a52cbe6f260e471a00"), "name" : "hong-gd", "class" : "de", "midterm" : { "kor" : 100, "eng" : 60, "math" : 80 } }
{ "_id" : ObjectId("622947082cbe6f260e471a01"), "name" : "lee-ss", "midterm" : { "kor" : 70, "eng" : 100 }, "final" : { "kor" : 100, "math" : 20, "sci" : 50 }, "class" : "de" }
{ "_id" : ObjectId("622947cb2cbe6f260e471a02"), "name" : "kim-sd", "class" : "de", "kor" : 100, "eng" : 40, "math" : 400 }
{ "_id" : ObjectId("622947cb2cbe6f260e471a03"), "name" : "hong-gd", "class" : "de" }

cursor == 1회용 변수 한번사용시 없어짐



쿼리문확인
https://docs.mongodb.com/manual/tutorial/query-documents/
공식문서 확인필

projection 출력 , 출력할게 있으면 나옴 없으면 그냥 없이나옴

find()의 두번째 매개변수이며 0,1,F,T로 걸러주는 역할을함 



 db.multi.find()  // multi 라는 컬렉션의 모든 도큐먼트 확인
{ "_id" : ObjectId("622946a52cbe6f260e471a00"), "name" : "hong-gd", "class" : "de", "midterm" : { "kor" : 100, "eng" : 60, "math" : 80 } }
{ "_id" : ObjectId("622947082cbe6f260e471a01"), "name" : "lee-ss", "midterm" : { "kor" : 70, "eng" : 100 }, "final" : { "kor" : 100, "math" : 20, "sci" : 50 }, "class" : "de" }
{ "_id" : ObjectId("622947cb2cbe6f260e471a02"), "name" : "kim-sd", "class" : "de", "kor" : 100, "eng" : 40, "math" : 400 }
{ "_id" : ObjectId("622947cb2cbe6f260e471a03"), "name" : "hong-gd", "class" : "de" }



 db.multi.find({}) // 위랑 같음

,find의 두번째{} 가 프로젝션

db.multi.find({},{name:1})
{ "_id" : ObjectId("622946a52cbe6f260e471a00"), "name" : "hong-gd" }
{ "_id" : ObjectId("622947082cbe6f260e471a01"), "name" : "lee-ss" }
{ "_id" : ObjectId("622947cb2cbe6f260e471a02"), "name" : "kim-sd" }
{ "_id" : ObjectId("622947cb2cbe6f260e471a03"), "name" : "hong-gd" }



db.multi.find({},{_id:0,name:1})
{ "name" : "hong-gd" }
{ "name" : "lee-ss" }
{ "name" : "kim-sd" }
{ "name" : "hong-gd" }



db.multi.find({},{_id:0,name:true,midterm:1})   // 1이랑 true같음 1은 전부,0은 X
{ "name" : "hong-gd", "midterm" : { "kor" : 100, "eng" : 60, "math" : 80 } }
{ "name" : "lee-ss", "midterm" : { "kor" : 70, "eng" : 100 } }
{ "name" : "kim-sd" }
{ "name" : "hong-gd" }



db.multi.find({class:'de'})  // class 가 'de'인 얘들만



쿼리 오퍼레이터

$regex : "s" --> s가 포함되어있는것을 찾기

$regex : "s$" --> 끝자리가 s인것을 찾기

$regex : "^s" --> 첫자리가 s인것을 찾기





db.multi.find({'midterm.kor':{$gt:50}})  // midterm에 kor이 50보다 큰

// {<field>:{<orp>:<value>}}

연산자 확인 [Query and Projection Operators — MongoDB Manual](https://docs.mongodb.com/manual/reference/operator/query/)

// 국어점수가 존재하는  도큐먼트 출력 

db.mulit.find({kor:{$exists:true}})

//midterm에 국어점수 존재

midterm.kor 과 kor의 차이

midterm.kor 은 딕셔너리에 들어가있는 kor이고 그냥 kor은 바로 1단계에 있는얘들

 db.multi.find({'midterm.kor':{$exists:true}})

//국어점수가 50점보다 크고 , 100점이하인

db.multi.find({kor:{$gt:50},kor:{$lte:100}})

db.multi.find({$and:[{kor:{$gt:50}},{kor:{$lte:100}}])

// 국어점수가 50점보다 크거나 같고, 100점보다 작은

db.multi.find({kor:{$gte:50},kor:{$lt:100}})

db.multi.find({kor:{$gte:50,$lt:100}})  // 조건이 and로 묶이는샘 



 // 1과 $exists 차이? -> 애초에 프로젝션에서 1,0하는거 $exists는 조건쪽

// 0 과 false, 1과 true는 차이가 없다 같은 구문 



// 정렬 (1:asc,-1:desc)

db.multi.find().sort({name:1})   // name기준

db.multi.find().sort({name:-1})



// 제한  `skip(1)`,`limit(1)`,`sort()`

db.multi.find().sort({kor:1}).limit(1)   // 몇개출력? 으로 제한  , 정렬기준 제일 위에 하나

db.multi.find().sort({kor:-1}).limit(1)



db.multi.find().skip(1)   // 맨처음 하나 스킵



//업데이트 `$set`

// 하나 업데이트 updateOne

db.multi.updateOne({name:/hong/},{$set:{name:'홍길동'}}) //name hong찾아서 홍길동으로 바꿈

{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

matchedCount:1 // 하나 찾았고,"modifiedCount" : 1//바꿔줌



//중간고사(midterm) 점수가 있는 모든 학생들의 class 를 'graduated'로 바꾸자

db.multi.updateMany({midterm:{$exists:true}},{$set:{class:'graduated'}})
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }

확인 db.multi.find({},{_id:0})

// replace

db.multi.replaceOne({final:{$exists:true}},{class:'job'})   // -> 문서 자체가 바뀌어버림,_id는 유지 



// 국어점수가 60점보다 적거나 같은 도큐먼트들을 찾아서 

// 국어 점수를 0점으로 만드는 자바스크립트 함수 

// 함수이름은 updateKor()

// 업데이트 결과 리턴

```javascript
 function updateKor(){
... var tmp = db.multi.updateMany({kor:{$lte:60}},{$set:{kor:0}})
... return tmp
... }

updateKor()
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
```





Update Operators : [Update Operators — MongoDB Manual](https://docs.mongodb.com/manual/reference/operator/update/)

// 이름이 '홍길동' 인 도큐먼트 하나만 삭제

db.multi.deleteOne({name:'홍길동'})

// class field가 존재하는 도큐먼트들을 모두 삭제하자 

db.multi.deleteMany({class:{$exists:true}})

`$exists`



db.myfriends.insertOne({name:'아이언맨',buddy:['토르','헐크','호크아이']})

db.myfriends.insertOne({name:'슈퍼맨',buddy:['배트맨','원더우먼','아쿠아맨','조커']})



배열 추가 ,제거

// updateOne을 사용하여,아이언맨의 친구(buddy)에 캠틴아메리카,블랙위도우 추가

db.myfriends.updateOne({name:'아이언맨'},{$push:{buddy:{$each:['캡틴아메리카','블랙위도우']}}})

// updateOne을 사용하여, 슈퍼맨의 친구중 가장 뒤에 있는 (조커)친구를 빼자 

db.myfriends.updateOne({name:'슈퍼맨'},{$pull:{buddy:'조커'}})

db.myfriends.updateOne({name:'슈퍼맨'},{$pop:{buddy:1}})  // 1이 마지막 , - 1이 맨앞 

`$push`,`$pull`,` $pop`,





// find

db.myfriends.find({buddy:/토르/})))

// buddy에  `/토르/` 가있는 컬렉션 찾아서 보여줌 



show dbs

show collections 

db   // 현재 db

use db이름  // 사용 혹은 만듬



db.myfriens.find().pretty()

![image-20220310113609755](Mongo.assets/image-20220310113609755.png)

json모양으로 보기편하게 보여줌 



## aggregation 

NOSQL은 집계함수 많이 안씀,집계사용

aggregation  [Aggregation — MongoDB Manual](https://docs.mongodb.com/manual/aggregation/)

db.collection.aggregate()



db.multi.insertMany([{name:'hong-gd',kor:100,eng:30,math:60},{name:'kim-sd',kor:40,eng:70,math:100},{name:'park-jy',kor:100,end:100,math:100},{name:'huh-jy',kor:100,eng:100,math:100},{name:'lee-ss',kor:60,eng:100,math:70}])

// kor70이상 kor있는값 새로운 그룹으로 `$avg` kor값 끌어와서 평균

// `$match`  -> multi collection 에서 kor field의 값이 70보다 큰 doc

// `$project` ->  가지고온 doc 에서 kor field만 가져오기

// `$group` -> 전체 다 하나로 group(test라는이름으로)  => 평균구하지 .($avg)//

 원래 있는 컬럼 쓸려면 _id:'$eng' 와 같이 사용 

```javascript
db.multi.aggregate({$match:{kor:{$gt:70}}},{$project:{kor:1}},{$group:{_id:'test','average':{$avg:'$kor'}}})
```

// $field: 해당 field값을 사용할때 .(= $$current.field)



db.multi.aggregate(

{$match:{name:/s/}},

{$group:{_id:'test',sum:{$sum:'$kor'}}}

)

name 필드에 s가 들어가는애들을 가져와서
id는 test로 sum이라는 새 필드명을 국어점수의 합으로 그룹





db.score.insertMany([
   {name:"홍길동",kor:90,eng:80,math:98,test:"midterm"},
   {name:"이순신",kor:100,eng:100,math:76,test:"final"},
   {name:"김선달",kor:80,eng:55,math:67,test :"midterm"},
   {name:"강호동",kor:70,eng:69,math:89,test:"midterm"},   
   {name:"유재석",kor:60,eng:80,math:78,test:"final"},
   {name:"신동엽",kor:100,eng:69,math:89,test:"midterm"},
   {name:"조세호",kor:75,eng:100,math:100,test:"final"}
])



db.score.aggregate(

{$project:{_id:0,name:1,kor:1,eng:1,math:1}}

)



db.score.aggregate(

{$match:{kor:{$gt:80}}}

)



db.score.aggregate(

{$group:{_id:'$test','avg':{$avg:'$kor'}}}

)

// 스테이지에 순서에따라 결과가 달라질수있음 



## mapreduce

aggregation framework가 처리하지 못하는 복잡한 집계 작업에 사용

 javascript function을 사용하여 복잡한 작업 처리

자바 스크립트 함수로 만들어 사용

query > map > reduce > out

// map 컬렉션에서 필요한거 가져오고 하나하나에 뭔가적용

// reduce  -> map이 가져온걸로 뭔가 작업(집계?)



// mapreduce

// test가 final인 doc 들의 이름,국어,영어 출력하고 '국어와 영어의 합'도 같이 출력 

// myMap() 을 실행하는 컬랙션이 this



```javascript
function myMap(){
emit(this.score,{name:this.name,kor:this.kor,eng:this.eng,test:this.test})
}
```

```javascript
 function myReduce(key,values){
	 var result = {name:new Array(),kor:new Array(),eng:new Array(),total: new Array()}
 	values.forEach(function(val){
 		if(val.test == 'final'){
			 result.name += val.name + ' ';
			 result.kor += val.kor + ' ';
			 result.eng += val.eng + ' ';
			 result.total += val.kor + val.eng + ' ';
		 }
	 })
 return result
 }
```



db.score.mapReduce(myMap,myReduce,{out:{replace:'myRes'}})

db.myRes.find()



db.myRes.find()
{ "_id" : null, "value" : { "name" : "조세호 유재석 이순신 ", "kor" : "75 60 100 ", "eng" : "100 80 100 ", "total" : "175 140 200 " } }





# pymongo 

 크롤링 데이터활용: [Ljaewon-123/crawling_pra (github.com)](https://github.com/Ljaewon-123/crawling_pra)

python_mongodb : [python_mongodb](https://github.com/Ljaewon-123/crawling_pra/tree/master/python_mongodb)

python_mongodb_geo : [python_mongodb_geo](https://github.com/Ljaewon-123/crawling_pra/tree/master/python_mongodb_geo)



`2dsphere`  what is??

[2dsphere](https://docs.mongodb.com/manual/core/2dsphere/) indexes support queries that calculate [geometries on an earth-like sphere](https://docs.mongodb.com/manual/geospatial-queries/#std-label-geospatial-geometry).

To create a index, use the [`db.collection.createIndex()`](https://docs.mongodb.com/manual/reference/method/db.collection.createIndex/#mongodb-method-db.collection.createIndex) method and specify the string literal as the index type:`2dsphere``"2dsphere"`

[2dsphere](https://docs.mongodb.com/manual/core/2dsphere/) 인덱스는 [지구와 같은 구의 형상](https://docs.mongodb.com/manual/geospatial-queries/#std-label-geospatial-geometry)을 계산하는 쿼리를 지원합니다.

인덱스를 만들려면 [`db.collection.createIndex()`](https://docs.mongodb.com/manual/reference/method/db.collection.createIndex/#mongodb-method-db.collection.createIndex) 메서드를 사용하고 문자열 리터럴을 인덱스 유형으로 지정합니다.`2dsphere``"2dsphere"`

```
db.collection.createIndex( { <location field> : "2dsphere" } )
```

값이 [GeoJSON 개체](https://docs.mongodb.com/manual/geospatial-queries/#std-label-geospatial-geojson) 또는 [레거시 좌표 쌍](https://docs.mongodb.com/manual/geospatial-queries/#std-label-geospatial-legacy)인 필드입니다







db.starbucks02.find()

```javascript
db.starbucks02.createIndex({location:'2dsphere'})
{
        "numIndexesBefore" : 1,
        "numIndexesAfter" : 2,
        "createdCollectionAutomatically" : false,
        "ok" : 1
}
```



```javascript
db.starbucks02.find({
		location:{$near:{$geometry:{type:'Point',coordinates:[127.4374521447789,36.35228873845548,]}}}	
	}
)
```

가장 가까운거 부터 찾아줌 



대전 복합터미널 36.35228873845548, 127.4374521447789

// 내위치에서 최대 500미터 안

```javascript
db.starbucks02.find({
		location:{$near:{$geometry:{type:'Point',coordinates:[127.4374521447789,36.35228873845548,]},$maxDistance:2000}}	
	}
)
```





 현재위치부터 가까운 순서대로

"지역" 단어가 포함된 좌표들의 거리

```javascript
db.starbucks02.aggregate([
	{

		$geoNear:{

			near:{type:'Point',coordinates:[127.4374521447789,36.35228873845548,]},
            spherical:true,
            query:{s_name:/대전/},
            distanceField:'distance'

		}

	}

])
```



대전 한국 병원 : 127.43556531618916,36.34851222773056

만남공원: 127.42987488772067,36.36176750692886

봉촌어린이공원:  127.41430548753996,36.35180612846237

대전 없음

```javascript
db.starbucks02.find({
    location:{
        $geoIntersects:{
            $geometry:{
	            type:'Polygon',
    	        coordinates:[[[127.43556531618916,36.34851222773056],
        	                [ 127.42987488772067,36.36176750692886],
            	            [127.41430548753996,36.35180612846237],
                	        [127.43556531618916,36.34851222773056]]]
        }}
    }
})
```

Polygon 다각형 몇각이든 상관없음

```javascript
db.starbucks02.find({
    location: {
        $geoIntersects: {
            $geometry:{
                type: 'Polygon',
                coordinates: [[
                    [127.02765299419028, 37.49875565056365],
                    [127.0437891634432, 37.511011780209415],
                    [127.07043959205164, 37.49756397521862],
                    [127.02765299419028, 37.49875565056365]
                ]]
            }}}})
```









원

```javascript
db.starbucks02.find({
    location:{
        $geoWithin:{
            $centerSphere:[[127.4374521447789,36.35228873845548],0.5/3963.2]
        }
    }
})
```

