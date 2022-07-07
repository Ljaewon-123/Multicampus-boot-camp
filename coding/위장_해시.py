'''
로직은 괜찮은데 답까지의 한걸음이 부족함
딕셔너리 이용해서 풀때는 왠만하면 벨류에 숫자만 넣고 할 수있게 다 그렇게품 복잡하게 안하네...

답을 풀수있는 다른 방법을 생각해보자 이거 return cnt-1 따위 될줄 알았으면 나도 풀었는데
완전탐색트리 같은거 생각하고 있었음 아무도 그렇게 짤 생각 안했는데 나만 하고있었음 다 왔는데 혼자 어렵게 풀어서 못풀면 너무 억울하자나
'''

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
    for i in clothes:                       # 요소들을 딕셔너리 넣고 종류와 몇개인지 세는 리스트를 만듬
        if i[1] in dic:
            dic[i[1]].append(i[0])
    # print(dic)
    for k in dic.keys():
        lst.append(len(dic[k]))
    # lst = [4, 1, 1, 1]  # 1묶 7 2묶 15 3묶 13 4묶 4
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


'''Best
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:  # items() 안써도 됨 
        if t not in clothes_type:  
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
'''