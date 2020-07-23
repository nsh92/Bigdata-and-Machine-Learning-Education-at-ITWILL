# -*- coding: utf-8 -*-
"""
1. 축(axis) : 행축, 열축
2. 행렬곱 연산(dot) : np.dot()
   - 회귀방정식 = [X*a] + b
   X1, X2 -> a1, a2
   model = [X1 * a1 + X2 * a2] + b
   -> model = np.dot(X, a) + b 행렬곱 연산이 이래 쓰일 수 있다
   
   - 신경망에서 행렬곱 예
     [X * w] + b
"""
import numpy as np
# 1. 축(axis) : 행축, 열축
'''
행 축 : 동일한 열의 모음(axis=0) -> 열 단위
열 축 : 동일한 행의 모음(axis=1) -> 행 단위
'''
arr2d = np.random.randn(5,4)
arr2d
print('전체 원소 합계 :', arr2d.sum())
print('각 행 단위 합계 :', arr2d.sum(axis=1))
print('각 열 단위 합계 :', arr2d.sum(axis=0))
## 결과값이 차원이 축소되어 나오는 거 참고


# 2. 행렬곱 연산 : np.dot()
X = np.array([[2,3],[2.5,3]])
X
#array([[2. , 3. ],
#       [2.5, 3. ]])
X.shape # (2, 2)

a = np.array([[0.1],[0.05]])
a.shape # (2, 1)

b = 0.1 # 절편
y_pred = np.dot(X, a) + b
y_pred
#array([[0.45],
#       [0.5 ]])

'''
np.dot(X,a) 전제조건
1. X, a : 행렬 구조
2. 수일치 : X열 차수 = a행 차수
'''

# [실습] 강의자료 60page
X = np.array([[0.1,0.2],[0.3,0.4]])
X.shape #2행2열

w = np.array([[1,2,3],[2,3,4]])
w.shape # 2행3열

# 행렬곱
h = np.dot(X, w)
h
h.shape # 2행3열 = 2,2 * 2,3



































