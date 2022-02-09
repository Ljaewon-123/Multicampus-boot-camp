from bs4 import BeautifulSoup
import urllib.request
import requests

tag = input('search tags: ')
url = f'https://www.instagram.com/explore/tags/{tag}'

resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')
# print(soup)
print(soup.find('div',class_='KL4Bh'))
# div = soup.select('div',class_='')
# 이게 잘안되서 셀레니움을 사용함

