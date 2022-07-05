def solution(scoville, K):  # 무조건 heap써야하나봄 시간때문에 ㅋㅋ
    answer = 0

    while True:
        if len(scoville) < 2:
            return -1
        scoville = sorted(scoville)

        a = scoville.pop(0)
        b = scoville.pop(0)
        c = a + b * 2
        scoville.append(c)
        answer += 1
        print(answer)
        print(scoville)
        if scoville[0] > K:
            break


    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville,K)