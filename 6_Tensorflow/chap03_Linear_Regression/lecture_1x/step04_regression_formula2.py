# -*- coding: utf-8 -*-
"""
step04_regression_formula2
행렬곱으로 다중선형회귀
- X(n) -> Y
- y_pred = X1 * a1 + X2 * a2 ...
- y_pred = tf.matmul(X, a) + b
"""
import tensorflow as tf

# X, Y 변수 정의
X = [[1.0, 2.0]] # [1, 2] : 입력
y = 2.5 # 정답

# a, b 변수 정의 : 수정가능한 난수 상수로
a = tf.Variable(tf.random.normal([2, 1]))# 기울기[2, 1] : 수일치 때문
b = tf.Variable(tf.random.normal([1])) # 하나의 상수

# model 식 정의
# y_pred = tf.math.add(tf.matmul(X * a), b)
y_pred = tf.matmul(X, a) + b
print(y_pred)

'''
tf.matmul(X, a) : 행렬곱
1. X, a -> 행렬
2. X열수 == a행수
'''
# model error
err = Y - y_pred

# loss function : 손실 반환
loss = tf.reduce_mean(tf.square(err))

print("최초 기울기와 절편")
print("a = {}, b = {}".format(a.numpy(), b.numpy()))
print("model error = ", err.numpy())
print("loss function = ", loss.numpy())

'''
1차 실행
최초 기울기와 절편
a = [[-0.09693469]
 [ 0.07095173]], b = [0.39862967]
model error =  [[4.7564015]]
loss function =  22.623356

2차 실행
a = [[-0.37992278]
 [ 0.6837082 ]], b = [-0.48958328]
model error =  [[4.7020893]]
loss function =  22.109644












