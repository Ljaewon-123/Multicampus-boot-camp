from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG
from datetime import datetime, timedelta
from pendulum import yesterday
from airflow.operators.python import PythonOperator

dag = DAG(
   dag_id='air_jinja',
   schedule_interval="@once",
   start_date=yesterday('Asia/Seoul'),
   template_searchpath='/home/jaewon/sh_code',
)

def templated_test(d1):
    print("{{ ds }}")
    print("ds test:", d1)

test1 = 'It would be passes, but jinja does not word {{ ds }} '

task=BashOperator(
    task_id='test_jinja',
    bash_command='jinja.sh',
    params={'test':test1},
    dag=dag,
)

task2=PythonOperator(
    task_id='python_task',
    python_callable=templated_test,
    op_args=["{{ ds }}"],
    dag=dag,
)

task >> task2
