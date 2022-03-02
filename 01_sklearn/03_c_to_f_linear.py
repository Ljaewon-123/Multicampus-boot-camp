import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def celsius_to_fahrenheit(x):
    return (x*1.8)+32

# 혼자할때 1번 준비만 보고 만들수있느냐ㅏ 이거롤 남은 번호에서 연습하면됨? 근데? 이미 좀 늦은거같기두..

# 1. 데이터 준비
data_C = np.array(range(0,100))
data_F = celsius_to_fahrenheit(data_C)

x = data_C
y = data_F

# 2. 데이터 분할
train_x ,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1) # 왜? 학습 검증
train_x =  train_x.reshape(-1,1)
test_x =  test_x.reshape(-1,1)
# 3. 준비
linear = LinearRegression()
# 4. 학습
linear.fit(train_x,train_y)
# 5. 예측
predict = linear.predict(test_x)  # 지도 학습? 
print(test_x)
print(predict)

pred_f = linear.predict([[30]])
print('30 to fahrenheit: ', pred_f)

accuracy = linear.score(test_x,test_y)  # 정확도
print(accuracy)