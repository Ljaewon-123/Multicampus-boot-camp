## 선형 리스트
# 오버헤드라는 단점이 존재함 ( 삽입,삭제)가 오버헤드를 생성 그럼 삽입,삭제가 없다면?
# 가끔 일어나는 오버헤드는 감당할 가치가 있다
# 공간 측면에서 연결리스트보다 유리 데이터 접근속도가 빠름
# 시계열 데이터 (시간순서로 생성되는 데이터) 신문의 날짜별 기사.고전 소설 연대별


# 함수 선언부
def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

def insert_data(postion,friend):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1,postion,-1):
        katok[i] , katok[i-1] = katok[i-1],katok[i]
        # katok[i] = katok[i-1]  # 다른 방법
        # katok[i-1] = None
    katok[postion] = friend

def delete_data(postion):
    katok[postion] = None
    klen = len(katok)
    for i in range(postion+1,klen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])

# 전역 변수부
katok = []

## 메인 코드부

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')


insert_data(3,'미나')

delete_data(4)

# katok.append(None)  #1
# katok[6] = katok[5]   #2
# katok[5] = None
# katok[5] = katok[4]
# katok[4] = None
# katok[4] = katok[3]
# katok[3] = None
# katok[3] = '미나'  # 3

print(katok)
while True:
    print('선택하세요(1:추가 , 2:삽입, 3:삭제, 4:종료')
    select = int(input('추가할 데이터'))
    if select == 1:
        add_data(select)
        print(katok)
    elif select == 2:
        pos = int(input('추가할 위치 --->'))
        data = int(input('추가할 데이터 --->'))
        insert_data(3, pos)
        print(katok)
    elif select == 3:
        delete = int(input('삭제할 위치 --->'))
        delete_data(delete)
        print(katok)
    elif select == 4:
        print(katok)
        break
