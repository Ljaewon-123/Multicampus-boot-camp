from bs4 import BeautifulSoup
import urllib.request

# urlopen 안에있는 url 정보 요청
resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver')
# resp 안에는 document로 들어가있음 (str) 응답되는 document를 reponse객체에 담아서 줌
# print(resp)
soup = BeautifulSoup(resp,'html.parser')
# print(type(soup))

a = soup.find_all("p",class_='rank_tx')
b = soup.find_all("a",)
# print(b)
# print(a)

movies = soup.find_all("dl",class_='lst_dsc')
# print(movies[0])
for movie in movies:
    # 제목
    title = movie.find("a").get_text()
    # title = movie.find_all("p",class_='rank_tx')
    # title = soup.find_all('a')[0].text
    # 별점
    star = movie.find('span',class_='num').text
    print(f'{title} [{star}]')