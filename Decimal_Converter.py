

# B = [list(map(int, x)) for x in a]      ##### !! 중요 문자열 -> int 로 반환

b =[]*8

def binary(num):
    while(True):
        a = divmod(num, 2)

        while (num > 1):

            if 0 in a:
                print(0, end = "")
                b.append(0)
                num = a[0]
                break
            elif 1 in a:
                print(1, end="")
                num = a[0]
                b.append(1)
                break
        if 0 == num:
            print(0, end="")
            b.append(0)
            break
        elif 1 == num:
            print(1, end="")
            b.append(1)
            break
    # print()
    string = "".join([str(_) for _ in b])
    print(string[::-1])     # 뒤집어줌  현재 string는 문자열 상태  최종결과
    return b    # 무엇을 리턴해야 할까?


def Re_converter(return_num):
    # a = divide(286)
    # print(a)          # 그냥 return 을 바꿔서 한번에
    y = []
    for i in range(len(return_num)):
        if return_num[i] == 0:
           y.append(0)
        else:
           y.append(2**i)
    # print(y)
    cnt = 0
    for i in y:             # lambda? # 리스트 컴프리헨션(list comprehension) ?? 리스트가 필요없음
        cnt += i
    print(cnt)

binary(286)
Re_converter(binary(286))


