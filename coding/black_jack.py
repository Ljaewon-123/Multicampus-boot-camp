# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다. 넘지 않는다 == 초과 라고하면 M 이 21이면 21까지는 됨
# 중복불가란말 없으니 그냥 한다
# 방법은 그려지는데 구현에서 애먹음
# 3번이 쭈르륵 그다음 2번이 한칸식 움직이면서 3번 주르륵 마지막은 2,3번 끝에 있고 1번이 주르륵

from random import *

while True:
    a= int(input('첫번째수:'))
    b= int(input('두번재수:'))
    # a = 10
    # b = 100

    if not a>=3 and a <= 100:
        continue
    elif not b >=10 and b <= 300000:
        continue
    else:
        break

lst = []
sum1 = []
for i in range(a):
    # print(randint(3, b))
    num = randint(3,b)
    lst.append(num)

print(lst)
cnt = 0
i = 0
while i < len(lst):

    if cnt == a-2:
        sum1.append(lst[i] + lst[-2] + lst[-1])
        i += 1
        if i == a-3:
            break

    else:
        sum1.append(lst[0]+lst[1+cnt]+lst[i+2])
        i += 1
        if a-3 == i:  # 마지막에서 두번재를 가르키면 cnt가 커지면서 2번이 움직이게됨
            sum1.append(lst[0] + lst[1+cnt] + lst[i + 2])
            cnt += 1
            # print(cnt)
            i = 0

            continue

print(sum1)

while True:
    # a = max(sum1)
    # print(a)
    if not sum1:
        print('안되니까 다시 돌려 귀찮아서 while문 다시 안씀 ')
        break
    if max(sum1) > b:
        sum1.remove(max(sum1)) # ValueError: max() arg is an empty sequence ## 전부 삭제되어서 비어있는거
        continue
    elif max(sum1) <= b:
        print(max(sum1))
        break

'''Best
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)
count = 0

for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)
'''