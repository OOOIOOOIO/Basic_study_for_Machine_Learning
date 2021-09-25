#  시도별 인구 변동 현황 데이터 추출하기

import openpyxl

# 파일 열기
fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\stat_104102.xlsx"

# 엑셀파일 가져오기
book = openpyxl.load_workbook(fileName)

# 첫번쨰 시트 추출
sheet = book.worksheets[0]

# 시트의 행을 순서대로 추출하기
excel_record = []

for record in sheet.rows :
    excel_record.append([
        record[0].value, # 행의 1번쨰 값을 가져옴 ex) 1행 1열
        record[10].value # 행의 10번째 값을 가져옴 ex) 4행 10열
    ])

# 필요 없는 행(부분) 제거하기
# del()로 0행을 지우면 그 다음행은 1행이 아니라 다시 0행이 된다.
del(excel_record[0])
del(excel_record[0])
del(excel_record[0])
del(excel_record[0]) # 1 ~ 4행 삭제 --> 0번째 행을 지우면 1행 0행이 되는 메커니즘
del(excel_record[17]) # 21 - 4 = 17(인덱스 기준)
del(excel_record[17]) # 22(21) ~ 23(22)행 삭제 --> 마찬가지로 22행을 삭제하면 23행이 22행이 된다.

# 출력하기
# for data in excel_record :
#     print(data)
# print()

#==============================================================================================

# "1,000" --> ,가 있으면 int()로 형변환 못 함 / "1000"은 가능
# replace(',', '')를 해줘서 ,를 없애줘야됨. 그 후 int()로 형변환 하기
for data in excel_record :
    data[1] = data[1].replace(",", "") # , 삭제하기
    data[1] = int(data[1]) # 형변환하기


# 데이터를 인구순으로 정렬하기(오름차순)
sorted_data = sorted(excel_record, key = lambda x : x[1]) # 정렬하기


# 정렬된 데이터 출력하기
for data in sorted_data :
    print(data)
print()


# 하위 5개의 지역을 추출하기
# enumerate() : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력 받아 인덱스 값과 같이 리턴해준다.
print("===========인구 변동 하위 5개 지역============")
for i, local in enumerate(sorted_data) :
    if i >= 5 : break
    print(i + 1, "위 :", local)
