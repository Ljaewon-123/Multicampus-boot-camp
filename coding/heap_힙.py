def solution(scoville, K):
    answer = 0

    while any(K > i for i in scoville):  # any // for문을 쭉 돌면서 너무 오래걸림
        scoville = sorted(scoville)

        a = scoville.pop(0)
        b = scoville.pop(0)
        c = a + b * 2
        scoville.append(c)
        answer += 1
        if all(scoville) > K:
            break
        if len(scoville) < 2:
            return -1

    return answer