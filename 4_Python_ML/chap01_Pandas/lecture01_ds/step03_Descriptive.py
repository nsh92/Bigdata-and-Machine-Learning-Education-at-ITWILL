# -*- coding: utf-8 -*-
"""
- DataFrame의 요약통계량
- 상관계수
"""
import pandas as pd
product = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\product.csv")
product.info()
product.head()
product.tail()

# 요약통계량 : R의 summary 함수
summ = product.describe()
print(summ)

# 행/열 통계
product.sum(axis = 0)
product.sum(axis = 1)

# 산포도 : 분산, 표준편차
product.var()  # (axis = 0) : 기본값
product.std()

# 빈도수 : 집단변수
a_cnt = product['a'].value_counts()
print(a_cnt)
'''
3    126
4     64
2     37
1     30
5      7
'''
b_cnt = product['b'].value_counts()
print(b_cnt)

# 유일값 보기
print(product['c'].unique())  # [3 2 4 5 1]

# 상관관계
product.corr()  # 상관계수 정방행렬

# iris dataset 적용
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")
# 우측 상단의 주소가 일치하다면 상대경로로 파일의 이름만 입력해도 됨
iris.info()

## subset 생성
iris_df = iris.iloc[:,:4]
iris_df.shape # (150, 4)
iris_df.describe() # 4 변수의 요약 통계량

## 상관관계
iris_df.corr()

## 집단변수
species = iris.Species
species.value_counts() # 50개씩

species.unique() # 'setosa', 'versicolor', 'virginica'

list(species.unique())











