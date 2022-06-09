프로젝트때 급하게 한거라 아직 

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



