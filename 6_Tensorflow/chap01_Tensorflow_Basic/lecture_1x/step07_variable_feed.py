# -*- coding: utf-8 -*-
"""
초기값이 없는 변수 : Feed 방식
변수 = tf.placeholder(dtype, shape)
- dtype : 자료형(tf.float, tf.int32, tf.string)
- shape : 자료구조([n] : 1차원, [r,c] : 2차원, 생략 : 공급data 결정)
"""
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior()

a = tf.placeholder(dtype=tf.float32)            # 가변형
b = tf.placeholder(dtype=tf.float32)            # 가변형
c = tf.placeholder(dtype=tf.float32, shape=[5]) # 고정형
d = tf.placeholder(dtype=tf.float32, shape=[None,3]) # 고정형 : 2d(행 가변)

c_data = tf.random_uniform([5])

# 식 정의
mul = tf.multiply(a, b)
add = tf.add(mul, 10)
c_calc = c * 0.5  # vector * scala

with tf.Session() as sess:
    # 변수 초기화 생략
    # 식 실행
    mul_re = sess.run(mul, feed_dict = {a : 2.5, b : 3.5})
    print("mul =", mul_re)
    
    # data 공급    
    a_data = [1.0, 2.0, 3.5]
    b_data = [0.5, 0.3, 0.4]
    feed_data = {a : a_data, b : b_data}
    mul_re2 = sess.run(mul, feed_dict = feed_data)
    print("mul2 =", mul_re2)

    # 식 실행 : 식 참조
    add_re = sess.run(add, feed_dict = feed_data)
    print("add =", add_re)
    
    print("c_calc =", sess.run(c_calc, feed_dict = {c:c_data}))
    




















