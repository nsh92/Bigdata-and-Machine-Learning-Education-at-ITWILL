# -*- coding: utf-8 -*-
"""
파이프라인 vs 그리드 서치
1. SVM model
2. Pipeline    : model workflow (전처리 -> 모델생성 -> 테스트)
3. Grid Search : model tuning
"""
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler # 스케일링 전처리 클래스
import numpy as np
from sklearn.pipeline import Pipeline # 모델의 워크플로우를 만들어주는 클래스
# 1. SVM model
X, y = load_breast_cancer(return_X_y=True)  # x y값 동시에 받겠다
X.shape # (569, 30)
X.mean(axis=0) # 열단위 평균
X.min() # 0.0
X.max() # 4254.0

## X변수 정규화 : MinMaxScaler() : 생성자임
scaler = MinMaxScaler().fit(X)
X_nor = scaler.transform(X)
X_nor
X_nor.mean(axis=0)
X_nor.min() # 0.0
X_nor.max() # 1.0000000000000002

## 모델 생성
X_train, X_test, y_train, y_test = train_test_split(X_nor, y, test_size=0.3)
svc = SVC(gamma='auto')

## 모델 평가
model = svc.fit(X_train, y_train)
score = model.score(X_test, y_test) # 0.9473684210526315


# 2. 파이프라인 : model workflow
## 위 일련의 절차를 얘 하나로 만듦
## 1) 파이프라인의 스텝 : [ (튜플 스텝1), (스텝2), ... ] 객체 생성 -> 파이프라인 모듈의 인수
pipe_svc = Pipeline([('scaler', MinMaxScaler()), ('svc', SVC(gamma='auto'))])
                     # 스텝1 : 스케일러             스텝2 : 모델
                     # (객체이름, 클래스생성자())

## 2) 파이프라인 모델
model = pipe_svc.fit(X_train, y_train)

## 3) 모델 테스트
score = model.score(X_test, y_test)
score # 0.9473684210526315


# 3. 그리드 서치 : 모델 튜닝
## 파이프라인 모델을 기반으로 최적의 파라미터를 찾아 튜닝함
from sklearn.model_selection import GridSearchCV
help(SVC)
# svc파라미터 : C=1.0, kernel='rbf', degree=3, gamma='보통auto'
## 1) parameter 설정
params = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
### 그리드서치를 위한 dict 형식 구조 : {'객체명__파라미터':파라미터범위설정} 언더바 두개
params_grid = [{'svc__C':params, 'svc__kernel':['linear']},                       # 선형 dict만들고 콤마 또dict가 포인트
               {'svc__C':params, 'svc__gamma':params, 'svc__kernel':['rbf']}]     # 비선형

## 그리드서치 객체
gs = GridSearchCV(estimator=pipe_svc, param_grid=params_grid, scoring='accuracy', cv=10)
# scoring : 평가방법, cv : 교차검정

model = gs.fit(X_train, y_train)

acc = model.score(X_test,y_test) # 0.9824561403508771

model.best_params_
#  {'svc__C': 1.0, 'svc__gamma': 1.0, 'svc__kernel': 'rbf'}














