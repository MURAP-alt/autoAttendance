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
print(status[30].string)

# 無振り攻撃
print(status[36].string)

# 無振り防御
print(status[42].string)

# 無振り特攻
print(status[48].string)

# 特防
print(status[54].string)

# 素早さ
print(status[60].string)

columns = ["Name", "Url"]
df = pd.DataFrame(columns=columns) # 列名を指定する
print(df)