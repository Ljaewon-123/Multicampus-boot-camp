from bs4 import BeautifulSoup

import requests

url = 'https://comic.naver.com/webtoon/weekdayList?week=tue'

resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

ul = soup.find('ul',class_='img_list')

a = ul.select('dt > a')
# print(a)
star = ul.select('.rating_type > strong')
# print(star)
lst = []
for i in range(len(a)):
    title = a[i]['title']
    star1 = star[i].text

    dict = {}
    dict['title'] = title
    dict['star'] = star1
    # print(dict)
    lst.append(dict)

# print(lst)

dc = {}
dc['weebtoon'] = lst
print(dc)

for web in dc['weebtoon']:
    if web['title'] == '집이 없어':
        print( web['title'],web['star'])