from selenium import webdriver
from time import sleep
import sys

# パスを通すためのimport文
import chromedriver_binary
from selenium.webdriver.common.keys import Keys

# コマンドラインからユーザー名パスワードを入力
args = sys.argv

# print("ユーザー名: " + args[1])
# print("パスワード: " + args[2])

driver = webdriver.Chrome()
driver.get("http://co-works.net:91/aipo/")

# ユーザー名入力
nameForm = driver.find_element_by_id("member_username")
nameForm.send_keys(str(args[1]))

# パスワード
pw = driver.find_element_by_id("password")
pw.send_keys(str(args[2]))

sleep(1)

# ログインボタン
loginButton = driver.find_element_by_name("login_submit")
loginButton.submit()

sleep(2)

# 出勤
inAttend = driver.find_element_by_xpath("")
inAttend.click()

sleep(1)

driver.quit()
sys.exit()