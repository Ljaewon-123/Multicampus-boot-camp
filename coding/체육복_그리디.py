def solution(n, lost, reserve):  # 여벌 체육복 있는 사람은 딱 1벌만 더있는거
    answer = 0
    lst = [1 for _ in range(n)]
    # print(lst)
    for i in lost:
        lst[i - 1] -= 1
    for i in reserve:
        lst[i - 1] += 1
    print(lst)  # 0 이 있는게 중요한 거니까 0을 먼저 찾자
    # 0번지가 0인경우
    for i in range(len(lst)):
        if i == 0:  # 처음이 0인경우
            if lst[i + 1] == 2:
                lst[i + 1] -= 1
                lst[i] += 1
            else:
                pass
        elif i == len(lst) - 1:  # 끝이 0인경우
            # print(lst[len(lst)-1],lst[i-1],len(lst)-1)
            if lst[i - 1] == 2:  #
                lst[i - 1] -= 1
                lst[i] += 1
        elif lst[i] == 0:  # 그외 중간이 0인경우
            if lst[i - 1] == 2:
                lst[i - 1] -= 1
                lst[i] += 1
            elif lst[i + 1] == 2:  #
                lst[i + 1] -= 1
                lst[i] += 1

    print(lst)
    for i in lst:
        if i > 0:
            answer += 1
    return answer

'''
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''