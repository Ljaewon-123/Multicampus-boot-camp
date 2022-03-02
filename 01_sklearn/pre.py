import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression , LogisticRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans

# 1. 데이터 준비
iris = load_iris()
x = iris.data
y = iris.target


# 2. 데이터 분할
train_x ,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)
# 3. 준비

model = KMeans()

model.fit(train_x,train_y)

pred = model.predict(test_x)

# print(test_x)
# print(pred)

df = pd.DataFrame(test_x)
df.columns = ['sepal_length','sepal_width','petal_length','petal_width']
df['category'] = pd.DataFrame(pred)

print(df)
centers = pd.DataFrame(model.cluster_centers_)
centers.columns = ['sepal_length','sepal_width','petal_length','petal_width']
center_x = centers['sepal_length']
center_y = centers['sepal_width']

plt.scatter(df['sepal_length'],df['sepal_width'],c=df['category'])
plt.scatter(center_x,center_y,s=100,c='r',marker='*')
plt.show()
