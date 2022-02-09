# -*- coding:utf-8 -*-
# 해당 파이썬 코드 한글로 인코딩

from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)
# print(resp)
# print(resp.text)
# BeautifulSoup 파서트리 만듬
soup = BeautifulSoup(resp.text,'html.parser')
# print(soup)

# webtoon = soup.find_all('ul',class_='img_list')
webtoon = soup.find('ul',{'class':'img_list'})
# print(webtoon)

dl_list = webtoon.select('dl')
# ['href'] 도 가능
lst = list()
for dl in dl_list:
    title = dl.find('a')['title']  # title 속성
    star = dl.find('strong').text

    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    lst.append(tmp)

# print(lst)
res = {}
res['webtoons'] = lst
# print(res)
res_json = json.dumps(res,ensure_ascii=False)
print(res_json)

with open('webtoons.json','w',encoding='utf-8') as f:
    f.write(res_json)