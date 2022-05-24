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

