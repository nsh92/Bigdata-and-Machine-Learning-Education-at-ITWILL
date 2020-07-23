# -*- coding: utf-8 -*-
"""
step3 교차검정
균등분할해가지고 교차검정을 수행하는 과정을 살펴보자
"""
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import accuracy_score
# 1. dataset load
digit = load_digits()

X = digit.data
y = digit.target

X.shape # (1797, 64)
y       # [0, 1, 2, ..., 8, 9, 8]


# 2. model 생성
rf = RandomForestClassifier()
model = rf.fit(X,y)
pred = model.predict(X) # class에서의 형태로 예측함 : 1차원
pred2 = model.predict_proba(X) # 확률로 예측함     : 2차원

acc = accuracy_score(y, pred)
acc # 0.9814814814814815
# 얘는 같은 형태니까 바로 비교분석이 되지만 proba저것은 곤란함
# argsort로 가장 높은 확률을 보이는 변수만 배출하게끔 해줘야 함

## 확률 -> 인덱스배출(10진수)
## numpy.argxxx() : index 반환 함수
## argsort, argmax 등
pred2_dit = pred2.argmax(axis=1)
pred2_dit # [0, 1, 2, ..., 8, 9, 8]
acc = accuracy_score(y, pred2_dit) # 1.0

## 귀찮긴한데, 불가피하게 확률로만 예측해야하는 경우가 있음


# 3. 교차검정 : 모듈을 키고 원래 해놨던 모델을 집어넣는다
score = cross_validate(model, X, y, scoring='accuracy', cv=5)
score
'''
{'fit_time': array([0.21449566, 0.21042275, 0.213377  , 0.21448183, 0.21444082]),
 'score_time': array([0.00996923, 0.00897598, 0.00997329, 0.00996971, 0.00997424]),
 'test_score': array([0.92777778, 0.91666667, 0.9637883 , 0.95264624, 0.91364903])} 이게 중요
'''
test_score = score['test_score'] # array([0.92777778, 0.91666667, 0.9637883 , 0.95264624, 0.91364903])
test_score.mean() # 0.934905601980811 각 모델에 대한 산술평균





















