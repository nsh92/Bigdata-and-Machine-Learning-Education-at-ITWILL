# -*- coding: utf-8 -*-
"""
data scaling(정규화, 표준화) : 이물질 제거
 - 용도 : 특정 변수의 값에 따라서 model에 영향을 미치는 경우
   ex) 범죄율(-0.1 ~ 0.99), 주택가격(99 ~ 999)
 - 정규화 : 변수의 값을 일정한 범위로 조정
 - 표준화 : 평균0 표준편차1 이용 z=(x-mu)/sd
"""
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


# 1. dataset load
X, y = load_boston(return_X_y = True)
X.shape # (506, 13)
y.shape # (506,)


# 2. data scaling
# X : 0~1로 정규화
# Y : 표준화(평균0, 표준편차1)
X.max()  # 711
X.mean() # 70.07396704469443
y.max()  # 50
y.mean() # 22.532806324110677

## 정규화함수 생성
def normal(x):
    nor = (x-np.min(x))/(np.max(x)-np.min(x))
    return nor

## 표준화함수 생성
def zscore(y):
    mu = y.mean()
    z = (y - mu) / y.std()
    return z

x_nor = normal(X)
x_nor.mean() # 0.09855691567467571
y_nor = zscore(y)
y_nor.mean() # -5.195668225913776e-16 : 0에 수렴한다는 의미(의도하였던 평균0에 가깝다는 의미)
y_nor.std()  # 0.9999999999999999 : 1에 수렴


# 3. dataset split (75:25)
x_train, x_test, y_train, y_test = train_test_split(x_nor, y_nor, random_state = 123)
x_train.shape # (379, 13)
x_test.shape  # (127, 13)

# 4. 모델 생성
lr = LinearRegression()
model = lr.fit(X=x_train, y=y_train)
model

# 5. 모델 평가
y_pred = model.predict(X=x_test)
mse = mean_squared_error(y_test, y_pred) # 0.2933980240643525 # 오차율 30%
r2s = r2_score(y_test, y_pred)           # 0.6862448857295749 # 정확률 70%















