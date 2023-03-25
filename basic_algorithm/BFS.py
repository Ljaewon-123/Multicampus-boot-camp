# BFS 너비우선 탐색       간선에 길이가 같은 노드 탐색
from collections import  deque

def bfs(graph,start,visited):
    queue = deque([start])
    # 현재노드 방문
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        #아직 안방문 원소 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5, ], [3, 5], [3, 4], [7], [2, 6, 8, ], [1, 7]]
visited = [False] * 9
bfs(graph,1,visited)
