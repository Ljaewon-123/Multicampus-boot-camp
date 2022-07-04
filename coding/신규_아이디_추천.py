def solution(new_id): # 처음부터 했어야 했는데 중간 확인 안하고 쭉 달리다 보니 늦음 예제만 맞고 정확도 낮음
    answer = ''
    new_id = new_id.lower()
    new_id = list(new_id)
    print(new_id)
    for id in new_id:
        if not (id.isalpha() or id.isdigit() or id == '-' or id == '_' or id == '.'):
            a = new_id.index(id)
            new_id[a] = ''
    if not new_id or new_id[0] == '':
        pass

    # new_id = "".join(new_id)
    for new in range(len(new_id)):
        if new_id[new] == '.':
            if new == len(new_id)-1:
                break
            if new_id[new + 1] == '.':
                new_id[new] = ''
    print(new_id)
    new_id = "".join(new_id) # 빈칸을 없앰
    print(new_id)
    new_id = list(new_id)
    print(new_id)

    if new_id[0] == '.':
        del new_id[0]

    if new_id[-1] == '.':
        del new_id[-1]
    print(new_id,'asdf')
    if not new_id:
        new_id.append('a')
    if len(new_id) >= 16:
        del new_id[15:]
    print(new_id,'qwer')
    if new_id[-1] == '.':
        del new_id[-1]
    print(new_id)
    while True:
        if len(new_id) <= 2:
            new_id.append(new_id[-1])
        elif len(new_id) >= 3 :
            break
    print(new_id)
    new_id = "".join(new_id)  # 여기여기 join
    answer = new_id
    print(answer)
    return answer


new_id = "z-+.^."
'''
"
예1 "...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	"z--"
예3	"=.="	"aaa"
예4	"123_.def"	"123_.def"
예5	"abcdefghijklmn.p"
'''


solution(new_id)

''' Best  로직 비슷한데 그냥 ㅁㄴㅇㄻㄴㅇㄻㄴㅇㄹ

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
'''