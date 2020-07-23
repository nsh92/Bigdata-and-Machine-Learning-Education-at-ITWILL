# -*- coding: utf-8 -*-
"""
1. 그룹 객체에 외부 함수 적용
 - obj.apply(func1)                # 함수 하나
 - obj.agg([func1, func2, ...])    # 여러 함수

2. data 정규화 
"""

# 1. 그룹 객체에 외부 함수 적용
'''
apply vs agg
 - 공통점 : 그룹 객체, 일반 DF객체에 외부 함수를 적용한다
 - 차이점 : 적용 함수의 개수
'''

## apply
test = pd.read_csv('C:/ITWILL/4_Python-II/data/test.csv')
grp = test['data2'].groupby(test['key'])
grp.size()
grp.sum()
grp.max()
grp.min()

## 사용자 정의 함수 생성
def diff(grp):
    result = grp.max() - grp.min()
    return result

## 내장함수 apply
grp.apply(sum) 
grp.apply(max)
grp.apply(min)

## 사용자정의함수 apply
grp.apply(diff)
# a      0
# b    100

## agg([func1, func2, ...])
agg_func = grp.agg(['sum', 'max', 'min', diff])  # 내장함수만 따옴표
agg_func
'''
     sum  max  min  diff
key                     
a    300  100  100     0
b    500  200  100   100
'''


# 2. data 정규화 : 다양한 특징을 갖는 (독립)변수를 대상을 일정한 범위로 조정
import numpy as np
## 1) 사용자 정의 함수 : 0 ~ 1
def normal(x):
    n = (x - np.min(x))/(np.max(x) - np.min(x))
    return n

x = [10, 20000, -100, 0]  
normal(x)  # [0.00547264, 1.        , 0.        , 0.00497512]

## 2) 자연log 함수로 정규화
np.log(x) # 밑수 e 자연로그 : 0, 음수인 경우는 무한대, 결측치로 처리함
# [2.30258509, 9.90348755,        nan,       -inf]

e = np.exp(1)
# np.exp(1) = 2.718281828459045
# np.log(10) = 2.3025... : 10은 e의 2.3025...승이다

# 지수 -> 로그값
np.exp(2.3025)  # 9.999
'''
로그 vs 지수 : 역함수 관계
- 로그 : 지수값 반환
- 지수 : 로그값 반환
'''
iris = pd.read_csv('C:/ITWILL/4_Python-II/data/iris.csv')

# 컬럼명 추출
cols = list(iris.columns)
cols 
iris_x = iris[cols[:4]]
iris_x.shape # (150, 4)
iris_x.head()

# x변수 정규화
iris_x_nor = iris_x.apply(normal)
iris_x_nor.head()

iris_x.agg(['var', 'mean', 'max', 'min'])
'''
      Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
var       0.685694     0.189979      3.116278     0.581006
mean      5.843333     3.057333      3.758000     1.199333
max       7.900000     4.400000      6.900000     2.500000
min       4.300000     2.000000      1.000000     0.100000
'''























