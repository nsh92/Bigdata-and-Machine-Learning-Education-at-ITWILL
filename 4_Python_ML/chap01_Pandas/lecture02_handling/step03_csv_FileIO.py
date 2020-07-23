# -*- coding: utf-8 -*-
"""
1. csv file read
2. csv file write
3. random sampling
"""
import pandas as pd

# 1. csv file read
iris = pd.read_csv('iris.csv')
iris.info()

# 컬럼명의 : 특수문자 or 공백 --> 사용가능한 다른 문자로 변경
# 아이리스 컬럼명의 불편한 .을 족쳐보자
iris.columns = iris.columns.str.replace('.', '_')
                                     # (바꿀대상, 바꾸고자하는거)
iris.head() # 점이 _로 바뀜
            # 이제 iris. 으로도 호출가능하겠네

## 컬럼명이 없을 때 읽기
st = pd.read_csv('student.csv', header = None)
                                # header = None 이걸 생략하면 첫 컬럼을 이름으로 인식하더라
st                              # 기본 넘버링으로 컬럼명이 들어가졌음
col_names = ['학번', '이름', '키', '몸무게']
st.columns = col_names  
st                              # 컬럼명 수정

## 행 이름 변경
# st.index = 수정 값 

## 비만도지수(BMI) 
## BMI = 몸무게 / 키**2  (단, 몸무게는 kg, 키는 m)
BMI = [st.loc[i,'몸무게'] /( st.loc[i,'키']*0.01)**2 for i in range(len(st))]

print(BMI)
st['BMI'] = BMI  # 만들었으니 DF에 컬럼으로 추가
st['BMI'] = st['BMI'].round(2) # 소수점 처리
st


# 2. csv file write
## 불러오고 필요한 작업을 하였으니 저장해야지
st.to_csv('student_df.csv', index = None, encoding = 'utf-8')

st_df = pd.read_csv('student_df.csv') # 저장했으니 다시 불러와보고
st_df.info()                          # 작업했던 와꾸 그대로 왔음
st_df


# 3. random sampling
wdbc = pd.read_csv('wdbc_data.csv')
wdbc.info()

wdbc_train = wdbc.sample(400)   # 400개를 랜덤 샘플하겠다
wdbc_train.shape                # (400, 32)
wdbc_train.head()


# 판다스의 기본 문법 마무리