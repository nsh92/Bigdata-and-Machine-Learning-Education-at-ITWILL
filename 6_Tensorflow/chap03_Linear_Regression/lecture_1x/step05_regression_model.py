# -*- coding: utf-8 -*-
"""
step05_regression_model : ver1.x
 - X(1) -> Y
 - 손실함수(loss function) : 오차 반환 함수
   -> 모델 학습 : 최적의 기울기, 절편 -> loss값 0에 수렴
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

# 1. X, Y 정의
x_data = np.array([1,2,3])
y_data = np.array([2,4,6])

# 2. X, Y 변수 정의
X = tf.placeholder(dtype=tf.float32, shape=[None]) # 실수형, 가변길이
Y = tf.placeholder(dtype=tf.float32, shape=[None])

# 3. a, b 변수 정의
a = tf.Variable(tf.random_normal([1])) # 기울기 상수 하나
b = tf.Variable(tf.random_normal([1])) # 절편

# 4. 식 정의
model = tf.multiply(X, a) + b  # 회귀방정식
err = Y - model # 오차
loss = tf.reduce_mean(tf.square(err)) # 손실 함수

# 5. 최적화 객체
optimizer = tf.train.GradientDescentOptimizer(0.1) # 학습률 = 0.1
train = optimizer.minimize(loss) # 손실 최소화 : 최적의 기울기 및 절편 수정

init = tf.global_variables_initializer()

# 6. 반복 학습
with tf.Session() as sess:
    sess.run(init) # a, b 변수 초기화
    a_val, b_val = sess.run([a, b])
    print("a = {}, b = {}".format(a_val, b_val))
    
    feed_data = {X : x_data, Y : y_data}
    
    # 반복학습 : 50회
    for step in range(50):
        _, loss_val = sess.run([train, loss], feed_dict = feed_data) # _ : 특별히 의미는 없으나 받기는 해줘야 하는 표시
        print("step = ", (step+1), "loss = ", loss_val)
        a_val_up, b_val_up = sess.run([a, b])
        print("a = {}, b = {}".format(a_val_up, b_val_up))

'''
a = [-0.44323733], b = [-1.1143204]
step =  1 loss =  39.98915
->
step =  50 loss =  1.4501318e-05
a = [2.0043166], b = [-0.00981251]
'''






















