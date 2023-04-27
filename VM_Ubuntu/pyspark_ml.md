# pyspark ml 



처음이라 참고를 많이한 코드 

처음 느낀건 머신러닝 자체보다 머신러닝에 들어갈수있도록 데이터를 전처리하는데에 힘을더 많이 쓴것같다.

파일을 나눌수도있었는데 스파크세션사용해서 그냥 한 파일에 다 넣어 만들었다.

tool를 사용 안해서 이게 편했음

분류모델

```python
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
plt.rc('font',family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# pyspark - sql
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import mean, col, split, regexp_extract, when, lit
from pyspark.sql.functions import isnan,count

# pyspark - ML
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer,VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import QuantileDiscretizer


spark = SparkSession.builder.master("yarn").appName("test_ml").getOrCreate()

# load data
df = spark.read.format('csv').option('header','true').load('/user/jaewon/data/train.csv')
df.show(5)
# print(df.limit(3).toPandas())

pandas_df = df.toPandas()

df = df.drop('Cabin')  # 결측치 많아서 제외

df.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns])\
  .show()

df = df.withColumn('Initial',regexp_extract(col('Name'),"([A-Za-z]+)\.",1)) # ()이게 하나의 그룹임

df.limit(3).show()


df = df.replace(['Mlle','Mme', 'Ms', 'Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],
                ['Miss','Miss','Miss','Mr','Mr',  'Mrs',  'Mrs',  'Other',  'Other','Other','Mr','Mr','Mr'])


# Initial 변수 값들로 그룹핑한 후 평균 Age 구하기
#df.groupby('Initial').avg('Age').collect()

df = df.withColumn('Age',
                  when((df['Initial'] == 'Miss') & (df['Age'].isNull()),
                      22).otherwise(df['Age']))
df = df.withColumn('Age',
                  when((df['Initial'] == 'Other') & (df['Age'].isNull()),
                      46).otherwise(df['Age']))
df = df.withColumn('Age',
                  when((df['Initial'] == 'Master') & (df['Age'].isNull()),
                      5).otherwise(df['Age']))
df = df.withColumn('Age',
                  when((df['Initial'] == 'Mr') & (df['Age'].isNull()),
                      33).otherwise(df['Age']))
df = df.withColumn('Age',
                  when((df['Initial'] == 'Mrs') & (df['Age'].isNull()),
                      36).otherwise(df['Age']))

# Embarked 변수에도 결측치가 2개 있었는데 무엇인지 확인해보기
df.groupBy('Embarked').count().show()

# Embarked의 결측치는 최빈값인 'S'로 대체해주기
df = df.na.fill({"Embarked": "S"})
# 결측치가 채워졌는지 다시 확인
df.groupBy('Embarked').count().show()

# Family size라는 파생변수 생성
df = df.withColumn("Family_Size",
                  col('SibSp')+col('Parch')) # df['SibSp']도 가능!

# Alone이라는 Binary 파생변수 생성하는데, 우선 0으로 다 해놓기
df = df.withColumn('Alone', lit(0))
# 조건에 맞게 Alone 변수값 변경
df = df.withColumn('Alone',
                  when(col('Family_Size') == 0, 1)\
                  .otherwise(col('Alone')))


convert_cols = ['Sex', 'Embarked', 'Initial']

# 추후에 IndexToString할려면 indexer 객체를 사용하면 됨!
indexer = [StringIndexer(inputCol=col,outputCol=col+'_index').fit(df) for col in convert_cols]
for i in indexer:
    print(i)
    print('-'*80)

print(type(indexer))

# Pipeline을 이용해 stage에다가 실행 과정 담아 넘기기
# 이후 Estimator.fit()이나 Transformer.transform()둘중 하나 호출
pipeline = Pipeline(stages=indexer) # 호출시 stages가 순서대로 호출 
df = pipeline.fit(df).transform(df)  # 학습 # 입력 데이터 변환

un_cols = ["PassengerId","Name","Ticket","Cabin","Embarked","Sex","Initial"]

df = df.drop(*un_cols)
print("삭제 후 남은 칼럼들:", df.columns)

# VectorAssembler 여러열을 벡터열로 병합
feature = VectorAssembler(inputCols = df.columns[1:],
                         outputCol='features')

# df = df.astype('float')
# 타입변환을 위해 급하게 만듬
from pyspark.sql.types import IntegerType

df = df.withColumn("Age", df["Age"].cast(IntegerType()))
df = df.withColumn("SibSp", df["SibSp"].cast(IntegerType()))
df = df.withColumn("Parch", df["Parch"].cast(IntegerType()))
df = df.withColumn("Fare", df["Fare"].cast(IntegerType()))
df = df.withColumn("Pclass", df["Pclass"].cast(IntegerType()))
df = df.withColumn("Survived", df["Survived"].cast(IntegerType()))


feature_vector = feature.transform(df) # 데이터프레임 형태로 반환
print('feature type:', type(feature))
print('feature_vector type', type(feature_vector))

feature_vector.limit(3).toPandas()

titanic_df = feature_vector.select(['features', 'Survived'])

# split train, test
(train_df, test_df) = titanic_df.randomSplit([0.8, 0.2], seed=42)



print('realily end?')

# 분류 모델 
from pyspark.ml.classification import LogisticRegression
# 파라미터 튜닝 & 교차 검증
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
from pyspark.ml.tuning import CrossValidator
# 파이프라인
from pyspark.ml import Pipeline
# 메트릭 얻는 라이브러리
from pyspark.ml.evaluation import BinaryClassificationEvaluator
# ROC AUC(Sklearn)
from sklearn.metrics import roc_curve, auc


# 모델 정의
lr = LogisticRegression(labelCol='Survived')

# 튜닝할 파라미터 grid 정의 (그리드 지정된 매개변수를 고정값으로)
                                    # model.parameter 식으로 정의
paramGrid = ParamGridBuilder().addGrid(lr.regParam,
                                      (0.01, 0.1))\
                              .addGrid(lr.maxIter,
                                      (5, 10))\
                              .addGrid(lr.tol,
                                      (1e-4, 1e-5))\
                              .addGrid(lr.elasticNetParam,
                                      (0.25, 0.75))\
                              .build() # 그리드 지정된 모든 조합 빌드후 리턴

# 교차검증 정의 - Pipeline식으로 정의
tvs = TrainValidationSplit(estimator=lr,
                          estimatorParamMaps=paramGrid,
                          evaluator=MulticlassClassificationEvaluator(labelCol='Survived'),
                          trainRatio=0.8)

# 학습은 fit으로!
model = tvs.fit(train_df)
# 평가는 transform으로!
model_prediction = model.transform(test_df)

# 메트릭 평가
print('Accuracy:',
     MulticlassClassificationEvaluator(labelCol='Survived',
                                      metricName='accuracy').evaluate(model_prediction))
print('Precision:',
     MulticlassClassificationEvaluator(labelCol='Survived',
                                      metricName='weightedPrecision').evaluate(model_prediction))


```

