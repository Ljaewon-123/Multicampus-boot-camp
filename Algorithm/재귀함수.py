### 재귀함수

## 함수
def openBox():
    global count
    print('open box')
    count -= 1
    if count == 0:
        print('rings IN')
        return
    openBox()
    print('종이상자 닫기')
    return



## 전역
count = 10
## 메인
openBox()
