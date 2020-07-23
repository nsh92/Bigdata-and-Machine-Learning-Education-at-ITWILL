# -*- coding: utf-8 -*-
"""
행렬곱 함수(np.dot) 이용 y 예측치 구하기
 y_pred = np.dot(X, a) + b
 4장 step04,05 참고
 
np.dot(X, a) 전제조건
1. X, a : 행렬 구조
2. 수일치 : X열 차수 = a행 차수
"""
from scipy import stats # 단순회귀모델
from statsmodels.formula.api import ols # 다중회귀
import pandas as pd
import numpy as np
score = pd.read_csv('C:/ITWILL/4_Python-II/data/score_iq.csv')
score.info()'''
 0   sid      150 non-null    int64
 1   score    150 non-null    int64  --> y
 2   iq       150 non-null    int64  --> x1
 3   academy  150 non-null    int64  --> x2
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
'''
formula = "score ~ iq + academy"
model = ols(formula, data = score).fit() # 모델생성
model.params # 회귀계수조회
'''
Intercept    25.229141
iq            0.376966
academy       2.992800
'''
## 다중회귀를 행렬 와꾸로 모델링할 수 있다

model.summary() # 모델 결과 확인

model.fittedvalues # 모델 예측치 확인

# 직접 계산해보자
# y_pred = np.dot(X, a) + b
X = score[['iq', 'academy']]
X.shape # (150, 2) : x1 x2
a = np.array([[0.376966], [2.992800]]) # 리스트를 넘파이 어레이로
a.shape # (2, 1)

matmul = np.dot(X, a) # 행렬곱
matmul.shape # (150, 1) = X(150,2) * a(2, 1)
b = 25.229141
y_pred = matmul + b # (브로드캐스트 연산)
y_pred.shape # (150, 1)

# 2차원 -> 1차원
y_pred1d = y_pred.reshape(150) # 벡터로 출력됨
y_pred1d.shape # (150,)

y_ture = score['score']
y_ture.shape   # (150,)
df = pd.DataFrame({'y_true':y_ture, 'y_pred':y_pred1d})
df.head()
df.tail()
cor = df.corr()
cor # 0.972779


















