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


