from airflow.operators.bash_operator import BashOperator
from airflow.models import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 11, 1)
}

dag = DAG(
    dag_id='hello_today',
    default_args=args,
    schedule_interval="@once",
#    start_date=datetime(2019,11,1),  # poss?
    )

# Bash Operator
cmd = 'echo "Hello! Today is {{ ds }}"'
BashOperator(task_id='date', bash_command=cmd, dag=dag)

