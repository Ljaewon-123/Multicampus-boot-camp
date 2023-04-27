import random

### 기본 정렬 알고리즘

## 함수
def findMinIndex(ary):  ## 가장 작은 수
    minIdx = 0
    for i in range(1,len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

## 전역
testAry = [random.randint(0,99) for _ in range(20)]


## 메인
print(testAry)
minPos = findMinIndex(testAry)
print('최솟값--->',testAry[minPos])