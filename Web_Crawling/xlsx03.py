#  시도별 인구 변동 현황 데이터 추출하기


# 엑셀을 접근하는 법 : A5.value --> A열의 5번째 값
# A :chr(65) / Z : chr(90) --> 아스키코드로 표현
# a --> chr(97) / chr(122) --> z
# ex) print(chr(66)+"5")
import openpyxl

# 파일 열기
fileName = r"C:\Users\polit\python_MachineLearning\Web_Crawling\stat_104102.xlsx"

# 엑셀파일 가져오기
book = openpyxl.load_workbook(fileName)

# 시트 가져오기
sheet = book.active # 활성화되어 있는 시트

# 계에서 서울 인구수를 제외한 인구수 합산 및 출력하기
for i in range(10) :
    totalValue = sheet[str(chr(66 + i) + "4")].value.replace(",", "")

    seoulValue = sheet[str(chr(66 + i) + "5")].value.replace(",", "")

    total = int(totalValue)
    seoul = int(seoulValue)

    result = total - seoul

    # , 를 넣고 싶을 떄 --> format(변수, ",")
    # result = format(total - seoul, ",")
    print("서울을 제외한 인구수 ", result)



# 필요 없는 데이터 지우기
    sheet[str(chr(65 + i) + "23")].value = ""

# 데이터 넣기
    sheet[str(chr(65) + "22")].value = "서울을 제외한 인구수"
    sheet[str(chr(66 + i) + "22")].value = result

# 스타일 바꾸기
    cell = sheet[str(chr(65 + i) + "22")]
    cell.font = openpyxl.styles.Font(size = 14, color = "00FF00") # name을 사용해 글씨체 바꿀 수 있음



# 엑셀파일에 결과 쓰기
fileName2 = r"C:\Users\polit\python_MachineLearning\Web_Crawling\xlsx_Res03.xlsx"

book.save(fileName2)
print("파일이 저장되었습니다.")
