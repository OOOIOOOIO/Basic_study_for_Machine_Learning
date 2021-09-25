# 웹상의 정보를 추출하기 위한 라이브러리 불러오기
# urllib 라이브러리 : Http, FTP를 사용해서 데이터를 다운로드할 떄 사용하는 라이브러리
# urllib : URL을 다루는 모듈을 모아 놓은 패키지
# urllib 패키지에 있는 모듈 중에서 request 모듈을 이용하는데
# request 모듈 안 urlretrieve() 함수를 사용한다. (다운로드 함수)
# urlretrieve() 함수는 파일을 바로 저장한다.

# request 모듈 안 urlopen() 함수는 파일을 바로 저장하지 않고 메모리에 로딩한다.

import urllib.request

# url.request.urlretrieve 사용하기


url = "https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png" # URl 긁어오기

downloadPath = r"C:\Users\polit\python_MachinLearning\Web_Download\daum.png" # 다운로드 받을 경로 지정
# unicodeescape Error --> 이스케이프 문자 에러 \ --> \\로 바꿔주면 됨 or r을 써줌

urllib.request.urlretrieve(url, downloadPath) # 파일, 데이터 다운받기. urlretrieve(URL, 저장할 파일 경로)
print("urlretrive를 사용해 이미지 다운로드 완료")



# urllib.request.urlopen 사용하기

url2 = "https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png"

imgPath = r"C:\Users\polit\python_MachinLearning\Web_Download\daum.png" # 다운로드 받을 경로 지정

readImg = urllib.request.urlopen(url2).read() # 파일, 데이터 읽기, mem 같은 변수(메모리 공간) 필요함

with open(imgPath, mode = "wb") as f : # wb : w -> 쓰기 모드, b -> 바이너리 모드(텍스트가 아닌 이미지 같은 파일)
    f.write(readImg)
print("urlopen을 사용해 이미지 다운로드 완료")


"""
 파일로 저장하는 과정
f = open("파일이름", "읽기 / 쓰기 모드") ex) f = open("a.txt", "r" or "w")
f.write("파일 쓰기 테스트") --> 쓰기 모드
f.close() --> 파일 닫기

 위의 과정을 with문으로 간단히 바꾸기(close() 해 줄 필요 없음)
with open("파일 이름", "읽기 / 쓰기 모드") as f :
    f.write("파일 쓰기 테스트") --> 쓰기 모드
"""
