# 스타일시트 연습

from bs4 import BeautifulSoup

# html 파일 열기 
fp = open(r"C:\Users\polit\python_MachineLearning\BS\book.html", "r", encoding = "utf-8")

soup = BeautifulSoup(fp, "html.parser")

# 똑같은 표현
print(soup.select_one("ul#itBook > li#DataScience").string) # ul의 id가 idBook이고 그 l 밑에 li id가 DataSciende 인 요소
print(soup.select_one("ul > li#DataScience").string) # ul 밑에 li의 id가 DataSciende 인 요소
print(soup.select_one("#itBook > #DataScience").string)
print(soup.select_one("#itBook #DataScience").string) # ">" 생략 가능
print(soup.select_one("#DataScience").string)
print(soup.select_one("li[id='DataScience']").string)
print(soup.select_one("li:nth-of-type(3)").string)

print(soup.select("li")[3].string) # 4번째 li 선택
print(soup.find_all("li")[3].string) # 똑같음
