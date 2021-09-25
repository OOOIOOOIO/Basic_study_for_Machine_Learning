# 셀레니윰을 이용하여 네이버 로그인하기

from selenium import webdriver

userId = "your id"
userPw = "your pw"

# 크롬 사용
driver = webdriver.Chrome(r"C:\Users\polit\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(3) # 최대 기다리는 시간
# 네이버 로그인 페이지
url_login = "https://nid.naver.com/nidlogin.login"

# url을 이용하여 브라우저 열기
driver.get(url_login)
print("로그인 페이지에 접속하였습니다.\n")


# 로그인하기

# 1. ID와 PW 입력하기

# ID를 입력하는 input 태그를 찾아오기
# <input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value="">
inputId = driver.find_element_by_id("id")


# 입력 박스에 있는 텍스트를 모두 지우기
inputId.clear()


# 입력 박스에 id 입력하기
inputId.send_keys(userId)


# PW를 입력하는 input 태그를 찾아오기
# <input type="password" id="pw" name="pw" placeholder="비밀번호" title="비밀번호" class="input_text" maxlength="16">
inputPw = driver.find_element_by_id("pw")


# 입력 박스에 있는 텍스트를 모두 지우기
inputPw.clear()


# 입력 박스에 pw 입력하기
inputPw.send_keys(userPw)


# 2. 로그인 버튼을 찾아서 전송하기

# 로그인하는 태그 찾아오기, 클래스로 찾을 때 타입을 조건으로 걸 수 있음
# <button type="submit" class="btn_login" id="log.login">span class="btn_text">로그인</span></button>
loginBtn = driver.find_element_by_css_selector("button.btn_login[type = submit]") # button 태그에 btn_login 클래스 타입은 submit


# 아이디와 비밀번호를 전송하기
loginBtn.submit() # 로그인 버튼 누르기
print("로그인에 성공하였습니다..")
