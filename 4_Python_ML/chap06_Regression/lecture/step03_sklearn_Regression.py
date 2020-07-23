# -*- coding: utf-8 -*-
"""
sklearn(사이키런) Linear Regression
기계학습 관련 패키지
"""
from sklearn.linear_model import LinearRegression # 모델 객체 생성
from sklearn.model_selection import train_test_split # train / test split
from sklearn.metrics import mean_squared_error, r2_score # 모델 평가
from sklearn.datasets import load_diabetes # 데이터셋 업로드
import numpy as np # 숫자처리

######################################
### diabetes
######################################
# 단순선형회귀 : x(1개) -> y
# 1. 데이터셋 로드
X, y= load_diabetes(return_X_y = True) # True : 동시에 받겠다
X.shape # (442, 10)
y.shape # (442,)
y.mean() # 152.13348416289594

# 2. x, y 변수
# x(bmi 비만도지수) -> y
x_bmi = X[:,2]
x_bmi.shape # (442,)

# 3. 모델 생성 : 객체 -> 트레이닝 -> 모델
obj = LinearRegression() # 생성자 객체 (저 친구는 모듈이 아니라 클래스임 : 클래스() : 생성자)
model = obj.fit(x_bmi, y) # (X, y) # 모델 생성
# 에러 표시 : X자리가 행렬구조여야 한다
x_bmi = x_bmi.reshape(442, 1) # 2d로 전환
model = obj.fit(x_bmi, y)

## 예측치
y_pred = model.predict(x_bmi)

# 4. 모델 평가 : MSE(정규화), r2_score
MSE = mean_squared_error(y, y_pred) # 3890.4565854612724
score = r2_score(y, y_pred          # 0.3439237602253803
print('mse=', MSE)
print('r2_socre =', score)
# r2스코어 : 일치하는 수준을 점수화시킴 (1만점)

# 5. split(70 : 80)
x_train, x_test, y_train, y_test= train_test_split(x_bmi, y, test_size=0.3)
x_train.shape # (309, 1)
x_test.shape  # (133, 1)


# 6. 모델 생성
obj = LinearRegression()
model = obj.fit(x_train, y_train) # data training
y_pred = model.predict(x_test)


# 모델 평가 : MSE(정규화), r2_score(비정규화)
MSE = mean_squared_error(y_test, y_pred)
print(MSE, score) # mse : 3527.673201079187, r2score :  0.3439237602253803
y_test[:10]
y_pred[:10]

import pandas as pd # 상관계수 알아보기
pd.DataFrame({'y_true' : y_test, 'y_pred' : y_pred})
cor = df['y_true'].corr(df['y_pred'])
cor # 0.9727792069594754

import matplotlib.pyplot as plt # 시각화
plt.plot(x_test, y_test, 'ro')  # 산점도
plt.plot(x_test, y_pred, 'b-')  # 선
plt.show()


######################################
### iris.csv
######################################
# 다중회귀모델 : y(1) <- x(2~4)
iris = pd.read_csv('C:/ITWILL/4_Python-II/data/iris.csv')
iris.info()
'''
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object 
'''

# 2. x,y 변수 선택
cols = list(iris.columns)
cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

y_col = cols[0]
x_cols = cols[1:4] # or cols[1:-1]

# 3. dataset split
iris_train, iris_test = train_test_split(iris, test_size=0.3, random_state=123)
'''
test_size : 검정데이터셋 비율(default = 0.25)
random_state : 샘플링 시드값(id) : 다음번에 시행할때 시드값이 같으면 동일하게 뽑도록하게함
'''
iris_train.shape # (105, 5)
iris_test.shape  # (45, 5)
iris_train.head()
iris_test.head()

# 4. model 생성 : train data
lr = LinearRegression()
model = lr.fit(X=iris_train[x_cols], y=iris_train[y_col])
model
y_pred = model.predict(X=iris_test[x_cols]) # 예측
y_true = iris_test[y_col] # 정답
y_true.min() # 4.3
y_true.max() # 7.9

# 평균제곱오차 : mean((y_true - y_pred)**2)
mse = mean_squared_error(y_true, y_pred)
score = r2_score(y_true, y_pred)
print('MSE =', mse, ', r2score =', score)

# y_true vs y_pred 시각화
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (10,5))
chart = fig.subplots()
chart.plot(np.array(y_true), color = 'b', label = 'real') #np.array 안해주면 와꾸 오지게 깨짐
chart.plot(y_pred, color = 'r', label = 'fitted')
plt.legend(loc = 'best')
plt.show()


























