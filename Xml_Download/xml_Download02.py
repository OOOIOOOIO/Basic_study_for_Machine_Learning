# 매개변수 : 지역별 코드를 지정하는 변수
# stnId 코드 --> 108 = 전국, 109 = 서울/경기도, 105 = 강원도,
# 131 = 충정북도, 133 = 충정남도, 146 = 전라북도, 156 = 전라남도, 143 = 경상북도
# 159 = 경상남도, 184 = 제주도


# RSS 데이터 읽기
# 도스창에서 sys.argv를 통해 매개변수에 따라 다르게 출력해보기

import sys
import urllib.request as req
import urllib.parse as parse

# 명령줄 인수가 제대로 입력되었는지 확인
if len(sys.argv) <= 1 : # 명령줄 인수가 1개 혹은 없다는 뜻 --> 에러
    print("사용법 : python 인수1 인수2")
    sys.exit() # 프로그램 종료

regionCode = sys.argv[1] # 도스창에서 argv[0] --> 파일(인수1), argv[1] --> 변수(인수2)

rssUrl = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp" # url 긁어옴

values = {
        'stnId' : regionCode
} # 딕셔너리 타입으로 조건 받기


params = parse.urlencode(values) # 인코딩하기 --> 딕셔너리가 key = value로 바뀜

url = rssUrl + '?' + params # params 리턴값  --> ?stnId = 숫자 

print("url =", url)

data = req.urlopen(url).read()

text = data.decode('utf-8') # 출력하기 위해 디코딩하기

print(text)
