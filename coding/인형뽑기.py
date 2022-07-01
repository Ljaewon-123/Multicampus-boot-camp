def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for pos in range(len(board)):  # 행렬 제대로 생각하고 맞추긴했음
            if board[pos][i - 1] == 0:
                pass
            else:
                print(board[pos][i - 1],pos,i-1)
                stack.append(board[pos][i - 1])
                board[pos][i - 1] = 0
                break  # 파이썬의 break는 for문 하나만 탈출한다 ' 라는 개념
    print(stack)
    for x in range(len(moves) - 1, 0, -1):
        # print(stack[x])
        if stack[x] == stack[x - 1]:
            answer += 1
            del stack[x]
            del stack[x - 1]
        else:
            del stack[x]

    return answer

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

solution(board,moves)