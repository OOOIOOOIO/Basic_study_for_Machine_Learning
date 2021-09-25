# CSV 파일 데이터 추출해보기

import codecs # 인코딩해주는 모듈

fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\csvTest02.csv"

csvData = codecs.open(fileName, "r", "euc-kr").read()
print(csvData)

print("요딴식으로 나옴 : ",csvData[0:8]) # 그래서 레코드값, 필드값을 만들어줘야됨

data = []
# \r : CR, \n : LF --> CRLF(엔터키)
records = csvData.split("\r\n") # 레코드값


for rec in records :
    if rec == "" : continue # 비어있으면 건너뛰기
    fields = rec.split(",") # 필드값
    # print(rec)
    # print(fields)
    data.append(fields)
    # print(data)
for field in data :
    print(field, field[0])
