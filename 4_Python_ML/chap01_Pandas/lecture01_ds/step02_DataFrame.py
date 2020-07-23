# -*- coding: utf-8 -*-
"""
DataFrame 자료구조 특징
 - 2차원 행렬구조(table 유사함)
 - 열(컬럼) 단위 데이터 처리 용이
 - Series들(1차원)의 모임 -> DataFrame(2차원)
"""
import pandas as pd
from pandas import Series, DataFrame

# 1. 데이터프레임 생성

## 1) 기본 자료 구조(list, dict) 이용
name = ['hong', 'lee', 'kang', 'yoo']
age = [35, 45, 55, 25]
pay = [250, 350, 450, 200]
addr = ['서울시', '부산시', '대전시', '인천시']
data = {'name':name, 'age':age, 'pay':pay, 'addr':addr}  # 얘는 dict고 얘를 껴서 합쳤을 때, 순서가 랜덤임
frame = pd.DataFrame(data = data)
print(frame)
'''
   name  age  pay addr
0  hong   35  250  서울시
1   lee   45  350  부산시
2  kang   55  450  대전시
3   yoo   25  200  인천시
'''
frame = pd.DataFrame(data = data, columns = ['name', 'age', 'addr', 'pay']) # 이렇게 순서를 인위적으로 조정해줄 수 있음
print(frame)
'''
   name  age addr  pay
0  hong   35  서울시  250
1   lee   45  부산시  350
2  kang   55  대전시  450
3   yoo   25  인천시  200
'''

## 컬럼 추출
age1 = frame['age']  # 혹은 frame.age
print(age1)
print(age1.mean()) # 40.0
print(type(age1))  # <class 'pandas.core.series.Series'> 시리즈로 추출됐음

## 새 컬럼 추가
gender = Series(['남', '남', '남', '여'])  # 1차원 생성
frame['gender'] = gender # 젠더는 기존에 없던 컬럼임 = 추가하겠다
print(frame)
'''
   name  age addr  pay gender
0  hong   35  서울시  250      남
1   lee   45  부산시  350      남
2  kang   55  대전시  450      남
3   yoo   25  인천시  200      여
'''

## 2) numpy 넘파이 이용 : 선형대수 관련 함수를 제공하는 라이브러리
import numpy as np
frame2 = DataFrame(np.arange(12).reshape(3,4),
                   columns = ['a', 'b', 'c', 'd'])  
                   # 12만큼의 벡터데이터 -> 3행4열 와꾸 + 컬럼이름 -> 데이터프레임
print(frame2)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

## 행/열 통계 구하기 axis : 축
frame2.mean(axis = 0)  # 행축 : 열단위 : 기본값
'''
a    4.0
b    5.0
c    6.0
d    7.0  열 단위 평균
'''
frame2.mean(axis = 1)  # 열축 : 행단위
'''
0    1.5
1    5.5
2    9.5  행 단위 평균
'''


# 2. DataFrame 칼럼 참조
frame2.index   # 행 이름  RangeIndex(start=0, stop=3, step=1)
frame2.values  # 값
'''
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
'''

## emp.csv 로딩
emp = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\emp.csv", encoding='utf-8')
print(emp.info())  # R의 str과 유사
# 3컬럼과 5관측치
# 컬럼이름, 관측치 길이, 데이터 타입

emp.head()  # head(emp)

## 1) 단일 컬럼 선택
print(emp['No'])
print(emp.No)        # 동일한 결과 # 근대 컬럼 이름에 .이 섞인 경우는 []를 사용해줘야 함
print(emp.No[1])     # 컬럼 안의 구체적 원소 선택
print(emp.No[1:])    # 원소의 범위 선택
print(emp['No'][1])  # 컬럼 이름에 .이 있으면 이렇게 원소 선택 
print(emp['No'][1:]) # 범위 선택
## 차트 그리기
no = emp.No
no.plot()
pay = emp['Pay']
pay.plot()

## 2) 복수 컬럼 선택 : 중첩 리스트
print(emp[['No', 'Pay']])
'''
    No  Pay
0  101  150
1  102  450
2  103  500
3  104  350
4  105  400
'''
## 연속 컬럼 선택은 되나?
print(emp[['No' : 'Name']]) # 오류 발생 : 콤마 사용과 함께 지정해줘야 함

