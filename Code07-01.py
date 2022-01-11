## 큐
# front 와 rear 이 같으면 비어있는거

## 함수

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
# enqueue
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'

print('출구<-----',queue,'<---입구')

# dequeue
front += 1
data = queue[front]
queue[front] = None
print('밥 손님 ----> : ', data)
front += 1
data = queue[front]
queue[front] = None
print('밥 손님 ----> : ', data)
front += 1
data = queue[front]
queue[front] = None
print('밥 손님 ----> : ', data)
front += 1
data = queue[front]
queue[front] = None
print('밥 손님 ----> : ', data)