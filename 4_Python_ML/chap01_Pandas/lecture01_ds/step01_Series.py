# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징
 - 1차원의 배열 구조
 - 수학 통계 함수 제공
 - 범위 수정, 블럭 연산
 - indexing/slicing
 - 시계열 데이터 생성(뒤에서)
"""

import pandas as pd         # 별칭으로 임포트
from pandas import Series   # 패키지 -> 클래스 구체적으로 지목하여 임포트

# 1. 시리즈 객체 생성
## 1) list 이용
lst = [4000, 3000, 3500, 2000]
ser = pd.Series(lst)  # 리스트가 들어가서 시리즈란 클래스와 만나 객체 생성
print('lst = ', lst)
print('ser =\n', ser)
# 같은 1차원이지만, 시리즈는 인덱스와 함께 출력되었음

## object.member
print(ser.index)    # RangeIndex(start=0, stop=4, step=1)
print(ser.values)   # [4000 3000 3500 2000]

ser1_2 = Series([4000, 3000, 3500, 2000], index=['a', 'b', 'c', 'd'])
print(ser1_2)

## 2) dict 이용
person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
ser2 = Series(person)
print('ser2 = ', ser2)
'''
name    홍길동
age      35
addr    서울시
dtype: object
'''
print(ser2.index)   # Index(['name', 'age', 'addr'], dtype='object')
print(ser2.values)  # ['홍길동' 35 '서울시']

## 인덱스 사용 : object[n or 조건식]
print(ser2['age'])  # 35
print(ser[0])       # 4000

## 부울리언 조건식
print(ser[ser >= 3000])
'''
0    4000
1    3000
2    3500
'''


# 2. 인덱싱 : 리스트와 동일
ser3 = Series([4, 4.5, 6, 8, 10.5])  # 생성자
print(ser3[0])   # 4.0
print(ser[:3])   # 3개 : 2번 인덱스까지 출력
print(ser3[3:])  # 3번 인덱스 부터 : 3, 4번 인덱스 출력
print(ser3[-1])  # 오류뜸 : 걍 마이너스를 못 씀


# 3. Series 결합과 NA 처리
p1 = Series([400, None, 350, 200], index = ['a', 'b', 'c', 'd'])
p2 = Series([400, 150, 350, 200], index = ['a', 'c', 'b', 'e'])
p3 = p1 + p2  # 시리즈 결합
print(p3)
'''
a    800.0
b      NaN
c    500.0
d      NaN
e      NaN
순서에 상관없이 동일한 인덱스 끼리 더해짐
한쪽이 none이 거나 상대방에 없는 인덱스의 경우 걍 결측치로 되었음
'''


# 4. 결측치 처리 방법(평균, 0, 제거)
print(type(p3))
# <class 'pandas.core.series.Series'>

## 1) 평균 대체
p4 = p3.fillna(p3.mean())  # 평균으로 na를 체워라
print(p4)  # NAN -> 평균

## 2) 0으로 대체
p5 = p3.fillna(0)
print(p5)  # NAN -> 0

## 3) 아예 제거
p6 = p3[pd.notnull(p3)]  # 결측치 아닌 것만 담아라 # 서브셋 개념
print(p6)


# 5. 범위 수정, 블럭 연산
print(p2)
'''
a    400
c    150
b    350
e    200
'''
## 1) 범위 수정
p2[1:3] = 300
print(p2)
'''
a    400
c    300
b    300
e    200
리스트에선 불가능한 작업
'''
## 2) 블럭 연산
print(p2 + p2)  # 두배 출력
print(p2 - p2)  # 0 출력

## 3) broadcast 연산(1차원 vs 0차원)
v1 = Series([1,2,3,4])
scala = 0.5

b = v1 * scala  # 벡터 * 스칼라
print(b)  # 각 원소에 대하여 곱해짐
# 원래는 리스트가지고 이러려면 for 구문을 썼어야 했지

## 4) 수학 / 통계 함수
## 시리즈 클래스 자체적으로 함수 멤버가 있다
print('sum=', v1.sum())
print('mean=', v1.mean())
print('var=', v1.var())
print('std=', v1.std())
print('max=', v1.max())
'''
sum= 10
mean= 2.5
var= 1.6666666666666667
std= 1.2909944487358056
max= 4
'''

## 호출 가능한 멤버 확인
print(dir(v1))

print(v1.shape)  # (4,)
print(v1.size)   # 4

























