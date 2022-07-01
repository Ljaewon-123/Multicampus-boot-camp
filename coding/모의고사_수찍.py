def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    su1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ]

    for i in range(len(answers)):
        # 수포자 1은 5를 주기로 반복
        if answers[i] == su1[i % 5]:
            cnt[0] += 1
        # 수포자 2는 8을 주기로 반복
        if answers[i] == su2[i % 8]:
            cnt[1] += 1
        # 수포자 3은 10을 주기로 반복
        if answers[i] == su3[i % 10]:
            cnt[2] += 1
    # len(set(cnt))==1 좋은 방법이긴 한데 여기선 아님
    # answer.append(cnt.index(max(cnt)) + 1) 최대치 뽑을 때 좋은데 다른 조건에서 걸려서 못씀
    max_cnt = max(cnt)

    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i + 1)

    return answer

# answers	= [1,2,3,4,5]
answers = [1,1]
solution(answers)

