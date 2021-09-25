# 파이썬 데이터를 YAML로 쓰기

# yaml.load(str) : str(YAML)을 PYTHON 데이터로 변환
# yaml.dump(value) : value(PYTHON)을 YAML 형식으로 출력

import yaml

person = [
{"name" : "Hong", "age" : 20, "gender" : "man"},
{"name" : "Kim", "age" : 30, "gender" : "woman"},
{"name" : "Park", "age" : 40, "gender" : "man"}
]

yaml_data = yaml.dump(person)
print(yaml_data)
s
print("\n===========================================================\n")

# YAML 데이터를 파이썬 데이터로 변환하기

data = yaml.load(yaml_data)
for p in data :
    print(p)
