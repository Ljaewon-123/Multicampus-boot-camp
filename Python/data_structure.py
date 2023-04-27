

from random import *


#자료구조 변환
# menu = set(리스트 혹은 튜플 이름)
# print(menu,type(menu))

# 두가지 방법이있다
b=[]

a = list(range(1,21))
print(a)

for i in range(1,21):
    b.append(i)
print(b)



shuffle(a)
print(a)
# print(sample(a,1))
a = set(a)
x = sample(a, 1)
x = set(x)
y = a - x
y = sample(y, 3)


print("-- 당첨자 발표 -- \n"+
      "치킨 당첨자 :" + str(x)[1:-1] + "\n"+
      "커피 당첨자 :" + str(y) + "\n"+
      "--축하합니다--" )
