'''
JSON 파일
 - 네트워크에서 표준으로 사용되는 파일 형식
 - 파일 형식 : {key:value, key:value}, {key:value, key:value}

 - json 모듈
  1. encoding : python object(list, dict) -> json file  # save
  2. decoding : json file -> python object              # read
'''
import json
# 1. encoding : object -> 문자열(json)
'''
python object -> json 문자열 -> file save
형식) json.dumps(object)
'''
user = {'id': 1234, 'name': '홍길동'}  # dict
print(type(user))  # <class 'dict'>


json_str = json.dumps(user, ensure_ascii=False)  # 아스키말고 유니코드로 저장하겠따
print(json_str)         # {"id": 1234, "name": "홍길동"}
print(type(json_str))   # <class 'str'>  # 모양은 dict지만 까보니 스트링이다


# 2. decoding : 문자열 -> object
'''
json 문자열 -> python object
형식) json.loads(json 문자열)
'''
py_obj = json.loads(json_str)  # 파이썬에서 읽을 수 있게 로드한다
print(py_obj)         # {'id': 1234, 'name': '홍길동'}
print(type(py_obj))   # <class 'dict'> 중요


# 3. json read / write
## 파일을 읽어온다 : 디코딩
## 1) json file read : decoding
import os
print(os.getcwd())  # C:\ITWILL\3_Python-I\workspace
file = open("./chap07_fileio/data/usagov_bitly.txt", mode='r', encoding='utf-8')
data = file.readlines()  # 전체 내용을 줄단위로 읽겠다 : 리스트로
file.close()
print(data)
# row = {'key':value, ...}
# 제이슨 문자열을 파이썬으로 읽을 수 있게
rows = [json.loads(row) for row in data]
print(type(rows))  # 리스트 : 바깥 와꾸
print(len(rows))   # 3560 보아하니 잘 들어왔내

for row in rows[:10]:
    print(row)
    print(type(row))  # <class 'dict'> : 제이슨이 파이썬오브젝트로

# 제이슨 오브젝트 -> 판다스의 데이터프레임
import pandas as pd

rows_df = pd.DataFrame(rows)
print(rows_df.info())
# <class 'pandas.core.frame.DataFrame'>   # 데이터프레임이다
# RangeIndex: 3560 entries, 0 to 3559     # 양은 이렇다
# Data columns (total 18 columns):        # 컬럼이 18개다
print(rows_df.head())
print(rows_df.tail())

## 2) json file write : 제이슨 인코딩
file = open("./chap07_fileio/data/json_text.txt", mode='w', encoding='utf-8')
print(type(rows))  # <class 'list'> 파이썬 객체임
for row in rows[:100]:  # row = {key:value, ...} : dict
    json_str = json.dumps(row)     # dict 를 json 문자열로
    file.write(json_str)           # 파일로 저장하겠다
    file.write('\n')               # 이렇게 해줘야 한줄 저장하고 줄바꾸고 한줄저장하고 줄바꾸고 저장함, 안해주면 맨 마지막 문장만 저장됨
print('파일 저장 완료ㅋ')

## 3) 저 파일 다시 불러와보자
file = open("./chap07_fileio/data/json_text.txt", mode='r', encoding='utf-8')
data = file.readlines()
print(len(data))  # 100
# json decoding
rows = [json.loads(row) for row in data]  # 제이슨 문자열을 파이썬 객체로
rows_df = pd.DataFrame(rows)
print(rows_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 18 columns):
'''










