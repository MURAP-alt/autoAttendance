# スクレイピングの練習

from selenium import webdriver

# パスを通すためのimport分
import chromedriver_binary
from selenium.webdriver.common.keys import Keys


# Google検索する
# driver = webdriver.Chrome()
# driver.get("https://www.google.co.jp")

# text = driver.find_element_by_name("q") # ID属性から検索用テキストボックスの要素を取得し
# text.send_keys("selenium") # 文字列"selenium"をテキストボックスに入力

# text.send_keys(Keys.ENTER)


# 特定のボタンをクリックする
driver = webdriver.Chrome()
driver.get("https://yakkun.com/swsh/zukan/n1")

driver.find_element_by_xpath("//div[@id='zukan_header']/p/span/a").click()


# btn = driver.find_element_by_name("btnK")
# btn.click()

# driver.close()
# driver.quit()