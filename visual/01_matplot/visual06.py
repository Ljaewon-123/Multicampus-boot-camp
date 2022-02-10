import matplotlib.pyplot as plt
from random import randint

fig,ax = plt.subplots()

x = list(randint(0,10)for i in range(100))

ax.hist(x,bins=10,cumulative=True)   # cumulative == 그래프 겹치기??,, 가중치 x축 으로 가중치
ax.hist(x,bins=10,cumulative=False)

plt.xticks(list(range(0,11)))
plt.yticks(list(range(0,101,5)))

plt.xlim(0,10)   # x축 제한 0~ 10
plt.ylim(0,100)  # y축 제한 0~ 100

plt.show()