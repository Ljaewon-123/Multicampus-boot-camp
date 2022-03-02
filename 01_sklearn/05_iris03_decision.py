from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# 1.
iris = load_iris()
x = iris.data
y = iris.target

# 2.
train_x, test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)

# 3.
model = DecisionTreeClassifier()

# 4.
model.fit(train_x,train_y)

# 5.
pred = model.predict(test_x)
for i in range(len(test_x)):
    print(f'{test_x[i]} : {pred[i]}')

print(model.score(test_x,test_y))