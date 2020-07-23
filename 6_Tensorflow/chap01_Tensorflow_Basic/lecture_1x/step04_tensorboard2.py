# -*- coding: utf-8 -*-
"""
step04_텐서보드2

name_scope 이용 : 영역별 tensorflow 시각화
 - 모델 생성 -> 모델 오차 -> 모델 평가
"""
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() 
tf.reset_default_graph() # 보드 초기화

# 상수 정의 : X, a, b, Y
X = tf.constant(5.0, name="x_data") # 입력 X
a = tf.constant(10.0, name="a")     # 기울기
b = tf.constant(4.45, name="b")     # 절편
Y = tf.constant(55.0, name="Y")     # 정답

# name_scope
with tf.name_scope("Regress_model") as scope:
    model = (X * a) + b  # y 예측치
    
with tf.name_scope("Model_error") as scope:
    model_err = tf.abs(tf.subtract(Y, model)) 

with tf.name_scope("Model_evaluation") as scope:
    square = tf.square(model_err)
    mse = tf.reduce_mean(square)

with tf.Session() as sess:
    tf.summary.merge_all()
    writer = tf.summary.FileWriter(r"C:/ITWILL/6_Tensorflow/graph", sess.graph)
    writer.close()
    print("X =", sess.run(X))
    print("Y =", sess.run(Y))
    print("y_pred =", sess.run(model))
    print("model err =", sess.run(model_err))
    print("MSE =", sess.run(mse))










