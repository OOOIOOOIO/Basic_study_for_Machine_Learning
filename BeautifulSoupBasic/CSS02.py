from bs4 import BeautifulSoup
import urllib.request as req

# 위키피디아 한용운 시 제목 가져오기

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%ED%95%9C%EC%9A%A9%EC%9A%B4"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

list = soup.select("#mw-content-text > div.mw-parser-output > div:nth-child(7) > table > tbody > tr >  td > ul > li > a")

#mw-content-text > div.mw-parser-output > div:nth-child(7) > table > tbody > tr > td:nth-child(1) > ul > li:nth-child(1) > a
#mw-content-text > div > ul > li > a

for i in list :
    name = i.string
    print(name)
