from bs4 import BeautifulSoup

import requests

# url = 'https://comic.naver.com/webtoon/weekday'
url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

### 수요웹툰만
ul = soup.find('ul',class_='img_list')

dls = ul.select('dl')


lst = []
for info in dls:
    title = info.find('a')['title']  # 속성으로 가져옴 title 속성 값을 가져옴
    star = info.find('strong').text

    dict = {}
    dict['title'] = title
    dict['star'] = star
    # print(dict)
    lst.append(dict)

print(lst)


#### 전체 요일
# div = soup.find_all('div',class_='col_inner')
# # print(div[4])
#
#
# for divs in div:
#     li = divs.select('li')
#     # print(li)
#     for i in li:
#         title = i.find('a',{'class':'title'}).text
#
#         print(title)

