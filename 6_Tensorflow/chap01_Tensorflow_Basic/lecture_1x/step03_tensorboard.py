# -*- coding: utf-8 -*-
"""
step03_텐서보드
 - 텐서보드 & 사칙연산 함수
 1. 텐서보드 : 텐서플로우 시각화 도구
 2. 사칙연산 함수
    tf.add(x, y, name)
    tf.subtract(x, y, name)
    tf.div(x, y, name)
    tf.multiply(x, y, name)
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()  

# 사칙연산 : 식 정의
# name : 공백, 특수문자, 한글 사용 불가, _는 가능
## 연산 흐름을 함 보자
a = tf.add(1, 2, name='a')
b = tf.multiply(a, 6, name='b')
c = tf.subtract(20, 10, name = 'c')
d = tf.div(c, 2, name='d')
g = tf.add(b, d, name='g')
h = tf.multiply(g, d, name='h')

# 상수정의
x = tf.constant(1, name='x')
y = tf.constant(2, name='y')

with tf.Session() as sess :
    print("h=", sess.run(h))  # h= 115
    tf.summary.merge_all() # 텐서들을 모으는 역할
    writer = tf.summary.FileWriter(r"C:/ITWILL/6_Tensorflow/graph", sess.graph)
    writer.close()
    































