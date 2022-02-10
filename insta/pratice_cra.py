from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
### 받아온 코드
service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)


def scroll():
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
        time.sleep(3)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_page_height == last_page_height:
            break
        last_page_height = new_page_height


url = "https://pixabay.com/images/search/bread/"
driver.get(url)
time.sleep(3)
scroll()

html = driver.page_source
soup = bs(html, 'html.parser')
imgs = soup.select('a.link--h3bPW > img')
for img in imgs:
    print(img['src'])