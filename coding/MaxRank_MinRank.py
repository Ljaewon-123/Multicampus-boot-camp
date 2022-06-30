def order(num):
    if num <= 1:
        result = 6
    elif num == 2:
        result = 5
    elif num == 3:
        result = 4
    elif num == 4:
        result = 3
    elif num == 5:
        result = 2
    elif num == 6:
        result = 1
    return result

def solution(lottos, win_nums):
    cnt_min = 0
    cnt_max = 0
    combine = 0
    for lot in lottos:
        if lot == 0:
            cnt_max += 1
            continue
        for win in win_nums:
            if win == lot:
                cnt_min += 1
    combine = cnt_min + cnt_max
    cnt_min = order(cnt_min)
    cnt_max = order(combine)
    answer = [cnt_max,cnt_min]
    return answer


lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]
# result = [3,5]
solution(lottos,win_nums)


''' Best
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''

