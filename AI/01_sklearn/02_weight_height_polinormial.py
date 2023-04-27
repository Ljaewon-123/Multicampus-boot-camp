import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np

# 1. 데이터 준비
df = pd.read_csv('weight_height.csv',encoding='cp949')
# print(df)
# 학교명 , 학년 , 성별 , 키 , 몸무게
df = df[['학교명','학년','성별','키','몸무게']]
# print(len(df))
df.dropna(inplace=True)

df['grade'] = list(map(lambda x:0 if x[-4:]  == '초등학교' else 6 if x[-3:] == '중학교' else 9 ,df['학교명'])) + df['학년']

# print(df)
# print(df[6000:7000])
df.drop(['학교명','학년'],axis = 'columns',inplace=True)
df.columns = ['gender','height','weight','grade']
# df['gender'] = list(map(lambda x:0 if x == '남' else 1,df['gender']))
# df.gender = df.gender.map(lambda x:0 if x == '남' else 1)  # 각컬럼에 적용
df.gender = df.gender.map({'남' : 0, '여' : 1})
# print(df)

x = df[['weight','gender']]
y = df['height']

poly = PolynomialFeatures()
x = poly.fit(x).transform(x)


# df['grade']
# 2. 데이터 분할
train_x ,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
# train_x = train_x.values.reshape(-1,1)  # 학습변수
# test_x = test_x.values.reshape(-1,1)    # 실제적으로 쓰는값
# 3. 준비
linear = LinearRegression()
# 4. 학습
linear.fit(train_x,train_y)
# 5. 예측
predict = linear.predict(test_x)
print(test_x)
print(predict)
# print(predict[[50]])           # 50번째 리스트 잖어라
# print(linear.predict([[50]]))  # 테스트 값에  50 넣는거구

accuracy = linear.score(test_x,test_y)
print('acc:',accuracy)

plt.plot(test_x,test_y,'b.')
plt.plot(test_x,predict,'r.')
plt.xlim(10,140)
plt.ylim(100,220)
plt.show()