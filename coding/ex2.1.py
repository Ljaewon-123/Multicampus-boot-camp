array = [45,12,85,32,89,39,69,44,42,1,6,8]   # 삽입정렬 코드

tmp = 0

for i in range(1,len(array)):
    for j in range(i,0,-1):     # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:   # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:       # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

array = [45,12,85,32,89,39,69,44,42,1,6,8]
for i in range(len(array)):
    for j in range(i,0,-1):
        # print('notnot',i,j)
        if array[j] < array[j-1]:
            tmp = array[j]
            array[j] = array[j-1]
            array[j-1] = tmp
            # print(array,i,j)

print(array)


array = [45,12,85,32,89,39,69,44,42,1,6,8]
for i in range(1,len(array)):
    for j in range(i-1,-1,-1):   # for j in range(i-1,-1,-1):   #  for j in range(i, 0, -1):
        print(i,j)