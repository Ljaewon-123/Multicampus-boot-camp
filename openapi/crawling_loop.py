from bs4 import BeautifulSoup
import requests

url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5'
# find는 처음 만난 것만? find_all[0]

resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

# titles = soup.find_all('span',class_='title')
# print(titles)

# for title in titles:
#     print(title.text.strip())

page = soup.find('nav',class_='pagination')

# nums = list()
# for pa in page:
#     if pa.text.isdigit():
#         nums.append(pa.text)
# print(nums)

nums = list(filter(None,map(lambda  x : x.text if x.text.isdigit() else None, page)))
print(nums)

# sub_url='https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage='
sub_url = url[:-1]
for i in nums:
    soup = BeautifulSoup(requests.get(sub_url+i).text,'html.parser')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())




#### 이거 안됨 왜안됨? select('a') 를 한시점에서 현재페이지 인 strong를 잡지 못해서 안됨 <<<< 근데 현재페이지 빼고는 다잡음
#### soup를 soup_new 로 새로 만들고 내부에서 사용해주지 않아서 그랫던거임

# atag = page.select('a')[2:-2]
# strong = page.find('strong',class_='active').text
# # print(atag[-1])
# url_tag =[]
# for i in range(len(atag)):
#     # print(atag[i].get_text())
#     # print(strong)
#     url_tag.append(atag[i].get_text())
#
# urls = url[:-1]
# # print(urls)
# # print(url_tag)
#
# for i in range(len(url_tag)):
#     url_ch = urls + url_tag[i]
#     # print(url_ch)
#     resp_new = requests.get(url_ch)
#     soup_new = BeautifulSoup(resp_new.text, 'html.parser')
#
#     titles_new = soup_new.select('span[class=title]')
#     for title in titles_new:
#         print(title.text.strip())
