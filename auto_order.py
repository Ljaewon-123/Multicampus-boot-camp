class SoldOutError(Exception):
    pass
chicken = 10
waiting = 1
try:
    while(True):
        print('[남은 치킨: {0}]'.format(chicken))
        order = int(input('치킨 몇마리 주문 하시겠습니까??'))
        if order < 1 or order == '':
            raise ValueError
        if order > chicken:  # 남은 치킨보다 주문량이 많을때
            print('재료가 부족합니다')
        else:
            print(f'[대기번호 {waiting}] {order}마리 주문이 완료되었습니다.')
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
except ValueError as e:
    print(e)
    print('잘못된 값 입력')

except SoldOutError:
    print('재고가 소진되어 더이상 주문을 받지 않습니다')
