# PYPI : Python Pakage Index --> 파이썬 패키지 --> pip를 이용해 설치
# 커맨드 창에 pip3 install beautifulsoup4
# from bs4 import BeautifulSoup 오류 없으면
# 후에 ide에서 실행

from bs4 import BeautifulSoup
import urllib.request as req

# 기상청 데이터 처리하기 
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp" # url 따오기

# urlopen() 으로 데이터 가져오기
res = req.urlopen(url)

# 웹데이터 분석하기
soup = BeautifulSoup(res, "html.parser") # url 분석

title = soup.find("title").string

wf = soup.find("wf").string # 요소명 찾기 --> 요소를 찾으면 .stringd으로 데이터를 가져오기

print(title, "\n", wf)
