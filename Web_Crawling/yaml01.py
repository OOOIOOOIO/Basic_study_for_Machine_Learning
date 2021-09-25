    < YAML 데이터 >

 YAML은 들여쓰기 사용해 계층 구조를 표현하는 것이 특징인 데이터 형식

 XML보다 간단하며, JSON과 거의 비슷하다.

 YAML은 JSON 대용으로 많이 사용되며 애플리케이션 설정 파일을 작성할 때 많이 사용된다.

 웹 프레임워크인 Ruby, Symfony(PHP)의 설정 파일 형식으로 사용되고 있다.

 파이썬 / PHP / Ruby 등을 포함한 여러 프로그래밍 언어에서 YAML형식을 다루기 위한
라이브러리가 제공되고 있다.

 파이썬에서 YAML을 다루기 위해서 PyYAML이라는 모듈을 설치해야 한다.
ex) pip3 install pyyaml


    < 구조 >

 YAML의 기본은 배열, 해시, 스칼라(문자열, 숫자, 불린)이다.

 배열을 나타낼 때는 하이픈(-)을 붙여서 사용한다. 하이픈 뒤에는 공백을 사용한다.
ex) - apple
    - orange
    - banana

 중첩 배열(배열 안에 배열)
ex) - yellow
    -
        - orange
        - banana
    - Red
    -
        - apple
        - strawberry


 해시 표현방법(해시 : 자바스크립트의 객체와 같은 것을 의미 ("키" : "값"))
ex) name : kim
    property :
        age : 10
        color : brown

 배열과 해시를 조합하면 조금 더 복잡한 데이터를 표현할 수 있다.
ex) - name : lee
    color : brown
    age : 10
    hobby :
        - food
        - movie
    - name : smith
    color : white
    age : 15
    hobby :
        - music
        - game
    - name : kim
    color : black
    age : 7
    hobby :
        - reading
        - dance

 YAML은 플로우 스타일(Flow Style : 한줄로 표현할 수 있는 방법)을 지원함
{key1 : value1, key2 : value2} 이때 쉼표(,), 콜론(:) 뒤에는 반드시 공백이 있어야 한다.
 ex) - name : kim
     color : black
     age : 7
     hobby : ["reading", "dance"]


 YAML은 주석을 사용할 수 있다. 주석 기호는 # 으로 시작한다.
ex) #노란색 과일
    - banana
    - orange

 YAML은 여러줄의 문자열을 지정할 수 있다.
ex) multi-line : |
        i am a boy
        i am a girl
        i like book

=====================================================================================

 YAML의 앵커와 별칭(alias)
 &aaa1 --> 앵커(일종의 변수 선언)
 *aaa1 --> 별칭 ( == &aaa1)

 &aaa1 'bbbb'
