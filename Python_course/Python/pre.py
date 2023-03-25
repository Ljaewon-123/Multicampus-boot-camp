#### 연습문제 2_2의 1번
# a = input('16진수 한글자 입력: ')
#
# if a == 'A':
#     print('10진수 ==> 10')
# elif a == 'B':
#     print('0진수 ==> 11')
# elif a == 'C':
#     print('0진수 ==> 12')
# elif a == 'D':
#     print('0진수 ==> 13')
# elif a == 'E':
#     print('0진수 ==> 14')
# elif a == 'F':
#     print('0진수 ==> 15')
# else:
#     print('16진수가 아닙니다')

##### 연습문제 2_2의 2번

# a = int(input('교환할 돈은 얼마? '))
# M_50000 = a //50000
# a %= 50000
# M_10000 = a // 10000
# a %= 10000
# M_5000 = a // 5000
# a %= 5000
# M_1000 = a // 1000
# a %= 1000
# M_500 = a // 500
# a %= 500
# M_100 = a // 100
# a %= 100
# M_50= a // 50
# a %= 50
# M_10= a // 10
# a %= 10
#
# print(f'50000 원{M_50000}장,',end = '')
# print(f'50000 원{M_10000}장,',end = '')
# print(f'50000 원{M_5000}장,',end = '')
# print(f'50000 원{M_1000}장,')
# print(f'50000 원{M_500}장,',end = '')
# print(f'50000 원{M_100}장,',end = '')
# print(f'50000 원{M_50}장,',end = '')
# print(f'50000 원{M_10}장,')
# print(f'바꾸지 못한 돈 ==> {a}원')




###  연습문제 2_2의 3번

# from random import *
#
# a = randint(1,6)
# b = randint(1,6)
#
# print(f'A의 주사위 숫자는 {a}입니다.')
# print(f'A의 주사위 숫자는 {b}입니다.')
# if a > b:
#     print('A user Win')
# elif a < b:
#     print('B user Win')
# else:
#     print('Draw')


##### 연습문제 3 의 1번

# for y in range(5):
#     for x in range(1,6-y):
#         print('*',end = '')
#     print()


#######  연습문제 3 의 2번

# for y in range(1,6):
#     for x in range(5-y):
#         print(end=' ')
#     for z in range(2 * y-1):
#         print('*', end='')
#
#
#     print()




##### 연습문제 3 의 3번

# a = input('숫자입력 : ')
#
# while True:
#     a = input('다시입력 : ')
#
#     if a == '7':
#         print(f'{a}입력! 종료')
#         break

##### 연습문제 3 의 4번

# a = int(input('현재잔액: '))
# cnt = 1
# while True:
#     print(f'노래를 {cnt}곡 불렀습니다.')
#     a -= 2000
#     cnt += 1
#     print(f'현재 {a}원 남았습니다.')
#
#     if a == 0:
#         print('잔액이 없습니다. 종료합니다.')
#         break


# split() 구분자 (공백, 콤마, 기준 으로 문자열 나눔)
# 리스트로 변환
# capitalize() 문장의 첫번째 문자열의 첫문자를 대문자
# title() 각단어의 첫문자를 대문자로 변경
# swapcase() 대문자는 소문자로, 소문자는 대문자로 변경
# strip() 문자열의 앞뒤의 공백을 제거
# lstrip() 문자열의 왼쪽 공백을 제거
# rstrip() 문자열의 오른쪽 공백을 제거
# isalpha()  문자여부 결과 반환
# isdigit() 숫자인지 결과 반환
# isspace() 하나의 문자에 대해 공백여부 반환
# isalnum() 문자또는 숫자인지 확인
# islower() 소문자 여부
# isupper() 대문자 여부
# ljust(자리수)  왼쪽 정렬
# rjust(자리수)  오른쪽 정렬
# center():가운데 정렬



# string = 'python'
# a = 1234
# print(a)
# print('{:->10}'.format(a))
# print('{:-^10}'.format(a))

# x=[1,2,3,4]
# x.insert(0,10)
# x.pop()
# x.remove(3)
# print(x)
#
# a = [4,5,8,2,3,9,1]
# a.extend(1)
# print(a)
# a.sort(reverse=True) # 내림차순 정렬
# print(a)
# sorted()  # 원본변경안함
# a.sort(key=str.lower) # 대소문자 구분 안하고함
#
# a_sort = sorted(a,reverse= True)
# print(a_sort)

