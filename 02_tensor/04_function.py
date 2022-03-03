def f(x):

    return 2 * x + 1

x = [1,2,3,4,5]
y = list(map(lambda x:f(x),x))
print(x)
print(y)