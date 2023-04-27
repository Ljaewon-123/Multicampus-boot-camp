import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression ,LogisticRegression

# logistic 하다 논리적이다 T,F로 구분

# 1. 데이터 준비
# [1,0] 1시간 공부했고 , 0시간 과외했다 -> [0]: fail
# [8,1] 8시간 공부 , 1시간 가외 ->[1]: pass
x = [
    [1,0],
    [2, 0],
    [5, 1],
    [2, 3],
    [3, 3],
    [8, 1],
    [10, 0],
]
y = [
    [0],
    [1],
    [0],
    [0],
    [1],
    [1],
    [1],
]

# 2. 데이터 분할
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
# 3. 준비
logistic = LogisticRegression()
# 4. 학습
logistic.fit(train_x,np.ravel(train_y)) # ravel ?? 왜 써야 하는지?? 1차원으로 바꿈 원본 수정됨
# x가 2차원이면 괜춘한데 y는 절대안됌  reshape는 list는 안됌
# print(train_x)
# print(np.ravel(train_y))
# print(train_y)

# 5. 예측
pred = logistic.predict(test_x)

for i in range(len(test_x)):
    print('{} 시간 공부 {} 시간 과외 : {}'.format(test_x[i][0],test_x[i][1],'pass' if pred[i] == 1 else 'fail'))

print('acc : ',logistic.score(test_x,test_y))