# s4 = {1,3,2,4,5,5,6,3}
# print(s4)
# s4.add(10)  # 하나 추가
# print(s4)
# s4.update([11,12])  #여러개 추가
# print(s4)
# s5 = {1,2,[3,4]} # 내부리스트 포함 안됨 튜플은 가능
# s6 = {1,2,3,4,}
# s6.remove(1)  # 없으면 에러
# s6.discard(1) # 에러 안뜸
# # 요소 전체를 지움
# s6.clear()
# print(s6)
# # del   변수 자체부터 다 지움
# return 문을 만나면 함수를 바로종료
# return 을 여러개를 한변수에 담으면 리스트 형식으로 됨
# 가변길이 매개변수 : *args ,**kwargs
# 매개변수가 정해져 있지 않은 경우, 여러개값 전달받을때
# *args : arguments 인수값을 받음     #언패킹
# **kwargs : keyWord arguments 의 약자, key = value 값을 받음  딕셔너리 유용
# def sumN(*args):
#     total = 0
#     for x in args:
#         total += x
#     print(total)
#
# def ad(a,*args):      # * 튜플로 나오냐 나오지 않냐의 차이  print(*args)를하게 되면 형식무시 숫자그대로출력
#     print(a,args)
#     print(a,*args)
# ad(1,2,3,4,5)

# sumN(1,2,3)
# sumN(1,2,3,4,5)
# sumN(1,2,3,4,5,1,6,1,2)
# def show(**k):   키 = 값  사실상 튜플을 넣을때 사용하는것
#     for key in k.keys():
#         print(key,end =  ' ')
#     print()
#     for value in k.values():
#         print(value,end = ' ')
#     print()
#     for item in k.items():
#         print(item,end = '')

# def ast(a,**kwargs):
#     print(a,kwargs)
#     print(a,*kwargs)
# ast(1,b=2,c=3,d=4)

# show(name='홍길동',id = '123', phone = '12312412')
# 전역변수를 단순히 가지고 오는 경우엔 global 생략 가능 변경될때만 구분지을것
# a = 10
# def show():
#     global a  # 함수내부에서 전역변수 바꾸기
#     a = a + 1
#     print(a)
# show()
# print(a)
# def outF(x,y):
#     def inF(a,b):
#         return a+b
#     return inF(x,y)
#
# print(outF(12,20))

# 12-29

# abs() 절대값 계산
# all() 모든 요소가 참이면 True
# iterable (반복 가능한 자료형): 리스트 튜플 딕셔너리
# any() 하나라도 참이면 True
# True : 0이 아닌값 False : 0
# chr() 아스키코드 문자
# ord() 문자에 대한  아스키 코드값 반환      좋은데????
# divmod(a,b) a를 b로나누 몫과 나머지 반환   (몫,나머지)
# enumerate() 시퀀스를 인덱스와 값을 포함해서 enumerate 형의 객체로 반환  (인덱스,값)
# 시퀀스 : range() ,문자열,리스트,튜플
# for i , season in enumerate(['봄','여름','가을','겨울']):    (인덱스,값)
#     print(i,season)
# eval(표현식) 표현식의 연산 결과 반환
# print(eval('10 + 3'))
# print(eval(' x + 1'))     x = 1
# filter(function,iterable) iterable자료의 요소를 function로 거름
# def pos(x):
#     return x>0
# print(list(filter(pos,[0,1,-1,10,-3,5])))
# pow(x,y)   x의 y 제곱 x**y
# add2 = lambda  x,y : x+y
# print(add2(10,20))
# add3 = lambda  x = 10,y = 10 : x+y
# print(add3(10,20))
# print(add3())
# map()  리스트나 튜플,문자열 등 반복가능한 구조의 요소별로 지정된 함수를 적용 하여 원본은 변경하지않고 list,tuple로 반환
# list(map(함수,리스트)) tuple(map(함수,튜플))
# num1 = [1,2,3,4]
# def add10(num):
#     for i in range(len(num)):
#         num[i] += 10
#     print(num)
#
# add10([1,2,3])
# num2 = list(map(lambda num:num+10,num1))
# print(num2)
# number1 = [3.5,3.4,2.0,4.6]
# num1 = list(map(lambda num:int(num),number1))
# print(num1)
# num1 = list(map(int,number1))
# print(num1)
# print((lambda x:x+10)(25))    람다 표현식을 변수 할당않하고 그 자체를 호출해서 사용
# zip(*iterable): iteralbe에서 동일한 인덱스 요소를 추출하여 묶어서 반환
# print(zip([1,2,3,],[4,5,6]))
# print(list(zip([1,2,3,],[4,5,6])))  # 튜플형태로 나옴  print(dict(zip(['a','b','c'],[4,5,6])))  #딕셔너리 형태로 나옴
# from 모듈명 import 변수명 or 함수명
# __시작하는 스페셜변수나 메서드 를 제외한 모든것을 참조 from random import *
# import sys
# sys.path.append('C:\Python_Word\Day1')  #모듈이 있는 파일 경로 확정
# if __name__ == '__main__':
# def main():
#     Module_gbb.input_num()

