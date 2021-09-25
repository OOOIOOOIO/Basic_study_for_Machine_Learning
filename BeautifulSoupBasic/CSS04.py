from bs4 import BeautifulSoup

# html 파일열기
fp = open(r"C:\Users\polit\python_MachineLearning\BS\fruit_vegitable.html", "r", encoding = "utf-8")

soup = BeautifulSoup(fp, "html.parser")

# 데이터 추출하기
print(soup.select_one("#fruits > li:nth-of-type(2)").string) # 포도

print(soup.select_one("#vegitable > li:nth-of-type(2)").string) # 파프리카

print(soup.select_one("#fruits > li.red").string) # 사과

print(soup.select_one("#vegitable > li.white").string) # 무우

 # 무우와 파프리카가 green이 겹침. select는 리스트형태로 가져오니까 [1] 인덱싱으로 두번째 요소 가져옴
print(soup.select("#vegitable > li.green")[1].string) # 파프리카

# 마찬가지
print(soup.select("li.green")[2].string) #


# find 메서드를 이용해서 추출하기
condition = {"data-lo" : "us",
            "class" : "red"}

# find(name --> 태그, attrs --> 속성) or find(id = "") or 연속적으로 사용 가능
print(soup.find_all("li", condition)[0] .string) # 사과 --> find_all : 여러개 리스트로 리턴 / [1] --> 파프리카

print(soup.find(id = "vegitable").find("li", condition).string) # 파프리카
