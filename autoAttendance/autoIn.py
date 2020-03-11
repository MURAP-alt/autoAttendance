from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys
# パスを通すためのimport文
import chromedriver_binary
from selenium.webdriver.common.keys import Keys

# コマンドラインからユーザー名パスワードを引数で取得
args = sys.argv

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
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
attendIn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/table/tbody/tr/td[1]/div[1]/div[2]/div/form/table/tbody/tr/td[1]/input")
attendIn.send_keys(Keys.ENTER)

sleep(1)

driver.quit()
sys.exit()