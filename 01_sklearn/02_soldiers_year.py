import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# 상관관계 확인

# 1. 데이터 준비
# df = pd.read_csv('soldiers.csv',encoding='cp949')
# print(df)
names = ['순번','date','가슴둘레','소매길이','height','허리둘레','샅높이','머리둘레','발길이','weight']
df = pd.read_csv('soldiers.csv',encoding='cp949',names=names,header=0,low_memory=False)
# print(df)
df = df[['date','height','weight']]
# print(len(df))
df.dropna(inplace=True) # inplace=True df의 새로운 프레임을 df에 적용함 -> 같은 변수에 저장시킴
# print(len(df))
# print(df)
# 년도만 남기기
df['date'] = list(map(lambda x:int(str(x)[:4]) if len(str(x))>4 else x,df['date'])) # 문자 개수세는데 문자열 함수 찾지마라
# 2013: 0 /2014: 1 / 2017: 4
df['date_new'] = list(map(lambda x:0 if x == 2013 else 1 if x ==2014 else 2 if x== 2015 else 3 if x== 2016 else 4,df['date']))
df['height'] = list(map(lambda x:float(str(x)[:5]) if len(str(x))>5 else x ,df['height']))
# df['weight'] = list(map(lambda x:float(str(x).split()[0].strip()) ,df['weight']))
df['weight'] = list(map(lambda x:str(x).split(' ')[0] ,df['weight']))
df['weight'] = list(map(lambda x:float(x) if x else None,df['weight']))
df.dropna(inplace=True)
# print(df)
x = df[['weight','date_new']]  # 2차원 이라 할필요없음
y = df['height']
# 2. 데이터 분할 왜? 학습용과 검증용으로 
# train_x ,test_x
train_x ,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
# print(train_x)
# print(train_y)
# train_x = train_x.values.reshape(-1,1)  # 학습변수
# test_x = test_x.values.reshape(-1,1)    # 실제적으로 쓰는값

# 3. 준비
linear = LinearRegression()

# 4. 학습
linear.fit(train_x,train_y)  # linear 객체가 알아서 학습
# 5. 예측 및 평가
predict = linear.predict(test_x)
print(test_x)
print(predict)

print(linear.predict([[70,4]]))

'''
plt.plot(test_x,test_y,'b.')
plt.plot(test_x,predict,'r.')
plt.xlim(20,150)
plt.ylim(150,220)
plt.grid()
plt.show()  # 파란색은 실제값 빨간색은 학습값
'''

