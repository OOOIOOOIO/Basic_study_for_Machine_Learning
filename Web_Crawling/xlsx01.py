"""
    < 액셀 파일 분석 >

 파이썬에서 엑셀 파일을 분석하기 위해서는 파이썬 액셀 라이브러리를 설치 해야한다.

 openpyxl은 파이썬에서 액셀파일을 읽고 쓸 수 있는 라이브러리 이다.

 pip3 install openpyxl로 다운받기

 https://www.index.go.kr/main.do --> 여러가지 지표를 볼 수 있는 사이트

    < 구조 >

 보통 엑셀 파일을 book이라고 부른다. book 내부에는 여러개의 sheet가 존재한다.

 각 시트(sheet)는 행과 열을 가진 2차원의 셀(cell)로 구성되어 있다.

"""
# 소비자 물가 지수 데이터 추출하기

import openpyxl # xls --> 지원 x / xlsx 파일로 저장해야됨(통합문서)

# 엑셀파일 열기
fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\stat_106001.xlsx"

# 엑셀파일 가져오기
book = openpyxl.load_workbook(fileName)

# 엑셀파일에서 원하는 sheet를 추출하기
sheet = book.worksheets[0] # 첫번쨰 시트 가져오기

# 시트의 각 행(row)을 순서대로 추출해보기
excel_data = [] # 각 행을 담기위한 리스트

for row in sheet.rows :
    excel_data.append([
        row[0].value, # 행의 1번째 열의 값 ex) 1행 1열
        row[9].value # 행의 10번쨰 열의 값 ex) 7행 10열
    ])

# 필요 없는 행(여기선 헤더 부분) 제거하기
# del()로 0행을 지우면 그 다음행은 1행이 아니라 다시 0행이 된다
del(excel_data[0])

# 데이터 출력하기
for data in excel_data :
    print(data)
