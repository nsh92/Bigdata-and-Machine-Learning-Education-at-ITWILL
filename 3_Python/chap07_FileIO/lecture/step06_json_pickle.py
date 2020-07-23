'''
1. json 파일 2가지 형식
    1) 중괄호 : {key:value, ...}, {key:value, ...}
    -> json.loads(row) : dict 형식일 때
    2) 대괄호 : [{key:value, ...}, {key:value, ...}]
    -> json.load(row) : list 형식일 때

2. 피클 형식
'''
import json
import pandas as pd

# 1번 형식 중괄호

# 2번 형식 대괄호
file = open("./chap07_fileio/data/labels.json", mode='r', encoding='utf-8')
print(file.read())  # [{row}, {row}, ...]

rows = json.load(file)  # json 문자열 -> object
print(len(rows))  # 30
print(rows)

for row in rows[:5]:  # rows : [{row}, {row}, ...]
    print(row)        # {row} 뿅
    print(type(row))  # <class 'dict'>

file.close()

# list -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
# <class 'pandas.core.frame.DataFrame'>  # 데이터프레임이다
# RangeIndex: 30 entries, 0 to 29        # 양은 이렇다
# Data columns (total 5 columns          # 컬럼(dict의 key)은 5개다
print(rows_df.head())


# 2. pickle
'''
파이썬 객체(list, dict) -> file save(but by binary)
why? 나중에 data by binary -> 파이썬 객체  : 저장당시의 형식으로 매우 용이하게 되가져올 수 있다
'''
import pickle
'''
save : pickle.dump(data, file)
load : pickle.load(file)
'''
print(type(rows)) # <class 'list'>
## 1) pickle save
file = open("./chap07_fileio/data/rows_data.pik", mode='wb')  # 그냥 w는 문자형으로 쓰겠다는 거임 binary로 쓰겠다는 거임
pickle.dump(rows, file)  # rows란 리스트가 file객체에 binary형식으로 저장됨
print('pickle file saved')

## 2) pickle load
file2 = open("./chap07_fileio/data/rows_data.pik", mode='rb')  # binary 읽기 모드
rows_data = pickle.load(file2)
print(rows_data)
print(len(rows_data))













