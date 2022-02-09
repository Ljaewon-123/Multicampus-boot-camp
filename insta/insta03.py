from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)  # 이거는 위에는 다르게 객체임
driver.get('https://www.instagram.com/accounts/login/')
sleep(5) # 5초간 휴식

# id = driver.find_element_by_id()  취소선 사용하지 말것
id = driver.find_element(By.NAME,'username')
id.send_keys(input_id)
# 이름으로 찾음
pw = driver.find_element(By.NAME,'password')
pw.send_keys(input_pw)
sleep(2)

driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3)').click()
# css 선택자로 찾고 loginForm 이라는 id 에 div 자식의 3번째 div
# sleep(2)
# driver.refresh()  # 무한 로딩 해결?

sleep(3)

later = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button')
# 절대 경로
later.click()

# 크롤링이 잘안되면 샐레니움 써보자
# 가장 좋은것은 공식적인 요청을 받기 이런게 안되는 경우는 셀레니움 보기