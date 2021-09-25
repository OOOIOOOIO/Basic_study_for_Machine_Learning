                            < Selenium 소개 >

 Selenuium은 웹브라우저를 컨트롤하여 웹을 자동화(Automation)하는 도구 중의 하나이다.

 Selenium은 Selenium Server와 Selenium Client가 있다.
 로컬 컴퓨터의 웹브라우저를 컨트롤하기 위해서 Selenium Client를 사용한다.
 Selenium Client는 WebDriver라는 공통인터페이스와 각 브라우저 타입별로 웹 드라이버가 구성되어 있다.


 < 웹 자동화의 종류 >

화면의 좌표를 기준으로 한 자동화(가장 원초적인 자동화)

Selenium 도구를 이용하는 웹 자동(Phantom Js와 자주 쓰임),(태그, 속성, Dom 등을 기준으로 인식)

윈도우즈 자동화(타이틀, 캡션, 클래스 등을 기준으로 인식)

작업의 자동화


웹 드라이버 쓰는 법 -->
ex) WebDriver.FireFox, WebDriver.Chrom, WebDriver.Ie(익스플로어), WebDriver.PhantomJS(CLI(Command Line Interface - cmd형태) 형석의 브라우저)

    < 순서 >
Selenium 설치 --> pip3 instll selenium
Selenium 웹 드라이버 설치  --> ex)
Firefox 드라이버 설치 :  https://github.com/mozilla/geckodriver/releases
Chrome 드라이버 설치 : https://sites.google.com/a/chromium.org/chromedriver/downloads

    < 사용법 >

 from selenium import webdriver

 크롬을 사용하는 경우 -->
browser = webdriver.Chrome("크롬 드라이버가 있는 경로")

 파이어폭스를 사용하는 경우
browser = webdriver.Firefox('파이어폭스 드라이버가 있는 경로')

 특정 URL을 이용하여 브라우저를 실행시키는 방법
brower.get("https://www.google.com")


    < Selenium으로 DOM 요소를 선택하는 방법 >

 DOM 내부에 있는 여러개의 요소들 중에서 처음 찾아지는 요소를 추출한다.

find_element_by_id(id) --> id 속성으로 요소를 하나 추출한다.
find_element_by_name(name값) --> name 속성으로 요소를 하나 추출한다.
find_element_by_css_selector(query) --> CSS 선택자로 요소를 하나 추출한다.
find_element_by_Xpath(query) --> Xpath를 지정해서 요소를 하나 추출한다.
find_element_by_tag_name(name) --> 태그 이름으로 요소를 하나 추출한다.
find_element_by_link_text(text) --> 링크 텍스트로 요소를 하나 추출한다.
find_element_by_partial_link_text(text) --> 링크의 자식요소에 포함되어 있는 텍스트로 요소를 하나 추출한다.
find_element_by_class_name(name) --> 클래스 이름으로 요소를 하나 추출한다.


 DOM 내부에 있는 여러개의 요소들을 모두 추출하는 메소드
element에 s만 붙여주면 된다. elements
find_elements_by_css_selector(query)
find_elements_by_Xpath(query)
find_elements_by_tag_name(name)
find_elements_by_class_name(name)
find_elements_by_partial_link_text(text)


 위의 메소드를 이용해서 어떠한 요소도 찾지 못하는 경우에 발생하는 예외
NoSuchElementException 라는 예외 발생

 DOM 요소를 찾은 후 적용할 수 있는 메소드 혹은 속성 (자동화)
    < 메소드 >
clear() --> 글자를 입력할 수 있는 요소(ex) <input type = text>)의 글자를 지운다.
click() --> 요소를 클릭한
get_attribute(name or id or class...) --> 요소의 속성값을 추출한다.(ex) <input name = " ">, <li id = " ")
is_displayed() --> 요소가 화면에 출력되는지 확인한다.(True, False 리턴)
is_enabled() --> 요소가 활성화 되어있는지 확인한다.(True, False 리턴)
is_selected() --> 체크박스가 있다면 체크 상태인지 확인한다.(True, False 리턴)
screenshot(fileName) --> 화면을 캡쳐해서 filename으로 저장한다.
send_keys(value) --> 키를 입력한다. 일반적으로 text 데이터를 보낸다. (value는 text값)
                 --> value가 텍스트 데이터가 아닌 경우(특수키 : 방향키, 펑션키(f1, f2..f12), Enter, Space, Tab, crtl...)
                    특수키를 사용해야 하는 경우에는 별도의 모듈을 사용해야 한다.
                    from selenium.Webdriver.common.keys import Keys

                    방향키 : ARROW_DOWN / ARROW_LEFT / ARROW_RIGHT / ARROW_UP
                    BACKSPACE / DELETE / HOME / END / INSERT
                    ALT / COMMAND(MAC에서 사용) / CONTROL / SHIFT / ENTER / ESCAPE
                    SPACE / TAB / F1 ~ F12 /

submit() --> 사용자가 입력한 입력 양식을 전한다.
value_of_css_property(name) --> name에 해당하는 CSS 속성값을 추출한다.

------------------------------------------------------------
    < 속성 >
id --> 요소의 id 속성
location --> 요소의 위치
parent --> 현재 요소의 부모 요소
rect --> 크기와 위치정보를 가진 딕셔너리 자료형을 리턴한다.
screenshot_as_base64 --> 스크린샷을 base64형태로 추출한다.
screenshot_as_png --> 스크린샷을 PNG형식의 바이너리로 추출한다.
size --> 요소의 크기
tag_name --> 태그이름
text --> 요소내부의 글자


------------------------------------------------------------------
