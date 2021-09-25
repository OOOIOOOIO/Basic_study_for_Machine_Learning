# execute_script() 메소드를 이용한 자바스크립트 처리하기

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\polit\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(3) # 최대 기다리는 시간

driver.get("https://google.com")

res = driver.execute_script("window.alert('하이 나는 김성호!!')") # window.alert 자바 스크립트 명령어
print(res)
