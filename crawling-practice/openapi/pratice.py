from bs4 import BeautifulSoup
import requests

url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5'

resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

page = soup.find('nav',class_='pagination')

# pages = page.select('a')[2:-2]
# print(pages)

nums = list(filter(None,map(lambda  x : x.text if x.text.isdigit() else None, page)))
print(nums)

urls = url[:-1]
# print(urls)

for i in nums:
    url_new = urls+i
    print(url_new)
    resp_new = requests.get(url_new)
    soup_new = BeautifulSoup(resp_new.text,'html.parser')
    span = soup_new.find_all('span',class_='title')
    for ss in span:
        print(ss.text.strip())
