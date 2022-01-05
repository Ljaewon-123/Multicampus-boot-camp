# #### 파일 입출력 1번문제
#
# f = open("yesterday.txt", 'r')
#
# data = f.read().lower()
# data1 = data.split()
#
# print(data1)
# d = {}
#
# for i in data1:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i]  = 1
# print(d)
# for x ,y  in d.items():
#     print(x + ':' + str(y))


# #### 파일 입출력 2번 문제
# def sum(inputfile,save_file):
#
#     f = open(inputfile, 'r')
#     f1 = open(save_file,'w',encoding='utf-8')
#     data = f.read()
#     data1 = data.split()
#     print(data1)
#     data2 = [eval(data1[i] + '+' + data1[i+1]) for i in range(0,len(data1),2)]
#     print(data2)
#     i = 0
#     x = 0
#     while True :
#
#         a = data1[i] + '+' + data1[i+1] + '=' + str(data2[x])
#         print(a+'.0')
#         i += 2
#         x += 1
#         f1.write(a + '.0\n')
#         if x == len(data2):
#             break
#
# def main():
#     sum('list_num.txt', 'file1.txt')
#
# if __name__ == '__main__':
#     main()


# ####  파일 입출력 3번문제

# def input_member(input_file):
#     f = open(input_file,'a',encoding='utf-8')  # 저장되어있는 명단? 덮어씌기?
#     while True:
#         x = input('맴버를 입력하세요 (종료는 q) : ')
#         if x == 'q':
#             break
#         f.write(x+'\n')
#
#     f.close()
#
#
# def output_member(output_file):
#     f = open(output_file,'r',encoding='utf-8')
#     data = f.read()
#     print(data)
#
#
# def main():
#     while True:
#         b = input('저장 1, 출력 2, 종료 q : ')
#         if b == '1':
#             a = input('맴버 명단을 저장할 파일명을 입력하세요 : ')
#             input_member(a)
#         elif b == '2':
#             a = input('맴버 명단을 저장할 파일명을 입력하세요 : ')
#             output_member(a)
#         elif b == 'q':
#             break
#
# if __name__ == '__main__':
#     main()
