from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome(
    executable_path="choyeongkyung-sparta/bread_map/python_selenium_crawl/webdriver/chromedriver.exe")
url = "https://map.kakao.com/"

driver.get(url)
sleep(5)

# 지도에 뜨는 창 없애기
driver.find_element_by_css_selector('.layer_body').click()
# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector('#search\.keyword\.query')
search_box.send_keys("비건베이커리")
# 검색버튼 누르기
driver.find_element_by_id('search.keyword.submit').click()