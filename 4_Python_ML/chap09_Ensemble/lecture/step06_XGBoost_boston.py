# -*- coding: utf-8 -*-
"""
xgb회귀트리
"""
from xgboost import XGBRFRegressor
from xgboost import plot_importance 
from sklearn.datasets import load_boston # 주택가격 데이터
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score # 연속모델 평가 도구
# 1. 데이터 로드
boston = load_boston()
x_names = boston.feature_names
x_names # ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X, y = load_boston(return_X_y = True)
X.shape # (506, 13)
y # 비율척도임 : 연속변수 : 비정규화


# 2. 데이터 스플릿
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3)


# 3. 모델 생성
xgbr = XGBRFRegressor()
model = xgbr.fit(x_train, y_train)
model


# 4. 중요 변수
fscore = model.get_booster().get_fscore()
fscore 
'''
{'f5': 668,
 'f12': 588,
 'f7': 365,
 'f0': 1023,
 'f9': 189,
 'f4': 354,
 'f6': 303,
 'f10': 198,
 'f2': 185,
 'f11': 175,
 'f3': 25,
 'f1': 51,
 'f8': 42}
'''
x_names[0] # 'CRIM'
x_names[5] # 'RM'
plot_importance(model)
plt.show()


# 5. 모델 평가
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
mse # 8.582415843512058
score = r2_score(y_test, y_pred)
score # 0.8941196552331288


























