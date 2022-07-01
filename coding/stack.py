def in_stack(progresses,speeds):
    num = len(progresses)
    lst = []
    lst2 = []
    for i in speeds:
        lst2.append(i)
    answer=[]
    # print(lst2)
    for n in range(num):
        a = progresses.pop()
        b = lst2.pop()
        c = a+b
        lst.append(c)  # 역순으로 들어감
    lst = reversed(lst)
    # answer = lst.reverse()
    for i in lst:
        answer.append(i)
    # print(answer)
    return answer


def get_pop(lst):  # 0번지를 확인하고 이후 번지가 100인지 아닌지만 확인 하면됨
    cnt = 0
    print(lst)
    if len(lst) >= 2:
        for i in lst:
            if i >= 100:
                cnt += 1
                # print('100이 되잖아')
            else:
                break
        print(cnt)
        del lst[:cnt]
        return cnt
    elif len(lst) == 1:
        if lst[0] >= 100:
            return -1
        else:
            return 0
    else:
        return -2


def solution(progresses, speeds):
    answer = []
    num = len(progresses)

    while True:
        progresses = in_stack(progresses, speeds)
        cnt = get_pop(progresses)
        if cnt == -1:
            break
        elif cnt == 0:
            continue
        elif cnt >= 1:
            answer.append(cnt)
        if cnt == -2:
            print(answer, 'asdf')
            return answer
    answer.append(-cnt)
    print(answer,'asdf')
    return answer

progresses =[95, 90, 99, 99, 80, 99]
speeds =[1, 1, 1, 1, 1, 1]
solution(progresses,speeds)