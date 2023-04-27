import matplotlib.pyplot as plt

def f(x):
    return list(map(lambda i:2*i,x))

x = [1,2,3,4,5]

y = f(x)
print(y)

plt.plot(x,y)
plt.show()