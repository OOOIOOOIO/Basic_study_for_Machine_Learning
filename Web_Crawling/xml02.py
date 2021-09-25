# 기상청 xml데이터 처리하기

from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# XML 다운로드
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108" # url 긁어옴

fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\forecast.xml"

if not os.path.exists(fileName) : # 파일이 존재하는지 확인하는 메서드(현재 파일이 없으니 False)
    req.urlretrieve(url, fileName) # 파일(데이터) 저장하기

# 다운받은 파일 분석하기
xml_data = open(fileName, "r", encoding = "utf-8").read() # 파일 열기

soup = BeautifulSoup(xml_data, "html.parser") # 분석하기, .parser는 분석할 때 전부 소문자로 바꿈 

# 각 지역 확인하기
info = {}

# 로캐이션 태그 찾기 --> 리턴 값 : 리스트 형식(리스트 안에 딕셔너리형식으로 들어가 있음)
for location in soup.find_all("location") :
    cityName = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info) : # 맑음, 흐림, 등등을 기준으로 도시를 넣음(key = weather, [value = cityname])
        info[weather] = []
    info[weather].append(cityName)

# 날씨 별로 지역 분류하기

for weather in info.keys() :
    print("**", weather, "**\n")
    for name in info[weather] :
        print("--", name)
