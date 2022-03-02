from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# 1.
iris = load_iris()
x = iris.data
y = iris.target
# 2.
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=1)

# 3.
model = KMeans(n_clusters=3)  # 몇개인지 알려주면 그 n수만큼 묶어줌  그 n이 이 n이 아닌가???/
# 4.
model.fit(train_x)

# 5.
pred = model.predict(test_x)
print(test_x)
print(pred)

# 어떻게 군집한건지 그려보자
df = pd.DataFrame(test_x)
df.columns = ['sepal_length','sepal_width','petal_length','petal_width']
df['category'] = pd.DataFrame(pred)

centers = pd.DataFrame(model.cluster_centers_)
centers.columns = ['sepal_length','sepal_width','petal_length','petal_width']
center_x = centers['sepal_length']
center_y = centers['sepal_width']

plt.scatter(df['sepal_length'],df['sepal_width'],c=df['category'])
plt.scatter(center_x,center_y,s=100,c='r',marker='*')
plt.show()

