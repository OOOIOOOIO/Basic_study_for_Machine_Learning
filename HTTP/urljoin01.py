# 상대경로 : ./ or ../
# 절대 경로 : https://www.naver.com 같은 https:// 혹은 C:/

# urllib.parse.urljoin() 메소드를 통해 상대경로를 절대경로로 변환하기

from urllib.parse import urljoin

# urljoin(위치, 교체할 경로(상대 경로))
baseUrl = "https://www.example.com/html/a.html" # html폴더 안에 a 파일이 있다(절대경로)
print(baseUrl) # 현재 경로
print(urljoin(baseUrl, "b.html")) # 현재 폴더 안에서 b.html 파일로 바꿔서 보겠다 라는 의미(./ 생략)
print(urljoin(baseUrl, "./b.html")) # ./ --> 현재 폴더를 의미
print(urljoin(baseUrl, "../b.html")) # ../ --> 상위 폴더를 의미
print()

print(urljoin(baseUrl, "sub/c.html")) # ./ 생략, 현재 위치에서 sub폴더에 들어가서 c.html 파일에 접근하겠다 라는 의미
print(urljoin(baseUrl, "../index.html")) # 상위 폴더로 이동 후 index.html 열기
print(urljoin(baseUrl, "../image/a.png")) # 상위 폴더로 이동 후 image 폴더에서 a.png 열기
print()


# urlJoin() 두번쨰 매개변수에 상대경로가 아닌 절대경로를 지정하는 경우
print(urljoin(baseUrl, "https://www.other.com/aa")) # 절대경로 자체가 바뀜
print(urljoin(baseUrl, "//www.another.com/bb")) # 절대경로 자체가 바뀜 (//www.~~)
print()

print(urljoin(baseUrl, "C:/User.bb")) # 이것도 절대경로가 바뀜
