def solution(phone_book):
    answer = True
    dic = {x: 1 for x in phone_book}

    for p in phone_book:
        tmp = ""
        for num in p:
            tmp += num
            if tmp in dic and tmp != p:  # in 완전히 똑같아야 True임 문자열하고 다름
                # print(tmp,p)
                answer = False
                return answer
            else:
                pass
    return answer