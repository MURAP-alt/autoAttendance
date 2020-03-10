import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

response = requests.get("https://yakkun.com/swsh/zukan/n1")

data = BeautifulSoup(response.content,"html.parser")

# 名前とステータス取得記事一覧を出力
name = data.find("tr",{"class": "head"}).string
status = data.find_all("td")

# 名前表示
print(name)

# 無振りHP
h = status[30].string
print(h)

# 無振り攻撃
a = status[36].string
print(a)

# 無振り防御
b = status[42].string
print(b)

# 無振り特攻
c = status[48].string
print(c)

# 特防
d = status[54].string
print(d)

# 素早さ
s = status[60].string
print(s)

df = pd.DataFrame([
  [name, h, a, b, c, d, s],
  ["0002", "Lily", "Sales", "", ""]],
  columns=['名前', 'HP', '攻撃', '防御', '特攻', '特防', '素早さ'])
 
# CSV ファイル (employee.csv) として出力
df.to_csv("employee.csv",encoding="ANSI")