# 프로젝트 완성본

[cshun1006/DI: 3조 : 동헌이와 아이들 (github.com)](https://github.com/cshun1006/DI)



# 추가된 pip

pymongo



# 나중에 메인으로 올라갈 기능 들만 모음

저장한 DB데이터를 AWS 에 같이 저장해서 모두다 쓸수있도록

AWS 주소 치면 Django 서버가 자동으로 열리도록 



내가 만든것만??

장고부터는 깃으로 해결함 내 로컬폴더엔 많이 안올라갈듯 싶다

aws 배포쯤 되면 더 그럴듯



폴더명

# Data_Processing

json_class.py

프로젝트에 사용하는 API가 지원하는 옵션키들이 전부 필수키이기 때문에 어떤 요청을 할때마다 하나하나 지정해서 응답받아야 함으로 각API가 묶일수 있고 관리,수정이 쉽게 **Traffic클레스**로 만들고 

 한번에 모든 연도,시도,구군을 JSON파일로 바꿔서 저장하는 맴버함수 **Make_Json()**를 만듬 해당 함수를 만들기 위해 필요한 Year 연도 리스트와 SiDo라는 sidocode와 guguncode를 같이 가지고 있는 딕셔너리 형태의 변수를 **class변수(맴버변수)**로 만듬 

find_index()  매개변수에 (시도,구군)을 넣으면 알맞는 인덱스로 바꿔주는 맴버함수

후에 RDB를 사용하기 위해 Make_Json()으로 만들어진 JSON파일을  CSV로  변형후 다른이름으로 저장하는 **json_to_csv()**맴버함수 

Make_Json() 로 만들어진 연도별 전국 좌표를 구글맵 url에 키워드별 좌표를 검색해서 크롤링 

4년치 전국 하는데 50~60시간정도 걸렸다...

해당 기능을 하는 **add_crwaling**파일  내가만들었지만 수정 사항이 정말 많았다 특히 스크롤 부분에서 

div 내에 스크롤 태그의 문제 수정



아래랑 합침? 



google_map.py 

셀레니움 드라이버를 사용했고 BeautifulSoup가 먹지않는 구글지도 특성상 모든것을 셀레니움으로 처리해야했고 검색명,좌표의 변경은 url을  직접 수정하며 동작하게했다

저장한 json 파일을 불러와서 해당 좌표하나하나를 구글지도에 내주변 검색하기 기능을 사용해서 상호명,카테고리 등등을 지정 출력 프로토타입이다

pre_cra

google_map.py 이 코드를 json_class.py 에서 사용이 가능하게 SiDo 변수를 불러오고 find_index()함수를 사용했다 즉 만들어진 json파일의 모든 연도,시도,구군의 좌표값을 구글지도에 내주변 검색하기로 검색하고 크롤링해옴

 







# Pymongo

폴더에 insert_many.py 는 불러온 json 파일 mongo에 올리고 원하는 대로 find 해본 파일





# Hadoop Spark

기존에 있던 자바를 지우지 않고 진행하다가 새로 다운받은 자바 버전을 인식하지 못해서

원래 자바의 심볼릭링크 연결을 끊어주고 스파크가 원하는 /bin/java 에 

`ln -s /home/ubuntu/java/bin/java /bin/java` 심볼릭 링크 생성 



# Hadoop -> Spark -> DB 으로 업로드 

.sh 들은 sudo chmod를통해 실행가능 하도록 바꿔줘야함 

## 업로드 순서

json_class.py 를 통해 API값을 받아오고 하둡에 upload

몽고디비 키고

mysql에서 테이블 만들기, 업데이트 하고 

spark

 몽고디비에 넣고

mysql 에 테이블 짤라서 넣음 ( 일단 컬럼 수정부터)

spark

몽고디비 종료

## Hadoop 에 업로드

API 하나당 객체 하나이므로 파일 업로드 같은 경우 한폴더에 넣어 통째로 업로드 하며 파일 수같은 것은 json_class.py 에서 나온 객체수를 따른다. 연습 파일 본과 실제 업로드 본은 다를것

연습파일본은 객체 1~2 정도만 있을정도

특정 폴더를 **초기화** 시키며 하둡에 업로드 

.sh 

```terminal
hdfs dfs -put -f /home/jaewon/data /home/jaewo
```



## MongoDB

mode append가 아니라 overwrite를 사용하는 이유:

전부 형식이 똑같은 json으로 만들어진 파일의 doc가 하나이기 때문에 한 컬렉션에 여러개가 들어가 있으면 정확하게 필요한 데이터를 불러오기가 힘들어서 서로 다른 컬렉션에 저장한다.

.sh   // 쉘스크립트를 사용해서 mongodb 시작 이며 sudo 를 사용하는 특성상 자동으로 비밀번호를 입력하여 접속하게함

```terminal
echo '비밀번호' | sudo -kS service mongod start 
```

여기서 -kS는 sudo 쿠키를 초기화 함 

이후 .py 파일에서

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("yarn").appName("insert_mongo").getOrCreate()


json_file01 = spark.read.format('json').load('/home/jaewon/data/created_data/jaywalking.json')

json_file01.write.format('mongo').option('database','test').option('collection','test_insert').mode('overwrite').save()

```

스파크 세션과 spark객체 만들고 Make_Json에서 만들어진 json파일 불러오고 그것을 mongo에 test db test_insert col 에 overwrite로 초기화 하면서 저장 



## Mysql

mysql -- 파일화 안해도됨  해야할듯?

mysql를 실행시켜주는 .sh 파일과 SQL쿼리문을 실행시켜주는 .sql 파일이 있어야함 

```terminal
# sudo mysql -u root -p   # mysql 실행
# mysql_config_editor set --login-path=root --host=localhost --user=root --password

# mysql --login-path=root   

mysql --login-path=root < test.sql

# 앞으로 데이터가 계속  올라갈 테이블과 타입들을 맞춰줘야함
CREATE TABLE test([컬럼명] [타입],[컬럼명] [타입]);
```

이후 test.sql 에서 관련 쿼리문을 작성 



그후 spark 에서 실행 

설정한 user와 비번 databases 드라이버 사용 테이블 까지 지정 업로드 

연습용 csv 파일 로드후 Mysql 에 mysql이라는DB에 test1이라는 dbtable 에 저장 

```terminal
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("yarn").appName("insert_mongo").getOrCreate()

csv_file01 = 
spark.read.format('csv').option('header','true').load('/home/jaewon/data/jaywalking_accident.csv')
user='root'                                                                 
password='1234'    
url="jdbc:mysql://localhost:3306/mysql"
driver = 'com.mysql.cj.jdbc.Driver'
dbtable='test0'

url="jdbc:mysql://localhost:3306/stone"

#csv_file01.write.jdbc(url,dbtable,'overwrite',properties={'driver':driver,'user':user,'password':password})

# 설정해둔 스키마가 날라가서 지우고 다시만드는 식으로??
# sql같은 경우는 mongodb와 다르게 append를 해야 스키마가 유지되며 count(*) row가 유지된다
# mongodb는 NOSQL이라 그냥 append 하면 추가가 되는듯하다 용량이 늘어난것을 확인했음


csv_file01.write.jdbc(url,dbtable,'append',properties={'driver':driver,'user':user,'password':password})


# 처음 빈 테이블 에서 append
mysql> select count(*) from test0;
+----------+
| count(*) |
+----------+
|     1524 |
+----------+

# 위에서 한번 실행한뒤 다시 append
mysql> select count(*) from test0;
+----------+
| count(*) |
+----------+
|     1524 |
+----------+
결과가 같다 추가가 아니다 

# 중간중간에 들어갈 컬럼 수정 inf_population
csv_file01.selectExpr('id','year_code','gugun','household','male','female','sumKor','korM','korF','sumFor','forM','forF','HousePerPerson','over65').show(5)

# inf_ele_display
csv_file02.selectExpr('id','sido','gugun','year_code').show(5)

```



# AWS in Django

GIT을 사용해서 로컬에서 aws로 코드를 전달 

Gunicon으로 웹서버랑 wsgi 서버 따로 만들었고 
그거를 올려줬으니까 
python manage.py runserver를 안 해줘도 접근이 되어야하거든

Nginx,Gunicon,활용 

배포 url : http://35.77.242.184:8083/

# error

```
while (i := lang_code.rfind('-', 0, i)) > -1:
```

django 4.0은 파이썬 3.8버전부터 지원

우리는 pyspark의 원할한 지원을 위해 파이썬 3.7을 사용하기 때문에 

django버전을 낮춰주기로함

```
pip uninstall django
conda uninstall django

conda install django==3.2
```

 http://ec2-35-77-242-184.ap-northeast-1.compute.amazonaws.com:8083

그외 에러들은 [BD_Project/Documents at master · Ljaewon-123/BD_Project (github.com)](https://github.com/Ljaewon-123/BD_Project/tree/master/Documents)

폴더에 정리해둠

# Django

방화벽 열고 포트포워딩으로 mysql끼리 연결 

stone 라는 db사용

```sql
select user,host from mysql.user;  # 유저랑 호스트 확인
revoke all on *.* from 'root'@'%';
grant all PRIVILEGES on stone.* to 'root'@'%'; 
```

하고 방화벽 `고급설정`  아웃/인 바인더리

bin/ 의 mysql_di 열고

mysqld_di 포트열어야함

주소창에 `공유기 ip`   mysql 서버에서 암호 보안문자 확인

관리도구 포트 포워딩 해줌 그리고 nat/라우터 관리에서 `외부 ip주소` 를 확인

설정후 저장 

네이버에 내 ip 주소확인 

이후 cmd창에서 mysql -u [유저] -h '[p주소] -p

# Django 파일

1_page.html 에 **chart.js** 를 사용해 셀렉트에 따른,로딩에 따른 ajax로 mysql 데이터를 꺼내서 차트에 적용시킴

accident 프로젝트 mysql 에서 데이터를 객체 , 퀴리셋으로 가져오고 

views.py 에서 Ajax(GET)로 받아서 리턴을 다시 html에 보내줌 

chart.js 를 사용함 

chart.js를 Ajax로 사용한건 처음이였는데 ajax가 비슷비슷하게 활용할수있어서 의외로 편하게 만들었다.

2_page.html

해당 페이지 전부를 했다 **highcharts** 를 사용하여 pie와 column차트를 그렸고 이것도 마찬가지로 Ajax로 mysql에 연결된 데이터를 꺼내왔다

## 이후 django 파일 git hub

**이후 코드는 BD_project 파일에 올리지 않고 공유 파일에 따로 올린다**

내가 따로 분리해서 가지고 있으면 git을 사용하는 의미가 없기도 하고 여럿이서 django한 파일에 적용하는 만큼 git사용은 필수적이며 DB사용에 있어서도 팀원의 DB에 원격접속하여 django를 사용하고 후에 aws는 나혼자 할 수 없으니 공유파일에만 하기로 한다.

앞으로 DB파일 변경 or 수정 ,파일수정,추가 등등 많은 변경사항이 있는 만큼 공유폴더를 주로 사용하도록 한다.



## django 와 mysql 연결





mysql 워크벤치로 테이블 만들어서 장고 연결해봄

mysql 편집 완료하고

```sql
python manage.py inspectdb # mysql 의 구조 가져옴
python manage.py inspectdb > models.py  # 가져온 구조를 models.py에 복사
python manage.py migrate  

python manage.py showmigrations [app_name] # 앱 확인 
```



# csv 데이터 변경점

python manage.py inspectdb 

이게 한글이름을 아예 인식못해서 

이름만 바꿈 

옐로우카펫 -> yellowcarpet

지역구별_인구수 -> population

어린이보호구역 ->  child_zone

가변전광판 -> ele_display  

교통사고발생현황 -> car_acc 

과속방지턱  -> speed_bump 

무인감시카메라  ->   un_camera

스마트가로등 -> smart_lamp  

스마트횡단보도 -> smart_cross 

# crontab

crontab -e   edit

crontab -l 크론탭설명 보겠다



# git

처음으로 브렌치를 나눠서 작업해봤다 브렌치를 나눴는데도 서로 충돌에러가 났고 그걸 해결하면서 깃의 사용법을 조금더 익히게 된거같다.
