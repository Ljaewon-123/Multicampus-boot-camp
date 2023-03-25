# 마찬가지로 최대한 스택 사용
# post_operator
# import post_operator_conversion as po
from post_operator_conversion import *

cer = '((3*5)-(6/2))'
total = []

post = post_operator(cer)
for i in post:
    total.append(i)
    if i == '*' :
        total.pop()
        b = total.pop()
        a = total.pop()
        b = int(b)
        a = int(a)
        c = a*b
        total.append(c)
    elif i == '+':
        total.pop()
        b = total.pop()
        a = total.pop()
        b = int(b)
        a = int(a)
        c = a + b
        total.append(c)
    elif i == '-':
        total.pop()
        b = total.pop()
        a = total.pop()
        b = int(b)
        a = int(a)
        c = a - b
        total.append(c)
    elif i == '/':
        total.pop()
        b = total.pop()
        a = total.pop()
        b = int(b)
        a = int(a)
        c = a / b
        total.append(c)


print(total)

