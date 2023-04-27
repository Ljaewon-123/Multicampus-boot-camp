from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression ,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# svm 두그룹을 나눔  kernel Trick : 차원을 추가하여 분류 -> 2차원에서 불가능할때 3차원으로 바꿔서 길을 만듬

# 1. 데이터 준비
iris = load_iris()
x = iris.data
y = iris.target

# 2. 데이터 분할
train_x , test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
# 3. 준비
model = SVC(kernel = 'linear')
# 4. 학습
model.fit(train_x,train_y)
# 5. 예측
pred = model.predict(test_x)
print(test_x)
print(pred)

print(model.score(test_x,test_y))