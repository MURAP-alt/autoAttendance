from selenium import webdriver
from time import sleep
import sys

# パスを通すためのimport文
import chromedriver_binary
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://co-works.net:91/aipo/")

# ユーザー名入力
nameForm = driver.find_element_by_id("member_username")
nameForm.send_keys("taichi.muraoka")

# パスワード
pw = driver.find_element_by_id("password")
pw.send_keys("9999")

sleep(1)

# ログインボタン
loginButton = driver.find_element_by_name("login_submit")
loginButton.submit()

sleep(2)

# 退勤
out = driver.find_element_by_xpath("/html/body/div[1]/div[3]/table/tbody/tr/td[1]/div[1]/div[2]/div/form/table/tbody/tr/td[2]/input")
out.click()

sleep(1)

driver.quit()
sys.exit()