#   01-03

# if __name__ == '__main__':
#     main()
#  패키지는 디렉터리 안에 __init__.py가 있는것과 같다(비어있다)
# 패키지를 사용할 경우 모듈 import
# import는 패키지.모듈명
# import는 패키지.모듈명 as 별명
# from 패키지.모듈 import 함수
# from 패키지.모듈 import **
# from으로 시작하는건 함수를 import시키는거라 모듈. 등이 필요없다

# 패키지를 파이참 구성하는 방법
# [파일]->[new]->[python package]-> package 이름입력시 생성
# 패키지 생성되면 __init__.py 존재를 확인 가능

# import My_pack.pack1.module11
# My_pack.pack1.module11.fun11()
# import My_pack.pack1.module11 as m1
# m1.fun111()
# from My_pack.pack1.module11 import  fun11
# fun11()
# from My_pack.pack1.module11 import  *
# fun11()
# fun111()

# 리스트 컴프리헨션(list comprehension)
# 리스트를 빠르게,간결하게처리 :파아썬 코드 스타일
# result = [i for i in range(10)]
# result = [i for i in range(10) if i%2==0]           # 짝수만
# result2 = [i  if i%2==0 else 10 for i in range(10)]  # 짝수 가져오고 아닌값은 10을 표기해라
# 리스트 컴프리션의 이중 중첩 for문
# list1 = ['a','b','c']
# list2 = ['D','E','F']
# result = [j+i for i in list1 for j in list2  if not(i==j) ]
# print(result)
# 리스트 컴프리션의 문자열
# word = 'remeber to let her into your hert'.split()
# result = [[w.upper(), w.lower(), len(w)] for w in word]
# print(result)

# f = open('C:\Python_Word\DDPython_pre\\file1.txt','w')   #경로표시
# f.close()
#               한글 사용과 만들면서 쓰기
# data = '안녕'
# f = open('file2.txt','w',encoding = 'utf-8')
# f.write(data,)
# f.close()

# a = f.readline() : 한줄씩 읽어오기
# # 한줄만 읽어오기
# f = open('file1.txt','r',encoding='utf-8')
# line = f.readline()     #첫번째 라인 1개 읽기
# print(line)
# f.close()

# # 한줄씩 읽어오기
# f2 = open('file1.txt','r',encoding='utf-8')
# while True:
#     line = f2.readline()
#     if not line:
#         break
#     print(line,end= '')
# f2.close()
#
# # readlines() : 전체 라인을 읽어오기   여러개열을 리스트로 반환
# f3 = open('file1.txt','r',encoding='utf-8')
# lines = f3.readlines()
# print(lines)
# f3.close()

# f3 = open('file1.txt','r',encoding='utf-8')
# for line in f3:
#     print(line,end='')
# f3.close

# 파일 내에서 검색     문자에 문자\r\n 이 포함되어있음
# seek(offset,whence) : offset(상대위치)
#   - offset : 상태위치
#              시작 위치로부터 열의 위치
#   - whence : 위치
#              0 : 파일시작위치, 1: 현재위치 , 2: 파일의끝
# seek(0,0) : 시작위치 0열의 위치 => 0행 0열
# seek(10,0) : 시작위치부터 오른쪽으로 10열 이동한 위치 => 0행 10열
# seek(0,2) : 파일의 끝으로부터 0열의 위치 => 0행 0열

