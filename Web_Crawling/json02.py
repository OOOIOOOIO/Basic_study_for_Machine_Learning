import json

# json 데이터, {}를 하나의 객체로 봄, 객체 안에 또 다른 객체를 넣을 수 있음
price = {
"time" : "21-01-17",
"price" : {"apple" : 1000,
            "banana" : 2000,
            "orange" : 3000}
}

# .dumps : json형식으로 데이터를 출력할 떄 사용
jsonData = json.dumps(price)

print(jsonData)


# 파이썬으로 json을 분석하기  (api 깃허브 레파지토리)
import urllib.request as req
import os.path
import json

# json 데이터 다운로드하기
url = "https://api.github.com/repositories"
fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\rep.json"


if not os.path.exists(fileName) :
    req.urlretrieve(url, fileName)

json_data =open(fileName, "r", encoding = "utf-8").read()

# json 형식의 데이터를 파이썬형으로 변환하기
data = json.loads(json_data)

for dat in data :
    print(dat["name"] + " -- " + dat["owner"]["login"])
