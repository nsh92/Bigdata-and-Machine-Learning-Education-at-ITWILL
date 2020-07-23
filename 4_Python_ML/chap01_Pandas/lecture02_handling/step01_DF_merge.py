# -*- coding: utf-8 -*-
"""
DataFrame 병합(merge)
 ex) DF1(id) + DF2(id)) -> DF3 : merge
"""
from pandas import Series, DataFrame
import pandas as pd

# 1. Series merge : 1차원
s1 = Series([1,3], index=['a', 'b'])
s2 = Series([5,6,7], index=['a', 'b', 'c'])
s3 = Series([11,13], index=['a', 'b'])

## 행단위 결합 : rbind()
s4 = pd.concat(s1,s2,s3) # 문법적 오류 : 파라미터 입력값으로 인지함
s4 = pd.concat([s1,s2,s3], axis=0) # 행 결합
s4.shape  # (7,) : 1차원

## 열단위 결합 : cbind()
s5 = pd.concat([s1,s2,s3], axis=1)
s5.shape  # (3, 3) : 2차원


# 2. DataFrame 병합
wdbc = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\wdbc_data.csv")
wdbc.info()
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns)
'''

## DF1(16) + DF2(16) 로 분해하겠다(32컬럼짜리를)
cols = list(wdbc.columns)
len(cols) # 32

# 결합 : 컬럼 단위 결합
DF1 = wdbc[cols[:16]]
DF1.shape # (569, 16)
DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

DF4 = pd.concat([DF1, DF2], axis = 1)
DF4.info()

# id 컬럼 추가
id = wdbc.id
DF2['id'] = id  # 오류메세지는 아니고 경고메세지임
DF2.shape
DF2.head()

# 병합 
DF_merge = pd.merge(DF1, DF2)
DF_merge.info() # merge가 제대로 되었는지 확인



