import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    x = int(input())
    print(f'x는 머야 {x}')
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x) # 넣을 자료구조,들어갈수 heapq.heappush == 자동으로 정렬 오름차순

    else:
        heapq.heappush(right_heap, x)

    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)

    print(left_heap[0] * -1)