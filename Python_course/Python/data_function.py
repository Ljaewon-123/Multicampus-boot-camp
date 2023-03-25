from datetime import date as dt
from datetime import datetime as dat
from datetime import timedelta as td


today =  dt.today()
year = today.year
month = today.month
day = today.day
print(f'{today} {year} {month} {day}')

current_time = dat.now().time()

print(dat.now().time().hour)
print(dat.now().time().minute)
print(dat.now().time().second)
print(dat.now().time().microsecond)

print(today + td(days = 1))

current_time = dat.now()

print(current_time + td(hours=-1))
print(current_time + td(days = 1,hours=2))

# strftime()함수 : 날짜형식 문자열로 변환
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%Y-%m-%d %I:%M:%S:%p'))

# strptime() 문자열을 날짜형식으로 반환
today = '2021-12-13 14:33:20'
trans = dat.strptime(today,'%Y-%m-%d %H:%M:%S')
print(trans)