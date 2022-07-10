def solution(a, b):
    answer = 0
    num_a = len(a)

    for x in range(num_a):
        answer += (a[x] * b[x])

    return answer