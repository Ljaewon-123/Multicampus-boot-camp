def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 0
    # print(dic)
    for x in completion:
        if x in dic:
            dic[x] = dic[x]-1
    # print(dic)
    for k,v in dic.items():
        if v == 0:
            answer += k
    return answer