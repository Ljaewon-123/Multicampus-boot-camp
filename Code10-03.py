### 재귀함수  는 좀 느림
# 함수의 동작에 직접적으로 영향을 미친 변수가 있어야함

## 함수
def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)
## 전역

## 메인
print(addNumber(100))
