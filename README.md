# VM_*Ubuntu*

리눅스 기반의 os

`하둡,스파크,재플린 노트북`을 CLI로 다운,연결 및 이용

여기서 사용하는 기본 리눅스 명령어 정리는 linux.txt파일에 있음



[Hadoop](#Hadoop  3.3.1)

[Spark](#Spark  3.1.3)

[Spark_문법](#Spark 문법)

1. [Rdd](#Rdd)
2. [DataFrame](#DataFrame )

[Spark streaming](#Spark streaming 스파크 스트리밍)

[파이썬,쉘스크립트](#파이썬 파일로 실행하기)

[zeppelin]( #zeppelin)

[Mysql](#mysql)

[MongoDB](#MongoDB)

전체 역할에서
하둡은 저장과 연결
스파크는 DB에 넣어주기전 처리

추가 

[Webhdfs](#webhdfs)

[Airflow_Error](#Airflow_Error)  

# Hadoop  3.3.1

**대용량 데이터를 분산 저장할수 있는 자바기반 프로그램**

하둡의 구성 요소
하둡은 4개의 주요 모듈로 구성됩니다.

Hadoop Common :
하둡의 다른 모듈을 지원하기 위한 공통 컴포넌트 모듈
Hadoop HDFS :
분산저장을 처리하기 위한 모듈
여러개의 서버를 하나의 서버처럼 묶어서 데이터를 저장
Hadoop YARN :
병렬처리를 위한 클러스터 자원관리 및 스케줄링 담당
Hadoop Mapreduce :
분산되어 저장된 데이터를 병렬 처리할 수 있게 해주는 분산 처리 모듈
Hadoop Ozone :
하둡을 위한 오브젝트 저장소



hdfs - 하둡 설정 

yarn - 리소스,노드관리 해주는 관리자



2.9대 버전까지는 port가 50070이었으나 3.x대 부터는 9870으로 바뀌었다.



**싱글모드로 구현**

> 싱글모드는 한컴퓨터에 namenode,datanode가 있으며 서로 다른컴퓨터로 인식해 정보를 저장하게한다.





Secondary NameNode:  namenode 죽었을때 임시로 namenode가 되주는얘



`sudo apt install openssh-server ssh-askpass -y`

SSH(Secure Shell) 원격지 호스트 컴퓨터에 접속하기 위해 사용되는 인터넷 프로토콜

위 명령어는 ssh 서버를 열어서 별도의 물음 없이 접속허가를 내려주는 모듈이다



#ssh-keygen
namenode와 datanode는 서로를 다른컴퓨터로 인식
서로 접속시 특정키가 있으면 바로바로 접속가능 그게 ssh-keygen 임



-P '' 이전키 일단 아무것도 없는걸로 덮어씌기

`ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa`

rsa, dsa, ecdsa 등등의 공개키 알고리즘이 있는데, 보통 rsa 많이 사용 

열쇠만듬

ssh-keygen 시큐어셀 접속 

키는 rsa 타입 ~/.ssh/id_rsa여기에 키만듬

`cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`

> rsa:비대칭형의 공개키 암호방식
> des: 대칭키

(cat)명령 >> 파일 파일에 추가저장

id_rsa.pub만들어진 public키를 /.ssh/authorized_keys넣어줌

하둡이 자바기반  프레임 워크이기 때문에 

자바 in ubuntu 

>openjdk
>amazon corretto

위 2개중에서 amazon corretto를 다운

wget CLI에서 해당링크 연결된 무언가 응답받기 가능 브라우저비슷 

```linux
wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz
```



`tar -xvzf amazon-corretto-11-x64-linux-jdk.tar.gz`    # 압축해제

`ln -s amazon-corretto-11.0.14.10.1-linux-x64/ java`  # java라는 심볼링 링크 만들어줌 

ls -al

lrwxrwxrwx  1 jaewon jaewon        39 Mar 10 23:06 java -> amazon-corretto-11.0.14.10.1-linux-x64/

심볼링크 확인가능



`sudo vim ~/.bashrc `  # 자바 변수및 경로설정

![image-20220314221447455](README.assets/image-20220314221447455.png)

`source ~/.bashrc`      # bash.rc 저장 실행



**하둡과 스파크 사용을 위해 3.8인 파이썬 버전을 낮춰야함**

python3 --version  버전내려야함

`sudo add-apt-repository ppa:deadsnakes/ppa`  // 3.7버전을 설치하기위한 공간추가
`sudo apt update`



sudo vim ~/.bashrc

`sudo apt install python3.7 -y`    3.7버전 다운

![image-20220314221658402](README.assets/image-20220314221658402.png)

파이썬 & pip 별칭설정 앞으로 python,python3,pip명령어 들은 = 이후의 값을가지게됨

source ~/.bashrc

``` 
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
```

`tar -xvzf hadoop-3.3.1.tar.gz`

압축해제

`ln -s hadoop-3.3.1 hadoop`

가끔 심볼릭링크 깨질수있음
삭제하고 다시

`sudo vim ~/.bashrc`

![image-20220314224043850](README.assets/image-20220314224043850.png)

바로 저장실행
`source ~/.bashrc`



bashrc 설정 모음

```
```





`cd $HADOOP_CONF_DIR` 이후

`vim hadoop-env.sh `  하둡 환경  # 주석표시 풀고 추가 설정 해줌 들어가서 확인

54번줄

```
export JAVA_HOME=/home/jaewon/java
```



58번줄

```
export HADOOP_HOME=/home/jaewon/hadoop
```



68번줄

```
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
```



97번줄

```
export HADOOP_OS_TYPE=${HADOOP_OS_TYPE:-$(uname -s)}
```



198번줄에도 하나 tmp파일 어디에 저장?
임시저장소 가상머신 종료 시 하둡저장 파일 다 날라감

``` 
export HADOOP_PID_DIR=$HADOOP_HOME/pids
```



그뒤 `cd $HADOOP_CONF_DIR`  경로에서 중요 설정 해줌 

`vim core-site.xml`

**네임노드** = 데이터 노드 관리,클라이언트한테 요청을 받고 data node에 일을 시킴
데이터 노드에서 끌어와서 응답을 주기도함 
core-site 에  value로 준 **9000번 포트가 네임 노드임**

```html
<configuration>
        <property>
                <name>fs.defaultFS</name>
                <value>hdfs://localhost:9000</value>
        </property>
</configuration>
```

`vim hdfs-site.xml `

```html
<configuration>
        <property>
                <name>dfs.replication</name>
                <value>1</value>  # 싱글모드 데이터 노드가 하나, 저장이 1개에 노드에됨
        </property>
        <property>
                <name>dfs.namenode.name.dir</name>
                <value>/home/jaewon/hadoop/namenode_dir</value>
        </property>
        <property>
                <name>dfs.datanode.data.dir</name>
                <value>/home/jaewon/hadoop/datanode_dir</value>
        </property>
</configuration>
```

`vim mapred-site.xml`   # 맵리듀스 관련 설정

```html
<configuration>
        <property>
                <name>mapreduce.framework.name</name>
                <value>yarn</value>
        </property>
</configuration>
```



cat core-site.xml   기본적인 하둡 설정

cat hdfs-site.xml   싱글모드/데이터,네임노드를 컴퓨터 하나가 다함 ,네임하나에 데이터 여러개/멀티모드 

똑같은거 데이터 노드에 복사되야하는데 싱글모드라 안그래도됨 요청되었을때 저장 몇개? value에 1로 되어있음 
cat mapred-site.xml

프레임워크 얀모드로 설정

hdfs namenode -format   # 네임노드 초기화

hdfs datanode -format  	# 데이터 모드 초기화

포맷해야 사용가능 처음 설정 이후만



yarn 작업및 리소스관리   // 리소스 매니저 

2.0버전부터 도입 jobtrack를 분리 맵리듀스 하기 위해 필요한 애들을 자름 

분산모드

https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html
Cluster Setup

start-dfs.sh

start-yarn.sh

jps

stop-all.sh



`hdfs dfsadmin -report`   # 설정한 하둡 관련 설정  vm내부 브라우저 url에서 확인가능

```
localhost:9870    (vm안에서) 내가 설정한 하둡 브라우저로 확인가능  hdfs

localhost:8088    하둡 yarn이랑 관련된 페이지 // 스파크 실행시 스파크 확인가능 
```



# Spark  3.1.3

데이터 가공,처리하는 프레임워크

스파크 : 빅데이터 처리를 위한 오픈소스 분석엔진

####  스파크 클러스터

클러스터란 여러 대의 서버가 마치 한대의 서버처럼 동작하는 것을 뜻합니다. 스파크는 클러스터 환경에서 동작하며 대량의 데이터를 여러 서버에서 병렬 처리합니다



rdd
df 
ds  는 파이썬 지원안됨



bin 은 실행파일

sbin은 sudo가 실행하는 파일



하둡 사용가능유저 설정

HDFS 하둡 분산피일 시스템 



**설정에서 path오류로 다 날라갔을때**

```
cd /etc/environment.d/

export PATH=$PATH:/usr/bin:/bin

cd

ls

~ 에서 입력

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/jaewon/java/bin:/home/jaewon/java/bin:/home/jaewon/hadoop/bin:/home/jaewon/hadoop/sbin
```



스파크 설치

https://spark.apache.org/downloads.html

스파크 버전 3.1.3 

재플린 노트북 때문

하둡 따로 설치 버전

설치

```
wget https://dlcdn.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-without-hadoop.tgz
```

만일을 대비해 하둡 중지 후 작업

하둡 중지

/# stop-all.sh

stop-dfs.sh
stop-yarn.sh

`tar -xvzf spark-3.1.3-bin-without-hadoop.tgz `  # 압축해제

`ln -s spark-3.1.3-bin-without-hadoop spark `  # 심볼링크

자바는 하둡에 필요해서 하둡이 자바 기반이라 받음



`sudo vim ~/.bashrc`  들어가서 스파크 설정

![image-20220314230602314](README.assets/image-20220314230602314.png)

`source ~/.bashrc`



`cd $SPARK_HOME/conf`

개별 설정 파일 복사겸 이름 간소화

```
cp workers.template workers    			# 라이센스 등등
cp spark-env.sh.template spark-env.sh			# 설정
cp spark-defaults.conf.template spark-defaults.conf
```

해당 디렉토리에서

`vim spark-env.sh`

```scala
export JAVA_HOME=/home/jaewon/java
export HADOOP_CONF_DIR=/home/jaewon/hadoop/etc/hadoop
export YARN_CONF_DIR=/home/jaewon/hadoop/etc/hadoop
export SPARK_DIST_CLASSPATH=$(/home/jaewon/hadoop/bin/hadoop classpath)

export PYSPARK_PYTHON=/usr/bin/python3.7
export PYSPARK_DRIVER_PYTHON=/usr/bin/python3.7
```

`vim spark-defaults.conf`

```
spark.master                            yarn
```



이상으로 스파크 **싱글모드** 설치끝



## Spark 문법

스파크?

클라이언트 요청시 드라이버가 받아서 클러스터매니저에게 주면 슬레이브에 던져서 실행시킴

스파크는 기본적으로 scala(jvm 기반)

네임노드 클라이언트  마스터

세컨더리 네임노드 대체 네임노드

데이터 노드 데이터 저장 슬레이브

spark sql : df,쿼리문형태

spark  stream : 실시간처리

mllib : ml사용가능

spark core : rdd

yarn을 사용해서 하둡에 저장 --> 불러오는 주체가 하둡이라는 소리

standalone 이면 리눅스에 바로 저장  --> 같다

```
cd ~
jaewon@ubuntu:~$ start-dfs.sh
start-yarn.sh
pyspark      # 시작 
```

![image-20220314233936808](README.assets/image-20220314233936808.png)

각노드 작동 확인





http://localhost:8088  에서 pyspark확인가능
--> 하둡 yarn이라는 놈이 spark를 도와줌 연결?



lazy-evaluation (lazy-execution)

게으른 진화 게으른 실행?

작업들을 다읽은 후에 진행



### Rdd

Rdd란?

> 1차원 배열 데이터 
>
> 다수의 서버에 걸쳐 분산 방식으로 저장된 데이터 요소들의 집합을 의미하며, 병렬처리가 가능하고 장애가 발생할 경우에도 스스로 복구될 수 있는 내성을 가지고 있다
>
> 



RDD 가 SERIES 판다스의 시리즈 같은 것 으로  특정 상황에서 장애 복구하기에 편하다
DataFrame 가 DataFrame 이다.

```python
rdd01 = sc.range(0,1000,1,2)
```

0~1000 ,1씩증가, 파티션을 2개로 나눔

rdd01    ~~~~~.scala 내부에선 스칼라로  사용  객체로 보여줌



```
rdd01.collect()     # 내용확인
```

파티션 확인

```    scala
rdd01.getNumPartitions()
```

2
아까 파티션 2개라고 해서 2임 

```python
rdd01.take(5)
[0, 1, 2, 3, 4]
```

```python
rdd02 = rdd01.filter(lambda x:x % 2)
rdd02 = rdd01.filter(lambda x:x % 2 == 1)
rdd01에서 0이 아닌애들만 rdd02로감   홀수만 남음
```

```python
rdd03 = rdd01.filter(lambda x:not x % 2)  짝
rdd03 = rdd01.filter(lambda x:x % 2 == 0)  짝
```

컨트롤 + l == cls

```python
countries = ['korea','united states america','united kingdom','japan','france','germany','italia','canada','korea']
-> rdd로 바꿔야 collect가 통함
```

```python
g8 = sc.parallelize(countries,2)  # countries를 2개의 파티션으로 분할
g8.collect()
g8.count()
g8 = g8.distinct()   	# w중복제거
g8.collect()
```

파이썬 map 함수 리터럴값에 함수 적용 

```python
g8_upper = g8.map(lambda x:x.upper())
g8_upper.collect()		# 중간중간 내용확인
g8_list01 = g8.map(lambda x: list(x))
g8_list01 .collect()
g8_list01 = g8.map(lambda x: list(x))  # 문자열 하나하나를 리스트 넘버로 인식해서 아래와 같										  은 결과가 나옴
>>> g8_list01.collect()
[['j', 'a', 'p', 'a', 'n'], ['f', 'r', 'a', 'n', 'c', 'e'], ['i', 't', 'a', 'l', 'i', 'a'], ['c', 'a', 'n', 'a', 'd', 'a'], ['g', 'e', 'r', 'm', 'a', 'n', 'y'], ['k', 'o', 'r', 'e', 'a'], ['u', 'n', 'i', 't', 'e', 'd', ' ', 's', 't', 'a', 't', 'e', 's', ' ', 'a', 'm', 'e', 'r', 'i', 'c', 'a'], ['u', 'n', 'i', 't', 'e', 'd', ' ', 'k', 'i', 'n', 'g', 'd', 'o', 'm']]
>>> g8_list02 = g8.flatMap(lambda x:list(x))
>>> g8_list02.collect()
['f', 'r', 'a', 'n', 'c', 'e', 'i', 't', 'a', 'l', 'i', 'a', 'c', 'a', 'n', 'a', 'd', 'a', 'j', 'a', 'p', 'a', 'n', 'k', 'o', 'r', 'e', 'a', 'u', 'n', 'i', 't', 'e', 'd', ' ', 's', 't', 'a', 't', 'e', 's', ' ', 'a', 'm', 'e', 'r', 'i', 'c', 'a', 'u', 'n', 'i', 't', 'e', 'd', ' ', 'k', 'i', 'n', 'g', 'd', 'o', 'm', 'g', 'e', 'r', 'm', 'a', 'n', 'y']
>>> counting = sc.range(1,9,1,2)
```

```python
g8_list02 = g8.flatMap(lambda x:list(x))    #  다쪼개서 하나의 리스트로 통합 
```

map과 flatmap의 차이 

map은 각각의 요소에 적용시킴

flatmap은 적용시키고 전체적인 요소로 따짐



zip 요소의 개수가 같은 리스트를 딕셔너리 형태로 합쳐줌

```python
counting = sc.range(1,9,1,2)
counting_g8 = counting.zip(g8)
counting_g8.collect()
# 단순 결과만 보기 원한다면 한번해 해도된다
counting.zip(g8).collect()
```

```python
score = [('강호동',10),('유재석',30),('강호동',30),('신동엽',70),('유재석',60)]
score_rdd = sc.parallelize(score,2)   # score를 2개의 파티션으로 나눔
score_rdd.collect()

# reduceByKey 
score_rdd_rbk = score_rdd.reduceByKey(lambda x,y:x+y)
score_rdd_rbk.collect()
[('강호동', 40), ('신동엽', 70), ('유재석', 90)]
```

여기서 reduceByKey와 groupByKey의 차이

내가 느낀  [차이](# 내가 느낀 groupByKey() ,reduceByKey() 차이점)

훨씬 큰 데이터 셋에서 `reduceByKey`와 `groupByKey`는 셔플링하는 데이터 차이가 극명합니다. `groupByKey` 대신 사용할 수 있는 다른 함수들도 존재합니다.

 `reduceByKey`는 키를 기준으로 셔플링을 하기 전에 미리 각 파티션 내에 있는 데이터들을 먼저 combine을 수행합니다. 맵리듀스의 combiner를 사용하는 것과 동일한 역학을 수행하는 것

![image-20220315000140669](README.assets/image-20220315000140669.png)

 `groupByKey`는 모든 키-값 페어에 대해 셔플을 수행합니다. 이러한 동작은 단어 세기 예제와 같은 경우 불필요한 셔플을 발생하여 네트워크 자원을 더 많이 소모함

![image-20220315000213307](README.assets/image-20220315000213307.png)



```python
nums = sc.parallelize([1,2,3,1,1,2,5,4],2)

# 두개의 결과다름
nums.sortBy(lambda x:x).collect()  # 정렬된 형태로 나옴
nums.collect()
```

```python
arrs = g8.glom()   # 파티션 별로 리스트로 나눠줌   ## 주의 크기가 크면 에러가 잘남 
arrs.collect()
[['japan', 'france', 'italia', 'canada'], ['germany', 'korea', 'united states america', 'united kingdom']]
```

`nums.stats()`

pd의 info같은 거 해당 데이터의 어지간한건 다 보여줌



```scala
g8.take(3)
['japan', 'france', 'italia']
g8.takeOrdered(3)			# 정렬다음에 가져옴 오름차순
['canada', 'france', 'germany']
g8.top(3)  			# 내림차순 정렬후 가져옴
['united states america', 'united kingdom', 'korea']
```

```java
# count()를 이용하여 함수사용
g8.takeOrdered(g8.count())
['canada', 'france', 'germany', 'italia', 'japan', 'korea', 'united kingdom', 'united states america']
g8.top(g8.count())
['united states america', 'united kingdom', 'korea', 'japan', 'italia', 'germany', 'france', 'canada']
```

```scala
nums.countByValue()    	# 말그대로 각요소 카운팅 메모리에 넣고 세서 너무 많으면 강제종료 나옴 
defaultdict(<class 'int'>, {1: 3, 2: 2, 3: 1, 5: 1, 4: 1})
```

```python
# fold(기본값,연산): 데이터 연산,  **파티션 단위 연산**  각각 파티션 부터 먼저 다 더하고 파티션끼리 더해줌 
rdd02_fold = rdd02.fold(0,lambda x,y: x+y)   # sum이랑 똑같음 
rdd02_fold
```

집계함수

```python
# aggregate
rdd02_aggr = rdd02.aggregate(0,max,lambda x,y:x+y)
```

reduce

```python
rdd02_reduce = rdd02.reduce(lambda x,y:x+y)	# 데이터 병렬연산  함수??
reduce 내부요소 각각 병렬 연산 해줌 즉 요소 2개씩 가져와서 함수로 연산?
```

reduceByKey()같은 경우는 키를 가지고 해줌 

```python

# g8 에서 가장 긴 단어 찾자   g8.max()도 되긴됨 
def g8Max(x,y):
...     if len(x) > len(y):
...             return x
...     else:
...             return y
... 

get_max_lengtf = g8.reduce(g8Max)

# g8 에서 가장 짧은 단어 찾자
g8_min_length = g8.reduce(lambda x,y: x if len(x) < len(y) else y)
```

`g8.saveAsTextFile("/tmp/g8") `

텍스트 파일 저장   # "/tmp/g8" 이름?

`result = sc.textFile("/tmp/g8/part-000*")` # 왜 part-000*인지 확인가능 뒤에나옴

/# 이 파일 어디? tmp라서 날라간건 아님

/# 하둡에 저장된거지 파일로 우분투에 남아있지는 않음

```
hdfs dfs -ls /
Found 2 items
drwxr-xr-x   - jaewon supergroup          0 2022-03-13 23:24 /tmp
drwxr-xr-x   - jaewon supergroup          0 2022-03-13 21:20 /user
```

여기 /tmp가 
스파크 저장은 **하둡**에 저장됨
스파크 로드도 **하둡**에서 저장됨
왜?? sc마스터가 **yarn**이기 때문에 

저장한 파일보기

```
hdfs dfs -ls /tmp/g8/
위에 result로 저장한 파일이 나옴 
Found 3 items
-rw-r--r--   1 jaewon supergroup          0 2022-03-13 23:24 /tmp/g8/_SUCCESS
-rw-r--r--   1 jaewon supergroup         27 2022-03-13 23:24 /tmp/g8/part-00000
-rw-r--r--   1 jaewon supergroup         51 2022-03-13 23:24 /tmp/g8/part-00001
```

여기서 part-00000확인 가능 

**파티션 별로 파일이 저장됨**

```python
# 파티션 별로 어떻게 저장되었는지 확인할 수 있다.
hdfs dfs -cat /tmp/g8/part-00000
france
italia
canada
japan
hdfs dfs -cat /tmp/g8/part-00001
korea
united states america
united kingdom
germany

```



 **copyToLocal**

Hdfs에 있는 파일을 local directory에 다운로드, get 명령어와 유사

```java
Usage: hdfs dfs -copyToLocal [-ignorecrc] [-crc] URI {localdst}
```



##### 외부 data 하둡에 넣기

`hdfs dfs -mkdir -p /home/jaewon`
-p로 한번에 만들수있음

우분투 외부에서 내부로 드래그로 파일 옮길수 있음 
data.zip 파일 가져옴
mkdir data
`unzip data.zip -d ./data`  데이터 파일 밑에 압축해제 해줘



하둡 디스트리뷰트 파일 시스템 

하둡에 데이터 올리기 -put

`hdfs dfs -put /home/jaewon/data /home/jaewon/data` # 데이터

-put 보낼(로컬) 받을(하둡)

### 로컬 -> 하둡에 덮어쓰기 

`hdfs dfs -put -f [로컬경로] [하둡경로]` 파일 덮어쓰기



잘 들어갔나 확인

`hdfs dfs -ls /home/jaewon/data`

```
Found 4 items
drwxr-xr-x   - jaewon supergroup          0 2022-03-14 00:13 /home/jaewon/data/flights
drwxr-xr-x   - jaewon supergroup          0 2022-03-14 00:13 /home/jaewon/data/retails
-rw-r--r--   1 jaewon supergroup      96743 2022-03-14 00:13 /home/jaewon/data/shakespeare.txt
drwxr-xr-x   - jaewon supergroup          0 2022-03-14 00:13 /home/jaewon/data/simple-ml
```

커서객체 처럼

변수까지 저장되지는 않음 

```
countries = ['korea','united states america','united kingdom','japan','france','germany','italia','canada','korea']
g8 = sc.parallelize(countries,2)
g8 = g8.distinct()
```

다시 g8변수 만들어주고



```python
key = g8.keyBy(lambda x:x[0]) # keyBy 현재값으로 키를 생성하는 함수

key.collect()
[('f', 'france'), ('i', 'italia'), ('c', 'canada'), ('j', 'japan'), ('k', 'korea'), ('u', 'united states america'), ('u', 'united kingdom'), ('g', 'germany')]
```

keyBy 가 x[0]을 가르키니까 왼쪽에 하나만 나온게 key가 되는거



pyspark에서 객체내부 볼려면 무조건 collect() 해보기

```python
key.keys().collect()
['f', 'i', 'c', 'j', 'k', 'u', 'u', 'g']
key.mapValues(lambda x:list(x)).collect()   # 벨류에다가만 lambda하는거 한글자 한글자 해줘서 쪼개짐
[('f', ['f', 'r', 'a', 'n', 'c', 'e']), ('i', ['i', 't', 'a', 'l', 'i', 'a']), ('c', ['c', 'a', 'n', 'a', 'd', 'a']), ('j', ['j', 'a', 'p', 'a', 'n']), ('k', ['k', 'o', 'r', 'e', 'a']), ('u', ['u', 'n', 'i', 't', 'e', 'd', ' ', 's', 't', 'a', 't', 'e', 's', ' ', 'a', 'm', 'e', 'r', 'i', 'c', 'a']), ('u', ['u', 'n', 'i', 't', 'e', 'd', ' ', 'k', 'i', 'n', 'g', 'd', 'o', 'm']), ('g', ['g', 'e', 'r', 'm', 'a', 'n', 'y'])]
key.flatMapValues(lambda x:list(x)).collect()  # 리스트값의 한글자씩 키를 가지게됨 == 리스트의 모든 요소가 키를가짐
[('j', 'j'), ('j', 'a'), ('j', 'p'), ('j', 'a'), ('j', 'n'), ('f', 'f'), ('f', 'r'), ('f', 'a'), ('f', 'n'), ('f', 'c'), ('f', 'e'), ('i', 'i'), ('i', 't'), ('i', 'a'), ('i', 'l'), ('i', 'i'), ('i', 'a'), ('c', 'c'), ('c', 'a'), ('c', 'n'), ('c', 'a'), ('c', 'd'), ('c', 'a'), ('g', 'g'), ('g', 'e'), ('g', 'r'), ('g', 'm'), ('g', 'a'), ('g', 'n'), ('g', 'y'), ('k', 'k'), ('k', 'o'), ('k', 'r'), ('k', 'e'), ('k', 'a'), ('u', 'u'), ('u', 'n'), ('u', 'i'), ('u', 't'), ('u', 'e'), ('u', 'd'), ('u', ' '), ('u', 's'), ('u', 't'), ('u', 'a'), ('u', 't'), ('u', 'e'), ('u', 's'), ('u', ' '), ('u', 'a'), ('u', 'm'), ('u', 'e'), ('u', 'r'), ('u', 'i'), ('u', 'c'), ('u', 'a'), ('u', 'u'), ('u', 'n'), ('u', 'i'), ('u', 't'), ('u', 'e'), ('u', 'd'), ('u', ' '), ('u', 'k'), ('u', 'i'), ('u', 'n'), ('u', 'g'), ('u', 'd'), ('u', 'o'), ('u', 'm')]
```



그냥 map이면 쪼개지는데 mapValues 여서 안쪼개졌거나 groupByKey()이게 앞에있어서 안쪼개짐

```python
# 키별로 분류해서 벨류 리스트로 만듬 
key.groupByKey().mapValues(lambda x:list(x)).collect()
[('i', ['italia']), ('c', ['canada']), ('j', ['japan']), ('g', ['germany']), ('k', ['korea']), ('u', ['united states america', 'united kingdom']), ('f', ['france'])]

# 키별로 분류해서 벨류의 개수 카운팅
key.groupByKey().mapValues(lambda x:len(x)).collect()  # 뭐가 나올지 맞춰봐  키밑에 벨류가 몇개??
[('g', 1), ('j', 1), ('i', 1), ('c', 1), ('f', 1), ('k', 1), ('u', 2)]
```

**여기서 groupByKey() 는 lambda의 인수가 한개 **

키는 똑같고 벨류가 달라짐

reduceByKey()는 두개를 받는다 따로 그룹을 안해줘서 그런듯

```python
#[('g','germany'),...('u','united states america,united kingdom')]
key.reduceByKey(lambda x,y:x+","+y).collect()
[('g', 'germany'), ('j', 'japan'), ('i', 'italia'), ('c', 'canada'), ('f', 'france'), ('k', 'korea'), ('u', 'united states america,united kingdom')]
```

**('u', 'united states america,united kingdom')** 이결과가 핵심



**내가 느낀 groupByKey() ,reduceByKey() 차이점**

> groupByKey() 는 뒤에나올 mapValues(lambda x:x) 혹은 mapKeys()따라달라지고
>
> reduceByKey()는 그냥 키와 벨류값 모두 lambda의 인수로 사용할수있다.

```scala
key.countByKey()
defaultdict(<class 'int'>, {'j': 1, 'f': 1, 'i': 1, 'c': 1, 'g': 1, 'k': 1, 'u': 2})

```



localhost 에서 확인

```
result = sc.textFile('/tmp/g8/part-000*')
g8 = result.distinct()
g8_upper = g8.map(lambda x:x.upper())
g8_upper.collect()

yarn확인
localhost:8088
//
localhost:9870
rdd_리니지_yarn관리
```

rdd_리니지yarn관리

![우분투_브라우저](README.assets/우분투_브라우저.png)



yarn확인

![rdd_리니지_yarn관리](README.assets/rdd_리니지_yarn관리.png)





들어가기

![image-20220315011025709](README.assets/image-20220315011025709.png)



![application 이벤트 확인](README.assets/application 이벤트 확인.png)



깨알 몰랐던거  소문자로 바꾸고 1넣어줌 x가 그냥(x.lower(),1))형태

```python
g8.map(lambda x:(x.lower(),1)).collect()
[('france', 1), ('italia', 1), ('canada', 1), ('japan', 1), ('korea', 1), ('united states america', 1), ('united kingdom', 1), ('germany', 1)]

```



`vim spark_wc.py` 안에 집어넣기 어떤 동작인지 확인

결과는 data.zip푼거의 txt파일의 제일 많이쓴 단어 찾기

```python
import sys, re
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('Word Count')  # 워드카운트라는 이름으로 
sc = SparkContext(conf=conf)

if (len(sys.argv) != 3):   # argv 몇개 들어왔는지 확인
    print("wordcount.py input_file output_dir 형태로 실행해 주세요")
    sys.exit(0)
else:
    inputfile = sys.argv[1]
    outputdir = sys.argv[2]
    
wordcount = sc.textFile(inputfile)\
           .repartition(10)\    			# 파티션 10개로 만듬 
           .filter(lambda x: len(x) > 0)\		# 인자의 길이가 0보다 큰거만 가져온다 													공백지우기 
            .flatMap(lambda x: re.split('\W+', x))\ # 정규식 처리  형태를x와 같게하고 														매치,최소한번반복
             .filter(lambda x: len(x) > 0)\		# 다시 0보다 큰거만 
              .map(lambda x:(x.lower(), 1))\	# ('france', 1) 이런형태로 만듬
              .reduceByKey(lambda x, y: x + y)\    # 키는 같고 벨류는 그냥 더해짐 최														종적으로 카운팅??
              .map(lambda x:(x[1], x[0]))\		# [1]벨류,[0]키??
              .sortByKey(ascending=False)\
              .persist()			# 메서드는 스토리지 레벨을 인자로 받아 저장 공간을 										정할 수 있다.

wordcount.saveAsTextFile(outputdir)
top10 = wordcount.take(5)
result = []
for counts in top10:
    result.append(counts[1])
print(result)
```

```scala
py 파일만 머하는 놈인지 분석
spark_wc.py 실행 하는데 shakespeare.txt 를 result 디렉토리 에 결과 넣어줘
hdfs dfs -rm -r /user/jaewon/result  # 실행 X 잘못된 결과 파일 지운거
spark-submit spark_wc.py ~/data/shakespeare.txt ~/result

hdfs dfs -cat ~/result/part-00000   # 어떤 단어 몇개? 출력


```

### submit 파이썬 실행

stop-all.sh   `하둡종료`

**종료전 필수!!!**

`stop-all.sh`

stop-all.sh

![image-20220315013104733](README.assets/image-20220315013104733.png)



### DataFrame 

이번엔 DataFrame 문법

start-dfs.sh
start-yarn.sh
/# start-all.sh

localhost:9870
localhost:8088

데이터 프레임

```python
myRange = spark.range(1000).toDF('number')
toDF 라는 데이터 프레임 number 라는 이름으로
myRange.head(10)
myRange.tail(10)
```

```python
divisBy2 = myRange.where('number % 2 = 0')  # 짝
number 컬럼에서 2로나눈 나머지가 0인놈
divisBy2.head(5)
divisBy2.tail(5)
divisBy2.count()
```

localhost:9870
`Utilties -> browse the file system` 에서 파란색 링크 눌러서 디렉토리 확인가능



csv 데이터 스파크에서 읽기 

printSchema()   # row데이터 보기

```python
fligths2010 = spark.read.csv('/home/jaewon/data/flights/csv/2010-summary.csv')
fligths2010.printSchema()   # row데이터 보기
root
 |-- _c0: string (nullable = true)
 |-- _c1: string (nullable = true)
 |-- _c2: string (nullable = true)
```

다시 설정

```python
헤더를 다시 잡아줌  'header','true' --> 맨첫줄이 컬럼값!
flights2010 = spark.read.option('header','true').csv('/home/jaewon/data/flights/csv/2010-summary.csv')
flights2010.take(5)

카운트 어케 할건지 좀 보자 실행계획? 실행전 미리 확인 가능 
flights2010.sort('count').explain()
```

데이터 프레임 함수 , 스파크
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html#dataframe-apis



csv 가 아니라 json도 가능

```python
json 파일 은 show()가능   -> csv도 가능 하다.
f2015 = spark.read.format('json').load('/home/jaewon/data/flights/json/2015-summary.json')
f2015.show()
f2015.show(5)  위에서 내가 n값만큼
전부보기
f2015.show(f2015.count()) # f2015.count() count()이용해서 전체 보여줌
show()가 전부 보여주는건 아님
```



안시 표준쿼리 위해 테이블 하나 만들기

f2015 를이용해 flights2015 라는 이름의 테이블 만들어짐

`f2015.createOrReplaceTempView('flights2015')`

```python
f2015.createOrReplaceTempView('flights2015')
파이썬 문법으로 sql 하기 
안시 표준 쿼리로 하기
sqls = spark.sql('''
SELECT DEST_COUNTRY_NAME,COUNT(*)
FROM flights2015
GROUP BY DEST_COUNTRY_NAME
''')

# 똑같지만 스파크 sql 매소드로 만들기
dfs = f2015.groupBy('DEST_COUNTRY_NAME').count()
dfs.show()
```

테이블 만들어서 spark.sql이라고 쿼리문을 넣어주면 해당 테이블의 쿼리 형태로 내가 원하는 데이터 뽑기가능
혹은 스파크 모듈안에 매소드들 groupBy,count() 등등, 쿼리에 대응되는 매소드들 사용가능 

ansi로쓰고싶으면 spark.sql쓰고
밑에거는 그애 대응되는
메소드

`.explain()` 은 해당 데이터가 어찌 실행되는지를 기록하는 함후인데

```
sqls.explain()
dfs.explain()
```

다른 방식으로 만들었지만 결과는 같은 위 sqls,dfs를 보면 explain()으로 처리되는 과정이 같다는걸 볼수있다. 



안시 쿼리문은 **pyspark.sql.functions** 경로에 저장

하여 

`from pyspark.sql.functions import max` 식으로 사용가능

```python
from pyspark.sql.functions import max
f2015.select(max('count')).take(1)

f2015.select('DEST_COUNTRY_NAME').show(5)

spark.sql('SELECT DEST_COUNTRY_NAME FROM flights2015 LIMIT 5').show()


spark.sql('SELECT DEST_COUNTRY_NAME,ORIGIN_COUNTRY_NAME FROM flights2015 LIMIT 5').show()

f2015.select('DEST_COUNTRY_NAME','ORIGIN_COUNTRY_NAME').show(5)

```

스파크 sql이랑 안시쿼리로 똑같은거 만들어보는중



**expr, col**

```python
# expr은 함수내부에서 형식까지 지정가능하고 ,col은 그냥 컬럼하나 지정 
from pyspark.sql.functions import expr, col 
f2015.select(expr('DEST_COUNTRY_NAME'),col('DEST_COUNTRY_NAME')).show(5)
```

expr 같은 경우 selectExpr()로도 그역할을 할수있다.

```python
# 같은 결과 다른 과정
f2015.select(expr('DEST_COUNTRY_NAME as destination')).show(5)
f2015.select(col('DEST_COUNTRY_NAME').alias('destination')).show(5)
# 안시 쿼리
spark.sql('SELECT DEST_COUNTRY_NAME AS destination from flights2015 limit(5)').show()

# select(expr == 합쳐짐
f2015.selectExpr('DEST_COUNTRY_NAME AS destination').show(5)

# 컬럼 2개 비교 
f2015.selectExpr('*','(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) AS domestic_flights').show()


spark.sql('SELECT AVG(COUNT),COUNT(DISTINCT(DEST_COUNTRY_NAME)) FROM   flights2015').show()
f2015.selectExpr('AVG(COUNT)','COUNT(DISTINCT(DEST_COUNTRY_NAME))').show()
# 함수 따로 쓰는거보다 selectExpr 합쳐진게 많이 편할수있다.
+-----------+---------------------------------+                                 
| avg(count)|count(DISTINCT DEST_COUNTRY_NAME)|
+-----------+---------------------------------+
|1770.765625|                              132|
+-----------+---------------------------------+
```



**리터럴 값 자체 출력** # literal = 값 자체

```python
from pyspark.sql.functions import lit
f2015.select(expr('*'),lit(1).alias('one')).show()
spark.sql('SELECT *,1 AS ONE FROM flights2015 limit5').show(5)
-----------------+-------------------+-----+---+
|DEST_COUNTRY_NAME|ORIGIN_COUNTRY_NAME|count|one|
+-----------------+-------------------+-----+---+
|    United States|            Romania|   15|  1|
|    United States|            Croatia|    1|  1|
|    United States|            Ireland|  344|  1|
|            Egypt|      United States|   15|  1|
|    United States|              India|   62|  1|
+-----------------+-------------------+-----+---+

```

스파크 sql이 함수쓴다고 겁먹지 말고 안시 쿼리는 그냥 아는거 그대로 쓰면 그게 답임



결과가 들어간게 더 좋나??



pyspark

api가서 한번씩 보기 [pyspark.sql.functions.lit — PySpark 3.2.1 documentation (apache.org)](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.functions.lit.html)

withColumn

```python
# withColumn ,  콘마끼리 묶어서 나온것처럼 이어줌 
컬럼이름으로 오른쪽 조건에 맞게 컬럼을 만들어주고 원래 테이블에서 추가됨 근데 아직은 보여지기만 한거임
새로운걸로 대입해야 추가되는거  a = b
f2015.withColumn('DOMESTIC_FLIGHT',expr('DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME')).show()

spark.sql("select *,(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as domestic from flights2015").show(5)

f2015.withColumnRenamed('DEST_COUNTRY_NAME','DESTINATION').show()
기존 컬럼명 바뀜
안시 쿼리에서는 ALTER RENAME 이게 있음?? 
```

삭제

```scala
f2015.drop('count').show()
f2015.drop('count').columns  # 목록보기 가능
['DEST_COUNTRY_NAME', 'ORIGIN_COUNTRY_NAME']
```

summary 

cast 캐스트가 타입 바꿔주는거

count라는 컬럼을 가지고 오면서 string로 바꿔줌

```python
f2015.withColumn('count2',col('count').cast('string')).summary # astype()
f2015.withColumn('count2',col('count').cast('string')).show()
# 보여지는건 어차피 똑같다
# 하지만 타입을 count에서 string로 바꿔줌

# 똑같지만 안시 쿼리 이용
spark.sql('select *,cast(count as string) as count2 from flights2015').show()
```



filter , where

```python
# 3개다 결과는 같다 
f2015.filter(col('count')<2).show(5) # col 이라는 컬럼 지정 함수 필요
f2015.where('count < 2').show(5)    
spark.sql('select * from flights2015 where count < 2 limit 5').show() # 표준쿼리
+-----------------+-------------------+-----+
|DEST_COUNTRY_NAME|ORIGIN_COUNTRY_NAME|count|
+-----------------+-------------------+-----+
|    United States|            Croatia|    1|
|    United States|          Singapore|    1|
|          Moldova|      United States|    1|
|            Malta|      United States|    1|
|    United States|          Gibraltar|    1|
+-----------------+-------------------+-----+
```

조건 여러개 가능

```python
#  where 가 동시에 실행됨 그래서 가끔식 조건 여러개가 안될때 있음 
f2015.where(col('count') < 2).where(col('ORIGIN_COUNTRY_NAME') != 'Croatia').show(5)

spark.sql("select * from flights2015 where count < 2 and ORIGIN_COUNTRY_NAME != 'Croatia' limit 5").show()

spark.sql("select * from flights2015 where count < 2 and ORIGIN_COUNTRY_NAME NOT IN ('Croatia')").show(5)
```



중복 빼고 count ,distinct

```python
f2015.select('DEST_COUNTRY_NAME').distinct().count()
132        
park.sql('select count(distinct DEST_COUNTry_NAME) AS count from flights2015').show()
+-----+                                                                         
|count|
+-----+
|  132|
+-----+

```



Pyspark Row 사용해서 f2015랑 똑같은 스키마 적용

```python
>>> from pyspark.sql import Row
>>> new_rows = []
>>> new_rows = [
...     Row('Korea','Korea',5),
...     Row('Korea','Wakanda',1)
... ]
>>> rdd_rows = sc.parallelize(new_rows)
>>> schema = f2015.schema
>>> df_rows = spark.createDataFrame(rdd_rows,schema)
>>> df_rows.show()
+-----------------+-------------------+-----+
|DEST_COUNTRY_NAME|ORIGIN_COUNTRY_NAME|count|
+-----------------+-------------------+-----+
|            Korea|              Korea|    5|
|            Korea|            Wakanda|    1|
+-----------------+-------------------+-----+

```

```python
# f2015 와 df_rows를  union 하고, count = 1 이고 origin~ us 가 아닌 데이터
f2015.union(df_rows).where('count = 1').where(col('ORIGIN_COUNTRY_NAME') != 'United States').show()
ORIGIN_COUNTRY_NAME 얘가 아닌거임 DEST_COUNTRY_NAME 가 아니라 
```



정렬

```python
f2015.sort('count').show(f2015.count())  # accending = false???
f2015.orderBy(col('count').asc()).show(f2015.count())
f2015.orderBy(col('count').desc()).show(f2015.count())

spark.sql('select * from flights2015 order by count desc').show(f2015.count())


#  DEST ~ 내림차순, COUNT 오름차순 정렬후 5개만 출력
f2015.orderBy(col('DEST_COUNTRY_NAME').desc(),col('count').asc()).show(5)
spark.sql('select * from flights2015 order by DEST_COUNTRY_NAME desc, count asc limit(5)').show()

f2015.limit(5).show()
```



`inferSchema` 해당 스키마 예측을 정확하게 대신 좀 느려짐

```python
데이터 로드 
retails = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load('/home/jaewon/data/retails/2010-12-01.csv')

retails.printSchema()
# 컬럼 속성
root
 |-- InvoiceNo: string (nullable = true)
 |-- StockCode: string (nullable = true)
 |-- Description: string (nullable = true)
 |-- Quantity: integer (nullable = true)
 |-- InvoiceDate: string (nullable = true)
 |-- UnitPrice: double (nullable = true)
 |-- CustomerID: double (nullable = true)
 |-- Country: string (nullable = true)

# retails 로 retails테이블 만들기
retails.createOrReplaceTempView('retails')
retails.show()로 확인
spark.sql('select * from retails').show()  # 위와 같음

    
```

```python
retails.where(col('invoiceNo') != 536365).select('invoiceNo','Description').show(5,False)

retails.where('invoiceNo <> 536365').show(5,False)
+---------+-----------------------------+
|invoiceNo|Description                  |
+---------+-----------------------------+
|536366   |HAND WARMER UNION JACK       |
|536366   |HAND WARMER RED POLKA DOT    |
|536367   |ASSORTED COLOUR BIRD ORNAMENT|
|536367   |POPPY'S PLAYHOUSE BEDROOM    |
|536367   |POPPY'S PLAYHOUSE KITCHEN    |
+---------+-----------------------------+
```



**INSTR**

```
주어진 문자열에서 substr 열이 처음 나타나는 위치를 찾습니다. 인수 중 하나가 null이면 null을 반환합니다.
```

```PYTHON
# 조건을 변수로 담아서 사용 
from pyspark.sql.functions import instr 
priceFilter = col('UnitPrice') > 600
descripFilter = instr(retails.Description, 'POSTAGE') >= 1
retails.where(retails.StockCode.isin('DOT')).where(priceFilter | descripFilter).show()
# 'POSTAGE' 1개이상

Description 이 'POSTAGE 라는 걸 가지고 있는지 1개이상

spark.sql('''
select  * from retails 
where StockCode in ('DOT')
AND (UnitPrice > 600 OR INSTR(Description,'POSTAGE') >= 1)
''').show()
```



```PYTHON
dotCodeFilter = col('StockCode') == 'DOT'
priceFilter = col('UnitPrice') > 600
descriptFilter = instr(col('Description'),'POSTAGE') >= 1
instr Description 컬럼에 postage 가 있으면 인덱스 표시

retails.withColumn('isExpensive',dotCodeFilter & (priceFilter | descriptFilter)).where('isExpensive').select('UnitPrice','isExpensive').show(5)


spark.sql("select UnitPrice , ((StockCode = 'DOT') and (UnitPrice > 600 or instr(Description,'POSTAGE') >= 1))  AS isExpensive from retails where ((StockCode = 'DOT') and (UnitPrice > 600 or instr(Description,'POSTAGE') >= 1)) ").show() 
```

집계

```python
# (현재 갯수 * 가격)^2 + 5
from pyspark.sql.functions import pow
quantity = pow(col('Quantity') * col('UnitPrice'),2) + 5
retails.select(col('CustomerId'),quantity.alias('myQuantity')).show(5)

spark.sql('''
select CustomerId,(POWER((Quantity * UnitPrice),2) + 5) as myQuantity
FROM retails
''').show()

from pyspark.sql.functions import round,bround
retails.select(round(lit('2.5')),bround(lit('2.5')),lit('2.5')).show(5)

spark.sql('select round(2.5),bround(2.5) from retails').show(5)

bround 내림 
```

종합

`retails.describe().show()`

추가 집계

```python
etails.describe().show()

# count,mean,stddev,min,max
from pyspark.sql.functions import count,mean, stddev_pop , min,max
retails.select(count('UnitPrice'),mean('UnitPrice'),stddev_pop('UnitPrice'),min('UnitPrice'),max('UnitPrice')).show()

avg??
spark.sql('select count(UnitPrice),mean(UnitPrice) from retails').show()


from pyspark.sql.functions import monotonically_increasing_id
retails.select('*',monotonically_increasing_id()).show(5)
/# monotonically_increasing_id  자동으로 숫자 하나씩 올라가는 ,인덱스??


from pyspark.sql.functions import initcap
retails.select(initcap(col('Description'))).show(5,False)


from pyspark.sql.functions import lower,upper
retails.select(col('Description'),lower(col('Description')),upper(col('Description'))).show(5)
```

왜 스파크 사용??
크롤링 Json 하둡에 올려서 스파크가 가공,처리해줌, -> csv,json을 우리가 sql문으로 처리를 해줄뿐
스파크로 좀더 적당한 형태로 db저장 db-> 장고로 시각화 가능 

 ltrim,rtrim,trim,lpad,rpad 

```python
from pyspark.sql.functions import ltrim,rtrim,trim,lpad,rpad 
retails.select(ltrim(lit('     hello     ')).alias('ltrim'),rtrim(lit('     hello     ')).alias('rtrim'),trim(lit('     hello    ')).alias('trim'),lpad(lit('hello'),10,'*').alias('lpad'),rpad(lit('hello'),10,'*')).show()
# lit 리터럴값 으로 바로 컬럼

spark.sql('''
select ltrim('     hello     ') as ltrim , rtrim('     hello     ') as rtrim ,trim('     hello     ') as trim,
lpad('hello',10,'*') as lpad,rpad('hello',10,'*') as rpad
from retails
''').show()
```

regexp_replace 

```python
from pyspark.sql.functions import regexp_replace 
regex_str = 'BLACK|WHITE|RED|GREEN|BLUE'
retails.select(regexp_replace(col('Description'),regex_str,'COLOR').alias('color'),col('Description')).show(5,False)
/# regexp_replace (a,b,c) a의 b를 c로 바꿔달라

spark.sql('''
select regexp_replace(Description,'BLACK|WHITE|RED|GREEN|BLUE','color') as color, Description
from retails
''').show(5,False)
```

translate

```python
from pyspark.sql.functions import translate
retails.select(translate(col('Description'),'ABCD','1234'),col('Description')).show(5,False)
translate(1,2,3) 1컬럼의 2를,3 으로 문자열에 있어도 다 바뀜
```

regexp_extract  정규식 반환

```python
from pyspark.sql.functions import regexp_extract
extract_str = '(BLACK|WHITE|GREEN|BLUE)'
retails.select(regexp_extract(col('Description'),extract_str,1).alias('extract'),col('Description')).show(5,False)
regexp_extract(a,b,c) a의 b를 c개 ??
regexp_extract 패턴에 맞는놈 하나 가져옴



spark.sql("select Description,(instr(Description,'BLACK') >= 1 or instr(Description,'WHITE') >= 1) as has from retails where (instr(Description,'BLACK') >= 1 or instr(Description,'WHITE') >= 1)").show(retails.count(),False)

```

dataframe api 것들임 

시간함수 date

```python
from pyspark.sql.functions import current_date,current_timestamp
date_df = spark.range(10).withColumn('today_date',current_date()).withColumn('now_timestamp',current_timestamp())
date_df.show(5,False)

date_df.createOrReplaceTempView('dateTable')
spark.sql('select * from dateTable').show()  # 제대로 만들어졌나 확인

우분투 날짜가 하루 느림
from pyspark.sql.functions import date_add,date_sub
date_df.select(date_sub(col('today_date'),5),date_add(col('today_date'),5)).show(1)


spark.sql('SELECT DATE_SUB(today_date,5) as sub, DATE_ADD(today_date,5) as add FROM dateTable').show(1)


from pyspark.sql.functions import datediff,months_between,to_date
date_df.withColumn('week_ago',date_sub(col('today_date'),7)).select(datediff(col('week_ago'),col('today_date'))).show(1)
/# datediff 작은날짜 에서 큰날짜 빼줌  


date_df.select(to_date(lit('2022-03-15')).alias('now'),to_date(lit('2022-05-13')).alias('end')).select(months_between(col('now'),col('end'))).show(1)

# /months_between  개월차이


date_df.select(to_date(lit('2022-12-32'))).show(1)  # null

# simpleDateFormat (java)
dateFormat = 'yyyy-MM-dd'
clean_date = spark.range(1).select(to_date(lit('2022-12-31'),dateFormat).alias('date'))
clean_date.show()

dateFormat = 'yyyy-dd-MM'   # 일수먼저 쓰도록 지정가능 근데 출력은 실제 날짜로 나옴
clean_date = spark.range(1).select(to_date(lit('2022-11-12'),dateFormat).alias('date'))
clean_date.show()

spark.range(1).select(to_date(lit('2020-02-29'))).show()
```

 결측치

데이터 프레임 만들기

```python
null_df = sc.parallelize(
[
	Row(name = 'Kang',phone='010-0000-0000',address = 'Seoul'),
	Row(name = 'Shin',phone = '010-1111-1111',address = None),
	Row(name = 'You', phone = None, address = None)
]
).toDF()

// rdd 넣어서 toDF() 로 데이터 프레임으로 바꿈

null_df.show()


null_df.createOrReplaceTempView('nullTable')
spark.sql('select * from nullTable').show()
null_df.show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111|   null|
| You|         null|   null|
+----+-------------+-------+

```

`null_df.createOrReplaceTempView('nullTable')`

coalesce : null이 아닌 첫번째 컬럼 값 출력

```python
from pyspark.sql.functions import coalesce
null_df.select(coalesce(col('address'),col('phone')).alias('coalesce')).show()
+-------------+
|     coalesce|
+-------------+
|        Seoul|
|010-1111-1111|
|         null|
+-------------+
```

'''
ifnull  : 첫번째 값이 null이면 두번째 값 리턴

nullif  : 두값이 같으면 null, 같지 않으면 첫번째값 

nvl    :  첫번째 값이 null 이면 두번째 값 리턴

nvl2   : 첫번째 값이 null 이면 두번째값 리턴 아니면 세번째 값 리턴

'''

```python
spark.sql('''
select ifnull(null,'VALUE') ,NULLIF('SAME','SAME') ,NULLIF('SAME','NOTSAME') ,NVL(NULL,'VALUE'),NVL2(NULL,'VALUE','VALUE2') ,NVL2('NOTNULL','VALUE','VALUE2')
FROM nullTable
''').show(1)
```

 DataFrameNaFunction   na

/# DataFrameNaFunction : drop,fill,replace

```python
null_df.count()
null_df.na.drop().count()  # null있는 row날리기 dropna()같음
null_df.na.drop('any').count()  # any 하나라도 있으면 drop
null_df.na.drop('all').count()   # all 전부다 null이면 날림



>>> null_df.na.drop('all').show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111|   null|
| You|         null|   null|
+----+-------------+-------+

>>> null_df.na.drop('all',subset=['phone']).show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111|   null|
+----+-------------+-------+

>>> null_df.na.drop('all',subset=['address']).show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
+----+-------------+-------+

>>> null_df.na.drop('any',subset=['address']).show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
+----+-------------+-------+

>>> null_df.na.drop('all',subset=['phone','address']).show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111|   null|
+----+-------------+-------+

>>> null_df.na.drop('any',subset=['phone','address']).show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
+----+-------------+-------+

```

subset 으로 필요한 컬럼을 적용시켜줄수있다.

일단 fillna는 null값을  교체하는거

```python
>>> null_df.na.fill('n/a').show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111|    n/a|
| You|          n/a|    n/a|
+----+-------------+-------+

>>> null_df.na.fill('n/a',subset = ['name','address']).show()
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111|    n/a|
| You|         null|    n/a|
+----+-------------+-------+

# 키값으로 컬럼찾고 null을 벨류로 바꿔준다
>>> fill_cols_val = {'phone':'070-000-0000','address':'street'}
>>> null_df.na.fill(fill_cols_val).show()  
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|  Seoul|
|Shin|010-1111-1111| street|
| You| 070-000-0000| street|
+----+-------------+-------+

>>> null_df.na.replace('Seoul','서울','address').show()
null_df.na.replace(['Seoul'],['서울'],'address').show() 
# 그냥 replace랑 무슨차이 ? na?? null값을 바꿔줌 
+----+-------------+-------+
|name|        phone|address|
+----+-------------+-------+
|Kang|010-0000-0000|   서울|
|Shin|010-1111-1111|   null|
| You|         null|   null|
+----+-------------+-------+

```

구조체

구조체 : dataframe 안에 dataframe 

// 여러 컬럼을 묶어서 하나의 컬럼으로 만들어줌

```python
retails.selectExpr('(Description,invoiceNo) as complex','*').show(5,False)
```

```python
from pyspark.sql.functions import struct
complex_df = retails.select(struct('Description','invoiceNo').alias('complex'))
complex_df.createOrReplaceTempView('complexdf')
# 확인
complex_df.show()
spark.sql('select * from complexdf').show()

>>> from pyspark.sql.functions import struct
>>> complex_df = retails.select(struct('Description','invoiceNo').alias('complex'))
>>> complex_df.createOrReplaceTempView('complexdf')
>>> complex_df.select('complex').show(5,False) 
 # ,으로  두개의 컬럼 묶여 있는거임
+---------------------------------------------+
|complex                                      |
+---------------------------------------------+
|{WHITE HANGING HEART T-LIGHT HOLDER, 536365} |
|{WHITE METAL LANTERN, 536365}                |
|{CREAM CUPID HEARTS COAT HANGER, 536365}     |
|{KNITTED UNION FLAG HOT WATER BOTTLE, 536365}|
|{RED WOOLLY HOTTIE WHITE HEART., 536365}     |
+---------------------------------------------+
only showing top 5 rows

>>> complex_df.select('complex.Description').show(5,False)
# 컴플렉스의 디스크립션 몽고db마냥 어디의 뭐 이런식
+-----------------------------------+
|Description                        |
+-----------------------------------+
|WHITE HANGING HEART T-LIGHT HOLDER |
|WHITE METAL LANTERN                |
|CREAM CUPID HEARTS COAT HANGER     |
|KNITTED UNION FLAG HOT WATER BOTTLE|
|RED WOOLLY HOTTIE WHITE HEART.     |
+-----------------------------------+
only showing top 5 rows

>>> complex_df.select(col('complex').getField('invoiceNo')).show(5,False)
# 컴플렉스 필드에서 인보이스
+-----------------+
|complex.invoiceNo|
+-----------------+
|536365           |
|536365           |
|536365           |
|536365           |
|536365           |
+-----------------+
only showing top 5 rows

```

파이썬 기반의 pyspark 니까 split같은 메소드도 있다

```python
>>> from pyspark.sql.functions import split
>>> retails.select(split(col('Description'),' ')).show(5,False)
+------------------------------------------+
|split(Description,  , -1)                 |
+------------------------------------------+
|[WHITE, HANGING, HEART, T-LIGHT, HOLDER]  |
|[WHITE, METAL, LANTERN]                   |
|[CREAM, CUPID, HEARTS, COAT, HANGER]      |
|[KNITTED, UNION, FLAG, HOT, WATER, BOTTLE]|
|[RED, WOOLLY, HOTTIE, WHITE, HEART.]      |
+------------------------------------------+
only showing top 5 rows

>>> retails.select(split(col('Description'),' ').alias('arrays')).selectExpr('arrays[0]').show(5)
+---------+
|arrays[0]|
+---------+
|    WHITE|
|    WHITE|
|    CREAM|
|  KNITTED|
|      RED|
+---------+
only showing top 5 rows

```

size , array_contains

```python
# size 배열의 개수를 리턴해주는 함수
// 배열은 스파크 꺼라서 이렇게 밖에 못함
from pyspark.sql.functions import size
retails.select(size(split(col('Description'),' ')).alias('array_size')).show(5)
+----------+
|array_size|
+----------+
|         5|
|         3|
|         5|
|         6|
|         5|
+----------+

# 해당 글자 포함된거 t,f
from pyspark.sql.functions import array_contains
retails.select(array_contains(split(col('Description'),' '),'WHITE')).show(5)
+------------------------------------------------+
|array_contains(split(Description,  , -1), WHITE)|
+------------------------------------------------+
|                                            true|
|                                            true|
|                                           false|
|                                           false|
|                                            true|
+------------------------------------------------+

```

create_map

 컴플렉스랑 비슷한데 화살표-> 로 되어있고 왼쪽이 키 오른쪽이 벨류 map이라고 부름

```python
>>> from pyspark.sql.functions import create_map
>>> retails.select(create_map(col('StockCode'),col('Description')).alias('complex_map')).show(5,False)
+-----------------------------------------------+
|complex_map                                    |
+-----------------------------------------------+
|{85123A -> WHITE HANGING HEART T-LIGHT HOLDER} |
|{71053 -> WHITE METAL LANTERN}                 |
|{84406B -> CREAM CUPID HEARTS COAT HANGER}     |
|{84029G -> KNITTED UNION FLAG HOT WATER BOTTLE}|
|{84029E -> RED WOOLLY HOTTIE WHITE HEART.}     |
+-----------------------------------------------+

# 컴플렉스 에서 특정 키 가져옴
retails.select(create_map(col('StockCode'),col('Description')).alias('complex_map')).selectExpr("complex_map['84406B']").show()
--------------------+
| complex_map[84406B]|
+--------------------+
|                null|
|                null|
|CREAM CUPID HEART...|
|                null|
# select 에서 고른거랑 출력이랑 살짝 다름

```

사용자 정의 함수

```python
// 스파크 사용자 정의 함수
def power3(value):
...     return value**3

power3(3)
// udf user define functions  # 스파크 함수로 사용하고 싶어서
from pyspark.sql.functions import udf 
pow3 = udf(power3)

// 스파크에 함수저장안됨
user_def_df = spark.range(5,).toDF('num')
user_def_df.select(pow3(col('num')),col('num')).show()
```

조금더 큰 데이터로 집계함수 적용시켜봄

```python
/# 해당 retails 의 csv파일 다 읽음
retails_all = spark.read.format('csv').option('header','true').option('inferSchema','true').load('/home/jaewon/data/retails/*.csv')

retails_all.count()
retails_all.printSchema()

retails_all.createOrReplaceTempView('retailsAll')
retails_all.  + tap + tap  retails_all. 데이터 프레임이 사용할수 있는 모든게 뜸 
retails_all.a +taptap 가능

from pyspark.sql.functions import count
retails_all.select(count('StockCode')).show()
spark.sql("select count(StockCode) from retailsAll ").show()
spark.sql("select count(*) from retailsAll ").show()  # 카운트 null있는거 아니면 * 이거나 값이나 똑같음 


from pyspark.sql.functions import countDistinct
retails_all.select(countDistinct('*').alias('countDistinct')).show()
spark.sql("select count(distinct(*)) as countdistinct from retailsAll").show()


from pyspark.sql.functions import first,last
retails_all.select(first('StockCode'),last('StockCode')).show()

from pyspark.sql.functions import min, max
retails_all.select(min('Quantity'),max('Quantity')).show()


from pyspark.sql.functions import sumDistinct  # 중복제거하고 더하기
retails_all.select(sumDistinct('Quantity')).show()
spark.sql('select sum(distinct(Quantity)) from retailsAll').show()


from pyspark.sql.functions import count,sum,avg,expr


from pyspark.sql.functions import avg
retails_all.select(count('Quantity').alias('countQuantity'),sum('Quantity').alias('sumQuantity'),
avg('Quantity').alias('avgQuantity'),expr('mean(Quantity)').alias('meanQuantity')).show()


'''
분산,표준편차
var_pop : 모집단 분산(모분산)
steddev_pop : 모집단 표준편차 (모표준편차)
var_samp : 표본 분산
stddev_samp : 표본 표준편차
'''

from pyspark.sql.functions import var_pop,stddev_pop, var_samp,stddev_samp
retails_all.select(var_pop('Quantity').alias('varpop'),stddev_pop('Quantity').alias('stddevpop'),
var_samp('Quantity').alias('varsamp'),stddev_samp('Quantity').alias('stddevsamp')).show()

'''
공분산,상관관계
corr : 피어슨 상관관계(DataFrame.corr과 같음)
covar_pop : 모집단 공분산
covar_samp : 표본집단 공분산
'''

from pyspark.sql.functions import corr,covar_pop,covar_samp
retails_all.select(corr('invoiceNo','Quantity').alias('corr'),covar_pop('invoiceNo','Quantity').alias('pop'),covar_samp('invoiceNo','Quantity').alias('samp')).show()


# agg : aggregate
# collect_set   # 중복 x
# collect_list   # 중복 가능

from pyspark.sql.functions import collect_set,collect_list
retails_all.agg(collect_set('Country'),collect_list('Country')).show()

retails_all.groupBy('invoiceNo','CustomerId').count().show()
spark.sql('select invoiceNo,CustomerId,count(*) from retailsAll group by invoiceNo,CustomerId').show()


retails_all.groupBy('invoiceNo').agg(count('Quantity').alias('quan'),expr('count(Quantity) as qquan2')).show()



date_df = retails_all.withColumn('date',to_date(col('InvoiceDate'),'yyyy-MM-dd HH:mm:ss'))
date_df.show()


date_df.createOrReplaceTempView('date_df')
```

파이썬 해석

```python
------------------------------------------------------------------

# 가지고오기
wordcount = sc.textFile("/data/shakespeare.txt")
wordcount.take(10)

# 공백 데이터 제거
wordcount = wordcount.filter(lambda x: len(x) > 0)
wordcount.take(10)

# 문자가 아닌것으로 자르기 (전체 적용)
wordcount = wordcount.flatMap(lambda x: re.split("\W+", x))
wordcount.take(10)
wordcount.count()

# 공백 데이터 제거
wordcount = wordcount.filter(lambda x: len(x) > 0)
wordcount.count()

# (단어, 1) 형태로 변경
wordcount = wordcount.map(lambda x: (x.lower(), 1))
wordcount.take(10)

# 같은 키 값 기준으로 뒤의 숫자 더하기
wordcount = wordcount.reduceByKey(lambda x, y: x + y)
wordcount.take(10)

# (단어, 숫자) => (숫자, 단어) 형태로 변환
wordcount = wordcount.map(lambda x:(x[1], x[0]))
wordcount.take(10)

# 내림차순 정렬
wordcount = wordcount.sortByKey(ascending=False)

# persist() : 메모리에 올려놓고 작업하겠다.


----------------------------------------------------------------
```

윈도우 함수

```python
/# 윈도우 함수
from pyspark.sql.window import Window
from pyspark.sql.functions import desc

window_function = Window.partitionBy('CustomerId','date').orderBy(desc('Quantity')).rowsBetween(Window.unboundedPreceding,Window.currentRow)

max_quantity = max(col('Quantity')).over(window_function)

from pyspark.sql.functions import dense_rank,rank

win_dense_rank = dense_rank().over(window_function)
win_rank = rank().over(window_function)

date_df.where('CustomerId IS NOT NULL').orderBy('CustomerId').select(col('CustomerId'),col('date'),col('Quantity'),win_rank.alias('quantityRank'),win_dense_rank.alias('quantityDense'),max_quantity.alias('quantityMax')).show()

```



리눅스는 파일의 확장자가 그리 중요하지는 않다

#### 파일 load와 save

```python
# csv 
csv_file01 = spark.read.format('csv').option('header','true').load('/home/jaewon/data/flights/csv/2010-summary.csv')
or
csv_file02 = spark.read.option('header','true').csv('/home/jaewon/data/flights/csv/2010-summary.csv')

이거 파일로 저장
csv_file02.write.format('csv').mode('overwrite').save('/tmp/csv')
hdfs dfs -ls /tmp/csv  # 우분투에서 하는거
Found 2 items
-rw-r--r--   1 jaewon supergroup          0 2022-03-15 17:15 /tmp/csv/_SUCCESS
-rw-r--r--   1 jaewon supergroup       7077 2022-03-15 17:15 /tmp/csv/part-00000-69ec6f75-badf-480b-8573-6f0fb8b117ec-c000.csv

// 뭔진 모르겠는데 해당 경로의 파일내용좀 보여줘 
hdfs dfs -cat /tmp/csv/*.csv
 
# dataframewrite.mode : append,overwrite, error/errorifexists,ignore

json_file01 = spark.read.format('json').load('/home/jaewon/data/flights/json/2010-summary.json')
# json_file02

// 하둡 저장 왜??  클러스터 매니저 yarn 
스파크 클러스터 설정해주고있는 넘이 yarn임 
json_file01.write.format('json').mode('append').save('/tmp/json')

~$ : hdfs dfs -ls /tmp/json
Found 2 items
-rw-r--r--   1 jaewon supergroup          0 2022-03-15 17:24 /tmp/json/_SUCCESS
-rw-r--r--   1 jaewon supergroup      21353 2022-03-15 17:24 /tmp/json/part-00000-f44ac2de-eb6f-4ffd-b734-d3d97f252575-c000.json
```

// 뭔진 모르겠는데 해당 경로의 파일내용좀 보여줘 
`hdfs dfs -cat /tmp/csv/*.csv`  형태 알고있어야함 

'''
그외!
parquet : spark 컬럼 기반 데이터 저장 방식
orc : 하둡 컬럼 기반 데이터 저장 방식
text 파일로도 저장 가능
db 연동해서 저장 할수도있음

'''

네임노드 = 데이터 노드 관리,클라이언트한테 요청을 받고 data node에 일을 시킴
데이터 노드에서 끌어와서 응답을 주기도함 
core-site 에  value로 준 9000번 포트가 네임 노드임 

네임노드 클라이언트  마스터
세컨더리 네임노드  대체 네임노드
데이터 노드 데이터 저장 슬레이브



// 기존 csv파일 리드 해서 컬럼 변경 하고 저장한 이후에 다시 불러와서 사용해보기 연습 

```python
>>> csv_file02 = spark.read.option('header','true').csv('/home/jaewon/data/flights/csv/2010-summary.csv')
>>> csv_file02.show(5)
+-----------------+-------------------+-----+
|DEST_COUNTRY_NAME|ORIGIN_COUNTRY_NAME|count|
+-----------------+-------------------+-----+
|    United States|            Romania|    1|
|    United States|            Ireland|  264|
|    United States|              India|   69|
|            Egypt|      United States|   24|
|Equatorial Guinea|      United States|    1|
+-----------------+-------------------+-----+
only showing top 5 rows

>>> csv_file02.select('DEST_COUNTRY_NAME','ORIGIN_COUNTRY_NAME')
DataFrame[DEST_COUNTRY_NAME: string, ORIGIN_COUNTRY_NAME: string]
>>> csv_fix = csv_file02.select('DEST_COUNTRY_NAME','ORIGIN_COUNTRY_NAME')
>>> csv_fix.show(5)
+-----------------+-------------------+
|DEST_COUNTRY_NAME|ORIGIN_COUNTRY_NAME|
+-----------------+-------------------+
|    United States|            Romania|
|    United States|            Ireland|
|    United States|              India|
|            Egypt|      United States|
|Equatorial Guinea|      United States|
+-----------------+-------------------+
only showing top 5 rows

>>> csv_fix.write.format('csv').mode('overwrite').save('/tmp/csv')
>>> csv_file = spark.read.option('header','true').csv('/tmp/csv/*.csv')
>>> csv_file.show(5)
+-----------------+-------------+
|    United States|      Romania|
+-----------------+-------------+
|    United States|      Ireland|
|    United States|        India|
|            Egypt|United States|
|Equatorial Guinea|United States|
|    United States|    Singapore|
+-----------------+-------------+
only showing top 5 rows

```

// json 파일도 해보자

```python
json_file01 = spark.read.format('json').load('/home/jaewon/data/flights/json/2010-summary.json')
# 저장
json_file01.write.format('json').mode('append').save('/tmp/json')

json_file02 = spark.read.option('header','true').json('/home/jaewon/data/flights/json/2010-summary.json')

file02 = json_file02.select('DEST_COUNTRY_NAME','ORIGIN_COUNTRY_NAME')
# 내용 바꿔서 저장
file02.write.format('json').mode('append').save('/tmp/json/')
```

결과는 위csv랑 똑같은데 이번에는 mode의 차이를 보여주고자 한다

### save/load mode 

dataframewrite.mode : append,overwrite, error/errorifexists,ignore

![image-20220316202202471](README.assets/image-20220316202202471.png)

csv 파일 같은 경우는 **overwrite** 모드를 사용해서 파일이 한개 밖에 없지만 

![image-20220316202234658](README.assets/image-20220316202234658.png)

json 파일 같은 경우는 **append**를 사용해서 파일이 추가가된 모습

![image-20220316202223867](README.assets/image-20220316202223867.png)



![image-20220316100338530](README.assets/image-20220316100338530.png)

파란색 이 디렉토리이고 파란색 눌러서 경로를 찾을수 있다.

'''

그외!

parquet : spark 컬럼 기반 데이터 저장 방식

orc : 하둡 컬럼 기반 데이터 저장 방식

text 파일로도 저장 가능

db 연동해서 저장 할수도있음

'''



retails 로 다시연습

이번엔 rollup , cube 

```python
retails = spark.read.format('csv').option('header','true').option('inferSchema','true').load('/home/jaewon/data/retails/2010-12-01.csv')

from pyspark.sql.functions import to_date,col 
date_df = retails.withColumn('date',to_date(col('invoiceDate'),'yyyy-MM-dd HH:mm:ss'))  # withColumn 컬럼추가


notnull_df = date_df.drop()
notnull_df.createOrReplaceTempView('notnullDf')


spark.sql('''
select CustomerID,StockCode,sum(Quantity)
from notnullDf
group by CustomerID, StockCode
order by CustomerID desc, StockCode desc
''').show()

from pyspark.sql.functions import sum
rollup_df = notnull_df.rollup('Date','country').agg(sum('Quantity')).selectExpr('Date','Country',"`sum(Quantity)` as total_quantity").orderBy('Date')


rollup_df.where('Country IS NULL').show()
a집계
전체 집계 


cube
notnull_df.cube('Date','Country').agg(sum(col('Quantity'))).select('Date','Country','sum(Quantity)').show()
```

### join

새테이블 생성

```python
person = spark.createDataFrame(
[
	(1,'shin dongyep',2,[1]),
	(2,'seo janghun',3,[2]),
	(3,'you jaeseok',1,[1,2]),
	(4,'kang hodong',0,[0])
]
).toDF('id','name','program','job')


program = spark.createDataFrame(
[
	(1,'MBC','놀면 뭐하니'),
	(2,'KBS','불후의 명곡'),
	(3,'SBS','미운 우리 새끼'),
	(4,'JTBC','뭉쳐야 찬다')
]
).toDF('id','broadcaster','program')

job = spark.createDataFrame([(1,'main mc'),(2,'member')]).toDF('id','job')


person.createOrReplaceTempView('person')
program.createOrReplaceTempView('program')
job.createOrReplaceTempView('job')
```

// 같은 조건으로 조인

````python
person.join(program,person['program'] == program['id']).show()
spark.sql('select * from person join program on(person.program = program.id) ').show()

conditions = person.program == program.id 
person.join(program,conditions).show() 

person.join(program,conditions,'inner').show()

person.join(program,conditions,'outer').show()
spark.sql('select * from person full outer join program on(person.program = program.id)').show()

person.join(program,conditions,'left_outer').show()
person.join(program,conditions,'right_outer').show()
````

// 세미조인

```python
person.join(program,conditions,'left_semi').show()  # inner join 테이블에서 왼쪽만 남김 

person.join(program,conditions,'left_anti').show()  # inner join 에서 포함 안된 row

person.join(program,conditions,'cross').show()  # 카티시안 곱  , 아래랑 살짝 다름 왜? conditions 조건 잡아서 

person.join(program, how = "cross").show()
// how 이거 자체는 파이썬 

select *
from person,program 
where persos.program = program.id 


person.crossJoin(program).show()
```



// 서브 쿼리

```python
// person job 연결
person.join(job,person.id == job.id).show()
spark.sql('select * from person join job using(id)').show()

// array_contains  : array_contains(arr, tgt): arr 배열에 tgt이 존재하는지 확인
from pyspark.sql.functions import expr
person.join(job,expr('array_contains(job,id)')).show()  # job이 여러개라서 안되니까 이름 바꿔서
person.withColumnRenamed('id','num').withColumnRenamed('job','role').join(job,expr('array_contains(role,id)')).show()


### subquery를 사용하여 sbs 에서 프로그램을 하고있는 사람을 출력하자 
spark.sql('select name from person where (select broadcaster from program where broadcaster in (SBS))').show() 

spark.sql('''
select *
from person
where program = 
	(select id 
	from program
	where broadcaster in ('SBS'))   
''').show()
# where broadcaster = 'SBS'
```



## Spark streaming 스파크 스트리밍

vim streaming_test.py 여기에 작성

```python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

가져온거 쪼개기
# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

가져온거 실행
# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()

ssc.start()             # Start the computation  실행
ssc.awaitTermination()  # Wait for the computation to terminate 기다림
```

그뒤 터미널에서

9999포트로 스트리밍 서버 열음
 nc -lk 9999

new_window

submit으로 파이썬 파일 실행
spark-submit streaming_test.py localhost 9999

그후 다른 창에서 내가 넣어주는 값들 출력됨

// 스트리밍은 계속 동작하고 있으면서 입력을 받아준다.

스파크 sql 다시 연습

pyspark

```terminal
cat all.csv

hdfs dfs  -put ./all.csv /home/jaewon/all.csv    # 하둡에 파일올리기

hdfs dfs -ls /home/jaewon  # 잘 올라갔나 확인


pyspark

저장한 파일 가져옴 
multi = spark.read.format('csv').option('header','true').load('/home/jaewon/all.csv')

multi.count()
multi.createOrReplaceTempView('multi')

//  채팅을 많이 보낸 사람 순서대로 정렬  chat_from 
***** group by 로 카운트 하면 됨..
from pyspark.sql.functions import col
multi.groupBy('chat_from').count().orderBy(col('count').desc()).show()

// ??? 강사 에게 dm을 가장 많이 보낸사람
multi.where(col('chat_to') ==  "???강사").groupBy('chat_from','chat_to').count().orderBy(col('count').desc()).show()


// 시간별 채팅 횟수
from pyspark.sql.functions import substring
multi.groupBy(substring('chat_time',1,2)).count().orderBy(substring('chat_time',1,2)).show()
spark.sql('select substr(chat_time,1,2),count(*) from multi group by substr(chat_time,1,2) order by substr(chat_time,1,2) asc').show()

// 날짜별 채팅 횟수

multi.groupBy(col('chat_date')).count().orderBy(col('chat_date')).show()
spark.sql('select chat_date , count(*) from multi group by chat_date order by chat_date').show()


// 날짜와 시간별 채팅 횟수
rollup?
multi.groupBy('chat_date',substring('chat_time',1,2)).count().orderBy('chat_date',substring('chat_time',1,2)).show()

// 시간별 채팅한 사람
hour_chat = multi.groupBy(substring('chat_time',1,2).alias('hour'),'chat_from').count().orderBy(substring('chat_time',1,2),col('count').desc())
hour_chat.show()

hour_chat.write.format('csv').mode('overwrite').save('hour_chat')
hour_chat 저장
rdd 파티션 엄청  나눠짐

# coalesce(1) 하나로 합쳐라
hour_chat.coalesce(1).write.format('csv').mode('overwrite').save('/home/jaewon/hour_chat')
```

# 파이썬 파일로 실행하기

vim hour_chat.py

```terminal
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,substring
# 이파일 스파크로 동작 
# 스파크 세션 만드는데 클러스터 매니저는 yarn이고 이름지정해줌 
spark = SparkSession.builder.master("yarn").appName("hour_chat").getOrCreate() 
multi = spark.read.format('csv').option('header','true').load('/home/jaewon/all.csv')
hour_chat = multi.groupBy(substring('chat_time',1,2).alias('hour'),'chat_from').count().orderBy(substring('chat_time',1,2),col('count').desc())

hour_chat.coalesce(1).write.format('csv').mode('overwrite').save('/hour_chat')

:wq!
```

터미널 동작

```terminal
#pip install pyspark   python 명령어도 pyspark로 동작하게하고 싶어서
python hour_chat.py 
spark-submit hour_chat.py  # 위와 동일하게 동작 

hdfs dfs -cat /hour_chat/*.csv
```

# 쉘 스크립트

```terminal
.sh == 쉘스크립트 
vim multi.sh 

start-all.sh

sleep 20   

pyspark

:wq!

sudo chmod 755 multi.sh

ls -l | grep multi.sh   # multi.sh 파일의 상세정보만

./multi.sh
이 쉘스크립트 명령어는 하둡과 pyspark 를 자동으로 실행
```

`hdfs dfs -rmr 경로` 는 하둡에서폴더삭제





# zeppelin 

다운받고 

```
wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-netinst.tgz
```

압축해제 및 심볼링크 만들기 

```scala
tar -xvzf zeppelin-0.10.1-bin-netinst.tgz 
ln -s zeppelin-0.10.1-bin-netinst zeppelin
```

```terminal

source ~/.bashrc


cd $ZEPPELIN_HOME/conf


cp zeppelin-env.sh.template zeppelin-env.sh


vim zeppelin-env.sh

19 
export JAVA_HOME=/home/jaewon/java

79
export SPARK_HOME=/home/jaewon/spark

89
export HADOOP_CONF_DIR=/home/jaewon/hadoop/etc/hadoop
:wq!
```



`cp zeppelin-site.xml.template zeppelin-site.xml`

vim zeppelin-site.xml

```html
<property>
  <name>zeppelin.server.addr</name>
  <value>127.0.0.1</value>  # 127.0.0.1 내부에서만 접속 // 0.0.0.0 어디서든 접속 가능
  <description>Server binding address</description>
</property>

<name>zeppelin.server.port</name>
  <value>8082</value>  # 포트 다른애들이 많이 쓰는 포트라서 8080->8082 로 바꿈
<description>Server port.</description>
:wq!
```

~

재플린 실행

```terminal
start-all.sh
zeppelin-daemon.sh start  # 재플린 구동

localhost:8082 # 설정한 포트에서 확인 가능 
계정에 인터프린터
spark 검색
spark %spark , %sql , %pyspark , %ipyspark , %r , %ir , %shiny , %kotlin    // 동작 명령어 

#  anonymous -> interpreter -> spark 검색 -> edit
spark.master  		yarn
spark.submit.deployMode   client
# save


새로운 노트북 파일 만들어줌
주피터 노트북에서 스파크 쓰는 느낌

%pyspark

test = [1,2,3,4,5]
test_rdd = sc.parallelize(test)

test_rdd.collect()
[1, 2, 3, 4, 5]


zeppelin-daemon.sh stop  # 중지
stop-all.sh
```



# mysql

--- mysql 설치

```terminal
sudo apt install mysql-server -y


sudo service mysql start


sudo mysql_secure_installation 
n
1234
1234
y
n
y
y


cd /etc/mysql/mysql.conf.d

sudo vim mysqld.cnf
bind-address            = 217.0.0.1     -> 0.0.0.0
mysqlx-bind-address     = 127.0.0.1  -> 0.0.0.0   외부에서 접속 가능하게 잡아줌 

원래대로 라면 내가 사용할 ip만 접속하게 해줘야함 

~
# 실행 
sudo mysql -u root -p

show databases;
use mysql;

alter user 'root'@'localhost' identified with mysql_native_password by '1234';
CREATE USER 'root'@'%' IDENTIFIED BY '1234';
sudo 없이 사용하도록
'root'@'%' root 의 어떤 ip든 사용가능

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;  # 모든 권한 root@localhost 에줌
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

flush privileges; # 저장

CREATE TABLE test(id int, name VARCHAR(30));

INSERT INTO test VALUES(1, "hadoop");
INSERT INTO test VALUES(2, "spark");

select * from test;  # 만들어진거 확인

# mysql spark 연결 할려면 자바 가상머신 연결해주는 드라이버가 필요함 

wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java_8.0.28-1ubuntu20.04_all.deb


sudo dpkg -i mysql-connector-java_8.0.28-1ubuntu20.04_all.deb


cd /usr/share/java/
# /usr/share/java/mysql-connector-java-8.0.28.jar  // 드라이버 경로 스파크랑 sql 연결하는 드라이버

스파크 설정 경로
cd $SPARK_HOME/conf

vim spark-defaults.conf
맨 밑
spark.jars                              /usr/share/java/mysql-connector-java-8.0.28.jar

지금 재플린 노트북으로도 가능하긴함 

pyspark 에서 
mysql 비번 root에 요청


spark 에서

user='root'
password='1234'    
url="jdbc:mysql://localhost:3306/mysql"
driver = 'com.mysql.cj.jdbc.Driver'
dbtable='test'

test_df = spark.read.format('jdbc').option('user',user).option('password',password).option('url',url).option('driver',driver).option('dbtable',dbtable).load()
test_df.show()

test_insert = [(3,'mysql'),(4,'zeppelin')]
insert_df = sc.parallelize(test_insert).toDF(['id','name'])

insert_df.write.jdbc(url,dbtable,'append',properties={'driver':driver,'user':user,'password':password})


```



# MongoDB

하둡 안켜도 접속 가능

몽고디비 다운  https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

```terminal
// 1
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
// 2
20.04
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
// 3
sudo apt-get update
sudo apt-get upgrade -y
// 4
다운
sudo apt-get install -y mongodb-org
//5 실행
sudo systemctl start mongod
// sudo service mongod start   # 이것도 가능
sudo service mongod status  # 현재 몽고서버 확인 가능 

mongo # 실행키


# 중지
sudo systemctl stop mongod
sudo service mongod stop

# 재실행
sudo service mongod restart

db.test.insertOne({'id':'10','name':'mongodb'})
db.test.find()

exit
```

mongodb test 데이터베이스 사용
만일 데이터베이스를 계속 바꿔야 하는 상황이라면
해당 설정 안하고
코드에서 옵션으로 바꿔야함 

`cd $SPARK_HOME/conf`

`vim spark-defaults.conf`

```terminal
spark.mongodb.input.uri		mongodb://localhost/test
spark.mongodb.output.uri		mongodb://localhost/test
# spark.jar.packages			org.mongodb.spark:mongo-spark-connector_2.12:3.0.1    안먹힘
# jars ??? 로 하면 먹힘 
# spark.jars.packages			org.mongodb.spark:mongo-spark-connector_2.12:3.0.1

// 대신 해당 디펜더스 설치후 실행  jars들 가져와서 한번에 실행
pyspark --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.1  

몽고디비 내용 가져오기
test = spark.read.format('mongo').option('database','test').option('collection','test').load()
mongo 형태를 test db에 test coll 가져옴  

insert_df = spark.createDataFrame([('11','mongo-spark')],['id','name'])

insert_df.write.format('mongo').option('database','test').option('collection','test').mode('append').save()
기존 몽고 디비 데이터에 추가됨



```



# webhdfs

**새로 깔았는데 어째선지 home이 아니라 user이다 이거 유의할것**

직접 쓸때는 장고에 ajax를통한 url 전달

하둡경로로 쓰는거

curl -s http://127.0.0.1:9870/webhdfs/v1/user/jaewon/?op=LISTSTATUS

해당경로에 상태확인 

2.9대 버전까지는 port가 50070이었으나 3.x대 부터는 9870으로 바뀌었다.

3.대 버전부터는 따로 주소 지정안해줘도된다 



datanode 포트 확인

jps 에서 번호 확인

sudo apt install net-tools  // netstat 다운

netstat -v  버전확인

netstat -antup | grep LISTEN | sort -n

## webhdfs를 이용한 파일 업로드

post ? ,get,put 중에 하나를 연습해봄

curl -i -X POST "http://127.0.0.1:9870/webhdfs/v1/user/jaewon/data?op=APPEND"

POST는 Forbidden 에러로 안되니 PUT으로 해보자 

put도 안됐고



GET 방식은 되는데 POST나 PUT이 안됨 

get은 되니 webhdfs의 문제는 아니라고 생각해서 403에러인 권한 설정을 더 찾아봤다

**HADOOP 파일 접근권한과 append기능을 사용할수있게 hdfs-site.xml에 권한변경을 해줌**

```python
<property>

    <name>dfs.webhdfs.enabled</name>
    <value>true</value>

</property>
<property>
    <name>dfs.support.append</name>
    <value>true</value>
</property>

<property>
    <name>dfs.permissions</name>
    <value>false</value>
</property>

```

이후 하둡 재시작

PUT의 CREATE

curl -i -X PUT "http://localhost:9870/webhdfs/v1/home/jaewon/test.txt?op=CREATE"
HTTP/1.1 307 Temporary Redirect

```PYTHON
curl -i -X PUT -T ./test.txt "http://ubuntu:9864/webhdfs/v1/home/jaewon/test.txt?op=CREATE&namenoderpcaddress=localhost:9000&createflag=&createparent=true&overwrite=false"
HTTP/1.1 100 Continue

HTTP/1.1 201 Created
Location: hdfs://localhost:9000/home/jaewon/test.txt
Content-Length: 0
Access-Control-Allow-Origin: *
Connection: close

# 이후 하둡에 잘 들어간것을 확인
```

![image-20220411150101226](README.assets/image-20220411150101226.png)

POST 의 APPEND

curl -i -X POST "http://localhost:9870/webhdfs/v1/home/jaewon/test.txt?op=APPEND"
HTTP/1.1 307 Temporary Redirect

```PYTHON
curl -i -X POST -T /home/jaewon/test.txt "http://ubuntu:9864/webhdfs/v1/home/jaewon/test.txt?op=APPEND&namenoderpcaddress=localhost:9000"
HTTP/1.1 100 Continue

HTTP/1.1 200 OK
Content-Length: 0
Connection: close

# APPEND는 TXT파일같은경우 원래 파일의 새로운 내용을 추가 덮어씌우기는 아님 
```

![image-20220411150112695](README.assets/image-20220411150112695.png)

똑같은 text가 추가가된 모습

webhdfs 같은경우 소유자가 dr.who 라고 나옴

-rw-r--r--   1 dr.who supergroup         26 2022-04-10 22:54 /home/jaewon/test.txt
-rw-r--r--   1 jaewon supergroup      21158 2022-04-10 05:52 /home/jaewon/wwww.png

기존 wwww.png파일 hdfs dfs -rm 으로 지우고 webhdfs로 다시 해보자

이미지 파일인 png도 넣어봄

-rw-r--r--   1 dr.who supergroup         26 2022-04-10 22:54 /home/jaewon/test.txt
-rw-r--r--   1 dr.who supergroup      21158 2022-04-10 23:05 /home/jaewon/wwww.png

소유자가 바뀌었지만 bin데이터로 잘들어간 모습 



중요한건 장고에서 이미지를 다운해야 하기 때문에 

curl -i -L -o- "http://localhost:9870/webhdfs/v1/home/jaewon/wwww.png?op=OPEN"

의 Location:http://ubuntu:9864/webhdfs/v1/home/jaewon/wwww.png?op=OPEN&namenoderpcaddress=localhost:9000&offset=0

을 브라우저에 url에 입력을 하면 바로 다운이 된다 문제는  저장되는 이미지의 파일 경로를 어디로 해줄수있느냐가 될것같다 

아니 저장이 필요없나? 하둡에서 바로 장고로 이미지로를 불러줄수있다면 상관 없을거 같다 



#### pywebhdfs 는 모듈이라 직접 해볼것 

pywebhdfs 쓰니까 한번에됨... 내 하루는 어디로 갔는지

vim pyweb.py

**create_file**

```python
from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='127.0.0.1',port='9870',user_name='jaewon')
my_data = '01010101010101010101010101010101'
my_file = '/home/jaewon/test.txt'
hdfs.create_file(my_file, my_data,overwrite=True)
# 하지만 옮기는게 아니라 완전히 새로 만든는것
```

**append_file**

결국필요한 요청은 이미지파일 이기에 이미지를 이진수로 열어서 보내줌 

```python
from pywebhdfs.webhdfs import PyWebHdfsClient


with open('/home/jaewon/wwww.png','rb') as f:
    data = f.read()

hdfs = PyWebHdfsClient(host='127.0.0.1',port='9870',user_name='jaewon')
my_data = data
my_file = '/home/jaewon/wwww.png'
hdfs.create_file(my_file, my_data,overwrite=True)

```

잘 올라간거 확인

**read_file**

다운받을때 이진수 형태로 바꿔줘서 다운해줌 

```python
from pywebhdfs.webhdfs import PyWebHdfsClient


hdfs = PyWebHdfsClient(host='127.0.0.1',port='9870',user_name='jaewon')

my_file = '/home/jaewon/wwww.png'

image = hdfs.read_file(my_file)

# print(image)

with open('/home/jaewon/wwww2.png','wb') as f:
    f.write(image)
```

 

REST API

요청할때는 GET 방식으로 요청 뭔가 저장하고싶으면 POST방식으로 요청

무언가 수정하고싶다 PUT/PATCH

삭제 DELETE

403 이면 권한

하둡의 사용권한

bashrc 랑 권한일아 다름 

하둡 네임노드 데이터 노드 

세컨더리 네임노드 네임노드관련 정보들 폴더가 어떻게 만들어지고 

~~만들어졌습니다 

완전분산모드 

포멧하면 네임노드따라 데이터노드 따로 

주키퍼
하둡으로 따지면 네임,데이터노드
주키퍼 -> 네임노드 같은놈

--------------------------------------------------------------------------------

주키퍼
하둡으로 따지면 네임,데이터노드
주키퍼 -> 네임노드 같은놈

서버비가 없다
서버 4개가 없다
컴퓨터도 없다
돈이 없다 
실시간 처리를 위해 주키퍼에 카프카 설치
특성상 제공 인스턴스가 하나였다

----------------------------------------------------------------------------------------------------

# Airflow_Error



airflow 설정에러

```terminal
airflow db init
ModuleNotFoundError: No module named '_cffi_backend'
jaewon@ubuntu:~$ python -m pip install cffi

```

bash: airflow dags test air01 2022-04-15



task볼려면 실행된 dag_id나  날짜 누르고 네모 -> log네모



포트번호 겹칠 때

```terminal
airflow.cfg 에서 

486
base_url = http://localhost:포트번호
바꿔주기 

479
web_server_port = 8081

```



자꾸 sqllite를 지정해서 mysql을 지정하게 airflow.cfg를 바꿔줌 31

```terminal
sql_alchemy_conn =  mysql://root:1234@localhost:3306/airflow
```

airflow 에서 mysql 쓸려는데 안됨

```terminal
compilation terminated.
      error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> mysqlclient

```

```terminal
sudo apt-get install gcc -y
sudo apt-get install python3-dev -y

error: subprocess-exited-with-error
× python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [44 lines of output]
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for mysqlclient
  Running setup.py clean for mysqlclient
Failed to build mysqlclient
Installing collected packages: mysqlclient
  Running setup.py install for mysqlclient ... error
  error: subprocess-exited-with-error
  
  × Running setup.py install for mysqlclient did not run successfully.
  │ exit code: 1
  ╰─> [44 lines of output]

```

새로운 에러 발생

```terminal
sudo apt-get install python3-dev
sudo apt-get upgrade # 업그레이드 안된게 많아서 해줌

sudo apt --fix-broken install
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/libpython3.7-stdlib_3.7.13-1+focal3_amd64.deb
: Sub-process /usr/bin/dpkg returned an error code (1) 

마지막 에러 그이후 
pip install mysqlclient
ModuleNotFoundError: No module named '_sysconfigdata_m_linux_x86_64-linux-gnu'
심볼링 써봤으나 해결안됨
sudo ln -s   /usr/lib/python3.7/_sysconfigdata__linux_x86_64-linux-gnu.py  /usr/lib/python3.7/_sysconfigdata__x86_64-linux-gnu.py
ln: failed to create symbolic link '/usr/lib/python3.7/_sysconfigdata__x86_64-linux-gnu.py'

# sub-process 부터 해결해야함 
```

시도

```terminal
udo apt --fix-broken install  # 이후
The following additional packages will be installed:
  libpython3.7-stdlib
The following packages will be upgraded:
  libpython3.7-stdlib
# 에있는 libpython3.7-stdlib 삭제

sudo apt remove libpython3.7-stdlib # fix-broken 하라고함

# 수동 삭제 (일시적으로 이동시킴)
jaewon@ubuntu:~$ ls -l /var/lib/dpkg/info | grep -i libpython3.7-stdlib
-rw-r--r-- 1 root root   14454 Mar 31 19:34 libpython3.7-stdlib:amd64.list
-rw-r--r-- 1 root root   24005 Mar 16 10:35 libpython3.7-stdlib:amd64.md5sums
-rwxr-xr-x 1 root root    1155 Mar 16 10:35 libpython3.7-stdlib:amd64.prerm
jaewon@ubuntu:~$ sudo mv /var/lib/dpkg/info/libpython3.7-stdlib:amd64.* /tmp

## -fix-broken로 재설치 안됨  다시 원상복구 시킴 

```

시도2

```terminal
sudo dpkg -i --force-overwrite /var/cache/apt/archives/libpython3.7-stdlib_3.7.13-1+focal3_amd64.deb
이후
sudo apt -f install
sudo apt autoremove
이후
pip install mysqlclient
# 처음 문제는 해결 이후 
ModuleNotFoundError: No module named 'distutils.cmd'
에러 발생

sudo apt-get install python3-distutils # 해결 안됨 
sudo apt-get install python3.7-distutils # 버전지정후 distutils.cmd는 해결

```

다시 에러

```terminal
MySQLdb/_mysql.c:46:10: fatal error: Python.h: No such file or directory
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> mysqlclient

```

```terminal
파이썬 dev에 대한 파일과 lib 다운 안되어있다고 생각 다시 다운 시도
sudo apt-get install python3.7-dev
# 무사히 다운 성공!
Successfully built mysqlclient
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.1.0
```

### airflow mysql 연결

```terminal
ERROR - DB Creation and initialization failed: (MySQLdb._exceptions.OperationalError) (1049, "Unknown database 'airflow  #sqlite:////home/jaewon/airflow/airflow.db'")
(Background on this error at: http://sqlalche.me/e/13/e3q8)

```

에러 발생으로 다시 연결 (원래 잘됐었는데.....)

```terminal
pip3 install 'apache-airflow[mysql]'
```

에러 원인 찾음

```terminal
(1049, "Unknown database 'airflow  #sqlite:////home/jaewon/airflow/airflow.db'")

원래 설정이 sqllite로 되어있어 되던거였음 mysql에서 airflow라는 데이터 베이스를 찾지 못한거 같다 설정을 바꿨는데 디비를 만들어 주던가 지정된 디비를 프로젝트 디비명으로 바꿔주던가 해야할듯 
```

airflow.cfg 재설정

```terminal
sql_alchemy_conn =  mysql://root:1234@localhost:3306/fish
# sqllite설정 안지우려고 '#' 남겨뒀었는데 그러면 그 부분까지 DB이름으로 지정함 그래서 한줄 아래로 내려줌 DB를 airflow에서 fish로 바꿔주는건 맞는 선택이였음
~ airflow db init
```



### 실행중 에러

```terminal
airflow dags test kafka 2022-05-31 # 이후로는 웹에서 진행함

명령어로 실행 


During handling of the above exception, another exception occurred:

Message: 'Failed to execute task: %s.'
Arguments: ("\x1b[1mHTTPConnectionPool(host='localhost', port=9870): Max retries exceeded with url: /webhdfs/v1/?user.name=jaewon&op=GETHOMEDIRECTORY (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fec73785a50>: Failed to establish a new connection: [Errno 111] Connection refused'))\x1b[22m",)


hdfs.util.HdfsError: Failed to find datanode, suggest to check cluster health. excludeDatanodes=null

# 하둡 재시작 해보니 잘됨
# insert_mysql 에서도 에러가 발생하는데 하둡 파일정리한다고 파일 지워서 그런듯 다시만들어줌 그러니 해결 

# 에러발생 너무크거나 순서가 맞지 않을때? 그러나 sql부분만 해보면 문제없이 돌아감
MySQLdb._exceptions.OperationalError: (2013, 'Lost connection to MySQL server during query')

import MySQLdb # 이거 필요없는거라 한번 지우고 시도해봄  
# 안됨
```

`pip apache-airflow-providers-apache-spark`

 airflow에서 spark쓸려면 필요하다고함 ;

```python
SparkSubmitOperator # airflow와 spark의 연결은 sparksubmitoperator 필요함 그래서 해봤는데 

# 에러발생
ERROR - Failed to execute job 41 for task spark_submit_task (Cannot execute: spark-submit --master yarn --name arrow-spark /home/jaewon/airflow/dags/using_sql.py. Error code is: -9.; 18031)

# 되던것도 안됨 다른문젠가... 

airflow 에서 spark 세션 연결해서 mysql 이 원래 되던 파일이 있는데 kafka쪽 코드 돌리고 나면 똑같이 안됨
아마 pip hdfs를 사용했는데 이거 다음에 spark로 hadoop data꺼내오는게 안되는거 같음

아님
# 아님

spark구문에 첫번째는 실행됨 다른 문제같음 

```



고생한거에 비해 남는 메시지는 별로 없다...

?? sql 구문 코드만 따로 돌려봤는데 잘됨 

근데왜 합치면 그부분에서 에러가 날까?



따로 파이선 코드로 돌리면 잘됨 



계속 똑같은 에러

근데 됐다가 안됐다가함 왜일까..? 일단 한번 성공시켜보자 

```
2022-06-02, 06:09:49 UTC] {standard_task_runner.py:98} ERROR - Failed to execute job 70 for task spark_submit_task (Cannot execute: spark-submit --master yarn --name arrow-spark /home/jaewon/airflow/dags/using_sql.py. Error code is: -9.; 14619)


During handling of the above exception, another exception occurred:

Exception Handling이란? : 정상적인 프로그램 흐름을 중단하고 주변의 컨텍스트 또는 코드 블록에서 계속하기위한 메커니즘
```

예외 처리중 또다른 예외 발생....... 대체 무슨 예외?? 

### 마지막 문제 원인 찾은거 같음 (메모리 부족..)

```terminal
py4j.protocol.Py4JNetworkError: Answer from Java side is empty

# 중간중간에 나오는 에러.... 다른것만 찾아보다가 처음 찾아봤는데 메모리 에러라는 말이 있다.. 4gb가 넘게 있는데 벌써??

. 프로세스 목록 확인 
 
~$ ps 
 
 
2. 프로세스 목록 확인 - 자세한 정보
 
~$ ps -f
 
 
3. 모든 프로세스 리스트 확인
 
~$ ps -e
~$ ps -ef
 
python 이름으로 실행중인 process
ps aux

kill -9 PID  # 중지


# 메모리 남은거 확인 
free -h

확인 하고 그럼 1기가로 부족하다는 말인데..

아니그럼 될때가 있고 안될때가 있는데 무슨기준??

Hadoop 키기전 2.2Gi  키고나면 3.2Gi 정도 Swap: use 가 95 ~ 98%?정도됨
sql구문 실행시 마지막 확인으로는 4.5Gi 에서 간당간당함 Swap: 0
가끔 airflow실행시 멈췄는데 메모리 부족이였던거 같음
다 끝나면 돌아옴

sql구문만해도 메모리 꽉 찰라그럼 
그렇다면 kafka가 있는 파일은??

메모리 증설부터 시도해보자... 생각보다 더 오래 걸릴듯 하다.
```

해결! 

![image-20220607132524897](README.assets/image-20220607132524897.png)



mysqlclient문제 -> 설치안됨 -> pip깨짐 -> broken pipe안되서 다른방법사용-> python operator로 스파크세션 사용못함 submit-spark오퍼 사용 -> 에러 -> 메모리 부족이였음 -> 메모리 늘림_> 해결

따지고 보면 간단한거 같기도 하고... 일주일 정도 걸려서 해결했다...

처음보는 에러고 메모리 부족인데 코드머머..주르륵 보여줘서 늦게 알아차린거 같다 

앞으로는 모든 메시지를 주의깊게 봐야할듯

> 메모리 문제라서 가상머신의 메모리를 늘리는 선택을 했는데 만약에 그렇지 못한 상황이었다면???  spark_sumbit_task에는 스파크 세션에 접속해서 6가지 파일들을 하둡에서 불러오고 연결된 mysql에 저장하는 과정이 너무 메모리를 많이 잡아먹는데 만약 메모리 자원자체가 불가능한 상황이였다면......
>
> **[]를 이용해서 하나하나의 작업을 병렬로 처리했다면? 아니면 하나하나의 작업을 따로 했다면?? 시간은 더걸리지만 당장의 자원 문제는 해결할수 있었을 것이다**



