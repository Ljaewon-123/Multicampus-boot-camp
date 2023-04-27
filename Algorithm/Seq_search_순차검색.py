#### 순차 검색
import random

## 함수
def seqSearch(ary,fdata):
    pos = -1
    size = len(ary)
    for i in range(0, size, 1):  # (size)
        if (ary[i] == fdata):
            pos = i
            break
    return pos


## 전역
SIZE = 10
dataAry = [random.randint(1,99) for _ in range(SIZE)]
findData = dataAry[random.randint(0,SIZE-1)]
# findData = choice(dataAry)
## 메인
print('배열-->',dataAry)
postion = seqSearch(dataAry,findData)
if postion == -1:
    print(findData,'없음')
else:
    print(findData,'가',postion,'에 있음')


