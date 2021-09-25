# 기상청 데이터 긁어오기 
import urllib.request
import urllib.parse # url을 인코딩하기 위해 불러오는 모듈

rssUrl = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp" # url 긁어옴

# 매개변수 : 지역별 코드를 지정하는 변수
# stnId 코드 --> 108 = 전국, 109 = 서울/경기도, 105 = 강원도,
# 131 = 충정북도, 133 = 충정남도, 146 = 전라북도, 156 = 전라남도, 143 = 경상북도
# 159 = 경상남도, 184 = 제주도

# RSS 데이터 읽기

values = {
        'stnId' : '108',

}

params = urllib.parse.urlencode(values) # 인코딩하기 --> 딕셔너리가 key = value로 바뀜

url = rssUrl + '?' + params # 읽는 법 ?stnId = 숫저

print("url =", url)
print()


data = urllib.request.urlopen(url).read() # 메모리에만 띄워놓고 읽기. 저장은 x

text = data.decode('utf-8') # 출력하기 위해 디코딩하기

print(text)
