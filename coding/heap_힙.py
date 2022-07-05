import heapq


def insert_heapq(lst):
    h = []
    # 모든 원소를 차례대로 힙에 삽임
    for value in lst:
        heapq.heappush(h, value)
    # 힙에 합입도니 모든 원소를 차례대로 꺼내어 담기

    return h


def check_heap(heap, K):  # 낼름
    a = heapq.heappop(heap)
    if a < K:
        heapq.heappush(heap, a)
        return True
    elif a >= K:
        heapq.heappush(heap, a)
        return False


def solution(scoville, K):
    answer = 0
    heap = insert_heapq(scoville)
    # print(heap)
    # print(heapq.heappop(heap))
    # print(heap[0])
    while check_heap(heap, K):
        if len(heap) < 2:
            return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        c = a + (b * 2)
        heapq.heappush(heap, c)
        answer += 1
        # print(heap)

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville,K)