# f = open('file1.txt','r',encoding='utf-8')
# # f.seek(10,0)
# # f.seek(0,2)  # 파일의 마지막 위치
# f.seek(15,0)
# lines = f.readlines()
# print(lines)
# f.close()

# 텍스트 파일 읽기 : read() 함수
# 내용 전체를 읽어서 1개의 문자열로 반환
# f = open('file1.txt','r',encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# 파일 내에서 검색
# read() 함수사용
# f = open('file1.txt','r',encoding='utf-8')
# data = f.read()
# value = input('검색간 입력: ')
# if value in data:
#     print('exist')
# else:
#     print('not')
# append() 파일끝에추가
# f = open('file1.txt','a',encoding='utf-8')
# appendData = '\n\npython programming'
# f.write(appendData)
# f = open('file1.txt','r',encoding='utf-8')
# print(f.read())
# f.close()

# with 문
# with 문이 종료되면 파일객체는 자동으로 close()
# with open(파일명,열기모드) as 파일객체 :
#       수행코드
# with open('file1.txt','a') as f:     #  같다 f = open('file1.txt','w')
#     f.write('\hello\n')

# 파일 또는 디렉터리 존재 여부 확인
# import os.path
# print(os.path.exists('c:/Python_Word'))
# 디렉토리인지 파일인지 확인
# print(os.path.isdir('c:Python_Word/Day1'))
# print(os.path.isfile('c:Python_Word/Day1'))
# # 파일 삭제
# import os
# os.remove('경로')
# 파일크기 확인
# os.path.getsize('경로')
# # 파일압축 및 풀기
# import zipfile
# new = zipfile.ZipFile('압축파일이름','w')   # 파일 압축
# new.write('경로/파일명',compress_type=zipfile.ZipFile) # compress_type=zipfile.ZipFile 은 압축의 형식
# new.close()
# # 압축파일 풀기
# ext = zipfile.ZipFile('압축파일이름','r')
# ext.extractall('경로')
# ext.close()

# # 이진파일 : 글자가 아닌 비트 단위로 의미가 있는 파일  ex) 그림 ,음악,동영상 파일,엑세,한글파일,실행파일 등등
# # 텍스트 파일: 메모장으로 열고 내용이 보이는 파일
# # 이진파일 읽기
# f = open('이진파일 이름''rb')
# f.read(1)   # 1바이트씩 읽기
# # 이진파일 쓰기
# f = open('이진파일이름','wb')
# f. write()
# f1 = open('경로','rb')
# f2 = open('경로','wb')
# while True:
#     inStr = f1.read(1)
#     if not inStr:
#         break
#     f2.write(inStr)
# f1.close()
# f2.close()

# # 메모리에 로딩된 객체나 정의된 클래스를 파일로 저장하여 사용
# import pickle
# # 객체 저장 pickle.dump()
# f = open('list.pickle','wb')
# result = [1,2,3,4,5]
# pickle.dump(result,f)  # 리스트를 이진파일 형태로 파일에 저장
# f.close()
# # 객체 로딩 pickle.load()
# f = open('list.pickle','wb')
# result2 = pickle.load(f)  # f에있는걸 불러옴
# result2.append(100)
# print(result2)

# 01-04

# 기본적인 예외 처리 문장
# try:
#     에러가 발생할 문장들
# except 에러명:       # 에러명 없으면 아무 에러나 전부 잡음
#     에러가 발생하면 처리하는 코드(문장)들
# else:
#     에러가 발생하지 않으면 처리하는 문장
# finally:      # 마지막에 항상 나옴
#     에러와 상관없이 항상 수행하는 문장
#
# except ValueError as e:           e 가 에러의 구체적인 종류를 가져와줌
#     print('숫자 아닌데용',e)
# except (ZeroDivisionError,TypeError) as e:        # 함께 사용 가능
#     print('숫자 아닌데용',e)
#     print('형식잘못',e)
#
# 특정한 클래스의 인스턴스인지 확인: isinstance(인스턴스명,클래스명)
# self : 인스턴스가 사용하는것 (자신)

##  01-05

