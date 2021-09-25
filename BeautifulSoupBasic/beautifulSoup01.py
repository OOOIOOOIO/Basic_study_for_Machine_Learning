# PYPI : Python Pakage Index --> 파이썬 패키지 --> pip를 이용해 설치
# 커맨드 창에 pip3 install beautifulsoup4
# from bs4 import BeautifulSoup 오류 없으면
# 후에 ide에서 실행

from bs4 import BeautifulSoup

html = """
<html><body>
 <h1>스크레이핑 연습 </h1>
 <p>웹페이지를 분석해보기</p>
 <p>웹 데이터 정제하기</p>
</body>
</html>
"""

# html 분석하기

# 객체 생성 : BeautifulSoup(분석하고자 하는 데이터, 'html.parser')
#'html.parser' :  분석기 html을 분석해서 soup에 저장

soup = BeautifulSoup(html, 'html.parser') # 객체 생성

# 원하는 요소 접근하기
# body안에 있는 h1, p, p는 형제관계(sibling)
h1 = soup.html.body.h1 # 우리가 원하는 부분 html 안에 있는 body 안에 있는 h1에 접근

p1= soup.html.body.p

# 다음 p를 출력하고 싶으면 p1.next_sibling.next_sibling (next_sibling은 줄바꿈을 의미)
p2= p1.next_sibling.next_sibling # 한번만 next_sibling을 해주면 공백이 나옴

# .string을 이용해 원하는 요소의 내용을 추출하기
print("h1 = " + h1.string)

print("p1 = "+ p1.string)

print("p2 = "+ p2.string)
