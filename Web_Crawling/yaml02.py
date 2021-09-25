# YAML 데이터 분석해보기 

import yaml

# RGB 값 : ff ff ff (빨 초 파)

# yaml 데이터 정의
yaml_data = """
color_def :
    - &col1 "#ff0000"
    - &col2 "#00ff00"
    - &col3 "#0000ff"

color :
    title : *col1
    title2 : *col2
    title3 : *col3
"""

# YAML데이터 형식을 파이썬으로 바꾸기(분석하기)
data = yaml.load(yaml_data)

print(data,"\n")

# 별칭을 이용한 출력
print("title1 =", data["color"]["title"])
print("title2 =", data["color"]["title2"])
print("title3 =", data["color"]["title3"])
print()

# =====================================================================
yaml_data2 = """
data : 2021-09-17
productList :
    -
        id : 100
        name : banana
        color : yellow
        price : 1500
    -
        id : 200
        name : orange
        color : orange
        price : 700
    -
        id : 300
        name : apple
        color : red
        price : 1200
"""


# YAML데이터 형식을 파이썬으로 바꾸기(분석하기)
data2 = yaml.load(yaml_data2)

print(data2)
# name, color 출력

for prod in data2["productList"] :
    print(prod["name"], prod["color"])
