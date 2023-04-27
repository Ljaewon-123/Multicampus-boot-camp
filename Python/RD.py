from random import *

print(random())
print(random() * 10)
print(int(random() * 10))  # 1~10미만의 정수
print(int(random() * 10) + 1)  # 10을 포함

print(randrange(1, 46))  # 1~46미만의 임의값

print(randint(1, 45))  # 1~45 까지 포함하는 임의의 값

# 오프라인 날짜 정하는게 메인 set을 사용하ㅣ면?
# from random import *

i = 0
j = 0
a = {}
a = set(a)

while (i < 3):
    if i == 0:
        # a = randint(4,29)
        a.add(randint(4, 29))

    if i == 1:
        # b =  randint(4,29)
        a.add(randint(4, 29))
    if i == 2:
        # c =  randint(4,29)
        a.add(randint(4, 29))
    i = i + 1

a.add(randint(4, 29))

a = list(a)

print(a)

print("오프라인 스터디 모임 날짜는 매월 %d 일로 선정" % a[3])