결과 

>Accuracy: 0.7724137931034483                                                    
>Precision: 0.7709160571229536 



# Regression 모델

일단 따라 해봤는데 ....... 

```python
import os
import pandas as pd
import numpy as np

# pyspark for objecy, sql
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, SQLContext

from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col

# pyspark for ML
from pyspark.ml.regression import LinearRegression
from pyspark.mllib.evaluation import RegressionMetrics
from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.ml.tuning import ParamGridBuilder, CrossValidator, CrossValidatorModel
from pyspark.ml.feature import VectorAssembler, StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns
# Setting for visualization
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

from matplotlib import rcParams
sns.set(context='notebook', style='whitegrid',
       rc={'figure.figsize': (18, 4)})
rcParams['figure.figsize'] = 18, 4

# 재실행을 대비하기 위해 랜덤 시드 설정해놓기
rnd_seed = 23
np.random.seed = rnd_seed
np.random.set_state = rnd_seed

## 데이터 스미카 직접 명시해주기 ##
data_path = '/user/jaewon/data/cal_housing.data'
# data의 칼럼명을 스키마로 정의해주기
schema_string = 'long lat medage totrooms totbdrms pop houshlds medinc medhv'

fields = [StructField(field, FloatType(), True)for field in schema_string.split()]
schema = StructType(fields)

spark = SparkSession.builder.master('yarn')\
        .appName('Regression')\
        .getOrCreate()


# 데이터파일 로드
# cache 메소드를 이용해서 메모리에 keep해놓기
housing_df = spark.read.csv(path=data_path, schema=schema).cache()

# 상위 5개 행 미리 보기 -> 하나의 Row가 namedTuple 형태로 되어 있음..!
housing_df.take(5)



# 그룹핑해서 집계해보기
result_df = housing_df.groupBy('medage').count()
# 값 정렬 기준 설정해주고 내림차순으로 정렬
result_df.sort('medage', ascending=False).show(5)

# 수치형 변수들 기술통계량 살펴보기
housing_df.describe().show(10)

# 반환되는 통계량 값들을 소수점 제거하거나 하는 등 커스터마이징해서 출력
(housing_df.describe()).select('summary',
                              F.round('medage', 4).alias('medage'),
                              F.round('totrooms', 4).alias('totrooms'),
                              F.round('totbdrms', 4).alias('totbdrms'),
                              F.round('pop', 4).alias('pop'),
                              F.round('houshlds', 4).alias('houshlds'),
                              F.round('medinc', 4).alias('medinc'),
                              F.round('medhv', 4).alias('medhv')).show(10)
# 파생변수 생성하기
housing_df = (housing_df.withColumn('rmsperhh',
                                   F.round(col('totrooms')/col('houshlds'), 2))\
                        .withColumn('popperhh',
                                   F.round(col('pop')/col('houshlds'), 2))\
                        .withColumn('bdrmsperrm',
                                   F.round(col('totbdrms')/col('totrooms'), 2)))
housing_df.show(5)



# 사용하지 않을 변수 제외하고 필요한 변수들만 select
housing_df = housing_df.select('medhv',
                              'totbdrms',
                              'pop',
                              'houshlds',
                              'medinc',
                              'rmsperhh',
                              'popperhh',
                              'bdrmsperrm')

featureCols = ['totbdrms', 'pop', 'houshlds', 'medinc',
              'rmsperhh', 'popperhh', 'bdrmsperrm']

# VectorAssembler로 feature vector로 변환
# Scaling을 적용시키기 이전에 필요한 Feature들을 Vector로 변환하는 작업이 선행
assembler = VectorAssembler(inputCols=featureCols, outputCol='features')
assembled_df = assembler.transform(housing_df)
assembled_df.show(10, truncate=True)


# 위에서 만든 Feature vector인 'features' 넣기
standardScaler = StandardScaler(inputCol='features',
                               outputCol='features_scaled')
# fit, transform
scaled_df = standardScaler.fit(assembled_df).transform(assembled_df)

# scaling된 피처들만 추출해보기
scaled_df.select('features', 'features_scaled').show(10,
                                                    truncate=True)


# 데이터 분할 학습 8, 테스트 2
train_data, test_data = scaled_df.randomSplit([0.8, 0.2], seed=rnd_seed)

# Elastic Net 모델 정의
lr = LinearRegression(featuresCol='features_scaled',
                     labelCol='medhv',
                     predictionCol='predmedhv',
                     maxIter=10,
                     regParam=0.3,
                     elasticNetParam=0.8,
                     standardization=False)
# 모델 학습
linearModel = lr.fit(train_data)


# transoform 사용하면 모델 정의할 때 설정한 "예측 값 변수"를 새로 만들어 생성한 데이터프레임 반환
predictions = linearModel.transform(test_data)

print(type(predictions)) # 예측 결과값이 PySpark의 데이터프레임 형태로 반환됨!


# predictions 데이터프레임에서 y값과 예측값만 추출해 비교
pred_labels = predictions.select('predmedhv', 'medhv')
pred_labels.show()

print(f"RMSE:{linearModel.summary.rootMeanSquaredError}")
print(f"MAE: {linearModel.summary.meanAbsoluteError}")
print(f"R2 score: {linearModel.summary.r2}")

```

