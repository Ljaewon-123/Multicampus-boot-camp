#### 스택 심화    함수화
## 함수
def isStackFull():
    global SIZE,stack,top
    if  top >= SIZE - 1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack,top
    if isStackFull() :
        print('stack full')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if top <= -1:
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if isStackEmpty() :
        print('stack empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():         # 맨위에 있는 top 확인
    global SIZE, stack, top
    if isStackEmpty() :
        print('stack empty')
        return None
    return stack[top]


## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1  # 스택의 초기화

## 메인
push('커피1')
push('커피2')
push('커피3')
push('커피4')
push('커피5')
print(stack)
# push('커피6')

retDate = pop()
print(stack,retDate)
retDate = peek()
print(stack,retDate)
