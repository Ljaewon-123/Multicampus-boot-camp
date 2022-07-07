def Excute(lst):
    a = len(lst) / 2 -1

    for i in range(a):
        func(x,a,i)


    for x in range(len(lst)-1,0,-1):
        tmp = lst[0]
        lst[0] = lst[x]
        lst[x] = tmp

