#### 선택 정렬2 (완전)
import random

## 함수
# def selectionSort(ary):
#     n = len(ary)
#     for cy in range(0,n-1):
#         minIdx = cy
#         for i in range(cy+1, n):
#             if ary[minIdx] > ary[i]:
#                 minIdx = i
#         ary[cy], ary[minIdx] = ary[minIdx] , ary[cy]
#     return ary

def selectionSort(ary):     #### ?? 내림차순
    for i in range(len(ary)):
        for j in range(i,0,-1):
            if ary[j] > ary[j-1]:
                ary[j], ary[j-1] = ary[j-1], ary[j]
            # else:                 ## 이거 두줄이 들어가면 오름차순
            #     break
    return ary

## 전역
dataAry = [random.randint(100,200) for _ in range(8)]

## 메인
print('정렬 전-->',dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후-->',dataAry)