from bs4 import BeautifulSoup
import urllib.request as req

# 네이버에서 미국 환율 정보 가져오기 
# 웹문서 가져오기
url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)

# 분석하기
soup = BeautifulSoup(res, "html.parser")

usd = soup.select_one("div.head_info > span.value").string # 미국 환율 정보
print("usd : ",usd)


#mw-content-text > div.searchresults > ul > li:nth-child(1) > div.searchresult
# li:nth-child(1) --> li 태그 안 1번쨰 순서라는 뜻
