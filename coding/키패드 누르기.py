def printData(numData):
    numData = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    for i in range(0, 4):
        for k in range(0, 3):
            try:
                print(numData[i][k], end='')
            except:
                pass
        print()
    print('--------------------------------------')


def count_move(num, pos, numData):  # 현재위치랑 목표위치랑 해서 총 몇칸 움직여야 하는지 찾아줌
    row = 0  # 결국 2,5,8,0 을 누를 때 필요한거
    col = 0
    x, y = find_location(pos, numData)
    for i in range(0, 4):
        for k in range(0, 3):
            if num == numData[i][k]:
                row = i
                col = k
                break
    a = row - x
    b = col - y
    a = abs(a)
    b = abs(b)
    total = a + b
    # print(a,b)
    return total


def move_pos(num):  # 왼쪽 오른쪽은 간단, 위치 알필요 없고 그냥 가서 누르면됨
    pos = num
    return pos


def find_location(pos, numData):  # 현재 손가락이 있는 위치를 찾아줌
    for i in range(0, 4):
        for k in range(0, 3):
            if pos == numData[i][k]:
                row = i
                col = k
                return row, col
    return 0, 0


def solution(numbers, hand):
    answer = ''
    numData = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    printData(numData)
    # a = numData[3][0]
    left_pos = numData[3][0]  # 시작위치
    right_pos = numData[3][2]  # 시작위치
    for i in numbers:
        if i in [1, 4, 7]:
            left_pos = move_pos(i)
            answer += 'L'
        elif i in [3, 6, 9]:
            right_pos = move_pos(i)
            answer += 'R'
        else:
            left = count_move(i, left_pos, numData)
            right = count_move(i, right_pos, numData)
            if left < right:
                left_pos = move_pos(i)
                answer += 'L'
            elif left > right:
                right_pos = move_pos(i)
                answer += 'R'
            else:
                if hand == 'left':
                    left_pos = move_pos(i)
                    answer += 'L'
                elif hand == 'right':
                    right_pos = move_pos(i)
                    answer += 'R'
    print(answer)
    return answer