import requests
from bs4 import BeautifulSoup as bs

# 초기화 위치 중요 !
urls = []
n_url = []
content = []
for page in range(10):
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&cluster_rank=51&query=무단횡단&nso=so:r,p:all,a:all&start='
    raw = requests.get(url + str((page * 10) + 1))
    soup = bs(raw.text, 'html.parser')
    sources = soup.find_all('a','info')

    # 네이버 뉴스인 링크 가져오기 ( 다른 링크도 같이 가져와짐 )
    for source in sources:
        urls.append(source.attrs['href'])
    # print(urls)

# urls에서 진짜 네이버 뉴스 링크만 가져오기
for url in urls:
    if 'naver' in url:
        n_url.append(url)
    # print(n_url)
print(len(n_url))

# 중복 확인
# s = n_url.count('https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=102&oid=001&aid=0013064690')
# print(s)

# 네이버뉴스에서 제목,본문 가져오기
# 제목 h3#articleTitle .text
# 본문 div#articleBodyContents .text

for i in n_url:
   news_url = requests.get(i, headers={'User-Agent':'Mozilla/5.0'})
   soup2 = bs(news_url.text,'html.parser')
   text = soup2.find_all('div', '_article_body_contents article_body_contents')
   for j in text:
       content.append(j.get_text())

f = open('filename.txt', 'w', encoding='UTF-8')
f.writelines(content)
f.close()
