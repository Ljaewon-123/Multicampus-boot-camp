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


