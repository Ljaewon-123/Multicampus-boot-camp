###### 연습문제4   3번

# heart = '\u2665'
#
# a = input('숫자를 여러개 입력하세요. ')
#
# for i in a:
#     x = int(i)
#
#     for y in range(x):
#         print(heart, end='')
#     print()


##### 연습문제4     1번


# a = input('이메일 입력: ')
#
# b = a.find('@')
# c = a.find('.')
# e = a.count('@')
# f = a.count('.')
# g = a.find(' ')
#
# if g == -1:
#     if b == -1 or c ==-1:
#         print('이메일 형식이 아닙니다')
#         # @ . 없는경우
#     elif b > c:
#         print('이메일 형식이 아닙니다')
#         # 바뀐경우
#     elif b - c == -1 :
#         print('이메일 형식이 아닙니다')
#         # 사이에 문자가 없는경우
#     elif e >= 2:
#         print('이메일 형식이 아닙니다')
#         # @2번이상
#     elif f >= 2:
#         print('이메일 형식이 아닙니다')
#         # . 두번이상
#     elif b == 0:
#         print('이메일 형식이 아닙니다')
#         # @ 앞에 문자
#     elif c == 0:
#         print('이메일 형식이 아닙니다')
#         # . 앞에 문자
#     else:
#         print('이매일 확인')
# else:
#     print('이메일 형식이 아닙니다')


#### 연습문제4     2번

# str_data = '{a1:20},{a2:30},{a3:15},' \
#             '{a4:50},{a5:-14},{a6:15},'\
#             '{a7:20},{a8:70},{a9:-100}'
#
# # a = str_data.find('}', i, i + 5)
# # print(a)
# cnt = 0
# for i in range(len(str_data)):
#     a = str_data.find('}', i, i + 5)
#     if ':' in str_data[i]:
#         # print(a)
#         # print(str_data[i+1:a])
#         x = str_data[i+1:a]
#         x = int(x)
#         cnt += x
# print(f'총 합계는: {cnt}')



