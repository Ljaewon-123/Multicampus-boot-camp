from pyspark.sql import SparkSession

spark = SparkSession.builder.master("yarn").appName("toMysql").getOrCreate()

user="root"
password="1234"
url="jdbc:mysql://localhost:3306/fish"  # ip포트번호 aws에 맞게 조정/데이터 베이스 이름
driver="com.mysql.cj.jdbc.Driver"



pago_file = spark.read.format('json').load('/user/jaewon/data/pago.jsonl')

tidalBuWind_file = spark.read.format('json').load('/user/jaewon/data/tidalBuWind.jsonl')

jo_temp_data_file = spark.read.format('json').load('/user/jaewon/data/jo_temp_data.jsonl')

bu_temp_data_file = spark.read.format('json').load('/user/jaewon/data/bu_temp_data.jsonl')

jo_actual_condel_data_file = spark.read.format('json').load('/user/jaewon/data/jo_actual_condel_data.jsonl')

jo_actual_wind_data_file = spark.read.format('json').load('/user/jaewon/data/jo_actual_wind_data.jsonl')

obs_list_file  = spark.read.format('csv').option('header','true').load('/user/jaewon/data/full_obs.csv')


pago_file.write.option('truncate', True).jdbc(url,'pago','overwrite',properties={'driver':driver,'user':user,'password':password})
tidalBuWind_file.write.option('truncate', True).jdbc(url,'tidalBuWind','overwrite',properties={'driver':driver,'user':user,'password':password})
jo_temp_data_file.write.option('truncate', True).jdbc(url,'jo_temp_data','overwrite',properties={'driver':driver,'user':user,'password':password})
bu_temp_data_file.write.option('truncate', True).jdbc(url,'bu_temp_data','overwrite',properties={'driver':driver,'user':user,'password':password})
jo_actual_condel_data_file.write.option('truncate', True).jdbc(url,'jo_actual_condel_data','overwrite',properties={'driver':driver,'user':user,'password':password})
jo_actual_wind_data_file.write.option('truncate', True).jdbc(url,'jo_actual_wind_data','overwrite',properties={'driver':driver,'user':user,'password':password})
obs_list_file.write.option('truncate', True).jdbc(url,'obs_list','overwrite',properties={'driver':driver,'user':user,'password':password})
