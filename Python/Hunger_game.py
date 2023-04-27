from random import *

fruit = ['apple', 'banana', 'oranges']
x = randint(0, 2)
y = fruit[x]
word = ''

while True:
    succeed = True
    print('answer : {0}'.format(y))
    for i in y:
        if i in word:
            print(i,end = ' ')
        else:
            print('_',end = ' ')
            succeed = False
    print()

    if succeed:
        print('succeed')
        break

    a = input('Input letter > ')
    if a in y:
        print('Correct\n')
    else:
        print('Incorrect\n')
        a = ' '
    word = word + a