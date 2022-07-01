# def solution(id_list, report, k): 못품
#     dic = {}
#     lst = []
#     answer = []
#     for id in report:   # 신고자 리스트 만들기
#         reid = id.split()
#         if reid[1] in dic:
#             dic[reid[1]] = dic[reid[1]] + 1
#         else:
#             dic[reid[1]] = 1
#
#     # print(dic)
#     for key,v in dic.items():
#         if v >= k:
#             lst.append(key)
#     print(lst)
#     dic = {}
#     for id in id_list:
#         dic[id] = 0
#
#     for id in report:
#         reid = id.split()
#         for name in lst:
#             if reid[1] == name:
#                 dic[reid[0]] = dic[reid[0]] + 1
#
#
#     for i in dic.values():
#         answer.append(i)
#
#     return answer
#
#

# # result = [2,1,1,0]
# print(solution(id_list, report, k))

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}
    # print(answer)
    print(reports)
    print(set(report))
    for r in set(report): # 신고자 리스트 (여기까지는 같음) # split()랑 set이랑? set은 왜 dict ?? 그자리에 split()못씀 set쓰면 split처럼됨 이건 몰랐네 굳
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1  # 이거 개좋다 굿ㄷ

    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
solution(id_list, report, k)


''' Best
## set 잘쓰면서 여기는 왜 안썼냐 ㅋㅋㅋ 

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
'''
