# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder.master("yarn").appName("hdfs_spark").getOrCreate()
# appName 에는 코드를 돌리는 [파일명] 이 들어가면 된다


# user="root"
# password="1234"
# url="jdbc:mysql://localhost:3306/fish"  # ip포트번호 aws에 맞게 조정/데이터 베이스 이름
# driver="com.mysql.cj.jdbc.Driver"
# dbtable="obs_list"                          # 테이블이름

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


'''
 create table pago(
 obs_code varchar(20) PRIMARY KEY,
 record_time text,
 wave_height text ); 

create table tidalBuWind(
   obs_code varchar(20) PRIMARY KEY,
    record_time text,
     wind_dir text,
    wind_speed text );

create table jo_temp_data(
     obs_code varchar(20) PRIMARY KEY,
     record_time text,
     water_temp text );

create table bu_temp_data(
    obs_code varchar(20) PRIMARY KEY,
    record_time text,
    water_temp text );

create table jo_actual_condel_data(
    obs_code varchar(20) PRIMARY KEY,
   record_time text,
    wind_dir text );

create table jo_actual_wind_data(
    obs_code varchar(20) PRIMARY KEY,
     record_time text,
    wind_dir text,
     wind_speed text );


create table obs_list(
    obs_code varchar(20) PRIMARY KEY,
     data_type text,
     obs_lat text,
    obs_lon text,
    obs_post_name text,
     obs_object text );

csv_file = spark.read.format('csv').option('header','true').load('/user/jaewon/data/full_obs.csv')

csv_file.select('record_time','wave_height').show() 

기본키가 문자라서 append 하면 2번째에 에러남 첫번째는 그냥 쓰고 두번째부터 기본키를 제외하고 추가 

'''


