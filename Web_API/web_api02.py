# 웹 API 실습(openweathermap)

import requests
import json
# 보통 웹 API의 결과는 XML 혹은 JSON 형식으로 리턴한다.(둘 다 DOM 구조)
# openweathermap 사이트에서  API를 요청하면 JSON 형식으로 리턴 한다.
# 따라서 JSON형식의 데이터를 파이썬 데이터형식으로 변환해줘야하는데 이떄 json 모듈이 필요하다.
# jnon은 {} 이런 형식(딕셔너리)

# API키를 지정한다. 본인의 API키를 사용
apiKey = "29924279c460f7ed2d993fce2970a69c"

cityList = ["Seoul, KR",
            "Tokyo, JP",
            "New York, US"]

# API 지정
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# --> API 부르는 법 API key에 본인의 API키를 넣으면 된다.
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}" # --> {} {} .format()으로 넣어 줌


# 켈빈 온도를 섭씨 온도로 변환하는 함수
K2C = lambda k : k - 273.15

# 각 도시의 정보를 추출하기
for name in cityList :


# API의 URL 구성하기
    url = api.format(city = name, key = apiKey)


# API요청을 보내서 날씨 정보를 가져오기
    res = requests.get(url)


#JSON형식의 데이터를 파이썬형으로 변환하기
    data = json.loads(res.text)

# 결과를 출력해보기
    print("** 도시 = ", data["name"])
    print("| 날씨 = ", data["weather"][0]["description"])
    print("| 최저 기온 =", K2C(data["main"]["temp_min"]))
    print("| 최고 기온 =", K2C(data["main"]["temp_max"]))
    print("| 습도 =", data["main"]["humidity"])
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"])
