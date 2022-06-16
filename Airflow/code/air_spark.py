from airflow import DAG
from pendulum import yesterday
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator



dag = DAG(
dag_id='air11',
schedule_interval=None,
start_date=yesterday('Asia/Seoul'),
catchup=False
)


# spark-submit /home/big/airflow/dags/using_spark.py 과 같은 의미
# conn_id : browser -> Admin -> Connections 에 있음 (필요한 connection 추가나 수정 등 가능)

spark_submit_task = SparkSubmitOperator(
task_id='spark_submit_task',
application="/home/jaewon/airflow/dags/using_sql.py", # using_spark.py using_sql.py
conn_id='spark_default',
dag=dag
)

