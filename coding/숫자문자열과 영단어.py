def solution(s):
    answer = 0
    msg = ''
    lst = []
    cnt = 1
    dic = {}
    alpha = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', ]
    for i in alpha:
        dic[i] = cnt
        cnt += 1
        if i == 'zero':
            dic[i] = 0
    print(dic)

    for i in s:
        msg += i
        # print(msg)
        if msg in alpha:

            lst.append(str(dic[msg]))
            msg = ''
        elif msg.isdigit():
            lst.append(msg)
            msg = ''
    print(lst)
    for i in lst:
        msg += i
    answer = int(msg)
    return answer