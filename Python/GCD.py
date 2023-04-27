a ,b = 12, 18

cd = divmod(a,12)

# print(cd)
def GCD(a,b):
    lst1 =[]
    for i in range(1,a+1):
        cd = divmod(a,i)
        if cd[1] == 0:
            # print(i)
            lst1.append(i)
    lst2 = []
    for i in range(1,b+1):
        cd = divmod(b,i)
        if cd[1] == 0:
            # print(i)
            lst2.append(i)

    print(lst1,lst2)
    lst3 = []
    for i in lst1:
        for j in lst2:
            if i ==j :
                lst3.append(j)

    print(max(lst3))
    gcd = max(lst3)
    return gcd

GCD(72,90)

