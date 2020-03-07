import requests
from bs4 import BeautifulSoup
from time import sleep

oriUrl = "https://yakkun.com/swsh/zukan/n"

# 図鑑ナンバー入力
print("取得したい図鑑ナンバーの初めの番号を入力してください")
startNum = input()
print("取得したい図鑑ナンバーの終わりの番号を入力してください")
finishNum = input()

# URLを取得
def getUrl(num):
    url = oriUrl + str(num)
    response = requests.get(url)
    data = BeautifulSoup(response.content,"html.parser")
    return data

# 名前を表示する
def disp(data):
    print(data.find("tr",{"class": "head"}).string)

for num in range(int(startNum), int(finishNum) + 1):
    data = getUrl(num)
    sleep(1)
    disp(data)

# 同時処理
# for num in range(1, 80):
#     def getUrl():
#         url = oriUrl + str(num)
#         response = requests.get(url)
#         data = BeautifulSoup(response.content,"html.parser")
#         return data

#     def disp(data):
#         print(data.find("tr",{"class": "head"}).string)

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