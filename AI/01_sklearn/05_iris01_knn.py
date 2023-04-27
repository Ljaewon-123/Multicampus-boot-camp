from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression ,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# 1. 데이터 준비
iris = load_iris()
x = iris.data
y = iris.target


# 2. 데이터 분할
train_x ,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
# 3. 준비
model = KNeighborsClassifier()   # 분류? iris불러와서 종을 학습시킴 그런다음 데이터를 줄때 데이터를 k개에 가장 가까운 과반수로 분류함
# iris의 종을 입력값에 가까운 k값과 비교하여 분류하는 예측모델을 만드는 코드
# 4. 학습
model.fit(train_x,train_y)
# 5. 예측
pred = model.predict(test_x)
for i in range(len(test_x)):
    print(f'{test_x[i]} 예측 : {iris.target_names[pred[i]]}/ 실제: {iris.target_names[test_y[i]]}')
print(f'acc : {model.score(test_x,test_y)}')