>RMSE:78116.2564798975
>MAE: 56925.44456037988
>R2 score: 0.5435224404301482



# pipeline

```python
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

iris = load_iris()
data = iris.data
label = iris.target

iris_df = pd.DataFrame(data, columns=iris.feature_names)
iris_df['target'] = label

spark_df = spark.createDataFrame(iris_df)



# 1. Train/Test 데이터로 분할
train_df, test_df = spark_df.randomSplit(weights=[0.8, 0.2], seed=42)

# 2. Feature Vector로 만들기
ftr_columns = train_df.columns[:-1]
vec_assembler = VectorAssembler(inputCols=ftr_columns, outputCol='features')

train_ftr_vec = vec_assembler.transform(train_df)
test_ftr_vec = vec_assembler.transform(test_df)  # 테스트 데이터에 대해도 동일한 객체 사용

print('# 학습 원본 데이터:')
train_df.limit(5).show()

print('# Feature Vectorization 후 학습 데이터:')
train_ftr_vec.limit(5).show()


# 모델 정의
dt_clf = DecisionTreeClassifier(featuresCol='features', labelCol='target', maxDepth=10)

# 학습
dt_model = dt_clf.fit(train_ftr_vec)

# 학습, 테스트 데이터에 대해 예측
train_pred = dt_model.transform(train_ftr_vec)
test_pred = dt_model.transform(test_ftr_vec)

evaluator = MulticlassClassificationEvaluator(predictionCol='prediction', labelCol='target', metricName='accuracy')

train_acc = evaluator.evaluate(train_pred)
test_acc = evaluator.evaluate(test_pred)

print('Train Accuracy:', train_acc)
print('Test Accuracy:', test_acc)
```







사이킥런이랑 형태가 좀 비슷한거 같은데 비교해 보면서 다시 한번 보자



# Error

## pillow 관련에러 인듯

ImportError: cannot import name '_imaging' from 'PIL' (/usr/lib/python3/dist-packages/PIL/__init__.py)

다운한적도 없는데 자꾸 나는 에러

uninstall하면 없다더니 install하면 이미 있다고 그럼 그래서

`python -m pip install --upgrade pip`  이후에

`python -m pip install --upgrade pillow` 생김

이후 해결은 안됬지만 다른 에러로 넘어감

rmgn vkdlTjsdp 

`from PIL import Image`

