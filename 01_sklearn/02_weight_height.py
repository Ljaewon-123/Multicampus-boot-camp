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
# print(len(df))
# print(df)
# 초등학교면 0 / 중학교면 학년별 6 / 고등학교 9 + 학년
# a = list(map(lambda x:'중학교' if x[-4:] == '중학교' else x[-4:] ,df['학교명']))
# print(a)
# df['grade'] = list(map(lambda x,y:0 if y == '초등학교' and x == 1 else 1 if y == '초등학교' and x == 2 else 2
#                        if y == '초등학교' and x == 3 else 3 if y == '초등학교' and x == 4 else 4 if y == '초등학교' and x == 5 else 5
#                        if y == '초등학교' and x == 6 else 6 ,df['학년'],a))

df['grade'] = list(map(lambda x:0 if x[-4:]  == '초등학교' else 6 if x[-3:] == '중학교' else 9 ,df['학교명'])) + df['학년']
# lambda 쓴다고 반드시 모든 과정을 람다안에서 해결 안해도됨
# print(df)
# print(df[6000:7000]) 중간값 확인
df.drop(['학교명','학년'],axis = 'columns',inplace=True)
df.columns = ['gender','height','weight','grade']
# df['gender'] = list(map(lambda x:0 if x == '남' else 1,df['gender']))
# df.gender = df.gender.map(lambda x:0 if x == '남' else 1)  # 각컬럼에 적용
df.gender = df.gender.map({'남' : 0, '여' : 1})
# print(df)
is_boy = df.gender == 0
boy_df, girl_df = df[is_boy],df[~is_boy]

x = boy_df['weight']
y = boy_df['height']



# df['grade']
# 2. 데이터 분할
train_x ,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
train_x = train_x.values.reshape(-1,1)  # 학습변수
test_x = test_x.values.reshape(-1,1)    # 실제적으로 쓰는값
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

plt.plot(test_x,test_y,'b.')
plt.plot(test_x,predict,'r.')
plt.xlim(10,140)
plt.ylim(100,220)
plt.show()