# PYPI : Python Pakage Index --> 파이썬 패키지 --> pip를 이용해 설치
# 커맨드 창에 pip3 install beautifulsoup4
# from bs4 import BeautifulSoup 오류 없으면
# 후에 ide에서 실행

# CSS 선택자 사용하기
# BeautifulSoup.select_one("선택자") : CSS 선택자로 요소 하나를 추출하겠다라는 의미
# BeautifulSoup.select("선택자") : CSS 선택자로 요소 여러개를 추출하겠다라는 의미 (리스트 형태)

from bs4 import BeautifulSoup

# 분석할 대상 HTML 문서
html = """
<html><body>
    <div id = "lecList">
        <h1>데이터 과학</h1>
    </div>
    <div id = "lecture">
        <h1>빅데이터 강좌</h1>
        <ul class = "subject">
            <li>파이썬 강좌</li>
            <li>머신러닝을 위한 데이터 처리</li>
            <li>파이썬을 이용한 딥러닝이론</li>
        </ul>
        <ul>두번째 ul태그</ul>
    </div>
</body></html>
"""

# HTML  분석하기
soup = BeautifulSoup(html, "html.parser")


# CSS 쿼리로 데이터 추출하기
# CSS에서 "#"은 태그의 속성이 id일 경우, "."은 태그의 속성이 class일 경우, ">"  자식을 의미


# select_one() 사용
# id가 lecture인 div 밑에 있는 h1의 요소에 접근해서 .string으로 요소 내용을 가져온다는 의미
h1 = soup.select_one("div#lecture > h1").string

print(h1)

# select() 사용
subject = soup.select("div#lecture > ul.subject > li")

for li in subject :
    print(li.string) # subject는 요소이기 때문에  li.string으로 내용을 추출함 
