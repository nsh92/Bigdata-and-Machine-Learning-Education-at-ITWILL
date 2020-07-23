# -*- coding: utf-8 -*-
"""
step03_regression_formula
단순선형회귀 : X(1) -> Y
- y_pred = X * 기울기 + 절편
- err = Y - y_pred
- loss function(cost function) : 손실 함수 : 정답과 예측치 간의 오차 반환 함수
  -> function(Y, y_pred) -> 오차 반환
"""
import tensorflow as tf


# 변수 정의
X = tf.constant(6.5) # input
Y = tf.constant(5.2) # output
# constant : 수정이 안댐

# 상수 정의
a = tf.Variable(0.5)
b = tf.Variable(1.5)
# Variable : 수정 가능 : 절편과 기울기는 지속적으로 수정하여 개선값을 찾아야하기 때문

# 회귀모델 함수
def linear_model(X):
    y_pred = tf.math.multiply(X, a) + b #  (X * a) + b
    return y_pred

# 모델 오차(error)
def model_err(X, Y):
    y_pred = linear_model(X)
    err = tf.math.subtract(Y, y_pred) #  Y - y_pred
    return err

# 손실함수(loss function) : (정답, 예측치) -> 오차 반환(MSE)
def loss_function(X, Y):
    err = model_err(X, Y)
    loss = tf.reduce_mean(tf.square(err))
    return loss

'''
오차 : MSE
Error : 정답 - 예측치
Square : 부호(+), 패널티
Mean : 전체 관측치 오차 평균
'''

print("최초 기울기와 절편")
print("a = {}, b = {}".format(a.numpy(), b.numpy()))
print("model error = ", model_err(X, Y).numpy())
print("loss function = ", loss_function(X, Y).numpy())
'''
최초 기울기와 절편
a = 0.5, b = 1.5
model error =  0.4499998
loss function =  0.20249982
'''

# 상수를 수정해보자
a.assign(0.6)
b.assign(1.2)
print("a = {}, b = {}".format(a.numpy(), b.numpy()))
print("model error = ", model_err(X, Y).numpy())
print("loss function = ", loss_function(X, Y).numpy())
'''
a = 0.6000000238418579, b = 1.2000000476837158
model error = 0.09999943
loss function = 0.009999885
'''

'''
[키워드 정리]
최적화된 모델 : 최적의 기울기와 절편 수정 -> 손실(loss)이 0에 수렴
딥러닝 최적화 알고리즘 : GD, Adam -> 최적의 기울기와 절편 수정 역할
'''

















