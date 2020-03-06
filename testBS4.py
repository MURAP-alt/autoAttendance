import requests
from bs4 import BeautifulSoup


oriUrl = "https://yakkun.com/swsh/zukan/n"

for num in range(1, 80):
    url = oriUrl + str(num)

    response = requests.get(url)

    data = BeautifulSoup(response.content,"html.parser")

    print(data.find("tr",{"class": "head"}).string)

# htmlをインデントすることができる
# print(data.prettify())

#gigazineの記事一覧を出力
# print(data.find("section"))

# これだとaタグ一つしか取得できない
# print(data.a)

# これは全て取得できる
# print(data.find_all("a"))

# aタグのurlのみ取得
# print(data.a.get("href"))