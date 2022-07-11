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

'''
파이썬 데큐 쓰는것도 알아야할듯... 몰라도 되나? enumerate 이거 좋네 리스트랑 인덱스랑 붙어서 동작해야할 때 특히 더 좋은듯 

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]   # i 가 인덱스가 되니까 location 하고 똑같아짐 
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        print(cur)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            print(queue)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''