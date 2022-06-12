프로젝트때 급하게 한거라 정리할겸 다시 해보기 

---

# Airflow

**정의 Airflow : **

- Airbnb에서 만든 Workflow를 코드로 정의, 예약, 실행 및 모니터링 하는 오픈소스 플랫폼 
- DAG (Directed Acyclic Graph) 를 통한 간편한 시각화 
- 코드로 정의하였기 때문에 유지 관리, 버전 관리, 태스크 관리, 협업이 쉬워짐 
- data pipeline을 처리하기 위해 batch task 실행. (batch-oriented framework)



**특징**

- Scalable (확장성) : 모듈 형식으로 작성하여 프로그램을 확장하기 쉬움 
- Dynamic (동적) : python을 사용하여 파이프라인을 동적으로 인스턴스화 - 
- Extensible (확장가능성) : python 기반이기 때문에 여러 library를 이용한 확장 가능 
- Elegant (우아함) : 내장된 Jinja template engine을 사용하여 간결하고 명시적인 파이프라인 구성

**개념** 

- dag : 방향성 비순환 그래프(Directed Acyclic Graph). 작업 선택, 종속성 표현 (실행되는 순서 정의:  upstream >> downstream) -> 그래프가 순환되면, 상호 의존성으로 인해 deadlock에 빠질 수 있음
- task : 기본 실행(작업) 단위. 
- operator : task template. 단일 작업 실행. (task와 같은 의미로 사용되지만, 엄밀히 따지면 task는 operator manager)

**구조**

![image-20220609100215444](README.assets/image-20220609100215444.png)



![image-20220609095759709](README.assets/image-20220609095759709.png)

- Scheduler : task, dag 모니터링 -> task 예약
- Executor : task 객체를 실행시켜주는 역할 (default: SequentialExecutor)
- Worker : task 선택 및 실행
- Webserver : 말그대로의 웹서버 웹 ui 제공 
- Metastore : metadata database. scheduler, executor, webserver의 상태 저장
- User Interface : 사용자 환경 CLI 터미널
- Metadata Database : Scheduler가 파싱한 DAG와 Task 인스턴스 정보, Worker가 실행하면서 발생한 로그들이 airflow_db 라는 이름으로 저장



Task 실행시 Lifecycle 구간 마다 사용되는 Airflow 환경 변수를 그림으로 보여줌 