## 차트 그리기
emp[['No', 'Pay']].plot()


# 3. subset 만들기 : old DF -> new DF
## 1) 특정 컬럼 제외 : 컬럼이 적은 경우
emp.info()
subset1 = emp[['Name', 'Pay']]
subset1

## 2) 특정 행을 제외 : 행이 너무 많아서
subset2 = emp.drop(0)
subset2

## 3) 조건식으로 행 선택
subset3 = emp[emp.Pay > 350]
subset3

## 4) columns 이용 : 컬럼이 많은 경우
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")
print(iris.info())
print(iris.head())

iris['Sepal.Length']
iris.Sepal.Length  # 얘는 안대지 : 컬럼명에 .이 있기 때문 : Sepal까지만 컬럼으로 인식됨

cols = iris.columns  # 컬럼 이름만 추출
cols = list(iris.columns)  # 군더더기 빼고 컬럼 이름만
cols
type(cols)

iris_x = cols[:4]  # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
iris_y = cols[-1]  # 'Species'

## x, y 변수 선택 : 컬럼 선택
X = iris[iris_x]
y = iris[iris_y]
X.shape  # (150, 4) : 2차원
y.shape  # (150,)   : 1차원

X.head()
y.head()
y.tail()

# exam01 ~ exam02 품


# 4. DataFrame 행렬 참조 : DF[row, col]
# 1) DF.loc[row, col]  : label index
# 2) DF.iloc[row, col] : integer index
emp
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
- 열 이름 : No Name  Pay
- 행 이름 : 0 ~ 4
'''
# loc[행label-index, 열label-index]
emp.loc[1:3]  # 행 이름을 기준으로 가져옴 : 숫자가 아닌, 이름을 인식하는 거임
emp.loc[1:3, :] # 위와 같음 옆은 열을 지정하는 거임
emp.loc[1:3, 'No':'Name'] # 참고
## 중간에 특정 컬럼 제외
emp.loc[1:3, ['No', 'Pay']] # 열에 대가로를 안 쳐주면 3차원으로 인식해서 맛이 감

emp.loc[1:3, [1:2]] ## 안된다 : 이름을 보니깐

# iloc[행숫자index, 열숫자index]
emp.iloc[1:3] # 숫자 인덱스 : 이름이 아닌 숫자만 고려
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
'''
emp
emp.iloc[1:3, :2]
## 중간에 특정 컬럼 제외
emp.iloc[1:3, [0, 2]]
emp.iloc[1:3, ['No', 'Pay']]  ## 안된다 : 숫자만 보니깐


#######################################
## DF 행렬참조 example
#######################################
iris.shape  # (150, 5)

from numpy.random import choice
help(choice)
# choice(a, size=None, replace=True, p=None) : (뽑을 숫자, 저 숫자중에 얼만큼 뽑을거임?, 복원추출함?, 확률)

row_idx = choice(a=len(iris), size=int(len(iris)*0.7), replace=False)
row_idx
len(row_idx)  # 105개 추출

# train dataset
train_set = iris.iloc[row_idx]  # 추출된 넘버를 기반으로 데이터를 추출
train_set.head()

train_set2 = iris.loc[row_idx]  # 같은 결과
train_set2.head()
train_set.shape  # (105, 5)
train_set2.shape # (105, 5)  # 150 * 0.7

# test dataset : 리스트내포 등장
test_id = [i for i in range(len(iris)) if not i in row_idx]
# 이미 뽑았던 숫자가 아닌 거에 대하여 하나씩 리스트에 축적시켜라
len(test_id)

test_set = iris.iloc[test_id]
test_set.shape # (45, 5)

# x, y 변수 분리
cols = list(iris.columns)
x = cols[:4]
y = cols[-1]
iris_x = iris.loc[test_id, x]  # 스트링 문자열이니 iloc 사용불가
iris_y = iris.loc[test_id, y]
iris_x.shape  # (45, 4)
iris_y.shape  # (45,)













