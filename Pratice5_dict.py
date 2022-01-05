##### 연습문제 5   1번

# students = [{'name':'홍길동','korean':87,'math':98,'english':88,'science':95},
# {'name':'이몽룡','korean':92,'math':98,'english':96,'science':98,},
# {'name':'성춘향','korean':76,'math':96,'english':94,'science':90},
# {'name':'변학도','korean':98,'math':92,'english':96,'science':92},
# {'name':'박지성','korean':95,'math':98,'english':98,'science':98},
# {'name':'류현진','korean':64,'math':88,'english':92,'science':92},]
#
# print('이름\t 총점\t평균')
# b = 0
# for i in students:
#     print(i['name'],end=' ')
#     b = i['korean'] + i['math'] +i['english'] + i['science']
#     print(b,end = ' ')
#     print(b/4)

#### 연습문제 5 2번

# d = {}
# while(True):
#     a = input('영어 단어 등록 (종료는 quit): ')
#     if a == 'quit':
#         break
#     b = input(f'{a}의 뜻입력 (종료는 quit): ')
#     d[a] = b
#     # print(d)
#
# print(d)
#
# while(True):
#     a = input('영어 단어 입력 (종료는 quit): ')
#     if a == 'quit':
#         print('Exit!!!')
#         break
#     elif a not in d:
#         print(f'{a}는 사전에 없는 단어입니다')
#         continue
#     print(f'{a}의 뜻은 {d[a]}입니다')