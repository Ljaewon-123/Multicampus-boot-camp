def solution(nums):   # 무조건 a만큼 뽑는건데 종류가 그 및이 안되는 조건만 찾으면됨
    answer = 0
    dic = {}
    a = int(len(nums) / 2)
    for i in nums:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    # print(dic)
    cnt = 0
    for k in dic.keys():
        cnt += 1
    # print(cnt,a)
    if cnt < a:
        return cnt
    else:
        return a