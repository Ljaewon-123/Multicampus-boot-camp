#### 원형 큐
# 오버헤드가 없다, % SIZE
# rear 과 front 의 시작이 0이냐 -1이냐 의 차이

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else :
        return False

def  isQueueFull() :
    global SIZE, queue, front, rear
    if  (rear+1) % SIZE == front :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if isQueueFull() :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if isQueueEmpty() :
        print('큐 텅~')
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅~')
        return None
    return queue[(front+1) % SIZE]

## 전역
SIZE = 5
queue = [ None for _ in range(SIZE)]
front = rear = 0

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('선미')
enQueue('재남')
print('출구<---', queue , '<--입구')
print('밥 손님:', deQueue())
print('밥 손님:', deQueue())
print('출구<---', queue , '<--입구')
enQueue('아이유')
print('출구<---', queue , '<--입구')
enQueue('재남')
print('출구<---', queue , '<--입구')