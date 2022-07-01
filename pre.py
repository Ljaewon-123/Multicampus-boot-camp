# nameAry = ['블','레','마마','에이','걸스','트와이스']
# imim = nameAry[2]
# dic = {'asdf':123,'asdf125':125}
# for i in dic:
#       print(i)
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# # for i in report.split():
# #       print(i)
#
# for i in set(report):
#       print(i)
#
# dic['asdf'] += 3
# print(dic)
#
moves = [1,5,3,5,1,2,1,4]
input_list = [2,2,2]
a = 5 % 5
print(a)
# print(len(set(input_list))==1)

# for i in range(len(moves)-1,0,-1):
#       print(moves[i])
#       print(moves)
      # del moves[i]

# for i in moves:
#       print(type(i))
# while True:
#       moves.pop()
#       print(moves)
#       if not moves:
#             break
# board = [
#     [0,0,0,0,0],
#     [0,0,1,0,3],
#     [0,2,5,0,1],
#     [4,2,4,4,2],
#     [3,5,1,3,1],
# ]
# print(board[3][0])
# print(board[1][2])
# print(len(moves))
# for i in range(len(moves)):
#     print(i)

# for i in range(10):
#     for j in range(5):
#         print(i, j,'asdfasdf')
#         if j == 3:
#             print(i,j)
#             break
# print(len(board)) # 열만 따짐

# # 문자지만 비교가 가능하다
# for i in nameAry:
#       print(i,end=' ')
#
#       if i > imim:
#             print('small')
#       elif i < imim:
#             print('big')
#       else:
#             print('asdfasdf')

def solution(answers):
    # 가장 많은 문제를 맞힌 사람을 나타내는 리스트
    answer = []
    # 수포자 1
    supo_1 = [1, 2, 3, 4, 5]
    # 수포자 2
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 수포자 3
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자가 맞은 수를 기록하는 배열
    cnt = [0, 0, 0]

    # 입력받은 답안을 토대로 각 수포자가 얼마나 맞았는지 탐색
    for i in range(len(answers)):
        # 수포자 1은 5를 주기로 반복
        if answers[i] == supo_1[i % 5]:  # 왜 반복하는지 알았음
            cnt[0] += 1
        # 수포자 2는 8을 주기로 반복
        if answers[i] == supo_2[i % 8]:
            cnt[1] += 1
        # 수포자 3은 10을 주기로 반복
        if answers[i] == supo_3[i % 10]:
            cnt[2] += 1

    # 가장 많이 맞춘 수
    max_cnt = max(cnt)

    # 가장 많이 맞춘 사람을 배열에 담기
    for i in range(3):
        # 가장 많이 맞춘 수와 같은 cnt 요소의 인덱스를 +1 하여 answer에 담기
        if max_cnt == cnt[i]:
            answer.append(i + 1)

    return answer


# print(solution([1, 3, 2, 4, 2, 2, 3, 1, 4, 5, 2, 3, 4]))
print(solution([1,1]))


aa = []
cnt = [0,1,1]
max_cnt = 1
for i in range(3):
    if cnt[i] == max_cnt:
        aa.append(i + 1)
print(aa)