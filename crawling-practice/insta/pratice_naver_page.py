from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.get('https://www.naver.com/')
sleep(5)


later = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div/div[2]/a')
later.click()

sleep(3)

id = driver.find_element(By.NAME,'id')
id.send_keys(input_id)

pw = driver.find_element(By.NAME,'pw')
pw.send_keys(input_pw)

sleep(2)

driver.find_element(By.CSS_SELECTOR,'.btn_login_wrap > button').click()


