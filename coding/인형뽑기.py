def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for pos in range(len(board)):  # 행렬 제대로 생각하고 맞추긴했음
            if board[pos][i - 1] == 0:
                pass
            else:
                # print(board[pos][i - 1],pos,i-1)
                stack.append(board[pos][i - 1]) # 넣어준 순간에 터쳐야함
                board[pos][i - 1] = 0
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        answer += 2
                        del stack[-2]
                        del stack[-1]
                break  # 파이썬의 break는 for문 하나만 탈출한다 ' 라는 개념
    print(stack)

    print(answer)
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