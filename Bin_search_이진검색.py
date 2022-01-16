### 이진검색
# 사전에 정렬이 필요
import random
## 함수
def binSearch(ary,fdata):       ## 몇번째 데이터 인지를 구하는거
    pos = -1
    start = 0
    end = len(ary)-1
    while start <= end:
        mid =( start + end ) // 2
        if fdata == ary[mid]:
            return mid
        elif fdata > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

## 전역
SIZE = 10
dataAry = [random.randint(1,99) for _ in range(SIZE)]
findData = dataAry[random.randint(0,SIZE-1)]
dataAry.sort()  ## 정렬


## 메인
print('배열-->',dataAry)
postion = binSearch(dataAry,findData)
if postion == -1:
    print(findData,'없음')
else:
    print(findData,'가',postion,'에 있음')