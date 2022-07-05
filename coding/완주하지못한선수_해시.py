def solution(participant, completion):
    answer = ''

    for i in range(len(participant) - 1, -1, -1):

        for x in range(len(completion) - 1, -1, -1):
            if participant[i] == completion[x]:
                del participant[i]
                del completion[x]
                break

    for i in participant:
        answer += i
    return answer