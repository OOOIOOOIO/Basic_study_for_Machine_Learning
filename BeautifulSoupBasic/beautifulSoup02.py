# PYPI : Python Pakage Index --> 파이썬 패키지 --> pip를 이용해 설치
# 커맨드 창에 pip3 install beautifulsoup4
# from bs4 import BeautifulSoup 오류 없으면
# 후에 ide에서 실행

from bs4 import BeautifulSoup

html = """
<html><body>
 <h1 id = "title">BeautifulSoup 사용방법</h1>
 <p id = "subtitle">스크레이핑 연습하기</p>
 <p>원하는 데이터 추출하기</p>
</body>
</html>
"""
# h1 요소에 id 속성을 줌
# find()를 이용해 id 값을 찾아 올 수 있다
# find_all()은 똑같은 요소가 여러개 있을 때 찾아올 수 있음


# html 분석하기
soup = BeautifulSoup(html, 'html.parser') # 객체 생성


# find() 메서드를 이용한 데이터 추출하기
title = soup.find(id = "title") # id가 title인 요소 가져오기

print("title = " + title.string)

subtitle = soup.find(id = "subtitle") # id가 subtitle인 요소 가져오기

print("subtitle = " + subtitle.string)

print("\n" + "==================================================================" + "\n")

html_2 = """
<html>
    <body>
        <ul>
            <li><a href = "http://www.naver.com">네이버</a></li>
            <li><a href = "http://www.google.com">구글</a></li>
        </ul>
    </body>
</html>
"""
# <a> </a> 앵커태그


# html 분석하기
soup = BeautifulSoup(html_2, 'html.parser')

a1 = soup.html.body.ul.li.a # a 요소를 가져옴

print("a1 = " + a1.string)


# find_all() 메서드를 사용하여 데이터 추출

links = soup.find_all("a") # 앵커 태그가 2개라서 리스트로 저장됨

for i in links :
    print(i, i.string)

print()

# a 요소의 속성인 href 가져오기 : a.attrs['href'], attrs는 기본적으로 딕셔너리 타입

for j in links :
    print(j.string, "-->", j.attrs['href']) # 딕셔너리 : key값으로 접근
