# 스택 -> 리스트 사용 최상단 원소 출력 print(stack[::-1]  최하단 print(stack)  stack.append() stack.pop() stack =[]
# # 큐 구현 예제
# from collections import  deque
# queue = deque()
# queue.append()  -> 삽입
# queue.popleft()  -> 삭제
# print(queue)  #들어온 순서
# queue.revers() -> 역순 출력
# print(queue)  # 나중에 들어옴

# # 힙(Heap) 의 특징
# 힙은 항상 완전이진트리 자료구조
# 힙에서는 항상 루트노드를 제거 합니다
# 최소힙 루트 노드가 가장작은 값 값이 작은 데이터 우선 제거
# 최대힙 루트 노드가 가장큰 값 값이 큰 데이터 우선 제거

# ## 우선순위 큐 라이브러리를 활용한 힙 정렬 구현
# import sys
# import heapq        #최소힙
# input = sys.stdin.readline()
#
# def heapsort(iterable):
#     h = []
#     result = []
#     #모든 원소를 차례대로 힙에 삽임
#     for value in iterable:
#         heapq.heappush(h,value)
#     #힙에 합입도니 모든 원소를 차례대로 꺼내어 담기
#     return result
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.appen(int(input()))
# res = heapsort(arr)
# for i in range(n):
#     print(res[i])
