from pyspark.sql import SparkSession

spark = SparkSession.builder.master("yarn").appName("airflow using spark").getOrCreate()
# mysql
user="root"
password="1234"
url="jdbc:mysql://localhost:3306/mysql"
driver="com.mysql.cj.jdbc.Driver"
dbtable="test"

mysql_df = spark.read.format("jdbc").options(user=user, password=password,
url=url, driver=driver, dbtable=dbtable).load()
mysql_df.show()

