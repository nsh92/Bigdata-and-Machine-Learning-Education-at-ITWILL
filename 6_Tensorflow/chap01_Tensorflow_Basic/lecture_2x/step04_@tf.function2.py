# -*- coding: utf-8 -*-
"""
step04_@tf.function2
 - 텐서플로우2.0 특징
   3. @tf.function 함수 장식자(데코레이터)
      - 여러 함수들을 포함하는 메인 함수
"""
import tensorflow as tf

# model 생성 함수
def linear_model(x):
    return x * 2 + 0.2

# model 오차 함수
def model_err(y, y_pred):
    return y - y_pred
## 여기까진 일반적인 파이썬의 함수

# 모델 평가 함수 : main : 메인함수에 장식자를 적용한다, 나머지 함수는 굳이
@tf.function
def model_evaluation(x, y):
    y_pred = linear_model(x) # 함수 호출
    err = model_err(y, y_pred)
    return tf.reduce_mean(tf.square(err))

# x, y 데이터 생성
X = tf.constant([1,2,3], dtype=tf.float32)
Y = tf.constant([2,4,6], dtype=tf.float32)

MSE = model_evaluation(X, Y)
print("MSE = %.5f"%(MSE)) # MSE = 0.04000





























