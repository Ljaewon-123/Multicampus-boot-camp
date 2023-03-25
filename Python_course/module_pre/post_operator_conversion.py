# 중위 연산자를 후위 연산자로 바꾸기
# 파이썬의 리스트 특성을 최대한 활용해서 해보기

# a = '((A*B)-(C/D))'
# print(a)
def post_operator(a):
    symbol = []
    cnt = ''
    for i in a:
        if i == '(':
            pass
        else:

            symbol.append(i)
            if i != '*' and i != '+' and i != '-' and i != '/' and i != ')':
                cnt += symbol.pop()
                # print(cnt)
            elif i == ')':
                symbol.pop()
                cnt += symbol.pop()
    print(cnt)
    return cnt