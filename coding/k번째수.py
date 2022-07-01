def solution(array, commands):
    answer = []
    for lst in commands:
        a = array[lst[0]-1:lst[1]] # TypeError: 'NoneType' object is not subscriptable 안되면 한번에 하지말고 나눠서 일단 해보자
        a.sort()
        print(a)
        answer.append(a[lst[2]-1])

    print(answer)
    return answer

array =[1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array,commands)