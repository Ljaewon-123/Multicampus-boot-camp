def com(lst):      # 못품
    b = 1
    for i in lst:
        b *= i
    return b


def solution(clothes):
    answer = 0
    lst = []
    dic = {clothes[x][1]: [] for x in range(len(clothes))}
    # print(dic)
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
    # print(dic)
    for k in dic.keys():
        lst.append(len(dic[k]))
    lst = [4, 1, 1, 1]  # 1묶 7 2묶 15 3묶 13 4묶 4
    answer += sum(lst)
    print(dic)  # [2,1,1,1] 이면 2개씩 묶음일때 12 [2,1,1,1] 3개씩 묶음 8개 4개씩 2개
    print(lst)
    print(answer)
    num = len(lst)
    if len(lst) > 1:
        for i in range(1, num):
            a = i + 1  # 몇묶음??
            c = lst[:a]
            answer += com(c)
            for j in range(a - 1, -1, -1):
                for x in range(1, num):
                    if x + 1 >= num:
                        break
                    c.pop(j)
                    c.insert(j, lst[x + 1])
                    answer += com(c)
                    print(answer)

    print(answer)
    return answer