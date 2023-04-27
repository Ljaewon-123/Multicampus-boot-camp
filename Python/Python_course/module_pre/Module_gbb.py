# Module_gbb

from random import *

def gbb_game(you_n):
    com_n = randint(1, 3)

    if (com_n - you_n) == -2 :
        print('computer Win 컴퓨터가 이김')
        print(f'COM : {com_n}')
    elif (com_n - you_n) == 1:
        print('computer Win 컴퓨터가 이김')
        print(f'COM : {com_n}')
    elif (com_n - you_n) == 0:
        print('draw 비김')
        print(f'COM : {com_n}')
    else:
        print('User Win 유저가 이김')
        print(f'COM : {com_n}')

def input_num():
    a = int(input('you 입력 (1:가위, 2:바위 ,3:보) : '))
    gbb_game(a)
