# 이미지 데이터 가져오기

import requests
from bs4 import BeautifulSoup

res = requests.get("https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png")

# 바이너리 형식으로 이미지 저장하기

downPath = r"C:\Users\polit\python_MachineLearning\HTTP\logo.png" # logo.png로 저장을 하겠다는 의미. 경로에 붙여줘야됨

with open(downPath, "wb") as f : # logo.png 경로 설정을 하지 않으면 최상위 폴더에 저장됨
    f.write(res.content)

print("이미지 파일이 저장되었습니다.")

# 세션을 사용하는 경우

# 세션 시작 --> 세션 로그인 --> get 혹은 BeautifulSoup 사용해서 데이터 가져오기

# 세션 시작
session = requests.session() # 세션 시작하기

# 로그인 하기 --> post()
login_info = {
            "id" : "userId",
            "password" : "userPw"
}

url = "https://www.test.com/loginComfirm.php" # ID와 PW를 확인하는 페이지(로직) : 서버에 있는 스크립트

result = session.post(url, data = login_info)
result.raise_for_status() # 오류 체크 : 오류가 발생하면 예외처리를 한다


# 로그인 후 get 방식의 서비스를 요청할 경우
myUrl = "https://www.test.com/myPage.html"
res = session.get(myUrl)
res.raise_for_status()

# 뷰티풀슾 사용하기
soup = BeautifulSoup(res.text, "html.parser")
