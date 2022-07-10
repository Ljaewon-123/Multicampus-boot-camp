def solution(priorities, location):
    answer = 0

    while True:
        a = priorities.pop(0)
        location -= 1
        for i in range(len(priorities)):
            if a < priorities[i]:
                priorities.append(a)  # 큰게 있으면 넣어주는거
                # print(priorities,a,i)
                if location == -1:
                    location = len(priorities) - 1
                    # print('heello')
                break
            else:
                if i == len(priorities) - 1:
                    answer += 1

        if location == -1:
            return answer

    return answer  # 몇번째로 인쇄 되는지