# # 참고.  ` _ `: 변수에 특별한 이름을 부여하지 않고 사용하려할때
# for _ in range(10):
#     print('a')
# # _ 2개 사용 : 특수한 예약함수(매소드),변수에 사용

# 비공개 필드 : 클래스 내부에서만 사용되도록 한다
# __필드명

# class Car:
#     model = ''
#     def __init__(self,speed,color,model):
#         self.speed = speed
#         self.__color = color  # 클래스 내에서만 사용하는 비공개 필드
#     def getcolor(self):
#         return self.__color
#     def setcolor(self,color):     # 함수내 비공개 맴버변수 print는 그냥 됨
#         self.__color = color
#     def __modeln(self):           # 비공개 함수
#         return self.__color
#
# # 비공개 필드를 접근하려면 필드를 이용하는 매소드 정의하여 호출 ex) return
# c = Car(5,'black','ef')
# # print(c.color)  # 사용불가
# print(c.getcolor())
# print(c.setcolor('red'))
# print(c.getcolor())

# 특별한 메서드   매직 매서드
# __매서드이름__() : 미리 정의되어있는 메서드

# __ge__() : >=
# __gt__() : >
# __lt__() : <
# __le__() : <=
# __ne__() : !=
# __eq__() : ==
# __init__() : 생성자
# __repr__() : 인스턴스 print()문으로 출력   객체 맴버변수 출력?
# __add__() : +
# __del__() : 소멸자 ,인스턴스를 삭제

# # 선(line) 클래스
# # 필드: 길이,색상,두께
# # 메소드 : 더하기,크기비교
#
# class Line:
#     def __init__(self,length = 0):
#         self.length = length
#         print(f'{self.length}의 길이 선분이 생성되었습니다')
#     ##  other이 자동으로 들어옴
#     def __add__(self, other):
#         return self.length + other.length
#     def __sub__(self, other):
#         return self.length - other.length
#     def __mul__(self, other):
#         return self.length * other.length
#     def __div__(self, other):
#         return self.length / other.length
#     def __gt__(self, other):            # 왼쪽이 크면 true 아니며 false 결과비교는 T,F로 만나옴
#         return self.length > other.length
#     def __ge__(self, other):
#         return self.length >= other.length
#     def __lt__(self, other):
#         return self.length < other.length
#     def __le__(self, other):
#         return self.length <= other.length
#     def __eq__(self, other):
#         return self.length == other.length
#     def __ne__(self, other):
#         return self.length != other.length
#     def __divmod__(self, other):
#         return self.Age / self.Age        # divmod() 함수 사용가능
#     # def __del__(self):
#     #     print(self.length,'길이의 선분이 삭제되었다')
#     def __repr__(self):  # 화면에 정보를 출력할수있게 정보를 만든다
#         return f'선의 길이: {self.length}'
# line1 = Line(10)
# line2 = Line(5)
# print(line1 + line2)
# print(line1 > line2)        # if 의 조건문으로 수행 가능
# print(line1 == line2)
# print(line1 - line2)
# print(line1 * line2)
# print(line1)
# print(line2)

# # 클래스 변수 : 여러 인스턴스가 공유하는 변수
# class Car:
#     color = ''
#     speed = 10    # 클래스변수로 쓸게 아니라면 init 안에 넣어주는게 맞음
#     count = 0 #클래스변수
#
#     def __init__(self):
#         self.speed = 0
#         Car.count += 1  # 클래스 변수
#         print('현재 자동차 {0}대가 생산되었습니다'.format(Car.count))
# car1 = Car()
# print(Car.count)
# car2 = Car()
# # print(car1.count)
# # print(car2.count)
# print(Car.count)
# car3 = Car()

# # 상속
#
# class Car:  class Car(object) 와같은 object는 생략가능
#     speed = 0
#     color = ''
#
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#
#     def drive(self):
#         print(f'{self.speed}로 주행합니다')
#
#
# class Truck(Car):                             # 상위 클래스에서 맴버변수를 추가할때 그대로 사용하면 init는 생략
#     def __init__(self, speed, color, load):   # 서브 클래스의 init를 생략 하면 self.변수는 상위클래스 변수를 가져옴
#         super().__init__(speed, color)  # 부모 맴버 변수를 받고 하나 추가
#         self.load = load
#
#     def drive(self):  # 메소드 재정의(오버라이딩)
#         print(f'{self.speed}로 주행하고 {self.load}짐을 싣고 수행')
#
#     def loading(self):
#         print(f'최대 {self.load}짐을 운반할수있다')
#
#
# class Vehicle(Car):
#     def __init__(self, speed, color, seat):
#         super().__init__(speed, color)
#         self.seat = seat
#
#     def drive(self):  # 메소드 재정의(오버라이딩)
#         print(f'{self.speed}로 주행하고 {self.seat} 사람이 탐')
#
#
# truck1 = Truck(10, 'red', 1000)
# truck1.drive()
# truck1.loading()
# v = Vehicle(20, 'yello', 10)
# v.drive()

