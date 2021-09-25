# 커맨드 창에 pip3 install requests 를 사용해 다운로드
# 이후 ide에서 실행

import requests


# requests 모듈의 메서드

# http에서 사용하는 데이터 전송 방식 get, post 방식의 메소드를 제공

# get 방식의 요청
# r = requests.get("https://google.com")

# POST 방식은 딕셔너리형태로 키와 밸류를 만들어서 요청을 해야됨
# fromData = {"Key1" : "value1", "Key2" : "value2"}
# p = requests.post("https://naver.com", data = fromData)


# 웹 상에서 텍스트 데이터 가져오기

resData = requests.get("https://api.aoikujira.com/time/get.php") # 시간을 나타내는 웹 텍스트 데이터 가져옴

# 텍스트 형식으로 추출하기
text = resData.text  # --> .text
print(text)

# 바이너리 형식으로 데이터 추출하기
bin = resData.content # --> .content
print(bin)