![img](https://image-kr.bespinglobal.com/wp-content/uploads/2021/07/4.png)



# Airflow Code

- bash : airflow dags test {dag_id} {date} 
- airflow web에서 Trigger DAG  실행 후 로그 확인 가능 

```PYTHON
from airflow import DAG
from pendulum import yesterday, tomorrow
from airflow.operators.python import PythonOperator
from datetime import timedelta

# DAG 객체 생성
# airflow의 날짜, 시간에 pendulum 사용 (python datetime 객체와 동일)

dag = DAG(
    dag_id = 'air01',
    schedule_interval=timedelta(minutes=1),
    start_date= yesterday('Asia/Seoul')
)

def hello():
    print('Hello,Airflow!')


# python 함수 실행

task01=PythonOperator(
    task_id ='hello',
    python_callable=hello,
    dag=dag
)

```



![image-20220609094821109](C:\Users\이재원\AppData\Roaming\Typora\typora-user-images\image-20220609094821109.png)

timedelta를 사용하여 갱신중인것을 볼 수 있음 

`{logging_mixin.py:109} INFO - Hello,Airflow!`



```python
from airflow import DAG
from pendulum import yesterday
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id='air02',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)

# bash script start
task02=BashOperator(
    task_id='hello',
    bash_command='echo Hello, airflow',
    dag=dag
)
```

![image-20220609102217486](README.assets/image-20220609102217486.png)

airflow web에서 확인 가능

{} 내용이 살짝 다름 

BashOperator를 사용했었으니까 쉘 스크립트 sh 파일도 해보자

> 쉘 스크립트도 많이 까먹었다 재밌었는데.. 기본문법 간단하게 잡고 BashOperator에 써보자 

사용한 sh파일 쉘 스크립트 

간단하긴 한데 read반응이 airflow에서 어떨지 궁금해서 한번해봄 

```sh
#!/bin/sh



echo "Welcom to shell practice File!!
        This Files desigined by Ljaewon  asdhfae"

echo "Select maybe? item: item1,item2 or item3  so simply"


a=0

while [ "$a" -lt 5 ]
do
        a=$(expr $a + 1)
        echo $a
done


# while true ; do
#   echo "Please type something in (^C to quit)"
#   read INPUT_STRING
#   echo "You typed: $INPUT_STRING"
# done

echo "select item1 or item2 or item3"

while true ; do
        echo "hihi"
        read item
        case $item in
                "item1")
                        echo " you want stop? "
                        echo "(y/n)" # Yes|yes|y|Y) case 하나 더 사용해서 이런식도 나쁘지 않을듯
                        read a

                        if [ "$a" = "y" ]; then
                                break
                        else
                                continue
                        fi
                ;;
                "item2" | "item3")
                        echo "2 or 3"
                        echo "???"

                        cd /home/jaewon
                        cat starbucks_all.json
                ;;

                *) echo "Jush default"
                   echo " Try Again"
                ;;
        esac
done
```

실행하면 대충 아래와 같이 된다

![image-20220610042249611](README.assets/image-20220610042249611.png)

요건 적용코드 

```python
from airflow import DAG
from pendulum import yesterday
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id='air02',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)

templated_command="sh /home/jaewon/sh_code/while_pre.sh"
# 'sh /home/jaewon/sh_code/while_pre.sh'

# bash script start
task02=BashOperator(
    task_id='hello',
#    bash_command='echo Hello, airflow',
    bash_command=templated_command,
    dag=dag
)

```

`TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: sh /home/jaewon/sh_code/while_pre.sh`

근데 요런 에러떠서 안됨 

읽어보니 templated_command 즉 sh파일의 경로를 찾지 못했다는 거였음 그래서 공식문서 확인해봄

[BashOperator — Airflow Documentation (apache.org)](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html)

sh라고 명령어 그대로 쓰는게 아니였음 

바꾼후에 코드

```python
from airflow import DAG
from pendulum import yesterday
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id='air02',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul'),
    template_searchpath='/home/jaewon/sh_code',
)

# templated_command="sh /home/jaewon/sh_code/while_pre.sh"
# 'sh /home/jaewon/sh_code/while_pre.sh'

# bash script start
task02=BashOperator(
    task_id='hello',
    bash_command='while_pre.sh',
    dag=dag
)
```

**template_searchpath** 라는걸 사용해서 위치 지정후에 사용 template_searchpath쓸게 아니라면 dags밑에 넣어야함  그래서 결과는



![image-20220610041822904](README.assets/image-20220610041822904.png)

read에 값을 넣을수 없었음... 혹시나 했는데 

Jinja 라고 재밌어 보이는거 찾았는데 값을 전달해줄수는 있는듯 하다 나중에 공부하다 사용할 기회가 올듯 하다.



[Crontab.guru - The cron schedule expression editor](https://crontab.guru/)

1번에서 한건데 스케쥴 반복하는 것만 정리함

start_date : time window 시작(start_date에 실행되는 것이 아님!) 

end_date : time window 끝 

schedule_interval : start_date부터, data를 수집하는 간격

schedule_interval 

- cron */1 * * * * : 1분마다

-  timedelta 

  timedelta(minutes=1) : 매 분 

  timedelta(hours=1) : 매시간

- cron presets None : 스케쥴링 하지 않음 (트리거 되는 dag에서 사용)

  @once : 한번 

  @hourly : 매시간 (0 * * * *) 

  @daily : 매일 자정 (0 0 * * *) 

  @weekly : 매주 일요일 아침 자정 (0 0 * * 0) 

  @monthly : 매월 1일 자정 (0 0 1 * *) 

  @quarterly : 분기별 1일 자정 (0 0 1 */3 *) 

  @yearly : 매년 1월 1일 자정 (0 0 1 1 *)