# 포함관계(has-a) 서로 다른 클래스 를 이용하는 관계   동등관계

## 01-06

# 다중상속

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.name , self.age)
#     def greeting(self):
#         print(f'안녕하세요 제이름은 {self.name} 입니다')
#
#
# class University:
#     def __init__(self,deartment,grade):
#         self.deartment = deartment
#         self.grade = grade
#
#     def manage(self):
#         print('학점관리')
#
# class undergrade( Person ,University ): # 다중상속시 앞에있는 init를 가져온다 다른 맴버 함수는 다 가져온다
#
#     def study(self):
#         print(self.age)
# un = undergrade('이름',2)
# un.study()
# un.manage()
# un.greeting()
# #

#  굳이 따로 상속

# class undergrade( Person ,University ): # 다중상속시 앞에있는 init를 가져온다 다른 맴버 함수는 다 가져온다
#     def __init__(self,speed,color,deartment,grade):
#         Person.__init__(self,speed, color)
#         University.__init__(self,deartment, grade)
#
#     un = undergrade('빨리', '컬러', '부서', '등급')
#





#
# mor()확인
# class A:
#     def greeting(self):
#         print('hji')
#
# class B(A):
#     def greeting(self):
#         print('hi im B')
#
# class C(A):
#     def greeting(self):
#         print('hi im C')
#
# class D(B,C):
#     pass
#
# x = D()
# x.greeting()
# print(D.mro())    # 객체.mor() 상속의 호출 순서를 보여줌

# # 정적 매서드    클래스의 이름을 가지고 바로 매서드 접근 가능 객체 생성할 필요가 없어진다.
# # 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
# # 매서드 위에 @staticmethod 를 붙임
# # 매서드에 self를 붙임
# # 맴버 변수나,매서드가 필요가 없을때 사용
# # 순수하게 함수 역할을 할때만 사용할수 있다
#
# class Calc:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
#     @staticmethod       # 함수별로 하나씩 써줘야함
#     def mul(a,b):
#         return a*b
#
# cal = Calc()
# print(cal.add(3,2))
# # 클래스 이름으로 호출
# # 정적 매서드 호출 방식 : 클래스이름.정적매서드(*args)
#
# print(Calc.mul(10,20))


# # 클래스 매서드 : 인스턴스를 통하지 않고 매서드를 클래스에서바로 호출
#
# # @classmethod 를 매서드 위에붙임 : 매서드내에 인수르 cls를 지정
# # : cls = class
#
# # # 형식
# # 비교예시
# # class 클래스이름:
# #     @classmethod
# #     def 매서드명(cls,인수들):
# #         문장
# #
# # # 호출형식
# # 클래스이름.매서드명(인수들)
# # 클래스변수 이용 예시
#       똑같지만 다른 결과를 보기위한 클래스매서드
# # class Person:
# #     count = 0 #클래스 변수
# #     def __init__(self,name):
# #         self.name = name
# #         Person.count += 1   # 공유변수이고 객체 생성시마다 변함
# #     def printcount(self):
# #         print(f'{self.count}명이 태어났습니다 ')
# #
# # man1 = Person('kim')
# # man1.printcount()
# # man2 = Person('lee')
# # man2.printcount()
#
# class Person:
#     count = 0 #클래스 변수
#     def __init__(self,name):
#         self.name = name
#         Person.count += 1   # 공유변수이고 객체 생성시마다 변함
#
#     @classmethod
#     def printcount(cls):
#         print(f'{cls.count}명이 태어났습니다 ')
#
# man1 = Person('kim')
# Person.printcount()
# man2 = Person('lee')
# Person.printcount()


