# 파이썬의 csv모듈을 이용한 CSV파일 데이터 처리방법

# CSV 파일에 있는 필드 데이터가 큰따움표("")로 되어있는 경우에는
# codec모듈로 CSV파일을 분석하기 어렵다.
# 따라서, 이러한 경우엔 csv모듈을 이용하는데

# csv파일 읽기
# csv.reader(파일포인터, delimiter = ",", quotechar = '"')
# delimiter --> 구분문자를 지정(split느낌)
# quotechar --> 어떤 기호로 데이터를 감싸고 있는지 알려줌

# csv파일 쓰기
# csv.writer(파일포인터, delimiter = ",", quotechar ='"')

import csv, codecs


# 파일 쓰기
with codecs.open(r"C:\Users\polit\python_MachineLearning\Web_Crawling\csvTest03.csv", "w", "euc-kr") as fp : # fp --> 파일 포인터
    writer = csv.writer(fp, delimiter = ",", quotechar = '"') #객체
    writer.writerow(["상품코드", "상품이름", "상품가격"]) # 하나하나 적기
    writer.writerow(["1", "키보드", 20000])
    writer.writerow(["2", "마우스", 30000])
    writer.writerow(["3", "스피커", 40000])


# 파일 읽기
fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\CSVtest03.csv"
fp = codecs.open(fileName, "r", "euc-kr")
reader = csv.reader(fp, delimiter = ",", quotechar = '"') # 코덱과 다르 얘는 레코드 필드가 되어있음

for field in reader :
    print(field, field[0])
