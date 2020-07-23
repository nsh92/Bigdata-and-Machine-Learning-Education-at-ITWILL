# -*- coding: utf-8 -*-
"""
step02_gradientTape.py

자동 미분 계수
 - tf.GradientTape() 클래스 이용
 - 역방향 step 이용 (cf : 순방향 : 연산과정 -> loss)
 - 딥러닝 모델 최적화 핵심 기술
 - 가중치(w)에 대한 오차(loss)의 미분값 계산
   -> x(w)에 대한 y(loss)의 기울기 계산
"""
import tensorflow as tf

'''
[실습1]
한 점 A(2,3)을 지나는 접선의 기울기
2차 방정식 : y = x^2 + x
'''

x = tf.Variable(2.0) # x=2
with tf.GradientTape() as tape:
    # y = x^2 + x
    y = tf.math.pow(x, 2) + x

grad = tape.gradient(y, x) # x에 대한 y의 기울기
print("기울기 =", grad.numpy()) # 기울기 = 5.0

'''
[실습2]
x = 2.0 -> x = 1.0
'''
x = tf.Variable(1.0) 
with tf.GradientTape() as tape:
    # y = x^2 + x
    y = tf.math.pow(x, 2) + x
grad = tape.gradient(y, x)
print("기울기 =", grad.numpy()) # 기울기 = 3.0
# 정리 : 미분값(기울기) 양수인 상태에서는 x를 감소시켜야 최솟점이 내려간다

'''
[실습3] 미분값(기울기) 음수
'''
x = tf.Variable(-1.0) 
with tf.GradientTape() as tape:
    # y = x^2 + x
    y = tf.math.pow(x, 2) + x
grad = tape.gradient(y, x)
print("기울기 =", grad.numpy()) # 기울기 = -1.0
# 정리 : 미분값(기울기) 음수인 상태에서는 x를 증가시켜야 최솟점이 내려간다


