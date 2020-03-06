import requests
from bs4 import BeautifulSoup

response = requests.get("https://co-works.co.jp/")

data = BeautifulSoup(response.content,"html.parser")

#gigazineの記事一覧を出力
print(data.find("section"))