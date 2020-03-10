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

# //*[@id="stats_anchor"]/table/tbody/tr[10]/td[4]

# 名前を表示する
def dispName(data):
    print(data.find("tr",{"class": "head"}).string)
    # print(data.find("tr",{"class": "left"}))

# ステータスを表示
def dispSta(data):
    status = data.find_all("td")

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

for num in range(int(startNum), int(finishNum) + 1):
    data = getUrl(num)
    sleep(1)
    dispName(data)
    dispSta(data)

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